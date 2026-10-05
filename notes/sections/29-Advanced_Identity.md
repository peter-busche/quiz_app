# 🪪 Section 29: Advanced Identity — Study Guide

Slides 804–825 ([open slides](../../AWS_Certified_Developer_Slides_v45.pdf#page=804)) · Sections follow the slide order

> Slide 826 starts Section 30 (Security & Encryption) — see `30-Security_Encryption.md`.

---

## 🧠 The Mental Model (read this first)

Advanced Identity answers **four questions**:

| # | Question | Tool | Section |
|---|---|---|---|
| 1 | **How do I get *temporary* credentials?** | **AWS STS** (AssumeRole, GetSessionToken…) | 1️⃣–3️⃣ |
| 2 | **Is this request allowed?** | **Policy evaluation**: explicit DENY → ALLOW → default DENY (IAM ∪ resource policies) | 5️⃣–6️⃣ |
| 3 | **How do I write policies that scale?** | **Policy variables** (`${aws:username}`), **customer managed** policies | 7️⃣–8️⃣ |
| 4 | **How do I let a service act for me / use corporate logins?** | **`iam:PassRole`** + trust policy · **Directory Services** | 9️⃣–🔟 |

### 🔑 The rule that answers most questions
> **Long-term credentials are bad. Temporary credentials from STS (via roles) are good.**
> Root → never. Access keys on servers → never (except a personal computer). Everything else → **roles + STS**.

---

## 1️⃣ AWS STS — Security Token Service — slide [805](../../AWS_Certified_Developer_Slides_v45.pdf#page=805)

Grants **limited and temporary** access to AWS resources (up to **1 hour** per the course).

| API | Use for | Exam keyword |
|---|---|---|
| ⭐ **`AssumeRole`** | Assume a role **in your account or cross-account** | "cross-account", "temporary access to another account" |
| **`AssumeRoleWithSAML`** | Credentials for users logged in with **SAML** | "SAML", "corporate IdP / ADFS" |
| **`AssumeRoleWithWebIdentity`** | Credentials for users logged in with an IdP (**Facebook, Google, OIDC**) — ⚠️ **AWS recommends Cognito Identity Pools instead** | "web identity", "social login" |
| ⭐ **`GetSessionToken`** | Temp credentials **with MFA**, for an IAM user or root | "**MFA** required for API calls" |
| **`GetFederationToken`** | Temp credentials for a **federated user** | "federated user" |
| ⭐ **`GetCallerIdentity`** | Details about the **IAM user/role making the call** | "which identity am I using?" |
| ⭐ **`DecodeAuthorizationMessage`** | **Decode** the error message when an API call is **denied** | "**encoded authorization failure message**" |

### Your questions
| Question | Answer |
|---|---|
| **S29 Q2** — `UnauthorizedOperation` with an **encoded authorization failure message**, make it human-readable | **`aws sts decode-authorization-message`** |
| **S12 Q3** — IAM user credentials **require MFA for all API calls** | **`GetSessionToken`** |

---

## 2️⃣ Using STS to Assume a Role (incl. Cross-Account) — slides [806](../../AWS_Certified_Developer_Slides_v45.pdf#page=806)–807, [811](../../AWS_Certified_Developer_Slides_v45.pdf#page=811)

```
User/role ──AssumeRole API──▶ AWS STS ──▶ temporary security credentials
                                           (permissions of the target role)
                                                     │
                                                     ▼
                                   Role in SAME account or ANOTHER account
```

**Steps:**
1. **Define an IAM role** in your account or the other account
2. **Define which principals can access the role** (the role's **trust policy**)
3. Call **STS `AssumeRole`** → get credentials and **impersonate** the role
4. Temporary credentials valid **15 minutes to 1 hour** (per the course)

### Cross-account checklist
| Account | Needs |
|---|---|
| **Target account** (e.g. Production) | A role whose **trust policy** names the source account/user |
| **Source account** (e.g. Development) | The user's IAM policy allows **`sts:AssumeRole`** on that role ARN |

**Your S29 Q3:** developer in **Dev account** must modify resources in **Prod**, MOST secure, temporary → **cross-account role + `sts:AssumeRole`** (short-lived credentials)

---

## 3️⃣ STS with MFA — slide [808](../../AWS_Certified_Developer_Slides_v45.pdf#page=808)

- Use **`GetSessionToken`** from STS
- Protect APIs with an IAM policy **condition**: **`aws:MultiFactorAuthPresent: true`**
- `GetSessionToken` returns:
  - **Access ID**
  - **Secret Key**
  - **Session Token**
  - **Expiration date**

```json
{
  "Effect": "Allow",
  "Action": "ec2:StopInstances",
  "Resource": "*",
  "Condition": { "Bool": { "aws:MultiFactorAuthPresent": "true" } }
}
```

---

## 4️⃣ IAM Best Practices — slides [809](../../AWS_Certified_Developer_Slides_v45.pdf#page=809)–811

### General
- ⭐ **Never use root credentials**; enable **MFA on root**
- ⭐ **Least privilege** — never grant `"*"` access to a service
- Monitor API calls in **CloudTrail** (especially **denied** ones)
- ⭐ **Never store IAM keys** on any machine except a **personal computer or on-premises server**
- On-premises server best practice → **call STS for temporary credentials**

### IAM roles — one per workload
| Service | Role |
|---|---|
| **EC2** | Its own **instance role** |
| **Lambda** | Its own **execution role** |
| **ECS tasks** | Their own **task role** (`ECS_ENABLE_TASK_IAM_ROLE=true`) |
| **CodeBuild** | Its own **service role** |
| Any service | A **least-privileged role** |

> ⭐ **One role per application / Lambda function — don't reuse roles.**

### Cross-account access
Same pattern as section 2️⃣: role in the other account → define who can assume it → **`AssumeRole`**.

---

## 5️⃣ Authorization Model — Policy Evaluation — slide [812](../../AWS_Certified_Developer_Slides_v45.pdf#page=812)

```
Decision starts at DENY
        │
        ▼
Evaluate ALL applicable policies
        │
        ├── Explicit DENY?  ──yes──▶ ❌ Final: DENY
        │        no
        ├── ALLOW?          ──yes──▶ ✅ Final: ALLOW
        │        no
        └──────────────────────────▶ ❌ Final: DENY (implicit)
```

> ⭐ **Explicit Deny always wins.** No allow anywhere = implicit deny.

---

## 6️⃣ IAM Policies & S3 Bucket Policies — slides [813](../../AWS_Certified_Developer_Slides_v45.pdf#page=813)–817

- IAM policies → attached to **users, roles, groups**
- S3 bucket policies → attached to **buckets**
- ⭐ AWS evaluates the **UNION** of the principal's IAM policies **and** the bucket policy

| # | EC2 instance role (IAM) | Bucket policy | Result |
|---|---|---|---|
| 1 | Allows RW on `my_bucket` | None | ✅ **Can** read/write |
| 2 | Allows RW | ⚠️ **Explicit deny** to the role | ❌ **Cannot** |
| 3 | **No** S3 permissions | **Explicit allow** RW to the role | ✅ **Can** read/write |
| 4 | ⚠️ **Explicit deny** | Explicit allow RW | ❌ **Cannot** |

> Pattern: **any explicit deny → denied**; otherwise **an allow on either side → allowed** (same account).

---

## 7️⃣ Dynamic Policies with IAM — slides [818](../../AWS_Certified_Developer_Slides_v45.pdf#page=818)–819

**Goal:** give every user their own `/home/<user>` folder in an S3 bucket.

| Option | How | Verdict |
|---|---|---|
| 1 | One IAM policy **per user** (`georges` → `/home/georges`, `sarah` → `/home/sarah`…) | ❌ **Doesn't scale** |
| 2 | ⭐ **One dynamic policy** using the policy variable **`${aws:username}`** | ✅ |

```json
{
  "Effect": "Allow",
  "Action": ["s3:GetObject", "s3:PutObject", "s3:DeleteObject"],
  "Resource": "arn:aws:s3:::my-bucket/home/${aws:username}/*"
}
```

**Keyword map:** "each user only accesses **their own** folder", "single policy for all users" → **`${aws:username}`** policy variable.

---

## 8️⃣ Inline vs Managed Policies — slide [820](../../AWS_Certified_Developer_Slides_v45.pdf#page=820)

| | **AWS Managed** | **Customer Managed** | **Inline** |
|---|---|---|---|
| Maintained by | **AWS** | **You** | You |
| Updated | Automatically for new services/APIs | You control | You control |
| Reusable | ✅ | ✅ **Many principals** | ❌ **Strict 1:1** with one principal |
| Versioning | — | ✅ **Version control + rollback** | ❌ |
| Change management | — | ✅ **Central** | ❌ |
| Delete the principal | Policy remains | Policy remains | ⚠️ **Policy is deleted too** |
| Best for | Power users / admins | ⭐ **Best practice** | Strict one-off permissions |

---

## 9️⃣ Passing a Role to an AWS Service (`iam:PassRole`) — slides [821](../../AWS_Certified_Developer_Slides_v45.pdf#page=821)–823

- Many services need an IAM role **passed to them during setup** (happens **once**); the service later **assumes** it
- Examples: passing a role to an **EC2 instance**, a **Lambda function**, an **ECS task**, **CodePipeline**
- ⭐ The **person doing the setup** needs **`iam:PassRole`** (often with **`iam:GetRole`** to view it)

```json
{
  "Effect": "Allow",
  "Action": ["iam:GetRole", "iam:PassRole"],
  "Resource": "arn:aws:iam::123456789012:role/S3Access"
}
```

### Can a role be passed to any service? — slide 823
❌ **No.** A role can only be passed to a service its **trust policy** allows:

```json
{
  "Effect": "Allow",
  "Principal": { "Service": "lambda.amazonaws.com" },
  "Action": "sts:AssumeRole"
}
```

| Missing piece | Symptom |
|---|---|
| Your user lacks **`iam:PassRole`** | AccessDenied when creating the Lambda/EC2/ECS resource with a role |
| Role's **trust policy** doesn't allow the service | Service can't assume the role |

---

## 🔟 Microsoft Active Directory & AWS Directory Services — slides [824](../../AWS_Certified_Developer_Slides_v45.pdf#page=824)–825

### What is Microsoft AD?
- Found on any **Windows Server with AD Domain Services**
- Database of **objects**: user accounts, computers, printers, file shares, security groups
- **Centralized security management** — create accounts, assign permissions
- Objects organized in **trees**; a group of trees is a **forest**

### AWS Directory Services
| Option | What it is | Users managed in | Connects to on-prem AD? | MFA |
|---|---|---|---|---|
| ⭐ **AWS Managed Microsoft AD** | Your **own AD in AWS** | **AWS** (locally) | ✅ **Trust** relationship | ✅ |
| ⭐ **AD Connector** | **Directory gateway (proxy)** redirecting to on-prem AD | **On-premises AD** | ✅ Proxies auth | ✅ |
| **Simple AD** | AD-compatible managed directory **on AWS** | AWS | ❌ **Cannot join on-prem AD** | — |

**Keyword map:**
- "users stay **on-premises**", "**proxy**", "no users stored in AWS" → **AD Connector**
- "manage users **in AWS**" + "**trust** with on-prem AD" → **AWS Managed Microsoft AD**
- "simple / cheap AD-compatible directory, **no on-prem**" → **Simple AD**

---

## ➕ Bonus: SDK Credential Provider Chain (from your S29 Q1)

The AWS SDK looks for credentials **in order** and uses the **first** it finds (simplified):

```
1. Explicit credentials in code
2. ⭐ Environment variables (AWS_ACCESS_KEY_ID / AWS_SECRET_ACCESS_KEY)
3. Shared credentials / config file (~/.aws/credentials)
4. Container credentials (ECS task role)
5. ⭐ EC2 instance profile (instance role)   ← checked LAST
```

**Your S29 Q1:** EC2 app has **access keys in environment variables**; dev attached a **restrictive instance role**, but the app can still write to **all** buckets → **"The AWS credential provider looks for instance profile credentials last"** — the env-var keys win.
**Fix:** **remove the access keys** so the SDK falls through to the instance role.

**Related — S15 Q4:** role credentials in **plaintext in a Python file** → remove them; move SDK calls into a function (Lambda@Edge) whose **execution role** has the STS permissions.

---

## 🎯 Master Cheat Sheet

| I need to… | Answer |
|---|---|
| Temporary access to another account | **Cross-account role + `sts:AssumeRole`** |
| API calls that require MFA | **`GetSessionToken`** + `aws:MultiFactorAuthPresent` |
| Read an encoded "not authorized" error | **`sts decode-authorization-message`** |
| Find which identity is making calls | **`sts get-caller-identity`** |
| Credentials for SAML users | **`AssumeRoleWithSAML`** |
| Credentials for social/OIDC users | **Cognito Identity Pools** (instead of `AssumeRoleWithWebIdentity`) |
| Credentials on an on-prem server | **STS temporary credentials** |
| Credentials on EC2/Lambda/ECS/CodeBuild | **One IAM role per workload** |
| Per-user S3 home folders with one policy | **`${aws:username}`** |
| Reusable, versioned policy | **Customer managed policy** |
| Assign a role to Lambda/EC2/ECS | **`iam:PassRole`** + role **trust policy** |
| On-prem users, nothing stored in AWS | **AD Connector** |
| AD in AWS with trust to on-prem | **AWS Managed Microsoft AD** |
| Standalone AD-compatible directory | **Simple AD** |
| Restrictive role ignored on EC2 | **Remove access keys from env vars** (credential chain) |

---

## 🌳 Decision Tree for Exam Questions

```
What does the question need?
│
├── TEMPORARY CREDENTIALS
│    ├── another account / role                    ─▶ sts:AssumeRole
│    ├── MFA-protected API calls                   ─▶ GetSessionToken (+ aws:MultiFactorAuthPresent)
│    ├── SAML / corporate login                    ─▶ AssumeRoleWithSAML
│    ├── Google / Facebook / OIDC                  ─▶ Cognito Identity Pools
│    └── federated user                            ─▶ GetFederationToken
│
├── DEBUGGING ACCESS
│    ├── encoded authorization failure message     ─▶ DecodeAuthorizationMessage
│    ├── which identity am I?                      ─▶ GetCallerIdentity
│    ├── role ignored on EC2                       ─▶ env-var keys win → remove them
│    └── allowed or denied?                        ─▶ explicit DENY > ALLOW > implicit DENY
│
├── WRITING POLICIES
│    ├── per-user folders                          ─▶ ${aws:username}
│    ├── reusable / versioned                      ─▶ customer managed
│    └── strict 1:1, dies with principal           ─▶ inline
│
├── GIVING A SERVICE A ROLE
│    ├── user can't attach the role                ─▶ iam:PassRole (+ iam:GetRole)
│    └── service can't assume it                   ─▶ fix the role's trust policy
│
└── ACTIVE DIRECTORY
     ├── proxy to on-prem, users stay on-prem      ─▶ AD Connector
     ├── AD in AWS + trust with on-prem            ─▶ AWS Managed Microsoft AD
     └── standalone, can't join on-prem            ─▶ Simple AD
```

---

## 🚨 Top Exam Traps

1. **Explicit DENY always wins** — in IAM or bucket policy, either side.
2. **Same account: IAM policy OR bucket policy allowing is enough** (union) — unless something explicitly denies.
3. **MFA for API calls → `GetSessionToken`**, not `AssumeRole` or `GetFederationToken`.
4. **Encoded authorization failure message → `DecodeAuthorizationMessage`** (STS), not CloudTrail.
5. **AWS recommends Cognito Identity Pools over `AssumeRoleWithWebIdentity`.**
6. **Cross-account = role in the target account + `AssumeRole`** — never share access keys.
7. **Never store access keys on servers**; on-prem → STS; AWS compute → **roles**.
8. **Access keys in env vars override the EC2 instance role** — the instance profile is checked **last**.
9. **One role per application/function** — don't reuse roles.
10. **`${aws:username}`** makes one policy work for every user.
11. **Inline policies are deleted with their principal**; **customer managed** is the best practice.
12. **`iam:PassRole`** is needed by the **person** configuring the service; the **trust policy** decides which service can use the role.
13. **AD Connector = proxy (users on-prem)**; **Managed AD = users in AWS + trust**; **Simple AD can't join on-prem**.

---

## 💾 How to Use This Guide

1. Read the **Mental Model** and the "temporary credentials are good" rule.
2. Memorize the **STS API table** — each API maps to one exam keyword.
3. Walk through the **4 bucket-policy examples** until the union + explicit-deny rule is automatic.
4. Finish with the **Decision Tree** and **Top Exam Traps**, then drill `quizzes/my_questions/29-Advanced_Identity.md`.
