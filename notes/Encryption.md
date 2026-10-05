I went through your `questions_answers.md` with the quiz app's parser and found about 20 questions that are really about encryption. They all fit a three-step way of thinking, below.

**First, a correction to how you're framing it:** KMS isn't an *alternative* to S3's or other services' own encryption. When a service like S3, EBS, RDS, DynamoDB or Kinesis encrypts data at rest, it almost always uses **a KMS key underneath**. The real question isn't "KMS or something else?" It's:

1. Is the data **in transit or at rest**?
2. If at rest, **who does the encrypting**: the AWS service, or your code?
3. **Which key** is used, and who controls it?

## Step 1: In transit or at rest?

| In transit (moving over the network)                                                           | At rest (stored)                                                                   |
| ---------------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------- |
| **TLS/SSL certificates**, usually from **ACM**                                                 | **KMS keys**, sometimes CloudHSM or your own key                                   |
| Set on the thing clients connect to: **ELB, CloudFront, API Gateway**                          | Set on the thing that stores data: **S3, EBS, RDS, DynamoDB, Kinesis, SQS…**       |
| Enforced with **`aws:SecureTransport`** (S3) or **Viewer/Origin Protocol Policy** (CloudFront) | Enforced with **default encryption** or a **bucket policy** that requires a header |

**KMS is never the answer to an in-transit question.** That rule alone settles a lot of your questions:

| Your question                                                                                   | Answer                                                  | Why it's not KMS                                                                         |
| ----------------------------------------------------------------------------------------------- | ------------------------------------------------------- | ---------------------------------------------------------------------------------------- |
| **S7 Q1 / Q4**: SSL for a site behind an ELB, without loading the CPU-constrained EC2 instances | **SSL certificate on the ELB + SSL termination**        | In transit, so certificates. Terminating TLS on the load balancer offloads the CPU work. |
| **S15 Q1 / Q2**: encrypt traffic users ↔ CloudFront ↔ origin                                    | **Viewer Protocol Policy + Origin Protocol Policy**     | In transit, handled by CloudFront settings                                               |
| **S15 Q5**: HTTPS for an S3 static website                                                      | **CloudFront in front of S3 + SSL/TLS certificate**     | S3 website endpoints don't support HTTPS, so you add CloudFront                          |
| **S14 Q5 / Q7**: all data sent to S3 must be encrypted in transit                               | **Bucket policy denying `aws:SecureTransport = false`** | Forces HTTPS. Nothing to do with keys.                                                   |
| **S9 Q2**: third-party certificate for API Gateway + CloudFront                                 | **Import the certificate into ACM**                     | Certificates belong to ACM, not KMS                                                      |
| **S31 Q4**: secure communication for IoT devices                                                | **ACM + X.509 certificates**                            | TLS again                                                                                |

## Step 2: At rest, who encrypts?

```
                          ┌── The AWS SERVICE encrypts it (server-side)
Data stored at rest ──────┤     → turn on the service's encryption setting, then pick a key (Step 3)
                          │
                          └── YOUR CODE encrypts it before sending (client-side)
                                → call KMS APIs yourself:
                                     ≤ 4 KB  → kms:Encrypt
                                     > 4 KB  → kms:GenerateDataKey (envelope) / Encryption SDK
```

### A) The service encrypts it: just turn on its encryption

| Your question                                                              | Answer                                                                     | Lesson                                                                               |
| -------------------------------------------------------------------------- | -------------------------------------------------------------------------- | ------------------------------------------------------------------------------------ |
| **S19 Q8**: encryption at rest for Kinesis Data Streams                    | **Enable server-side encryption with a KMS key**                           | The service does it; KMS supplies the key                                            |
| **S30 Q3**: S3 documents encrypted at rest, keys rotated annually, EASIEST | **KMS with automatic key rotation**                                        | "Rotate keys" means you need control over the key, so a KMS key (SSE-KMS)            |
| **S14 Q1**: everything written to S3 must be encrypted                     | **Bucket policy denying PutObject without `x-amz-server-side-encryption`** | *Enforcing* at-rest encryption is done with a bucket policy                          |
| **S8 Q14**: cached data must be encrypted and highly available             | **ElastiCache for Redis** (cluster mode)                                   | Redis has built-in encryption and replication. You flip a setting, no KMS API calls. |

### B) Your code encrypts it: call KMS directly

| Your question                                                             | Answer                                                                              | Lesson                                                                                                                             |
| ------------------------------------------------------------------------- | ----------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------------------------------------------------- |
| **S21 Q14**: Lambda must encrypt a JSON file *before* uploading to S3     | **`GenerateDataKey`, then encrypt in the Lambda code**                              | "Before it is uploaded" means client-side. A file is likely over 4 KB, so envelope encryption.                                     |
| **S30 Q10**: encrypt each file with a **unique key**                      | **`GenerateDataKey` per file; store the encrypted data key with the data**          | One data key per object is exactly what envelope encryption does                                                                   |
| **S30 Q12**: 1 GB objects, 150 GB total                                   | **`GenerateDataKey`; use the plaintext key to encrypt**                             | Over 4 KB, so never plain `Encrypt`                                                                                                |
| **S30 Q11**: correct envelope encryption process                          | **Encrypt the data with a data key, then encrypt the data key with the master key** | The KMS key only ever encrypts the *small* data key                                                                                |
| **S30 Q6**: key policy is missing an action for encrypting large data     | **`kms:GenerateDataKey`**                                                           | Envelope encryption needs that permission in the key policy                                                                        |
| **S21 Q10**: Lambda env var secrets must be hidden even in the console    | **Encrypt client-side with the encryption helpers**                                 | Lambda's default env var encryption happens at rest, so the console still shows the values. Client-side KMS encryption hides them. |
| **S30 Q2**: "end-to-end encryption" with `GenerateDataKey` gets throttled | **Encryption SDK `LocalCryptoMaterialsCache` + quota increase**                     | Your code calls KMS too often, so cache the data keys                                                                              |

## Step 3: Which key? (S3 is the main example)

S3's "other ways of encrypting" are just **different choices of who holds the key**:

| S3 option       | Who manages the key                                         | Header               | Pick it when the question says…                                                                     |
| --------------- | ----------------------------------------------------------- | -------------------- | --------------------------------------------------------------------------------------------------- |
| **SSE-S3**      | S3, with an AWS-owned key                                   | `AES256`             | "encrypted at rest", nothing more, cheapest/simplest, default                                       |
| **SSE-KMS**     | **KMS** (AWS managed `aws/s3` or customer managed)          | `aws:kms`            | **audit key usage in CloudTrail**, **control who can use the key**, **key rotation**, cross-account |
| **DSSE-KMS**    | KMS, two layers of encryption                               | `aws:kms:dsse`       | "dual-layer encryption" for compliance                                                              |
| **SSE-C**       | **You** send the key on every request; AWS doesn't store it | customer-key headers | "company must manage the keys itself, outside AWS"; **HTTPS is required**                           |
| **Client-side** | You, often with KMS `GenerateDataKey`                       | none                 | "encrypt **before** upload", "S3/AWS must never see plaintext"                                      |

**The SSE-KMS trap:** with SSE-KMS, **every S3 read and write calls KMS** and counts against your KMS quota. That's why **S30 Q5** (EC2 reading SSE-KMS objects gets a `ThrottlingException`) is answered with **exponential backoff + a quota increase**. **S3 Bucket Key** also fixes it, cutting KMS calls by 99%.

The same key choice exists in other services:

| Service                             | Default                             | When you'd choose a KMS customer managed key                            |
| ----------------------------------- | ----------------------------------- | ----------------------------------------------------------------------- |
| DynamoDB                            | Always encrypted, AWS-owned key     | Audit or control needed                                                 |
| SQS                                 | SSE-SQS (AWS-owned key)             | Audit or control needed (SSE-KMS)                                       |
| EBS / RDS                           | Off, or `aws/ebs` / `aws/rds`       | Cross-account snapshot sharing, custom key policy                       |
| Secrets Manager                     | **KMS is mandatory**                | —                                                                       |
| Parameter Store                     | Plaintext, or SecureString with KMS | —                                                                       |
| CloudWatch Logs                     | AWS-owned                           | `associate-kms-key` (API only)                                          |
| Need dedicated hardware you control | —                                   | **CloudHSM** (**S30 Q9**: "tamper-resistant dedicated hardware device") |

## Exam keyword map

| Keyword in the question                                                  | Answer family                                                        |
| ------------------------------------------------------------------------ | -------------------------------------------------------------------- |
| HTTPS, SSL, TLS, "in transit", certificate, man-in-the-middle            | **ACM / TLS on ELB, CloudFront, API Gateway**; `aws:SecureTransport` |
| "at rest" for an AWS service, nothing else required                      | **Turn on the service's encryption** (SSE-S3, DynamoDB default…)     |
| audit key usage, rotate keys, control access to the key, cross-account   | **KMS customer managed key** (SSE-KMS)                               |
| encrypt **in your code**, before upload, unique key per file, large data | **KMS `GenerateDataKey`** / **Encryption SDK**                       |
| ≤ 4 KB secret                                                            | **KMS `Encrypt`**                                                    |
| `ThrottlingException` from KMS                                           | **Backoff**, **DEK caching**, **S3 Bucket Key**, **quota increase**  |
| dedicated, tamper-resistant hardware, you own the keys                   | **CloudHSM**                                                         |
| company supplies its own key on each request to S3                       | **SSE-C** (HTTPS required)                                           |
| encrypt specific form fields at the edge                                 | **CloudFront field-level encryption** (asymmetric)                   |

**One-sentence rule:** *TLS for moving data. For stored data, let the service encrypt it and pick the key: SSE-S3/AWS-owned by default, a KMS key when you need control or audit, CloudHSM when you need your own hardware. Call KMS APIs yourself only when your code must encrypt before sending.*

**Two things I noticed in your file:**
- **S10 Q4** has an empty answer. It's the same question as **S15 Q5**, so you can copy that answer over: CloudFront with S3 as the origin, plus an SSL/TLS certificate.
- **S30 Q11**'s answer says "top-level plaintext master key". That's AWS's own wording, but in KMS the master key never leaves KMS. What you actually send to KMS is the data key.

I can save this as `notes/sections/KMS-vs-Other-Encryption.md` if you'd like it with your other notes.

result: Use TLS/ACM for anything in transit, and KMS never answers those questions. For data at rest, let the service encrypt it and choose the key: SSE-S3/AWS-owned by default, a KMS key when you need audit/rotation/control, CloudHSM for dedicated hardware, SSE-C when you supply the key yourself. Call KMS APIs yourself only when your code encrypts before sending (≤4 KB: `Encrypt`, larger: `GenerateDataKey`). The examples come from about 20 questions in `questions_answers.md`.













===================================================================================================================================================
Several of them do, but each plays a different part. **CloudFront and the ALB actually do the TLS encryption. ACM supplies the certificate they use. Route 53 doesn't touch TLS at all;** it only handles DNS (with one small helping role, below).

## Who does what

| Service                           | Role in SSL/TLS                                                                                     | Analogy                              |
| --------------------------------- | --------------------------------------------------------------------------------------------------- | ------------------------------------ |
| **ACM** (AWS Certificate Manager) | **Issues, stores and auto-renews certificates.** It never handles traffic itself.                   | The **ID card office**               |
| **CloudFront**                    | **Terminates TLS** with users. It does the handshake and decrypts, using an ACM certificate.        | A **security guard** checking the ID |
| **ELB (ALB / NLB)**               | **Terminates TLS** on its HTTPS/TLS listener, using an ACM certificate                              | Another **security guard**           |
| **API Gateway**                   | **Terminates TLS** on its endpoint or custom domain, using an ACM certificate                       | Another security guard               |
| **Route 53**                      | **DNS only:** turns `www.example.com` into the address of CloudFront or the ALB. **No encryption.** | The **phone book**                   |

**Route 53's one TLS-related job:** when ACM issues a certificate with **DNS validation**, you add a CNAME record in Route 53 to prove you own the domain. In ACM that's a one-click "Create record in Route 53". Route 53 is just the place you prove domain ownership; it still doesn't encrypt anything.

## Each hop is its own TLS connection

```
            DNS lookup only
User ──────▶ Route 53 ("www.example.com → d123.cloudfront.net")

User ══TLS #1══▶ CloudFront ══TLS #2══▶ ALB ══TLS #3 (optional)══▶ EC2
      ▲                       ▲               ▲
  Viewer Protocol Policy   Origin Protocol    Target group protocol HTTPS
  + ACM cert (us-east-1)   Policy             (cert installed on the instance)
                           ALB listener uses
                           ACM cert (ALB's Region)
```

| Hop               | Who terminates TLS        | Where the certificate comes from                                      | Setting                                                            |
| ----------------- | ------------------------- | --------------------------------------------------------------------- | ------------------------------------------------------------------ |
| User → CloudFront | **CloudFront**            | ACM cert in **us-east-1**                                             | **Viewer Protocol Policy**                                         |
| CloudFront → ALB  | **ALB**                   | ACM cert in the **ALB's Region**                                      | **Origin Protocol Policy** (CloudFront) + **HTTPS listener** (ALB) |
| ALB → EC2         | **EC2** (your web server) | Your own cert on the instance; ACM certs **can't be exported** to EC2 | Target group protocol **HTTPS**                                    |

Most setups stop at the ALB: **SSL termination** on the ALB, plain HTTP inside the VPC. That's why your **S7 Q1/Q4** answer is "certificate on the ELB + SSL termination": it takes the encryption work off the EC2 CPUs.

## How this maps to your questions

| Your question                                                    | Who handles TLS                                      | ACM's role                               | Route 53's role                           |
| ---------------------------------------------------------------- | ---------------------------------------------------- | ---------------------------------------- | ----------------------------------------- |
| **S7 Q1/Q4**: SSL behind an ELB, no CPU impact                   | **ELB**                                              | Provides the certificate                 | —                                         |
| **S7 Q6**: subdomains on one HTTPS listener                      | **ALB**, using SNI                                   | Holds the certificates                   | —                                         |
| **S15 Q1/Q2**: users ↔ CloudFront ↔ origin                       | **CloudFront** (both protocol policies) + the origin | Provides the certificate                 | —                                         |
| **S15 Q5**: HTTPS for an S3 static website                       | **CloudFront** (S3 website endpoints can't do HTTPS) | Certificate in us-east-1                 | Alias record pointing at CloudFront       |
| **S9 Q2**: custom domain for API Gateway with a third-party cert | **API Gateway**                                      | **Import** the third-party cert into ACM | **Alias (A) record** to the custom domain |

## Exam rules of thumb

- "**Where do I get, import or renew** a certificate?" → **ACM**
- "**Who encrypts or decrypts** the traffic?" → **CloudFront, ALB/NLB or API Gateway**
- "**Offload SSL from EC2**" → **SSL termination on the ELB**
- "**Encrypt between CloudFront and users/origin**" → **Viewer / Origin Protocol Policy**
- "**Point my domain at CloudFront/ALB/API Gateway**" → **Route 53 alias record** (DNS, not encryption)
- "**Prove domain ownership for a certificate**" → **ACM DNS validation**, with the CNAME added in **Route 53**
- **Certificate Region:** CloudFront or edge-optimized API → **us-east-1**. ALB/NLB or Regional API → **same Region**.

result: CloudFront, ELB (ALB/NLB) and API Gateway do the actual TLS encryption, each on its own hop; ACM only issues, imports and renews the certificates they use; Route 53 is DNS only (alias records, plus the CNAME for ACM domain validation) and never encrypts traffic.