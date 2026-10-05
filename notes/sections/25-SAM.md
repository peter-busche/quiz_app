# 🐿️ AWS SAM (Serverless Application Model) Study Guide

Section 25 — slides 732–743 ([open slides](../../AWS_Certified_Developer_Slides_v45.pdf#page=732))

---

## 🧠 The One-Sentence Mental Model

> **SAM = a shorthand for CloudFormation + a CLI that builds, deploys, syncs, and runs it locally.**

Everything in this section falls into one of **two halves**:

| Half | What it is | Slides |
|---|---|---|
| 📄 **The Template** | A YAML file (CloudFormation with a `Transform` header) that describes your serverless app in fewer lines | 733–734, 738, 740 |
| 💻 **The CLI** | `sam ...` commands that turn the template into a running stack, or run it on your laptop | 735–737, 741–743 |

If a question mentions a **YAML property** → think Template.
If a question mentions a **command** → think CLI.

---

## 🗺️ The Big Picture (how the pieces connect)

```
                ┌──────────────── YOUR LAPTOP ────────────────┐
                │                                             │
  SAM Template  │  sam build ──▶ sam package ──▶ sam deploy ──┼──▶ S3 (zipped code)
  (YAML)   +    │                                             │         │
  App Code      │  sam local invoke / start-lambda / start-api│         ▼
                │  (test without deploying)                   │   CloudFormation
                │                                             │   ChangeSet ──▶ Stack
                │  sam sync --code  ──────────────────────────┼──▶ Lambda/API directly
                │  (bypasses CloudFormation, seconds)         │   (skips ChangeSet)
                └─────────────────────────────────────────────┘
                                                                     │
                                         CodeDeploy shifts traffic ◀─┘
                                         (Canary / Linear / AllAtOnce)
```

---

## 1️⃣ What SAM Is — slide [733](../../AWS_Certified_Developer_Slides_v45.pdf#page=733)

- **Framework** for developing and deploying serverless apps
- All configuration is **YAML**
- **Generates complex CloudFormation** from a simple SAM file
- Supports **anything CloudFormation supports**: Outputs, Mappings, Parameters, Resources…
- Uses **CodeDeploy** to deploy Lambda functions
- Can run **Lambda, API Gateway, DynamoDB locally**

**Why it matters for the exam:** SAM is *not* a separate engine — it is CloudFormation underneath. Any "can SAM do X that CloudFormation does?" question → **yes**.

---

## 2️⃣ The Template (Recipe) — slide [734](../../AWS_Certified_Developer_Slides_v45.pdf#page=734)

### 🔑 The header that makes it SAM

```yaml
Transform: 'AWS::Serverless-2016-10-31'
```

No Transform header → it's plain CloudFormation, not SAM.

### 🧱 The 3 core resource types

| SAM resource | Becomes (in CloudFormation) | Memory trick |
|---|---|---|
| `AWS::Serverless::Function` | Lambda function (+ role, + event triggers) | **F**unction = **F**aaS |
| `AWS::Serverless::Api` | API Gateway REST API | **Api** = API Gateway |
| `AWS::Serverless::SimpleTable` | DynamoDB table (single-attribute primary key) | **Simple**Table = simple DynamoDB |

> ⚠️ Trap: the names are **`Serverless::`**, never `Serverless::Lambda`, `Serverless::Table`, or `Serverless::Gateway`.

### 📦 Beyond the slides (good to recognize)

| Resource / section | Purpose |
|---|---|
| `Globals:` | Shared properties for all functions (runtime, memory, timeout, env vars, `Tracing: Active`) |
| `AWS::Serverless::HttpApi` | API Gateway **HTTP** API (cheaper/simpler than REST) |
| `AWS::Serverless::LayerVersion` | Lambda Layer (shared libraries) |
| `AWS::Serverless::StateMachine` | Step Functions state machine |
| `AWS::Serverless::Application` | Nested app, e.g. from the Serverless Application Repository (needs `CAPABILITY_AUTO_EXPAND`) |

---

## 3️⃣ Deployment Pipeline — slide [735](../../AWS_Certified_Developer_Slides_v45.pdf#page=735)

Think of it as **3 steps: Build → Package → Deploy**.

| Step | Command | What happens |
|---|---|---|
| 1. Build | `sam build` | Builds code + dependencies locally; transforms SAM template → CloudFormation template |
| 2. Package | `sam package` *(optional — `sam deploy` does it for you)* | **Zips** code and **uploads to S3** |
| 3. Deploy | `sam deploy` | **Creates & executes a CloudFormation ChangeSet** → Stack (Lambda, API Gateway, DynamoDB) |

**Remember the destinations:**
- Code goes to 🪣 **S3**
- Infrastructure goes through 📜 **CloudFormation ChangeSet**

> ⚠️ Trap: code is **not** uploaded to CodeCommit, ECR, or directly to Lambda during `sam deploy`.

---

## 4️⃣ SAM Accelerate (`sam sync`) — slides [736](../../AWS_Certified_Developer_Slides_v45.pdf#page=736)–[737](../../AWS_Certified_Developer_Slides_v45.pdf#page=737)

**Problem it solves:** CloudFormation deploys are slow. When you're iterating on code, you want changes in AWS in **seconds**.

**How:** `sam sync` uses **service APIs directly and bypasses CloudFormation** for code-only changes.

### 🎛️ The sync ladder (from broadest to narrowest)

| Command | Syncs | Uses CloudFormation? |
|---|---|---|
| `sam sync` | Code **and** infrastructure | ✅ Yes |
| `sam sync --code` | Code only | ❌ No — seconds |
| `sam sync --code --resource AWS::Serverless::Function` | All Lambda functions + dependencies | ❌ No |
| `sam sync --code --resource-id HelloWorldLambdaFunction` | One specific resource by logical ID | ❌ No |
| `sam sync --watch` | Watches files, syncs automatically | Depends ⬇️ |

### 👀 How `--watch` decides

```
File change detected
        │
        ├── includes CONFIGURATION change? ──▶ sam sync        (full, uses CloudFormation)
        │
        └── CODE only?                      ──▶ sam sync --code (fast, bypasses CloudFormation)
```

**Keyword map:**
- "quickly", "seconds", "without updating infrastructure" → `sam sync --code`
- "automatically when files change" → `sam sync --watch`
- "`--resource`" = by **type**; "`--resource-id`" = by **logical ID**

---

## 5️⃣ Policy Templates (Permissions) — slide [738](../../AWS_Certified_Developer_Slides_v45.pdf#page=738)

**What:** Pre-built, least-privilege permission templates you attach to a function with one line.

```yaml
MyFunction:
  Type: AWS::Serverless::Function
  Properties:
    Policies:
      - DynamoDBCrudPolicy:
          TableName: !Ref MyTable
```

### 📌 The 3 you must know

| Template | Grants | Keyword in question |
|---|---|---|
| `S3ReadPolicy` | **Read-only** access to S3 objects | "read objects from S3" |
| `SQSPollerPolicy` | **Poll** an SQS queue | "read/consume/poll messages from SQS" |
| `DynamoDBCrudPolicy` | **C**reate **R**ead **U**pdate **D**elete on DynamoDB | "create, read, update, delete items" |

> ⚠️ Traps: `SQSSendMessagePolicy` is for *sending*, not polling. `DynamoDBReadPolicy` is read-only, not CRUD.

These policies end up on the function's **execution role** (the role Lambda assumes — see your permissions notes).

---

## 6️⃣ SAM + CodeDeploy (Safe Lambda Deployments) — slides [739](../../AWS_Certified_Developer_Slides_v45.pdf#page=739)–[740](../../AWS_Certified_Developer_Slides_v45.pdf#page=740)

**What:** SAM **natively uses CodeDeploy** to shift traffic between Lambda versions through an **alias**.

### 🧩 The 4 properties (memorize these)

```yaml
MyFunction:
  Type: AWS::Serverless::Function
  Properties:
    AutoPublishAlias: live                 # ①
    DeploymentPreference:
      Type: Canary10Percent10Minutes       # ②
      Alarms:                              # ③
        - !Ref ErrorsAlarm
      Hooks:                               # ④
        PreTraffic: !Ref PreTrafficFunction
        PostTraffic: !Ref PostTrafficFunction
```

| # | Property | What it does |
|---|---|---|
| ① | `AutoPublishAlias` | Detects new code → **publishes a new version** → **points the alias** to it |
| ② | `DeploymentPreference` `Type` | How traffic shifts: **Canary**, **Linear**, or **AllAtOnce** |
| ③ | `Alarms` | **CloudWatch Alarms** that trigger an automatic **rollback** |
| ④ | `Hooks` | **PreTraffic** / **PostTraffic** Lambda functions that run tests before and after the shift |

### 🚦 Traffic shifting types

| Type | Behavior | Example |
|---|---|---|
| **Canary** | Small % first, then **the rest all at once** | `Canary10Percent10Minutes` |
| **Linear** | Equal % increments at fixed intervals | `Linear10PercentEvery1Minute` |
| **AllAtOnce** | 100% immediately | `AllAtOnce` |

### 🔄 Flow

```
New code ─▶ AutoPublishAlias publishes v2
         ─▶ PreTraffic hook runs tests
         ─▶ CodeDeploy shifts alias traffic v1 ─▶ v2 (Canary/Linear/AllAtOnce)
               │
               └── CloudWatch Alarm fires? ─▶ ROLLBACK to v1
         ─▶ PostTraffic hook runs tests
```

> ⚠️ Traps: traffic shifting is done by **CodeDeploy**, not CodePipeline, CodeBuild, or Route 53. Rollback is triggered by **CloudWatch Alarms**.

---

## 7️⃣ Local Testing — slides [741](../../AWS_Certified_Developer_Slides_v45.pdf#page=741)–[742](../../AWS_Certified_Developer_Slides_v45.pdf#page=742)

Four commands. The trick is matching **what you're emulating**:

| Command | Emulates | Lifetime | Use when… |
|---|---|---|---|
| `sam local start-lambda` | The **Lambda service** endpoint | Stays running | Running **automated tests** against a local Lambda endpoint |
| `sam local invoke` | **One function call** | Runs **once and exits** | Testing a function with a payload / generating test cases |
| `sam local start-api` | **API Gateway** (local HTTP server) | Stays running, **auto-reloads** changes | Hitting your functions through HTTP routes |
| `sam local generate-event` | An **event payload** (S3, API Gateway, SNS, Kinesis, DynamoDB…) | Prints JSON | You need a realistic event without writing JSON by hand |

### 🔗 The classic combo

```bash
sam local generate-event s3 put --bucket <bucket> --key <key> | sam local invoke -e - <function_logical_id>
```

### ⚠️ Gotcha

If your function calls **real AWS services** while running locally → use the correct **`--profile`** option.

**Keyword map:**
- "endpoint that emulates Lambda" / "automated tests" → `start-lambda`
- "once and quit" → `invoke`
- "local HTTP server" / "API" → `start-api`
- "sample payload" / "event" → `generate-event`

*(Beyond the slides: local commands run functions in **Docker** containers.)*

---

## 8️⃣ Multiple Environments — slide [743](../../AWS_Certified_Developer_Slides_v45.pdf#page=743)

- One SAM template, many environments (dev, prod…)
- Per-environment settings live in **`samconfig.toml`**
- Deploy with:

```bash
sam deploy --config-env dev
sam deploy --config-env prod
```

> ⚠️ Trap: *not* separate templates per environment, and *not* `--guided` every time.

---

## 🎯 Master Cheat Sheet

### Commands

| I need to… | Command |
|---|---|
| Build code + convert template | `sam build` |
| Zip + upload code to S3 | `sam package` (optional) |
| Deploy via CloudFormation ChangeSet | `sam deploy` |
| Deploy to a specific environment | `sam deploy --config-env <env>` |
| Sync code + infra | `sam sync` |
| Sync code only, fast (no CloudFormation) | `sam sync --code` |
| Auto-sync on file change | `sam sync --watch` |
| Emulate Lambda service locally | `sam local start-lambda` |
| Invoke a function once locally | `sam local invoke` |
| Run a local API Gateway | `sam local start-api` |
| Make a sample event | `sam local generate-event` |

### Template keywords

| Keyword | Meaning |
|---|---|
| `Transform: 'AWS::Serverless-2016-10-31'` | "This is a SAM template" |
| `AWS::Serverless::Function / Api / SimpleTable` | Lambda / API Gateway / DynamoDB |
| `Policies: - DynamoDBCrudPolicy` | Policy template on the execution role |
| `AutoPublishAlias` | New version + move alias |
| `DeploymentPreference` | CodeDeploy traffic shifting (Canary/Linear/AllAtOnce) + Alarms + Hooks |

---

## 🌳 Decision Tree for Exam Questions

```
Is the question about...
│
├── Identifying a SAM template?          ─▶ Transform: AWS::Serverless-2016-10-31
│
├── Deploying?
│    ├── Where does code go?             ─▶ S3
│    ├── How is infra updated?           ─▶ CloudFormation ChangeSet
│    ├── Fast code-only update?          ─▶ sam sync --code
│    └── Different environments?         ─▶ samconfig.toml + --config-env
│
├── Permissions for a function?          ─▶ Policy templates (S3ReadPolicy, SQSPollerPolicy, DynamoDBCrudPolicy)
│
├── Gradual / safe Lambda rollout?       ─▶ CodeDeploy: AutoPublishAlias + DeploymentPreference
│    ├── Auto rollback?                  ─▶ CloudWatch Alarms
│    └── Validate before/after?          ─▶ PreTraffic / PostTraffic hooks
│
└── Testing locally?
     ├── Emulate Lambda endpoint?        ─▶ sam local start-lambda
     ├── One-shot invoke?                ─▶ sam local invoke
     ├── Local API?                      ─▶ sam local start-api
     └── Need an event payload?          ─▶ sam local generate-event
```

---

## 🚨 Top Exam Traps

1. SAM **is** CloudFormation underneath — it supports Outputs, Mappings, Parameters, etc.
2. `sam package` is **optional**; `sam deploy` packages for you.
3. Code is uploaded to **S3**, not CodeCommit/ECR.
4. `sam sync --code` **bypasses CloudFormation**; plain `sam sync` does not.
5. Traffic shifting = **CodeDeploy**; rollback trigger = **CloudWatch Alarms**.
6. **Canary** = one small step then the rest; **Linear** = equal steps.
7. `start-lambda` (stays running, endpoint) ≠ `invoke` (runs once, exits).
8. Wrong AWS account locally? → **`--profile`**.
9. `SQSPollerPolicy` = read from queue; `DynamoDBCrudPolicy` = full CRUD; `S3ReadPolicy` = read-only.

---

## 💾 How to Use This Guide

1. Read the **Mental Model** and **Big Picture** first — everything hangs off "Template vs CLI".
2. Go section by section; click the slide links to see the original diagrams.
3. Cover the right column of the **Cheat Sheet** tables and quiz yourself.
4. Drill with `quizzes/my_questions/25-SAM.md` in the quiz app.
