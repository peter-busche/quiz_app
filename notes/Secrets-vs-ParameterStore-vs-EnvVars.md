# 🗝️ Where Do I Store This Value? Secrets Manager vs Parameter Store vs Environment Variables

Built from your `questions_answers.md` and the slides — the pattern AWS keeps testing.

---

## 🧠 The Pattern (memorize this ladder)

AWS literally teaches the same 3-tier ladder in two places — **ECS** ([slide 338](../AWS_Certified_Developer_Slides_v45.pdf#page=338)) and **CodeBuild** ([slide 717](../AWS_Certified_Developer_Slides_v45.pdf#page=717)):

| Slide 338 — ECS | Slide 717 — CodeBuild `buildspec.yml` `env:` |
|---|---|
| **Hardcoded** — e.g. URLs | **`variables`** — plaintext |
| **SSM Parameter Store** — sensitive variables (e.g. **API keys, shared configs**) | **`parameter-store`** |
| **Secrets Manager** — sensitive variables (e.g. **DB passwords**) | **`secrets-manager`** |

Add one rung at the bottom that your questions test, and you get the full ladder:

```
        MORE sensitive / more features / more $$$
                          ▲
  ③ SECRETS MANAGER       │  DB passwords · ROTATION · RDS integration · "MOST secure"
                          │
  ② PARAMETER STORE       │  shared / hierarchical config · API keys without rotation · cheap
                          │
  ① ENVIRONMENT VARIABLE  │  non-sensitive, per-function/container config · simplest · no extra call
                          │
  ⓪ IAM ROLE              │  AWS credentials (access keys) → DON'T STORE THEM AT ALL
                          ▼
```

### 🎯 The 4 questions to ask, in order

```
1. Is it an AWS access key / AWS credential?           ──YES──▶ ⓪ IAM ROLE (never store it)
                │ no
2. Must it ROTATE automatically? Is it a DB password?   ──YES──▶ ③ SECRETS MANAGER
   Does the question say "MOST secure"?
                │ no
3. Is it SHARED across apps/environments, HIERARCHICAL, ──YES──▶ ② PARAMETER STORE
   centrally managed, or sensitive-but-cheap?                    (SecureString if sensitive)
                │ no
4. Simple, non-sensitive, belongs to ONE function/container ───▶ ① ENVIRONMENT VARIABLE
```

---

## ⓪ IAM Role — when the "secret" is an AWS credential

**Rule:** AWS access keys never go in code, env vars, Parameter Store, or Secrets Manager. Give the compute an **IAM role** (instance profile, Lambda execution role, ECS task role).

| Your question | Answer | Lesson |
|---|---|---|
| **S29 Q1** — EC2 app uses access keys **stored in environment variables**; dev attached a restrictive IAM role but the app can still write to all buckets | **The credential provider looks for instance profile credentials last** | Env-var keys **override** the role in the SDK credential chain. Fix: **delete the keys, use only the role.** |
| **S15 Q4** — role credentials in **plaintext in a Python file** | Move the SDK calls to **Lambda@Edge** whose **execution role** has the STS permissions | Remove stored credentials; let a **role** provide them |

**SDK credential chain (simplified):** code/explicit → **environment variables** → shared credentials file → container (ECS task role) → **instance profile (last)**.

---

## ① Environment Variables — simple, per-resource, non-sensitive config

**Use when:** the value is **not sensitive** (or is only lightly sensitive and encrypted), belongs to **one** function/container/environment, and you want **zero extra API calls** (lowest latency, simplest).

| Where | How | Slide |
|---|---|---|
| **Lambda** | Function environment variables (String key/value, **4 KB** total, KMS-encrypted at rest) | [561](../AWS_Certified_Developer_Slides_v45.pdf#page=561), [600](../AWS_Certified_Developer_Slides_v45.pdf#page=600) |
| **ECS** | `environment` in the **task definition** | [334](../AWS_Certified_Developer_Slides_v45.pdf#page=334), [338](../AWS_Certified_Developer_Slides_v45.pdf#page=338) |
| **ECS (bulk)** | **Environment files from S3** | [338](../AWS_Certified_Developer_Slides_v45.pdf#page=338) |
| **CodeBuild** | `env: variables:` (plaintext) | [717](../AWS_Certified_Developer_Slides_v45.pdf#page=717) |
| **Elastic Beanstalk** | Environment properties (kept when **cloning**) | [375](../AWS_Certified_Developer_Slides_v45.pdf#page=375) |
| **API Gateway** | **Stage variables** = "environment variables for API Gateway" → passed to Lambda's **context** | [665](../AWS_Certified_Developer_Slides_v45.pdf#page=665) |

| Your question | Answer | Lesson |
|---|---|---|
| **S16 Q14** — Fargate container needs env vars to initialize | Define them under **`environment` in the task definition** | Non-sensitive config → plain env var |
| **S21 Q10** — Lambda env vars with **secret values** must be **hidden in the console/API even from key users**, **MINIMIZE complexity & latency** | **Encrypt client-side with the encryption helpers** (KMS) | "Minimize latency" + secret in a Lambda env var → keep the env var, **encrypt it with helpers** (not a Secrets Manager call) |

> ⚠️ Lambda env vars are encrypted **at rest** by default, but anyone with `lambda:GetFunctionConfiguration` sees them **in plaintext in the console**. "Obscure in the console" → **encryption helpers**.

Best practice slide [601](../AWS_Certified_Developer_Slides_v45.pdf#page=601): use env vars for **DB connection strings, S3 bucket names**; passwords/sensitive values **encrypted with KMS**.

---

## ② SSM Parameter Store — shared, hierarchical, cheap config

**Use when:** config is **shared** across functions/services/environments, needs a **hierarchy** (`/app/dev/...`, `/app/prod/...`), **versioning**, **central management**, or a **sensitive value that does NOT need rotation** and you want it **cheap**.

| Feature | Detail | Slide |
|---|---|---|
| Plaintext **or SecureString** (KMS optional) | Encryption is **optional** | [855](../AWS_Certified_Developer_Slides_v45.pdf#page=855) |
| **Hierarchy** + `GetParametersByPath` | Dev/prod folders per app | [856](../AWS_Certified_Developer_Slides_v45.pdf#page=856) |
| **Free** standard tier (4 KB, 10,000 params) / advanced (8 KB, policies, $0.05) | Cheapest option | [857](../AWS_Certified_Developer_Slides_v45.pdf#page=857) |
| **Parameter policies** — TTL / expiration notifications (advanced) | Force updates, but **not rotation** | [858](../AWS_Certified_Developer_Slides_v45.pdf#page=858) |
| **No built-in rotation** (DIY with EventBridge + Lambda) | | [861](../AWS_Certified_Developer_Slides_v45.pdf#page=861) |
| Can **read Secrets Manager secrets** via `/aws/reference/secretsmanager/...` | One API for both | [856](../AWS_Certified_Developer_Slides_v45.pdf#page=856) |
| **Public AWS parameters** (e.g. latest Amazon Linux AMI ID) | `/aws/service/...` | [856](../AWS_Certified_Developer_Slides_v45.pdf#page=856) |
| **CloudWatch Unified Agent** config is centralized in Parameter Store | | [484](../AWS_Certified_Developer_Slides_v45.pdf#page=484) |
| CloudFormation **SSM Parameter type** / `{{resolve:ssm:...}}` / `{{resolve:ssm-secure:...}}` | | [395](../AWS_Certified_Developer_Slides_v45.pdf#page=395), [864](../AWS_Certified_Developer_Slides_v45.pdf#page=864) |

**Keyword triggers:** *shared configuration*, *hierarchy*, *centralized*, *per environment (dev/prod)*, *version history*, *least cost / free*, *API key or license key with no rotation requirement*, *latest AMI ID*.

---

## ③ Secrets Manager — rotation, DB credentials, maximum security

**Use when:** the value is a **secret** (especially **database credentials**) and the question mentions **rotation**, **RDS/Aurora/Redshift/DocumentDB**, **cross-region replication**, or **"MOST secure"**.

| Feature | Detail | Slide |
|---|---|---|
| ⭐ **Automatic rotation every X days** (Lambda; provided for RDS, Redshift, DocumentDB) | The #1 differentiator | [859](../AWS_Certified_Developer_Slides_v45.pdf#page=859), [861](../AWS_Certified_Developer_Slides_v45.pdf#page=861)–[862](../AWS_Certified_Developer_Slides_v45.pdf#page=862) |
| **RDS integration** (MySQL, PostgreSQL, Aurora) | | [859](../AWS_Certified_Developer_Slides_v45.pdf#page=859) |
| **KMS encryption mandatory** | | [861](../AWS_Certified_Developer_Slides_v45.pdf#page=861) |
| **Multi-Region secrets** (replicas, promote for DR) | | [860](../AWS_Certified_Developer_Slides_v45.pdf#page=860) |
| RDS **`ManageMasterUserPassword`** creates and rotates the admin secret for you | | [865](../AWS_Certified_Developer_Slides_v45.pdf#page=865) |
| **RDS Proxy** stores DB credentials in Secrets Manager | | [152](../AWS_Certified_Developer_Slides_v45.pdf#page=152) |
| **$$$** — costs more than Parameter Store | | [861](../AWS_Certified_Developer_Slides_v45.pdf#page=861) |

| Your question | Trigger words | Answer |
|---|---|---|
| **S30 Q1** — RDS SQL Server credentials out of code, **automatically rotates**, **MOST secure** | *rotate* + *MOST secure* + *DB* | **Secrets Manager**, retrieve as needed |
| **S30 Q4** — Lambda + RDS connection string, **rotation every 30 days**, **SIMPLEST** | *rotation* | **Secrets Manager** with automatic rotation |
| **S30 Q7** — Lambda + RDS PostgreSQL, **rotate every week** | *rotate* | **Secrets Manager** with weekly rotation |
| **S30 Q8** — partner **API key** managed through code, **maximum security** | *maximum security* | **Secrets Manager** |

> ⚠️ **S30 Q8 vs slide 338:** slide 338 puts *API keys* in Parameter Store, but the question says **"maximum security"** → Secrets Manager wins. **"MOST/maximum secure" beats "cheapest"** as a tie-breaker.

---

## 🔌 How Each Service Consumes All Three

| Service | Env var (plain) | Parameter Store | Secrets Manager |
|---|---|---|---|
| **Lambda** | Function env vars | SDK `GetParameter(s)` in code (init outside handler) | SDK `GetSecretValue` in code |
| **ECS** | Task def `environment` / env files in S3 | Task def `secrets` → `valueFrom` = parameter ARN | Task def `secrets` → `valueFrom` = secret ARN |
| **CodeBuild** | `env: variables:` | `env: parameter-store:` | `env: secrets-manager:` |
| **CloudFormation** | `Parameters` (with `NoEcho`) | `AWS::SSM::Parameter::Value<String>` / `{{resolve:ssm:…}}` / `{{resolve:ssm-secure:…}}` | `{{resolve:secretsmanager:…}}` / `ManageMasterUserPassword` |
| **Elastic Beanstalk** | Environment properties | — (read in code) | — (read in code) |
| **API Gateway** | Stage variables | — | — |

> ⚠️ ECS: the role that fetches `secrets` for the container at startup needs `ssm:GetParameters` / `secretsmanager:GetSecretValue` (and `kms:Decrypt` if a customer managed key is used) — slide [321](../AWS_Certified_Developer_Slides_v45.pdf#page=321): *"Reference sensitive data in Secrets Manager or SSM Parameter Store."*

---

## 🔑 Keyword → Answer Cheat Sheet

| The question says… | Answer |
|---|---|
| **rotate / rotation / every N days** | **Secrets Manager** (always) |
| **database password / DB credentials / RDS** | **Secrets Manager** |
| **MOST / maximum secure** | **Secrets Manager** |
| **multi-region / DR secret** | **Secrets Manager** (replication) |
| **shared configuration / centralized / hierarchy / dev & prod paths** | **Parameter Store** |
| **least cost / free** + sensitive, **no rotation** | **Parameter Store SecureString** |
| **latest AMI ID** | **Parameter Store** public parameters |
| **CloudWatch agent config** | **Parameter Store** |
| **simple / minimize latency / per function** + non-sensitive | **Environment variable** |
| **hide secret env var in Lambda console** | **Env var + KMS encryption helpers** |
| **pass variables to an ECS container** | **Task definition `environment`** (or `secrets` for sensitive) |
| **different backend per API stage** | **API Gateway stage variables** |
| **AWS access keys / credentials in code or env vars** | **IAM role** — remove the keys |
| **plaintext secret in code** | Move it out: Secrets Manager / Parameter Store / role |

---

## ⚖️ Side-by-Side Summary

| | ① Env Vars | ② Parameter Store | ③ Secrets Manager |
|---|---|---|---|
| Best for | Non-sensitive, per-resource config | Shared/hierarchical config, cheap secrets | DB creds, rotating secrets |
| Encryption | KMS at rest (Lambda); plaintext elsewhere | **Optional** (SecureString) | **Mandatory** KMS |
| Rotation | ❌ | ❌ (DIY EventBridge + Lambda) | ✅ **Built in** |
| Sharing across services | ❌ copied per resource | ✅ | ✅ |
| Versioning | Via function/task versions | ✅ | ✅ (staging labels) |
| Size | Lambda 4 KB total | 4 KB / 8 KB | 64 KB |
| Cost | Free | Free (standard) / $0.05 adv. | **$$$** per secret + API calls |
| Extra API call at runtime | ❌ None | ✅ | ✅ |
| Cross-region | ❌ | ❌ | ✅ Replication |

---

## 🚨 Top Exam Traps

1. **"Rotate" anywhere in the question → Secrets Manager.** Parameter Store has **no built-in rotation** (parameter policies only expire/notify).
2. **AWS access keys never get stored** — not in env vars, not in Secrets Manager. Use an **IAM role**. Env-var keys **override** the instance profile (S29 Q1).
3. **"MOST secure" beats "cheapest"** — API key + maximum security → Secrets Manager (S30 Q8).
4. **KMS: mandatory in Secrets Manager, optional in Parameter Store.**
5. **Lambda env var secrets visible in the console → encryption helpers**, not a new service (S21 Q10, "minimize latency").
6. **Parameter Store can read Secrets Manager secrets** via `/aws/reference/secretsmanager/<id>`.
7. **CloudFormation:** `ssm` = plaintext, `ssm-secure` = SecureString, `secretsmanager` = secret; RDS admin password → **`ManageMasterUserPassword`**.
8. **CodeBuild/ECS:** never put secrets in plaintext env vars — reference **Parameter Store / Secrets Manager**.
9. **Env var limit (Lambda) = 4 KB**; standard parameter = 4 KB, advanced = 8 KB.
