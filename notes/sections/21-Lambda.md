# λ Section 21: AWS Serverless: Lambda — Study Guide

Slides 527–601 ([open slides](../../AWS_Certified_Developer_Slides_v45.pdf#page=527)) · Sections follow the lecture order

---

## 🧠 The Mental Model (read this first)

Almost every Lambda exam question is answered by one of **four questions**:

| # | Question | Where it's covered |
|---|---|---|
| 1 | **How is the function invoked?** (sync / async / event source mapping) | Sync → ALB → Async & DLQ → EventBridge → S3 → Event Source Mapping |
| 2 | **Who is allowed to do what?** (execution role vs resource policy) | Permissions |
| 3 | **Where does it run and what can it reach?** (VPC, storage, edge) | Edge → VPC → Performance → Layers → File Systems |
| 4 | **How does it scale and get deployed?** (concurrency, versions, CodeDeploy) | Concurrency → Dependencies → CloudFormation → Containers → Versions → CodeDeploy → URL |

### 🔑 The 3 invocation models — the backbone of this section

| | **Synchronous** | **Asynchronous** | **Event Source Mapping** |
|---|---|---|---|
| Who calls | Caller waits for the result | Service drops event into Lambda's **internal event queue** | Lambda **polls** the source |
| Examples | CLI/SDK, API Gateway, ALB, CloudFront (Lambda@Edge), Cognito, Step Functions | S3, SNS, EventBridge, CodeCommit, CodePipeline, CloudWatch Logs, SES | Kinesis Data Streams, DynamoDB Streams, SQS / SQS FIFO |
| Retries | **Client's job** (backoff) | Lambda retries **3 tries total** | Kinesis/DynamoDB: retry whole batch until success/expiry · SQS: returns to queue |
| On failure | Error returned to caller | **DLQ** (SQS/SNS) or **Destination** | Streams: Destination for discarded batches · SQS: **DLQ on the SQS queue** |
| Function invoked… | synchronously | asynchronously | **synchronously** (by the poller) |

---

## 1️⃣ AWS Lambda — Section Introduction — slide [527](../../AWS_Certified_Developer_Slides_v45.pdf#page=527)

"It's a serverless world." This section is the core of the serverless part of the exam — expect many questions.

---

## 2️⃣ Serverless Introduction — slides [528](../../AWS_Certified_Developer_Slides_v45.pdf#page=528)–529

- **Serverless** = developers don't manage servers; they just deploy code / **functions**
- Originally Serverless == **FaaS** (Function as a Service), pioneered by AWS Lambda
- Now means **anything managed**: databases, messaging, storage…
- ⚠️ Serverless **does not mean no servers** — you just don't manage / provision / see them

**Serverless services in AWS:** Lambda, DynamoDB, Cognito, API Gateway, S3, SNS & SQS, Kinesis Data Firehose, Aurora Serverless, Step Functions, Fargate

---

## 3️⃣ AWS Lambda Overview — slides [530](../../AWS_Certified_Developer_Slides_v45.pdf#page=530)–536

### EC2 vs Lambda

| Amazon EC2 | AWS Lambda |
|---|---|
| Virtual **servers** | Virtual **functions** — no servers to manage |
| Limited by RAM and CPU | Limited by **time** — short executions |
| Continuously running | Runs **on-demand** |
| Scaling = intervention | Scaling is **automated** |

### Benefits
- **Pricing:** pay per request + compute time; free tier **1M requests + 400,000 GB-seconds**
- Integrated with the whole AWS suite and many languages
- Monitoring through **CloudWatch**
- Up to **10 GB RAM** — ⭐ **more RAM also improves CPU and network**

### Languages
Node.js, Python, Java, C# (.NET Core) / PowerShell, Ruby, **Custom Runtime API** (e.g. Rust, Go), **Container Image** (must implement the **Lambda Runtime API**)
> ⚠️ For *arbitrary* Docker images, **ECS / Fargate** is preferred.

### Main integrations
API Gateway, Kinesis, DynamoDB, S3, CloudFront, CloudWatch Events / EventBridge, CloudWatch Logs, SNS, SQS, Cognito

### Classic patterns
- **Thumbnail creation:** new image in S3 → Lambda → thumbnail to S3 + metadata to DynamoDB
- **Serverless CRON:** EventBridge rule (every 1 hour) → Lambda

### Pricing math
| Item | Price |
|---|---|
| Requests | First **1M free**, then **$0.20 per 1M** |
| Duration (1 ms increments) | **400,000 GB-s free** (= 400,000 s at 1 GB, = 3,200,000 s at 128 MB), then $1.00 per 600,000 GB-s |

---

## 4️⃣ Lambda Synchronous Invocations — slides [537](../../AWS_Certified_Developer_Slides_v45.pdf#page=537)–538

- **Synchronous:** CLI, SDK, API Gateway, ALB
- Result is returned **right away**
- ⭐ **Error handling is client-side** (retries, exponential backoff)

| User invoked | Service invoked | Other |
|---|---|---|
| ALB, API Gateway, CloudFront (Lambda@Edge), S3 Batch | Cognito, Step Functions | Lex, Alexa, Kinesis Data Firehose |

---

## 5️⃣ Lambda & Application Load Balancer — slides [539](../../AWS_Certified_Developer_Slides_v45.pdf#page=539)–543

- Expose Lambda as an **HTTP(S) endpoint** via **ALB** (or API Gateway)
- The Lambda function must be registered in a **target group**
- ALB invokes Lambda **synchronously**

### Conversions
```
Client ──HTTP──▶ ALB ──JSON event──▶ Lambda ──JSON response──▶ ALB ──HTTP──▶ Client
```
| HTTP → JSON (request event) | JSON → HTTP (response) |
|---|---|
| ELB info, HTTP method & path, query string params (key/value), headers (key/value), body + `isBase64Encoded` | Status code & description, headers, body + `isBase64Encoded` |

### Multi-value headers (ALB setting)
`?name=foo&name=bar` → `"queryStringParameters": {"name": ["foo","bar"]}` — values arrive as **arrays**.

### Permissions
ALB invoking Lambda is allowed by the **Lambda resource-based policy**.

---

## 6️⃣ Lambda Asynchronous Invocations & DLQ — slides [544](../../AWS_Certified_Developer_Slides_v45.pdf#page=544)–545

```
S3 / SNS / EventBridge ──▶ [ Lambda internal Event Queue ] ──▶ Function
                                     │  retries (3 tries total: wait 1 min, then 2 min)
                                     └──▶ DLQ (SQS or SNS) on final failure
```

- Events go into an **Event Queue**; Lambda **retries on errors — 3 tries total** (1 min wait, then 2 min)
- ⭐ Processing must be **idempotent** (retries happen)
- Retries → **duplicate log entries** in CloudWatch Logs
- **DLQ** can be **SQS or SNS** (needs correct IAM permissions)
- Use async to speed up processing when you don't need the result (e.g. 1000 files)

**Async services:** S3, SNS, CloudWatch Events / EventBridge, CodeCommit (new branch/tag/push), CodePipeline (**Lambda must call back**), plus CloudWatch Logs, SES, CloudFormation, Config, IoT, IoT Events

---

## 7️⃣ Lambda & CloudWatch Events / EventBridge — slide [546](../../AWS_Certified_Developer_Slides_v45.pdf#page=546)

Two patterns:
- **Schedule:** EventBridge rule with **CRON or Rate** (e.g. every 1 hour) → Lambda
- **Event pattern:** EventBridge rule on **state changes** (e.g. CodePipeline) → Lambda

---

## 8️⃣ Lambda & S3 Event Notifications — slides [547](../../AWS_Certified_Developer_Slides_v45.pdf#page=547)–548

- Events: `s3:ObjectCreated`, `s3:ObjectRemoved`, `s3:ObjectRestore`, `s3:Replication`…
- **Object name filtering** (e.g. `*.jpg`)
- Targets: **SNS, SQS, Lambda** (Lambda is invoked **async**, can have a DLQ)
- Delivery usually in **seconds**, sometimes a **minute or longer**
- ⚠️ Two simultaneous writes to the same **non-versioned** object → maybe **only one** notification
- ⭐ To guarantee a notification for **every** successful write → **enable versioning**

**Pattern:** new file in S3 → Lambda → update metadata table in RDS or DynamoDB

---

## 9️⃣ Lambda Event Source Mapping — slides [549](../../AWS_Certified_Developer_Slides_v45.pdf#page=549)–554

**Sources:** Kinesis Data Streams, **SQS & SQS FIFO**, DynamoDB Streams
**Common denominator:** records must be **polled** from the source → Lambda is invoked **synchronously** with a batch.

### 🌊 Streams (Kinesis & DynamoDB)
- One **iterator per shard**, items processed **in order**
- Start from **new items, the beginning, or a timestamp**
- Processed items **are not removed** (other consumers can read them)
- Low traffic → **batch window** to accumulate records
- Parallel: up to **10 batches per shard** (still in order **per partition key**)

**Error handling (streams):**
- Default: on error, the **entire batch is reprocessed** until success or the items expire
- The **shard is paused** until the error is resolved (to keep order)
- Configure: **discard old events**, **limit retries**, **split the batch on error** (works around timeouts)
- Discarded events → **Destination**

### 📬 SQS & SQS FIFO
- Event source mapping **long polls** SQS
- **Batch size 1–10** messages
- ⭐ Set **queue visibility timeout = 6× the Lambda timeout**
- ⭐ **DLQ goes on the SQS queue, not on Lambda** (Lambda DLQ is only for async) — or use a Lambda **Destination** for failures
- FIFO: in-order, scales to **number of active message groups**
- Standard: **not** in order; scales as fast as possible
- On error, batch items go back **individually** (may be regrouped); occasional **duplicates** even without errors
- Lambda **deletes** items after successful processing

### 📈 Scaling
| Source | Scaling |
|---|---|
| Kinesis / DynamoDB Streams | **1 invocation per shard** (up to 10 batches/shard with parallelization) |
| SQS Standard | **+60 instances per minute**, up to **1000 batches** simultaneously |
| SQS FIFO | Same GroupID in order; scales to **number of active message groups** |

---

## 🔟 Lambda Event & Context Objects — slides [555](../../AWS_Certified_Developer_Slides_v45.pdf#page=555)–557

| **Event object** | **Context object** |
|---|---|
| JSON document with **data to process** | Info about the **invocation, function, runtime** |
| Comes from the **invoking service** (EventBridge, custom…) | Passed by **Lambda** at runtime |
| Converted by the runtime (e.g. Python `dict`) | Methods & properties |
| e.g. input args, service args | e.g. `aws_request_id`, `function_name`, `memory_limit_in_mb` |

**Memory trick:** *Event = WHAT happened. Context = WHERE/HOW I'm running.*

---

## 1️⃣1️⃣ Lambda Destinations — slide [558](../../AWS_Certified_Developer_Slides_v45.pdf#page=558)

| Invocation type | Destinations | For |
|---|---|---|
| **Asynchronous** | SQS, SNS, Lambda, EventBridge bus | **Successful AND failed** events |
| **Event source mapping** | SQS, SNS | **Discarded** event batches |

- ⭐ AWS **recommends Destinations over DLQ** (both can be used at once)
- Destinations can capture **success**; DLQ only captures **failure**
- For SQS sources you can also send to a DLQ **directly from SQS**

---

## 1️⃣2️⃣ Lambda Permissions — IAM Roles & Resource Policies — slides [559](../../AWS_Certified_Developer_Slides_v45.pdf#page=559)–560

```
      WHO can invoke me?                    WHAT can I call?
  (Resource-based policy)               (Execution role — IAM role)
 S3 / API GW / other account ──▶  λ  ──▶ DynamoDB / S3 / CloudWatch Logs …
```

### Execution role (outbound)
Grants the function permissions to AWS services. Managed policies:

| Policy | Allows |
|---|---|
| `AWSLambdaBasicExecutionRole` | Upload logs to **CloudWatch** |
| `AWSLambdaKinesisExecutionRole` | Read from **Kinesis** |
| `AWSLambdaDynamoDBExecutionRole` | Read from **DynamoDB Streams** |
| `AWSLambdaSQSQueueExecutionRole` | Read from **SQS** |
| `AWSLambdaVPCAccessExecutionRole` | Deploy in a **VPC** |
| `AWSXRayDaemonWriteAccess` | Upload traces to **X-Ray** |

- ⭐ **Event source mapping uses the execution role** to read event data
- Best practice: **one execution role per function**

### Resource-based policy (inbound)
- Gives **other accounts and AWS services** permission to use your function (like an S3 bucket policy)
- Access allowed if **IAM policy OR resource policy** allows it
- ⭐ When **S3** (or another service) calls your function → **resource-based policy**

---

## 1️⃣3️⃣ Lambda Environment Variables — slide [561](../../AWS_Certified_Developer_Slides_v45.pdf#page=561)

- Key/value pairs in **String** form
- Change behavior **without updating code**
- Lambda adds its own system env vars too
- Can store **secrets encrypted by KMS** (Lambda service key or **your own CMK**)
- Limit: **4 KB** total

---

## 1️⃣4️⃣ Lambda Monitoring & X-Ray Tracing — slides [562](../../AWS_Certified_Developer_Slides_v45.pdf#page=562)–563

### CloudWatch
- **Logs:** execution logs → CloudWatch Logs (execution role must allow writing logs)
- **Metrics:** Invocations, Durations, Concurrent Executions, Error count, Success Rates, **Throttles**, Async Delivery Failures, **Iterator Age** (Kinesis & DynamoDB Streams — how far behind you are)

### X-Ray
- Enable **Active Tracing** in config → Lambda runs the **X-Ray daemon for you**
- Use the **X-Ray SDK** in code
- Execution role needs **`AWSXRayDaemonWriteAccess`**
- Environment variables:

| Variable | Meaning |
|---|---|
| `_X_AMZN_TRACE_ID` | The tracing header |
| `AWS_XRAY_CONTEXT_MISSING` | Default `LOG_ERROR` |
| `AWS_XRAY_DAEMON_ADDRESS` | Daemon `IP_ADDRESS:PORT` |

---

## 1️⃣5️⃣ Lambda@Edge & CloudFront Functions — slides [564](../../AWS_Certified_Developer_Slides_v45.pdf#page=564)–569

**Edge function** = code attached to a **CloudFront distribution**, runs close to users, serverless, global, pay per use.

### Where each can run
```
Client ─[Viewer Request]─▶ CloudFront ─[Origin Request]─▶ Origin
Client ◀─[Viewer Response]─ CloudFront ◀─[Origin Response]─ Origin

CloudFront Functions: Viewer Request/Response ONLY
Lambda@Edge:          all 4 (Viewer + Origin)
```

### Comparison
| | **CloudFront Functions** | **Lambda@Edge** |
|---|---|---|
| Runtime | JavaScript | Node.js, Python |
| Scale | **Millions** req/s | Thousands req/s |
| Triggers | Viewer req/resp | Viewer + **Origin** req/resp |
| Max execution | **< 1 ms** | 5–10 s |
| Max memory | 2 MB | 128 MB – 10 GB |
| Package size | 10 KB | 1–50 MB |
| Network / file system access | ❌ | ✅ |
| Request body access | ❌ | ✅ |
| Pricing | Free tier, **1/6 price** of @Edge | Per request + duration |
| Authoring | Native in CloudFront | Author in **us-east-1**, replicated |

### Use cases
| CloudFront Functions | Lambda@Edge |
|---|---|
| Cache key normalization | Longer execution (several ms) |
| Header manipulation | Adjustable CPU/memory |
| URL rewrites / redirects | 3rd-party libraries (e.g. AWS SDK) |
| Request auth (create/validate **JWT**) | Network access to external services; file system / request body access |

---

## 1️⃣6️⃣ Lambda in VPC — slides [570](../../AWS_Certified_Developer_Slides_v45.pdf#page=570)–572

### By default
Lambda runs in an **AWS-owned VPC** → can reach the **public internet and DynamoDB**, but **cannot** reach private resources in *your* VPC (RDS, ElastiCache, internal ELB).

### In your VPC
- Define **VPC ID, Subnets, Security Groups**
- Lambda creates an **ENI** in your subnets
- Needs **`AWSLambdaVPCAccessExecutionRole`**
- Allow the Lambda security group in the **RDS security group**

### Internet access from a VPC Lambda
| Setup | Internet? |
|---|---|
| Lambda in VPC (default) | ❌ No |
| Lambda in **public subnet** | ❌ **Still no** — no public IP |
| Lambda in **private subnet + NAT Gateway/Instance** | ✅ Yes |
| **VPC endpoints** | ✅ Private access to AWS services without NAT |

> ⭐ CloudWatch Logs works **even without** an endpoint or NAT.

---

## 1️⃣7️⃣ Lambda Function Performance — slides [573](../../AWS_Certified_Developer_Slides_v45.pdf#page=573)–576

### Configuration
- **RAM:** 128 MB – **10 GB** in 1 MB increments
- More RAM → more **vCPU**; **1,792 MB = 1 full vCPU**; above that, up to **6 vCPU** (need multi-threading)
- ⭐ **CPU-bound? → increase RAM** (there's no CPU setting)
- **Timeout:** default **3 s**, max **900 s (15 min)**

### Execution context
- Temporary runtime environment that initializes external dependencies
- Kept around for reuse → next invocation **reuses** DB connections, HTTP/SDK clients
- Includes **`/tmp`**
- ⭐ **Initialize outside the handler** (connect to DB once, reuse across invocations)

### /tmp space
- Up to **10 GB**; for big downloads / scratch disk
- Persists while the context is frozen → **transient cache**
- Permanent storage → **S3**
- Encrypt `/tmp` content → generate **KMS data keys**

---

## 1️⃣8️⃣ Lambda Layers — slide [577](../../AWS_Certified_Developer_Slides_v45.pdf#page=577)

Two uses:
1. **Custom runtimes** (e.g. C++, Rust)
2. **Externalize dependencies** to reuse them → small app package + shared heavy libraries in layers

> Limit: **5 layers per function**, **250 MB total** (unzipped).

---

## 1️⃣9️⃣ Lambda File Systems Mounting — slides [578](../../AWS_Certified_Developer_Slides_v45.pdf#page=578)–579

- Lambda can mount **EFS** if it runs **in a VPC**
- Mounted to a local directory **during initialization**
- Must use **EFS Access Points**
- ⚠️ Watch **EFS connection limits** (1 function instance = 1 connection) and burst limits

### Storage options compared
| | `/tmp` | Layers | S3 | EFS |
|---|---|---|---|---|
| Max size | 10,240 MB | 5 layers, 250 MB | Elastic | Elastic |
| Persistence | **Ephemeral** | Durable | Durable | Durable |
| Content | Dynamic | **Static** | Dynamic | Dynamic |
| Type | File system | Archive | Object | File system |
| Shared across invocations | ❌ | ✅ | ✅ | ✅ |
| Speed | Fastest | Fastest | Fast | Very fast |
| Permissions | Function only | IAM | IAM | IAM + NFS |

---

## 2️⃣0️⃣ Lambda Concurrency — slides [580](../../AWS_Certified_Developer_Slides_v45.pdf#page=580)–584

- Account limit: **1000 concurrent executions** per region (raise via support ticket)
- **Reserved concurrency** = a **limit** at the function level
- Over the limit → **Throttle**:
  - **Sync** → `ThrottleError` **429**
  - **Async** → retry automatically, then **DLQ**

### ⚠️ The concurrency problem
Without reserved concurrency, **one busy function can use all 1000** and throttle every other function in the account (ALB users, API Gateway users, SDK callers…).

### Async + throttling
- On **429** or **5xx** errors, Lambda returns the event to the queue and retries for **up to 6 hours**
- Backoff grows **exponentially from 1 s to max 5 min**

### Cold starts & Provisioned Concurrency
- **Cold start:** new instance → load code + run init (outside handler) → first request is slower
- **Provisioned concurrency:** allocated **in advance** → **no cold starts**, low latency
- **Application Auto Scaling** can manage it (schedule or target utilization)

| | Reserved concurrency | Provisioned concurrency |
|---|---|---|
| Purpose | **Cap / guarantee** max concurrency | **Pre-warm** instances |
| Fixes | Noisy-neighbor throttling | **Cold starts** |

---

## 2️⃣1️⃣ Lambda External Dependencies — slide [585](../../AWS_Certified_Developer_Slides_v45.pdf#page=585)

- Install packages **alongside your code and zip together**
  - Node.js → npm, `node_modules`
  - Python → `pip --target`
  - Java → `.jar` files
- Zip **< 50 MB → upload directly**; otherwise **upload to S3 first**
- Native libraries must be **compiled on Amazon Linux**
- ⭐ **AWS SDK is included by default**

---

## 2️⃣2️⃣ Lambda and CloudFormation — slides [586](../../AWS_Certified_Developer_Slides_v45.pdf#page=586)–588

### Inline
- `Code.ZipFile` property
- ⚠️ **Cannot include dependencies**

### Through S3
- Reference `S3Bucket`, `S3Key` (full path to zip), `S3ObjectVersion` (if versioned)
- ⭐ Trap: update the zip in S3 but **don't change** `S3Bucket`/`S3Key`/`S3ObjectVersion` → CloudFormation **won't update** the function

### Multiple accounts
S3 bucket in Account 1 with a **bucket policy** allowing the other accounts' principals; CloudFormation **execution role** in Accounts 2/3 allows get & list on that bucket.

---

## 2️⃣3️⃣ Lambda Container Images — slides [589](../../AWS_Certified_Developer_Slides_v45.pdf#page=589)–591

- Deploy functions as container images **up to 10 GB** from **ECR**
- Base image must implement the **Lambda Runtime API**
- AWS base images: Python, Node.js, Java, .NET, Go, Ruby
- Test locally with the **Lambda Runtime Interface Emulator**

```dockerfile
FROM amazon/aws-lambda-nodejs:12
COPY app.js package*.json ./
RUN npm install
CMD [ "app.lambdaHandler" ]
```

### Best practices
1. Use **AWS-provided base images** (stable, Amazon Linux 2, cached by Lambda)
2. **Multi-stage builds** (copy only the artifacts you need)
3. Build from **stable → frequently changing** (put frequent changes last)
4. **Single ECR repository** for functions with large layers (ECR de-duplicates layers)

---

## 2️⃣4️⃣ Lambda Versions and Aliases — slides [592](../../AWS_Certified_Developer_Slides_v45.pdf#page=592)–593

```
 Users
   │
 DEV alias ─▶ $LATEST (mutable)
 TEST alias ─▶ V2
 PROD alias ─┬─ 95% ─▶ V1 (immutable)
             └─  5% ─▶ V2 (immutable)
```

| | **Versions** | **Aliases** |
|---|---|---|
| What | Snapshot of **code + configuration** | **Pointer** to a version |
| Mutable? | ❌ **Immutable** (except `$LATEST`) | ✅ Mutable |
| ARN | Own ARN | Own ARN |
| Numbering | Increasing numbers | Names like dev/test/prod |
| Superpower | Stable, reproducible releases | **Weighted traffic (canary)** + stable config for triggers/destinations |

> ⚠️ **Aliases cannot point to other aliases.**

---

## 2️⃣5️⃣ Lambda and CodeDeploy — slides [594](../../AWS_Certified_Developer_Slides_v45.pdf#page=594)–595

**CodeDeploy automates traffic shifting on a Lambda alias** (integrated into **SAM**).

| Strategy | Behavior | Examples |
|---|---|---|
| **Linear** | Grow traffic every N minutes until 100% | `Linear10PercentEvery3Minutes`, `Linear10PercentEvery10Minutes` |
| **Canary** | Try X%, then 100% | `Canary10Percent5Minutes`, `Canary10Percent30Minutes` |
| **AllAtOnce** | Immediate | — |

- **Pre & Post Traffic hooks** check the health of the function

### AppSpec.yml (all required)
| Field | Meaning |
|---|---|
| `Name` | Function name |
| `Alias` | Alias to shift |
| `CurrentVersion` | Version traffic points to **now** |
| `TargetVersion` | Version traffic shifts **to** |

---

## 2️⃣6️⃣ Lambda Function URL — slides [596](../../AWS_Certified_Developer_Slides_v45.pdf#page=596)–599

- **Dedicated HTTPS endpoint**: `https://<url-id>.lambda-url.<region>.on.aws` (never changes, IPv4 & IPv6)
- **Public internet only** — ⚠️ **no PrivateLink**
- Supports **resource-based policies** and **CORS**
- Applies to an **alias or `$LATEST`** only (not other versions)
- Throttle using **reserved concurrency**

### Security
| AuthType | Behavior |
|---|---|
| **`NONE`** | Public, unauthenticated — resource-based policy **must still grant public access** |
| **`AWS_IAM`** | IAM authenticates; principal needs **`lambda:InvokeFunctionUrl`** |

**AWS_IAM evaluation:**
- **Same account:** identity policy **OR** resource policy allows
- **Cross account:** identity policy **AND** resource policy must both allow

**CORS:** needed when calling the URL from a **different domain** (e.g. site on `example.com` calling `api.example.com`).

---

## 2️⃣7️⃣ Lambda Limits — slide [600](../../AWS_Certified_Developer_Slides_v45.pdf#page=600)

| Category | Limit |
|---|---|
| Memory | **128 MB – 10 GB** (1 MB increments) |
| Max execution time | **900 s (15 min)** |
| Environment variables | **4 KB** |
| `/tmp` disk | **512 MB – 10 GB** |
| Concurrent executions | **1000** (can be increased) |
| Deployment zip (compressed) | **50 MB** |
| Uncompressed code + dependencies | **250 MB** |
| Container image | **10 GB** |

> Need more than the deployment limits? Load extra files into `/tmp` at startup, use Layers, or a container image.

---

## 2️⃣8️⃣ Lambda Best Practices — slide [601](../../AWS_Certified_Developer_Slides_v45.pdf#page=601)

- **Heavy work outside the handler:** DB connections, AWS SDK init, dependencies/datasets
- **Environment variables** for connection strings, bucket names; **KMS-encrypt** secrets
- **Minimize package size**; split functions if needed; remember limits; use **Layers**
- ⚠️ **Never have a Lambda function call itself** (avoid recursion)

---

## 🔢 Numbers Cheat Sheet

| Number | Meaning |
|---|---|
| **3 s / 900 s** | Default / max timeout |
| **128 MB – 10 GB** | Memory |
| **1,792 MB** | = 1 full vCPU |
| **4 KB** | Environment variables |
| **50 MB / 250 MB** | Zipped / unzipped deployment |
| **10 GB** | `/tmp` max, container image max |
| **5 layers / 250 MB** | Layers limit |
| **1000** | Account concurrency |
| **3 tries** | Async retries (1 min, then 2 min) |
| **6 hours** | Async retry window on throttling/5xx |
| **6×** | SQS visibility timeout vs Lambda timeout |
| **1–10** | SQS batch size |
| **10 batches/shard** | Stream parallelization |
| **+60/min, 1000 batches** | SQS standard scaling |
| **429** | Sync throttle error |
| **< 1 ms / 2 MB / 10 KB** | CloudFront Functions limits |

---

## 🚨 Top Exam Traps

1. **SQS DLQ goes on the queue**, not on Lambda — Lambda DLQ is **async only**.
2. **Destinations > DLQ** (and destinations can capture **success**).
3. Lambda in a **public subnet has no internet** — use **private subnet + NAT**.
4. **CPU-bound → add RAM**.
5. **Initialize outside the handler** to reuse connections.
6. **Reserved** concurrency = cap; **Provisioned** concurrency = no cold starts.
7. CloudFormation won't update code unless **S3Key/S3ObjectVersion changes**.
8. **Aliases can't point to aliases**; versions are **immutable**.
9. Function URL: **no PrivateLink**; cross-account `AWS_IAM` needs **both** policies.
10. Two writes to a non-versioned S3 object may give **one event** → **enable versioning**.
11. S3/SNS/EventBridge calling Lambda → **resource-based policy**; Lambda calling DynamoDB → **execution role**.
12. Lambda@Edge is authored in **us-east-1**; CloudFront Functions only run on **viewer** triggers.

---

## 💾 How to Use This Guide

1. Read the **Mental Model** and **3 invocation models** table first — most questions hinge on it.
2. Go top-to-bottom; it matches the lecture and the slide order.
3. Cover the right-hand columns of tables and quiz yourself.
4. Finish with the **Numbers Cheat Sheet** and **Top Exam Traps**.
