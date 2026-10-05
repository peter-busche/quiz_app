# AWS Developer Exam: Question Patterns

"If the question says X, the answer is Y" rules pulled from the quizzes in `quizzes/udemy_questions/`.
References like `22#4` mean section 22, question 4.

---

## How to read the question wording

| Wording | Usually points to |
|---|---|
| MOST secure | IAM role (never access keys), least privilege, a specific resource ARN |
| LEAST operational overhead / SIMPLEST / EASIEST | A built-in managed feature (TTL, alias, stage, managed rotation) over custom code |
| MOST cost-effective | Serverless / pay-per-use, lazy loading, delete-and-recreate instead of deleting items |
| Numbers exceed a hard limit (Lambda concurrency, KMS request rate) | "Contact AWS Support / request a quota increase" is a real answer |
| MUST | The one unavoidable step (e.g. limit increase, VPC endpoint, CORS) |

---

## Sessions and state

| Clue | Answer | Trap / note |
|---|---|---|
| Serverless app, fault tolerant, "no sessions lost if an EC2 instance fails" | **DynamoDB** for session storage (22#5, 22#10, 22#24) | Sticky sessions, EBS, instance store all lose data |
| On-prem app keeps sessions in memory, migrating behind an ELB, "in-memory", sub-millisecond | **ElastiCache (Redis)** (08#5, 08#6, 08#9, 08#13, 08#20) | Both DynamoDB and ElastiCache are valid session stores; pick based on "serverless" vs "in-memory/cache" wording |
| Remove expired sessions / old items automatically, cheapest | **DynamoDB TTL** attribute (22#4, 22#15, 22#30) | A Lambda cron job that deletes items costs WCUs |
| Table must be empty every night, records needed for 1 hour | **Delete and recreate the table** (22#33) | TTL is not guaranteed to be immediate; scans + deletes cost capacity |

## Caching

| Clue | Answer | Trap / note |
|---|---|---|
| Users see stale data after an update | **Cache not invalidated** on write (08#1) | |
| Cache must be strongly consistent with the DB | **Write-through** (08#2) | |
| Only cache what is actually requested / reduce cache cost | **Lazy loading** (cache-aside) (08#16) | |
| Cache must be highly available, encrypted, or is expensive to repopulate | **ElastiCache for Redis** (cluster mode for HA) (08#3, 08#14, 08#17) | Memcached has no replication, persistence or encryption at rest |
| DynamoDB needs microsecond / sub-millisecond reads | **DAX** (22#35) | ElastiCache would need app-side cache logic |
| Read-heavy RDS | **Read replicas** + point read queries at the replica endpoint (08#8) | Multi-AZ standby cannot serve reads |
| Reporting app in another Region needs reads | **Cross-Region read replica** (08#19) | |
| Lambda + RDS, "too many connections" / "connection limit exceeded" | **RDS Proxy** (08#12) | Bigger instance or `max_connections` (08#15) only delays the problem |
| Spiky traffic to a relational DB, cost-effective | **Aurora** with **Aurora Auto Scaling** for replicas (08#11) | |
| Aurora HA across Regions | Primary in main Region, **Aurora Replica / Global Database** as failover in the other (08#10) | |
| Make an API faster for everyone | **API Gateway stage caching** (23#9, 23#15) | |
| Clients need to bypass / invalidate the API cache | Header **`Cache-Control: max-age=0`** (23#8, 23#14) | |
| CloudFront keeps serving old files | **Invalidate** the paths on the edge caches (15#3, 15#6) | |

## Identity and authentication (Cognito, IAM, STS)

| Clue | Answer | Trap / note |
|---|---|---|
| Guest / unauthenticated / "users won't log in" but need AWS resources | **Cognito identity pool** with **unauthenticated identities** + limited IAM role (27#4, 27#10) | User pools can't hand out AWS credentials |
| Sign-up / sign-in, user directory, email sign-up, store user attributes | **Cognito user pool** (27#11) | |
| MFA on login, social sign-in on sign-up, hosted login page with logo | **User pool** (MFA, social IdPs, customized **hosted UI**) (27#2, 27#3, 27#7) | |
| Users log in with Amazon/Facebook/Google and then access **S3/DynamoDB directly** | **Identity pool** (web identity federation) (27#6); both pools together when users also self-manage passwords (27#1) | |
| Corporate **SAML** directory | **Identity pool federated with SAML**, IAM trust-policy condition (27#8) | |
| Unique ID per user across all devices | **Developer-authenticated identities** in Cognito (27#5, 27#9) | |
| Sync user data between mobile devices | **Cognito Sync** (99#3) | |
| API auth by checking custom headers against a DynamoDB table | **Lambda authorizer** (23#6) | Cognito authorizer only validates Cognito tokens |
| Each user only sees their own DynamoDB items | IAM condition **`dynamodb:LeadingKeys`** = `${cognito/www.amazon.com:user_id}` (22#9, 22#34) | |
| One S3 policy, each user gets their own folder | **Policy variables** like `${aws:username}` (04#10) | |
| API calls need MFA | **`GetSessionToken`** (12#3) | |
| Temporary access to another account | Cross-account role + **`sts:AssumeRole`** (29#3) | Creating IAM users in prod |
| "Encoded authorization failure message" | **`sts decode-authorization-message`** (29#2) | |
| Code on EC2 / ECS / Lambda needs AWS access | **Instance profile / ECS task role / execution role** (05#5, 16#1, 16#2) | Access keys in env vars or code are always wrong |
| Several ECS services each need different permissions | **One IAM role per service** as task roles (16#16) | One shared role breaks least privilege |
| Switched to a role but app still uses old permissions | Credential chain: **env vars are checked before the instance profile** (29#1) | |
| Restrict what a member account in AWS Organizations can do | **Service Control Policy** (deny list for specific actions) (99#2, 99#6) | |
| Access keys leaked or lost | **Delete/deactivate and create new ones** (04#5, 04#8) | Keys can't be recovered |
| Resource-based policy: who gets access | **`Principal`** element (04#4) | |
| Standalone vs inline policies, groups | **Managed policies** attached to **groups** (04#2, 04#3, 04#7) | |

## Messaging and streaming (SQS, SNS, Kinesis)

| Clue | Answer | Trap / note |
|---|---|---|
| Same message to multiple queues / consumers | **SNS topic with SQS queues subscribed** (fan-out) (19#1) | |
| One tier can't keep up with bursts / decouple | **Put an SQS queue between tiers** (19#7, 19#9) | |
| Too many empty responses, polling is costly | **Long polling**: `WaitTimeSeconds` / `ReceiveMessageWaitTimeSeconds` = 20 (19#4, 19#15, 19#19, 19#11) | Short polling = more empty API calls |
| Message picked up again while still being processed | **Increase the visibility timeout** (19#5) | |
| Duplicates must be removed / strict order | **FIFO queue** + **message deduplication ID** (19#22) | |
| Message larger than 256 KB (e.g. 1 GB job) | **SQS Extended Client Library** storing the payload in **S3** (19#25) | |
| Get more messages per call | **`MaxNumberOfMessages`** up to 10 (19#3) | |
| Hide messages for a time after they are sent | **Delay queue** (19#18) | Visibility timeout applies after receive |
| Messages keep failing | **Dead-letter queue** / redrive policy (19#10, 19#20) | |
| Real-time, terabytes/hour, multiple consumers, replay | **Kinesis Data Streams** (19#2) | |
| Load a stream straight into S3 / Redshift / OpenSearch, no code | **Kinesis Data Firehose** (19#23, 19#24) | |
| Stream can't keep up with incoming data | **Add shards** (`UpdateShardCount`) (19#14, 19#6) | |
| Producers underuse shards | **Kinesis Producer Library (KPL)** (batching/aggregation) (19#27) | |
| Max useful KCL workers | **= number of shards** (19#13) | |
| Records missing when a consumer runs every 48 h | **Default retention is 24 hours** (19#16) | |
| Record order with Lambda | **Ordered within a shard, not across shards** (21#19) | |
| Encrypt stream data at rest | **Kinesis server-side encryption with KMS** (19#8) | |
| Send SMS, email, mobile push | **SNS** (19#21, 19#26) | SES is email only |

## Lambda

| Clue | Answer | Trap / note |
|---|---|---|
| "X invocations/sec, Y seconds each" | **Concurrency = rate × duration** (21#27 = 400, 21#33 = 30) | |
| Result is over 1,000 | **Request a concurrency limit increase** from AWS (21#3, 21#20) | Reserved concurrency can't exceed the account limit |
| Primary benefit of init outside the handler | **Execution environment reuse** (21#6) | |
| Same large file downloaded every invocation | **Cache it in `/tmp`** (21#12) | |
| Several functions share libraries | **Lambda layers** (21#17, 21#30) | |
| One function needs libraries not in the runtime | **ZIP with code + dependencies** (21#25, 24#26) | |
| Python function uploads to S3 with least code change | **Use the preinstalled boto3 SDK** (21#26) | |
| No logs in CloudWatch | **Execution role lacks CloudWatch Logs permissions** (21#5, 21#23) | |
| Stable ARN for "latest", rollback, % traffic to new version | **Alias** (weighted alias for traffic shifting) (21#15, 21#22, 21#35) | `$LATEST` isn't a stable released version |
| Invoke asynchronously | `--invocation-type Event` → **HTTP 202**; sync → **200** (21#11, 21#13, 21#18, 21#21) | |
| Run on a schedule | **EventBridge (CloudWatch Events) scheduled rule** (21#24) | |
| React to AWS events (EC2 state change, CodePipeline) | **EventBridge rule with an event pattern** (20#15, 24#18) | |
| Send the result/failure to another service | **Lambda destinations** (on-success / on-failure → SNS/SQS) (19#12, 19#17) | |
| Error adding an on-failure destination | **Execution role** needs `sqs:SendMessage` etc. (21#32) | |
| Services Lambda **polls** (event source mapping) | **SQS, Kinesis, DynamoDB Streams** (21#4) | S3/SNS push to Lambda instead |
| Run code when DynamoDB items change / copy changes elsewhere | **DynamoDB Streams + Lambda** (21#7, 22#16, 22#29) | |
| Duplicate log entries, same request ID | **Async invoke failed and Lambda retried it** (21#28) | |
| Duplicates from a Kinesis stream | **Unhandled error → the whole batch is retried** (21#31) | |
| Let S3 invoke the function | **`lambda add-permission`** (resource-based policy) (21#34) | Execution role controls what Lambda can call, not who calls it |
| Lambda@Edge stack fails in another Region | **Lambda@Edge must be in us-east-1** (21#1) | |
| Auth check on every CloudFront request | **Lambda@Edge viewer-request trigger** (15#4) | |
| Hide env var secrets even from key users in the console | **Encryption helpers** (client-side encryption) (21#10) | |
| Unique ID per invocation for logging | **`context.awsRequestId`** (21#2) | |
| Lambda in a private subnet needs DynamoDB/SQS | **VPC endpoint** (10#2, 10#5) | NAT works too, but isn't "private IPs only" |
| Burst of S3 events | **Lambda scales out concurrently** (21#36) | |

## DynamoDB

| Clue | Answer | Trap / note |
|---|---|---|
| Capacity maths | **RCU**: 4 KB units, strong = 1, eventual = 0.5; **WCU**: 1 KB units, round item size **up** (22#1, 22#7, 22#13, 22#17, 22#32) | Round per item before multiplying |
| Throttling but total capacity isn't used | **Hot partition** → better partition key / **random suffix** (22#14) | |
| Base table throttled after adding a GSI | **GSI write capacity too low** (22#6) | |
| `ThrottlingException` / occasional throttling | **Exponential backoff** (retries) (12#1, 22#22, 21#29) | |
| Query by a non-key attribute / top scores per game | **Global secondary index** with the new PK + sort key (22#8, 22#31) | LSI must be created with the table |
| Several items share a partition key | **Composite key** (partition + sort) (22#12, 22#25) | |
| Concurrent updates overwrite each other | **Conditional writes** (optimistic locking) (22#3) | |
| All-or-nothing group of writes | **`TransactWriteItems`** (22#23) | `BatchWriteItem` isn't atomic |
| Many items in one call, even across tables | **`BatchGetItem`** (22#2, 22#18) | |
| Fewest RCUs | **Query + eventually consistent** (22#20, 22#21) | Scan reads the whole table |
| Scan a big table quickly without hurting prod | **Parallel scan + rate limit** (`Limit`) (22#19, 22#26, 22#27) | |
| Reduce a scan's impact | **Smaller page size** (22#28) | |
| Least IAM permissions to "get, update or create" an item | `GetItem`, `UpdateItem`, `PutItem` (22#11) | |

## API Gateway

| Clue | Answer | Trap / note |
|---|---|---|
| Multiple versions / environments for testing | **Stages** + **stage variables** (23#4, 23#7, 23#11) | |
| Gradual rollout of a new API version | **Canary release** on the stage (`canarySettings`) (23#1) | |
| Test request validation before prod | **Deploy to a new stage**, test, then promote (23#3) | |
| Legacy **SOAP/XML** backend | **REST API + mapping templates** (JSON → XML) (23#5, 23#13) | HTTP APIs don't support mapping templates |
| HTTP GET proxied straight to Lambda | **Lambda proxy integration** (23#10) | |
| Track WebSocket connects/disconnects | **`$connect` / `$disconnect` routes** (23#12) | |
| One front door for many services | **API Gateway** (99#5) | |
| Custom domain + CloudFront + third-party cert | **Import the cert into ACM** (us-east-1 for edge-optimized) (09#2) | |

## S3 and CloudFront security

| Clue | Answer | Trap / note |
|---|---|---|
| All uploads must be encrypted | Bucket policy **deny `PutObject` without `x-amz-server-side-encryption`** (14#1) | |
| Must use HTTPS / encryption in transit | Bucket policy **deny when `aws:SecureTransport` is false** (14#5, 14#7) | |
| Temporary access to a private object | **Presigned URL** (13#3, 14#2, 14#9) | Making the object public |
| Other sites hotlink your images | **Remove public access, use signed URLs with expiry** (14#4) | |
| Premium content only for paying CloudFront users | **CloudFront signed URLs + OAI/OAC** so the bucket is private (14#8) | |
| JavaScript can't load assets from another bucket | **Enable CORS on the bucket being requested** (14#3) | CORS goes on the *target* bucket |
| HTTPS for an S3 static website | **CloudFront in front of S3** (15#5) | S3 website endpoints are HTTP only |
| Encrypt user → CloudFront → origin | **Viewer protocol policy + origin protocol policy** (15#1, 15#2) | |
| Slow uploads from around the world | **S3 Transfer Acceleration** (13#2, 13#4) | |
| More than ~5,500 GET/sec | **Spread objects across more prefixes** (13#1) | |
| Copies in another Region for compliance | **Cross-Region Replication** (11#1) | |
| Block specific countries | **AWS WAF geo-match rule** (or CloudFront geo restriction) (10#3) | Security groups / NACLs can't filter by country |
| Static site with HTML, images, JS, serverless | **S3 + CloudFront** (11#3) | |

## Encryption and secrets (KMS, Secrets Manager)

| Clue | Answer | Trap / note |
|---|---|---|
| Encrypt data over 4 KB / a unique key per file | **`GenerateDataKey`** → encrypt with the plaintext key, store the encrypted key next to the data (envelope encryption) (21#14, 30#10, 30#11, 30#12) | KMS `Encrypt` is limited to 4 KB |
| Which KMS permission for data keys | **`kms:GenerateDataKey`** (30#6) | |
| KMS throttling (`ThrottlingException`) | **Data key caching** with the Encryption SDK (`LocalCryptoMaterialsCache`), **backoff**, **quota increase** (30#2, 30#5) | |
| Rotate DB credentials automatically | **Secrets Manager** with rotation (30#1, 30#4, 30#7) | Parameter Store has no built-in rotation |
| Store a third-party API key | **Secrets Manager** (30#8) | |
| Rotate encryption keys yearly, easiest | **KMS automatic key rotation** (30#3) | |
| Dedicated, tamper-resistant hardware | **CloudHSM** (30#9) | |
| Managed private PKI / subordinate CAs | **AWS Private CA** (31#5) | |
| Find sensitive data (PII, financial) in S3 | **Amazon Macie** (31#1) | |
| Scan for vulnerabilities / best-practice deviations | **Amazon Inspector** (99#11) | |

## Monitoring (CloudWatch, X-Ray, CloudTrail)

| Clue | Answer | Trap / note |
|---|---|---|
| Filter traces by custom key/value | **X-Ray annotations** (indexed) (20#2, 20#21) | **Metadata** is not indexed or searchable |
| Search traces for a user / filter expression via the API | **`GetTraceSummaries`** (20#5) | |
| Upload segment documents via the API | **`PutTraceSegments`** (20#16) | |
| Trace requests across API Gateway, Lambda, DynamoDB, SNS | **X-Ray** (enable active tracing on Lambda) (20#7, 20#19) | |
| Record every API call / audit | **CloudTrail** (a trail applied to all Regions → one bucket) (20#6, 20#10) | CloudWatch is metrics/logs, not API audit |
| 1-second data / react within 30 seconds | **High-resolution custom metric** + **high-resolution alarm** (20#9, 20#13, 20#18) | Standard resolution is 60 s |
| New metric filter shows nothing | **Filters only count events after they're created** (20#4, 20#11) | |
| Turn log fields into a metric per location | **Metric filter with a dimension** (20#17) | |
| Metrics/logs from on-prem servers | **CloudWatch agent** + IAM credentials (20#3, 20#20) | |
| Centralize EC2 log files | **CloudWatch Logs agent** (20#14) | |
| Custom metric from a cron job | **Unified CloudWatch agent / `PutMetricData`** (05#3) | |
| One dashboard metric per app | **Custom namespace**, metric per app (20#1) | |
| Organize metrics by instance / ASG | **`--dimensions`** (99#9) | |
| Keep PII out of logs | **CloudWatch Logs data protection** (masking) (20#8) | |
| Forward events to other accounts | **EventBridge rule → event bus in the other account** (20#12) | |

## Deployments (see also `AWS-Deployment-Types-Guide.md`)

| Clue | Answer | Trap / note |
|---|---|---|
| Elastic Beanstalk, no capacity reduction during deploy | **Rolling with additional batch** (16#8, 17#1) | Plain rolling reduces capacity |
| Only new instances / fastest rollback / zero downtime | **Immutable** (or **blue/green**) (17#2, 17#3, 17#8) | |
| Platform upgrade (e.g. new Node.js) with no risk | **Blue/green with CNAME swap** (17#5) | |
| Beanstalk config files | **`.ebextensions/`** folder (17#4) | |
| Beanstalk source bundle rules | One ZIP/WAR, **no parent folder**, **≤ 512 MB** (17#7) | |
| 10% first, then the rest | **Canary** (e.g. `ECSCanary10Percent15Minutes`, `LambdaCanary10Percent5Minutes`) (24#3, 24#7, 24#10) | |
| Equal increments over time | **Linear** (24#23) | |
| Lambda AppSpec `resources` | `name`, `alias`, `currentversion`, `targetversion` (21#8) | |
| Hook order: EC2 | `BeforeInstall → AfterInstall → ApplicationStart → ValidateService` (24#25) | |
| Hook order: ECS | `BeforeInstall → AfterInstall → AfterAllowTestTraffic → BeforeAllowTraffic → AfterAllowTraffic` (24#16) | |
| Hook order: Lambda | `BeforeAllowTraffic → AfterAllowTraffic` (24#17) | |
| Validate an ECS deploy with a Lambda before traffic shifts | **Test listener** + Lambda on the **`BeforeAllowTraffic`** hook (16#9) | |
| Manual approval before prod | **CodePipeline approval action** (24#8) | |
| Tests/build → **CodeBuild**; install on servers (EC2 + on-prem) → **CodeDeploy**; Git repo → **CodeCommit** (24#1, 24#6, 24#15, 24#2, 24#4) | | |
| Push a Docker image only after a successful build | **`post_build`** phase in buildspec (24#19) | |
| CodeCommit over HTTPS / SSH | **Git credentials from IAM** / **upload SSH public key to IAM** (24#20, 24#11) | |
| Commit a file from Lambda | **CodeCommit SDK `PutFile`** (12#4, 24#5) | |
| Deploy an on-prem built package to EC2 | **Upload the bundle to S3** + CodeDeploy (24#21) | |

## Containers (ECS)

| Clue | Answer | Trap / note |
|---|---|---|
| Fewest instances / pack tasks | **`binpack`** strategy (16#10, 16#18) | |
| Spread across AZs, then instances | **`spread`** on `attribute:ecs.availability-zone`, then `instanceId` (16#12) | |
| No preference, simplest | **`random`** (16#7) | |
| Each task on a different instance | **Placement constraint `distinctInstance`** (16#4) | Constraints = rules; strategies = preferences |
| Only on certain instance types / groups | **`memberOf`** constraint with an expression (16#5, 16#6, 16#17) | |
| Many containers on port 80, one host | **Host port 0** (dynamic port mapping) with an ALB (05#4, 16#19) | |
| Pay per task, variable workloads | **Fargate** (16#11, 16#15) | |
| Sidecar sharing logs/metrics | **Both containers in one task definition** + a shared volume (16#13) | |
| Env vars for a container | Task definition **`environment`** parameter (16#14) | |
| Pull an ECR image | **`aws ecr get-login-password`** → `docker login` → `docker pull` (16#3, 16#20) | |

## Infrastructure as code (CloudFormation, SAM)

| Clue | Answer | Trap / note |
|---|---|---|
| SAM resources in a template | **`Transform: AWS::Serverless-2016-10-31`** (18#1) | |
| Preview stack changes | **Change set** (18#3) | |
| Stack works in one Region, fails in another with a custom AMI | **AMI IDs are Region-specific** → copy the AMI (18#4) | |
| Deploy local code referenced by a template | **`aws cloudformation package`** (or `sam package`) → **`deploy`** (25#1, 25#3, 25#7) | |
| Build and test Lambda + API Gateway locally | **SAM** (25#6) | |
| SAM resource types | `AWS::Serverless::Function`, `AWS::Serverless::SimpleTable`, `AWS::Serverless::Api` (25#2, 25#4) | |

## Networking and high availability

| Clue | Answer | Trap / note |
|---|---|---|
| Highly available / fault tolerant EC2 | **Subnet in each AZ**, ASG across AZs + ELB, RDS Multi-AZ (10#6, 08#18, 99#4) | |
| Route by subdomain / path | **Application Load Balancer** (07#6) | |
| Need the client's IP behind an ALB | **`X-Forwarded-For`** header (07#3, 07#5) | NLB preserves IP but has no HTTP headers |
| HTTPS without extra CPU on instances | **SSL termination on the load balancer** (07#1, 07#4) | |
| Keep an ASG at a CPU % | **Target tracking** policy (07#7) | |
| Send 20% of traffic to a new Region | **Route 53 weighted routing** (09#3) | |
| A record for a single EC2 instance | **Elastic IP** (09#1) | Public IPs change on stop/start |
| Capture IP traffic info | **VPC Flow Logs** (10#1) | |
| Run a script on every launch | **User data** in the launch template (05#1) | |
| SSH only from the corporate range | Security group: **443 from 0.0.0.0/0, 22 from the corporate CIDR** (05#2) | |

## Other services

| Clue | Answer | Trap / note |
|---|---|---|
| Coordinate several AWS services / replace custom state-machine code | **Step Functions** (Amazon States Language) (28#2, 28#3, 28#6) | |
| Keep the original input with a Step Functions error | **`ResultPath` in a `Catch`** (28#5) | |
| One mobile API combining data from several sources | **AppSync (GraphQL)** (28#4) | |
| Host static sites from Git branches, serverless | **Amplify Hosting** (28#1) | |
| SQL queries on logs in S3 | **Athena** (31#2) | |
| Athena partition queries time out / new partitions missing | **`MSCK REPAIR TABLE`** (99#7) | |
| Partitions that hurt performance | **Too fine-grained** or **skewed** partitions (31#3) | |
| Cloud IDE, bring your own device | **Cloud9** (99#8) | |
| Secure IoT device communication | **ACM / X.509 certificates** + TLS (31#4) | |
| Sign a request manually (SigV4) | Signature goes in the **`Authorization` header** or a **query string** (12#2) | |
