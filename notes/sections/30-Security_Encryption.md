# 🔐 Section 30: AWS Security & Encryption: KMS, Encryption SDK, SSM Parameter Store — Study Guide

Slides 826–870 ([open slides](../../AWS_Certified_Developer_Slides_v45.pdf#page=826)) · Sections follow the slide order

> IAM & STS (Advanced Identity) are on slides 804–825 — see Section 29.

---

## 🧠 The Mental Model (read this first)

This section answers **three questions**:

| # | Question | Services |
|---|---|---|
| 1 | **Where/when is data encrypted?** | In flight (TLS) · server-side at rest · client-side |
| 2 | **Who holds and uses the keys?** | **KMS** (AWS manages software, multi-tenant) vs **CloudHSM** (you manage keys on dedicated hardware) |
| 3 | **Where do I store secrets & config?** | **SSM Parameter Store** ($, simple) vs **Secrets Manager** ($$$, rotation) |

### 🔑 The single most tested idea

```
Data ≤ 4 KB  ──▶ KMS Encrypt / Decrypt API directly
Data  > 4 KB ──▶ Envelope Encryption  ==  GenerateDataKey  (or the Encryption SDK, which does it for you)
```

---

## 1️⃣ Why Encryption? — slides [827](../../AWS_Certified_Developer_Slides_v45.pdf#page=827)–829

| Type | Who encrypts | Who decrypts | Key point |
|---|---|---|---|
| **In flight (TLS/SSL)** | Sender | Receiver | HTTPS; prevents **MITM** attacks |
| **Server-side at rest** | **Server** after receiving | **Server** before sending | Server must have access to the **data key** (e.g. S3) |
| **Client-side** | **Client** | Receiving **client** | ⭐ **Server can never decrypt**; can use envelope encryption; works with any storage (S3, FTP…) |

**Keyword map:** "server must never be able to decrypt" → **client-side encryption**.

---

## 2️⃣ AWS KMS Overview — slides [830](../../AWS_Certified_Developer_Slides_v45.pdf#page=830)–832

- "Encryption" for an AWS service → almost always **KMS**
- AWS manages keys; **IAM** controls authorization; **CloudTrail** audits key usage
- Integrated with EBS, S3, RDS, SSM…
- ⚠️ **Never store secrets in plaintext** in code — encrypted secrets can live in code / **environment variables**
- Usable via **API calls** (SDK, CLI)

### Key types (cryptography)
| | **Symmetric (AES-256)** | **Asymmetric (RSA & ECC)** |
|---|---|---|
| Keys | **One key** encrypts and decrypts | **Public** (encrypt/verify) + **private** (decrypt/sign) |
| Used by | ⭐ **All AWS services integrated with KMS** | Encrypt/Decrypt or **Sign/Verify** |
| Access | Never get the key unencrypted — must call KMS API | **Public key downloadable**; private key never exposed |
| Use case | Default choice | ⭐ **Encryption outside AWS by users who can't call the KMS API** |

> "KMS Keys" is the new name for **CMK** (Customer Master Key).

### Key types (ownership) & pricing
| Type | Example | Cost |
|---|---|---|
| **AWS owned** | SSE-S3, SSE-SQS, SSE-DDB (default) | Free |
| **AWS managed** | `aws/rds`, `aws/ebs` | Free |
| **Customer managed (created in KMS)** | Your own key | **$1/month** |
| **Customer managed (imported)** | Your key material | **$1/month** |
| + API calls | — | **$0.03 / 10,000 calls** |

### Key rotation
| Key type | Rotation |
|---|---|
| **AWS managed** | **Automatic every 1 year** |
| **Customer managed** | **Must be enabled** — automatic & on-demand |
| **Imported** | ⚠️ **Manual only**, using an **alias** |

---

## 3️⃣ KMS Key Policies & Copying Snapshots — slides [833](../../AWS_Certified_Developer_Slides_v45.pdf#page=833)–835

### Copying snapshots across regions
```
eu-west-2: Snapshot (KMS Key A) ──copy + KMS ReEncrypt──▶ ap-southeast-2: Snapshot (KMS Key B)
```
⭐ KMS keys are **regional** → the snapshot is **re-encrypted with a key in the destination region**.

### Key Policies
- Control access to KMS keys, "similar" to S3 bucket policies
- ⭐ Difference: **you cannot control access without them**
- **Default key policy:** complete access for the **root user = entire AWS account** (then IAM policies decide)
- **Custom key policy:** define users/roles that can **use** and **administer** the key — useful for **cross-account**

### Copying snapshots across accounts (5 steps)
1. Snapshot encrypted with **your own customer managed key**
2. Attach a **KMS key policy** authorizing cross-account access
3. **Share** the encrypted snapshot
4. In the target account: **copy** the snapshot, encrypt with a key **in that account**
5. Create a volume from the snapshot

> ⚠️ Can't do this with an **AWS managed key** (you can't edit its key policy).

---

## 4️⃣ How KMS Works — Encrypt & Decrypt API — slide [836](../../AWS_Certified_Developer_Slides_v45.pdf#page=836)

```
Secret (< 4 KB) ──Encrypt API──▶ KMS [check IAM, encrypt with CMK] ──▶ Encrypted secret
Encrypted secret ──Decrypt API──▶ KMS [check IAM, decrypt with CMK] ──▶ Plaintext secret
```
- Every call **checks IAM permissions**
- ⭐ Limit: **4 KB** of data

---

## 5️⃣ Envelope Encryption — slides [837](../../AWS_Certified_Developer_Slides_v45.pdf#page=837)–839

- KMS `Encrypt` limit = **4 KB** → anything bigger needs **Envelope Encryption**
- ⭐ Exam: **> 4 KB == Envelope Encryption == `GenerateDataKey` API**

### Encrypt (client side)
```
1. GenerateDataKey ──▶ KMS returns:  Plaintext DEK  +  Encrypted DEK (encrypted with CMK)
2. Encrypt the big file locally with the Plaintext DEK
3. Store "envelope" = Encrypted file + Encrypted DEK   (discard the plaintext DEK)
```

### Decrypt (client side)
```
1. Send Encrypted DEK ──Decrypt API──▶ KMS returns Plaintext DEK
2. Decrypt the big file locally with the Plaintext DEK
```

**Memory trick:** *KMS only ever encrypts the small key (the DEK); your code encrypts the big data.*

---

## 6️⃣ Encryption SDK — slides [840](../../AWS_Certified_Developer_Slides_v45.pdf#page=840)–841

- ⭐ **Implements envelope encryption for you**
- Also available as a **CLI tool**; Java, Python, C, JavaScript
- Stores the **encrypted DEK inside the returned ciphertext**
- **Data Key Caching:** reuse data keys instead of creating new ones each time
  - ✅ Fewer KMS calls (cost, throttling) · ⚠️ security trade-off
  - Uses **`LocalCryptoMaterialsCache`** (max age, max bytes, max number of messages)

---

## 7️⃣ KMS Symmetric — API Summary — slide [842](../../AWS_Certified_Developer_Slides_v45.pdf#page=842)

| API | Does | Use when |
|---|---|---|
| `Encrypt` | Encrypts **≤ 4 KB** through KMS | Small secrets |
| `GenerateDataKey` | Returns **plaintext DEK + encrypted DEK** | ⭐ Encrypt **> 4 KB now** (envelope) |
| `GenerateDataKeyWithoutPlaintext` | Returns **only the encrypted DEK** | Need a DEK **later**, not now (must call `Decrypt` later) |
| `Decrypt` | Decrypts **≤ 4 KB** (including DEKs) | Reverse of Encrypt / unwrap a DEK |
| `GenerateRandom` | Random byte string | Randomness |
| `ReEncrypt` *(slides 833, 844)* | Re-encrypt under a different key | Cross-region snapshot copy |

---

## 8️⃣ KMS Request Quotas — slides [843](../../AWS_Certified_Developer_Slides_v45.pdf#page=843)–844

- Over the quota → **`ThrottlingException`**
- Fix: ⭐ **exponential backoff** (backoff & retry)
- Cryptographic operations **share one quota** — ⚠️ **including calls AWS makes for you** (e.g. **SSE-KMS** on S3)
- For `GenerateDataKey` → **DEK caching** (Encryption SDK)
- Request a **quota increase** via API or AWS Support

| Quota (shared, per second) | Value |
|---|---|
| Symmetric — most regions | 5,500 |
| Symmetric — some regions (us-east-2, ap-southeast-1/2, ap-northeast-1, eu-central-1, eu-west-2) | 10,000 |
| Symmetric — us-east-1, us-west-2, eu-west-1 | 30,000 |
| Asymmetric RSA / ECC | 500 / 300 |

---

## 9️⃣ S3 Bucket Key for SSE-KMS — slide [845](../../AWS_Certified_Developer_Slides_v45.pdf#page=845)

- Decreases **KMS API calls from S3 by 99%** and **KMS costs by 99%**
- A **bucket-level key** is generated from the KMS key → used to make **data keys** for objects
- You'll see **fewer KMS events in CloudTrail**

**Keyword map:** "SSE-KMS + throttling / high KMS cost on S3" → **S3 Bucket Key**.

---

## 🔟 Key Policy Examples & Principals — slides [846](../../AWS_Certified_Developer_Slides_v45.pdf#page=846)–848

- Examples: **default key policy** (account root) and a policy **allowing a federated user**
- **Principal options** in policies:
  - AWS **account & root user**
  - **IAM roles** and **IAM role sessions**
  - **IAM users**
  - **Federated user sessions**
  - **AWS services**
  - **All principals** (`*`)

---

## 1️⃣1️⃣ CloudHSM — slides [849](../../AWS_Certified_Developer_Slides_v45.pdf#page=849)–854

- **KMS** → AWS manages the **software**; **CloudHSM** → AWS provisions the **hardware**
- **Dedicated** HSM (Hardware Security Module) — ⭐ **you manage the keys entirely**
- Tamper resistant, **FIPS 140-2 Level 3**
- Symmetric **and** asymmetric (SSL/TLS keys); **no free tier**
- Must use the **CloudHSM Client Software**
- **Redshift** supports CloudHSM; good fit with **SSE-C**

### Who manages what
| AWS (via IAM) | You (via CloudHSM software) |
|---|---|
| Create/read/update/delete the HSM **cluster** | Manage the **keys** and **users** |

### High availability & integration
- Clusters spread **across multiple AZs**
- Integrates with AWS services through **KMS Custom Key Store** (EBS, S3, RDS…) — key usage logged in **CloudTrail**

### KMS vs CloudHSM
| Feature | KMS | CloudHSM |
|---|---|---|
| Tenancy | **Multi-tenant** | **Single-tenant** |
| Standard | FIPS 140-2 Level 3 | FIPS 140-2 Level 3 |
| Master keys | AWS owned / AWS managed / customer managed | Customer managed only |
| Key types | Symmetric, asymmetric, digital signing | + **hashing** |
| Key accessibility | Regional | In a **VPC**, shareable via **VPC peering** |
| Crypto acceleration | None | **SSL/TLS & Oracle TDE acceleration** |
| Access & auth | **IAM** | **You** create users & permissions |
| High availability | AWS managed | **Add HSMs across AZs** |
| Audit | CloudTrail, CloudWatch | CloudTrail, CloudWatch, **MFA support** |
| Free tier | Yes | **No** |

---

## 1️⃣2️⃣ SSM Parameter Store — slides [855](../../AWS_Certified_Developer_Slides_v45.pdf#page=855)–858

- Secure storage for **configuration and secrets**
- **Optional** KMS encryption (SecureString)
- Serverless, scalable, durable, easy SDK
- **Version tracking**, security through **IAM**, notifications via **EventBridge**, **CloudFormation** integration

### Hierarchy
```
/my-department/
    my-app/
        dev/   db-url, db-password     ◀── Dev Lambda
        prod/  db-url, db-password     ◀── Prod Lambda
/aws/reference/secretsmanager/<secret_id>          ◀── read a Secrets Manager secret via SSM
/aws/service/ami-amazon-linux-latest/...           ◀── public AWS parameters (latest AMI)
```
- ⭐ **`GetParametersByPath`** fetches a whole folder; `GetParameters` fetches specific names

### Tiers
| | Standard | Advanced |
|---|---|---|
| Max parameters (per account & region) | 10,000 | 100,000 |
| Max value size | **4 KB** | **8 KB** |
| Parameter policies | ❌ | ✅ |
| Cost | Free | **$0.05 / parameter / month** |

### Parameter Policies (advanced only)
- Assign a **TTL** to force updating/deleting sensitive data
- Multiple policies at once:
  - **Expiration** (delete the parameter)
  - **ExpirationNotification** (EventBridge)
  - **NoChangeNotification** (EventBridge)

---

## 1️⃣3️⃣ AWS Secrets Manager — slides [859](../../AWS_Certified_Developer_Slides_v45.pdf#page=859)–860

- Newer service meant for **secrets**
- ⭐ **Force rotation every X days**; generation on rotation uses **Lambda**
- Integrates with **RDS** (MySQL, PostgreSQL, Aurora)
- Secrets **encrypted with KMS** (mandatory)

### Multi-Region Secrets
- **Replicate** secrets across regions; replicas kept in sync with the primary
- **Promote** a replica to a standalone secret
- Use cases: multi-region apps, **disaster recovery**, multi-region DBs

---

## 1️⃣4️⃣ SSM Parameter Store vs Secrets Manager — slides [861](../../AWS_Certified_Developer_Slides_v45.pdf#page=861)–862

| | **Secrets Manager ($$$)** | **SSM Parameter Store ($)** |
|---|---|---|
| Rotation | ⭐ **Built-in automatic rotation** with Lambda | ❌ None built in — build it with **EventBridge + Lambda** |
| Rotation Lambda | **Provided** for RDS, Redshift, DocumentDB | You write it |
| KMS encryption | **Mandatory** | **Optional** |
| CloudFormation | ✅ | ✅ |
| API | Secrets-focused | **Simple API**; can read Secrets Manager secrets too |

**Keyword map:** "rotate database password automatically" → **Secrets Manager**. "Cheap config storage / hierarchy" → **Parameter Store**.

---

## 1️⃣5️⃣ CloudFormation — Dynamic References — slides [863](../../AWS_Certified_Developer_Slides_v45.pdf#page=863)–866

- Reference values from **Parameter Store** and **Secrets Manager** in templates
- CloudFormation resolves them during **create/update/delete**

| Prefix | For | Syntax |
|---|---|---|
| `ssm` | Plaintext SSM parameter | `{{resolve:ssm:parameter-name:version}}` |
| `ssm-secure` | **SecureString** SSM parameter | `{{resolve:ssm-secure:parameter-name:version}}` |
| `secretsmanager` | Secrets Manager secret | `{{resolve:secretsmanager:secret-id:secret-string:json-key:version-stage:version-id}}` |

### CloudFormation + Secrets Manager + RDS
| Option | How |
|---|---|
| **1. `ManageMasterUserPassword`** | RDS/Aurora **creates the admin secret implicitly** and manages it **and its rotation** in Secrets Manager |
| **2. Dynamic Reference** | (1) Generate the secret → (2) reference it in the DB instance → (3) **link the secret to the DB** (`SecretTargetAttachment`) for rotation |

---

## 1️⃣6️⃣ CloudWatch Logs Encryption — slide [867](../../AWS_Certified_Developer_Slides_v45.pdf#page=867)

- Encrypt logs with **KMS keys** at the **log group level**
- ⚠️ **Cannot be done in the CloudWatch console** — must use the **CloudWatch Logs API**:
  - **`associate-kms-key`** → log group **already exists**
  - **`create-log-group`** → log group **doesn't exist yet**

---

## 1️⃣7️⃣ CodeBuild Security — slide [868](../../AWS_Certified_Developer_Slides_v45.pdf#page=868)

- Access resources **in your VPC** → specify a **VPC configuration** for CodeBuild
- Secrets: ⚠️ **don't store them as plaintext environment variables**
- ⭐ Environment variables can **reference Parameter Store parameters** or **Secrets Manager secrets**

---

## 1️⃣8️⃣ AWS Nitro Enclaves — slides [869](../../AWS_Certified_Developer_Slides_v45.pdf#page=869)–870

- Process **highly sensitive data** (PII, healthcare, financial) in an **isolated compute environment**
- Fully isolated, hardened VMs — ⚠️ **not a container, no persistent storage, no interactive access, no external networking**
- **Cryptographic attestation** → only authorized code runs
- Only enclaves can access the sensitive data (**KMS integration**)
- Use cases: private keys, **credit card processing**, secure multi-party computation

### How to launch
1. Launch a Nitro-based EC2 instance with **`EnclaveOptions` = true**
2. Use the **Nitro CLI** to convert your app into an **Enclave Image File (EIF)**
3. Use the Nitro CLI with the EIF to **create the enclave**
4. The enclave is a separate VM with its **own kernel, memory, CPU**, talking to the parent instance over a **secure local channel**

---

## 🔢 Numbers Cheat Sheet

| Number | Meaning |
|---|---|
| **4 KB** | KMS `Encrypt`/`Decrypt` max · Standard parameter max |
| **8 KB** | Advanced parameter max |
| **10,000 / 100,000** | Standard / advanced parameters per account & region |
| **$1 / month** | Customer managed KMS key |
| **$0.03 / 10,000** | KMS API calls |
| **$0.05 / month** | Advanced parameter |
| **1 year** | AWS managed key auto-rotation |
| **99%** | S3 Bucket Key reduction in KMS calls & cost |
| **5,500 / 10,000 / 30,000** | Symmetric KMS quotas (by region) |
| **FIPS 140-2 Level 3** | Both KMS and CloudHSM |

---

## 🌳 Decision Tree

```
What does the question need?
│
├── Encrypt data...
│    ├── ≤ 4 KB                                ─▶ KMS Encrypt
│    ├── > 4 KB                                ─▶ GenerateDataKey (envelope) / Encryption SDK
│    ├── a key to use LATER                    ─▶ GenerateDataKeyWithoutPlaintext
│    ├── by users outside AWS                  ─▶ Asymmetric KMS key (public key)
│    └── server must never decrypt             ─▶ Client-side encryption
│
├── KMS throttling?
│    ├── general                               ─▶ Exponential backoff / quota increase
│    ├── lots of GenerateDataKey               ─▶ DEK caching (Encryption SDK)
│    └── S3 SSE-KMS                            ─▶ S3 Bucket Key
│
├── Manage keys myself on dedicated hardware?  ─▶ CloudHSM
│
├── Store a secret / config...
│    ├── auto-rotate DB password               ─▶ Secrets Manager
│    ├── multi-region / DR secret              ─▶ Secrets Manager multi-region
│    ├── cheap hierarchical config             ─▶ SSM Parameter Store
│    ├── > 4 KB or TTL/expiration              ─▶ Advanced parameter + parameter policy
│    └── use it in CloudFormation              ─▶ {{resolve:ssm|ssm-secure|secretsmanager:...}}
│
├── Encrypt CloudWatch Logs?                   ─▶ associate-kms-key / create-log-group (API, not console)
├── Secrets in CodeBuild?                      ─▶ Env vars referencing Parameter Store / Secrets Manager
└── Isolated processing of sensitive data?     ─▶ Nitro Enclaves
```

---

## 🚨 Top Exam Traps

1. **> 4 KB → Envelope Encryption → `GenerateDataKey`** (or the Encryption SDK) — never plain `Encrypt`.
2. **`GenerateDataKeyWithoutPlaintext`** = DEK for **later**; `GenerateDataKey` = encrypt **now**.
3. **AWS services use symmetric keys**; **asymmetric** = users **outside AWS** who can't call KMS.
4. **Imported keys can only be rotated manually (alias)**; AWS managed = **auto every year**; customer managed = **must enable**.
5. **KMS keys are regional** → cross-region snapshot copy = **ReEncrypt** with a key in the new region.
6. **Cross-account snapshot sharing needs a customer managed key + key policy** (not an AWS managed key).
7. **You cannot control access to a KMS key without a key policy** — default policy gives the **whole account (root)** access.
8. **ThrottlingException → exponential backoff**; SSE-KMS calls **count against your quota**; S3 → **Bucket Key**.
9. **KMS = multi-tenant, AWS manages software**; **CloudHSM = single-tenant, you manage keys and users**.
10. **Rotation built-in = Secrets Manager**; Parameter Store needs **EventBridge + Lambda**.
11. **KMS encryption: mandatory in Secrets Manager, optional in Parameter Store.**
12. **Parameter policies (TTL/expiration) & 8 KB values require the Advanced tier.**
13. **`ssm-secure`** for SecureStrings in CloudFormation — plain `ssm` is for plaintext.
14. **CloudWatch Logs encryption can't be set in the console** — use **`associate-kms-key`** / **`create-log-group`**.
15. **CodeBuild secrets → reference Parameter Store / Secrets Manager**, never plaintext env vars.
16. **Nitro Enclaves: no storage, no networking, no interactive access** — attestation + KMS.

---

## 💾 How to Use This Guide

1. Read the **Mental Model** — especially the **4 KB rule**.
2. Go top-to-bottom; it matches the slide order.
3. Cover the right-hand columns of tables and quiz yourself.
4. Finish with the **Decision Tree** and **Top Exam Traps**, then drill `quizzes/my_questions/30-Security_Encryption.md`.
