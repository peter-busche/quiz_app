# 🏗️ Section 26: Cloud Development Kit (CDK) — Study Guide

Slides 744–756 ([open slides](../../AWS_Certified_Developer_Slides_v45.pdf#page=744)) · Sections follow the slide order

---

## 🧠 The Mental Model (read this first)

> **CDK = write infrastructure in a real programming language → `cdk synth` "compiles" it into a CloudFormation template → CloudFormation deploys it.**

```
 Your code (TypeScript / Python / Java / .NET)
        │  uses CONSTRUCTS (L1 / L2 / L3)
        ▼
   cdk synth  ──▶  CloudFormation template (JSON/YAML)  ──▶  cdk deploy  ──▶  CloudFormation Stack
        │
        └──▶ sam local invoke -t <template>   (test Lambda locally with SAM CLI)
```

Almost every CDK question is one of **five types**:

| # | Question type | Answer keyword | Section |
|---|---|---|---|
| 1 | What is CDK / how does it deploy? | **Programming language → CloudFormation** | 1️⃣–2️⃣ |
| 2 | CDK vs SAM? | **All services + code** vs **serverless + YAML** | 3️⃣ |
| 3 | Which construct level? | **L1 = `Cfn*`, L2 = defaults + methods, L3 = patterns** | 6️⃣–9️⃣ |
| 4 | Which command? / deploy error? | **`cdk synth`, `cdk bootstrap`, `cdk diff`…** | 🔟–1️⃣1️⃣ |
| 5 | How do I test it? | **Assertions module: fine-grained vs snapshot** | 1️⃣2️⃣ |

---

## 1️⃣ What is CDK? — slide [745](../../AWS_Certified_Developer_Slides_v45.pdf#page=745)

- Define cloud infrastructure in a **familiar programming language**: **JavaScript/TypeScript, Python, Java, .NET**
- Built from high-level components called **constructs**
- ⭐ Code is **"compiled" into a CloudFormation template** (JSON/YAML)
- ⭐ Deploy **infrastructure and application runtime code together**
  - Great for **Lambda functions**
  - Great for **Docker containers in ECS / EKS**

---

## 2️⃣ CDK in a Diagram — slide [746](../../AWS_Certified_Developer_Slides_v45.pdf#page=746)

```
CDK Application (Programming language + Constructs)
        │
        ▼  CDK CLI: cdk synth
CloudFormation Template
        │
        ▼
CloudFormation (creates the stack)
```

---

## 3️⃣ CDK vs SAM — slide [747](../../AWS_Certified_Developer_Slides_v45.pdf#page=747)

| | **SAM** | **CDK** |
|---|---|---|
| Scope | ⭐ **Serverless-focused** | ⭐ **All AWS services** |
| Authoring | **Declarative JSON/YAML** template | **Programming language** (JS/TS, Python, Java, .NET) |
| Best for | Quickly getting started with **Lambda** | Complex infra, reuse, loops/conditions in code |
| Under the hood | **CloudFormation** | **CloudFormation** |

> **Keyword map:** "YAML template for serverless" → **SAM**. "Use Python/TypeScript to define infrastructure" / "all AWS services" → **CDK**. Both → **CloudFormation**.

---

## 4️⃣ CDK + SAM Together — slide [748](../../AWS_Certified_Developer_Slides_v45.pdf#page=748)

- ⭐ Use the **SAM CLI to locally test CDK apps**
- ⚠️ You **must run `cdk synth` first** (SAM needs the CloudFormation template)

```bash
cdk synth
sam local invoke -t MyCDKStack.template.json myFunction
```

---

## 5️⃣ CDK Hands-On Architecture — slide [749](../../AWS_Certified_Developer_Slides_v45.pdf#page=749)

```
Client ──upload image──▶ S3 Bucket ──trigger──▶ Lambda ──analyze──▶ Amazon Rekognition
                                                   └──save results──▶ DynamoDB
```
A typical example of "infrastructure **and** Lambda code deployed together" with CDK.

---

## 6️⃣ CDK Constructs — slide [750](../../AWS_Certified_Developer_Slides_v45.pdf#page=750)

- **Construct** = a component that encapsulates **everything CDK needs** to create the final CloudFormation stack
- Can be **one resource** (an S3 bucket) or **many related resources** (worker queue + compute)
- **AWS Construct Library** — constructs for **every AWS resource**, in **3 levels (L1, L2, L3)**
- **Construct Hub** — additional constructs from **AWS, 3rd parties, and the open-source CDK community**

---

## 7️⃣–9️⃣ The Three Construct Levels — slides [751](../../AWS_Certified_Developer_Slides_v45.pdf#page=751)–753

| | **L1 — CFN Resources** | **L2 — Curated / Intent-based** | **L3 — Patterns** |
|---|---|---|---|
| Represents | **Exactly** one CloudFormation resource | One AWS resource, higher-level API | ⭐ **Multiple related resources** |
| Name | ⭐ Starts with **`Cfn`** (e.g. `CfnBucket`) | e.g. `Bucket` | e.g. `LambdaRestApi`, `ApplicationLoadBalancerFargateService` |
| Properties | ⚠️ You **must configure all properties explicitly** | ✅ **Convenient defaults** & boilerplate handled | Whole architecture pre-wired |
| Methods | — | ⭐ Helper methods (e.g. `bucket.addLifeCycleRule()`) | — |
| Source | **Generated from the CloudFormation Resource Specification** | Hand-written by AWS | Hand-written by AWS |
| You need to know… | All resource details | **Not** all the details | Only the pattern's inputs |

### L3 examples (memorize)
| Construct | Builds |
|---|---|
| `aws-apigateway.LambdaRestApi` | **API Gateway backed by a Lambda function** |
| `aws-ecs-patterns.ApplicationLoadBalancerFargateService` | **Fargate cluster + Application Load Balancer** |

### Quick examples
```typescript
// L1 — raw CloudFormation, every property explicit
new s3.CfnBucket(this, 'L1Bucket', { bucketName: 'my-l1-bucket' });

// L2 — sensible defaults + helper methods
const bucket = new s3.Bucket(this, 'L2Bucket', { versioned: true });
bucket.addLifecycleRule({ expiration: Duration.days(365) });

// L3 — a whole pattern
new apigw.LambdaRestApi(this, 'Api', { handler: myFunction });
```

**Keyword map:**
- "name starts with **Cfn**", "**all properties** must be set", "maps 1:1 to CloudFormation" → **L1**
- "**defaults**", "**intent-based API**", "**methods** like `addLifecycleRule`" → **L2**
- "**patterns**", "**multiple resources**", "common architecture in one construct" → **L3**

---

## 🔟 Important CDK Commands — slide [754](../../AWS_Certified_Developer_Slides_v45.pdf#page=754)

| Command | Does |
|---|---|
| `npm install -g aws-cdk-lib` | Install the CDK CLI and libraries |
| `cdk init app` | Create a new CDK project from a template |
| ⭐ `cdk synth` | **Synthesize and print the CloudFormation template** |
| ⭐ `cdk bootstrap` | **Deploy the CDK Toolkit staging stack** |
| `cdk deploy` | Deploy the stack(s) |
| ⭐ `cdk diff` | **Differences between local CDK and the deployed stack** |
| `cdk destroy` | Destroy the stack(s) |

**Order of a first deployment:** `cdk init` → write code → `cdk bootstrap` (once per account/region) → `cdk synth` (optional, to inspect) → `cdk deploy`

> CDK `diff` ≈ CloudFormation **change set** preview. CDK `synth` ≈ "show me the template".

---

## 1️⃣1️⃣ CDK Bootstrapping — slide [755](../../AWS_Certified_Developer_Slides_v45.pdf#page=755)

- Provisions resources CDK needs **before** you can deploy CDK apps into an **AWS environment**
- ⭐ **AWS environment = account + region**
- Creates a CloudFormation stack called **`CDKToolkit`** containing:
  - **S3 bucket** — stores files (assets like Lambda code)
  - **IAM roles** — permissions to perform deployments
- ⭐ Run **once per new environment**:

```bash
cdk bootstrap aws://<aws_account>/<aws_region>
cdk bootstrap aws://123456789012/eu-west-1
```

> ⚠️ **Forgot to bootstrap?** → error **"Policy contains a statement with one or more invalid principal"**. New account **or new region** → bootstrap again.

---

## 1️⃣2️⃣ CDK Testing — slide [756](../../AWS_Certified_Developer_Slides_v45.pdf#page=756)

- Use the **CDK Assertions Module** + a test framework: **Jest** (JavaScript) or **Pytest** (Python)
- Verify resources, rules, conditions, parameters…

| Test type | What it does | When |
|---|---|---|
| ⭐ **Fine-grained assertions** (common) | Test **specific aspects** of the template — "does this resource have this property = this value?" | Check a single setting (e.g. bucket is encrypted) |
| ⭐ **Snapshot tests** | Compare the synthesized template against a **previously stored baseline** | Detect **any unexpected change** |

### Importing a template to test
| Method | For |
|---|---|
| `Template.fromStack(MyStack)` | A stack **built in CDK** |
| `Template.fromString(mystring)` | A stack **built outside CDK** |

---

## 🎯 Master Cheat Sheet

| I need to… | Answer |
|---|---|
| Define infra in Python/TypeScript/Java/.NET | **CDK** |
| Define serverless infra in YAML | **SAM** |
| See the generated CloudFormation | **`cdk synth`** |
| Compare local code with the deployed stack | **`cdk diff`** |
| Prepare a new account/region for CDK | **`cdk bootstrap aws://acct/region`** |
| Fix "invalid principal" deploy error | **Run `cdk bootstrap`** |
| Test a CDK Lambda locally | **`cdk synth` → `sam local invoke -t <template>`** |
| Raw CloudFormation resource, all props | **L1 (`Cfn*`)** |
| Resource with defaults + helper methods | **L2** |
| Multi-resource architecture in one construct | **L3 (patterns)** |
| Find community/3rd-party constructs | **Construct Hub** |
| Check a specific property in a test | **Fine-grained assertion** |
| Catch any template change in a test | **Snapshot test** |
| Test a template built outside CDK | **`Template.fromString()`** |

---

## 🌳 Decision Tree for Exam Questions

```
What is the question about?
│
├── Choosing a tool
│    ├── programming language / all AWS services   ─▶ CDK
│    ├── YAML / serverless only / quick Lambda       ─▶ SAM
│    └── both deploy via                             ─▶ CloudFormation
│
├── Constructs
│    ├── Cfn prefix / every property explicit        ─▶ L1
│    ├── defaults / methods / intent-based           ─▶ L2
│    └── multiple resources / patterns               ─▶ L3
│
├── Commands
│    ├── generate template                           ─▶ cdk synth
│    ├── what will change                            ─▶ cdk diff
│    ├── first deploy to account/region / "invalid principal" ─▶ cdk bootstrap
│    └── deploy / remove                             ─▶ cdk deploy / cdk destroy
│
├── Local testing of Lambda                          ─▶ cdk synth + sam local invoke -t
│
└── Unit testing
     ├── specific property                           ─▶ Fine-grained assertions
     └── whole template vs baseline                  ─▶ Snapshot test
```

---

## 🚨 Top Exam Traps

1. **CDK doesn't replace CloudFormation** — it **generates** CloudFormation templates.
2. **SAM = serverless + YAML; CDK = all services + programming languages.** Both use CloudFormation.
3. **SAM CLI can test CDK apps locally — but only after `cdk synth`.**
4. **L1 constructs start with `Cfn`** and need **all properties**; **L2** adds defaults and methods; **L3** = multi-resource **patterns**.
5. **Bootstrap once per account AND region** — creates the **`CDKToolkit`** stack (S3 bucket + IAM roles).
6. **"Policy contains a statement with one or more invalid principal"** → you didn't **bootstrap**.
7. **`cdk diff`** shows what will change; **`cdk synth`** only prints the template.
8. **Fine-grained assertions** test specific properties; **snapshot tests** compare to a baseline.
9. **`Template.fromStack`** = CDK stack; **`Template.fromString`** = template from outside CDK.

---

## 💾 How to Use This Guide

1. Read the **Mental Model** diagram — CDK → synth → CloudFormation.
2. Memorize the **L1 / L2 / L3** table and the **7 commands**.
3. Remember **bootstrap = once per account + region** and its error message.
4. Finish with the **Decision Tree** and **Top Exam Traps**.
