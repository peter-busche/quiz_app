# IAM Policies and Roles: Where Each One Lives

The one question to ask every time: **"Is this policy attached to the *caller* or to the *thing being called*?"**

- Attached to the **caller** (user, group, role) → **identity-based policy**. Answers *"what can I do?"* No `Principal` element.
- Attached to the **resource** (bucket, queue, key, function) → **resource-based policy**. Answers *"who can touch me?"* Always has a `Principal` element (04#4).
- Attached to an **account / OU** or a **session** → a **guardrail** (SCP, RCP, permission boundary, session policy). It never grants anything; it only caps the maximum.

---

## 1. All policy types at a glance

| Policy type | Attached to | Grants access? | Has `Principal`? | Typical use |
|---|---|---|---|---|
| **Identity-based: AWS managed** | Users, groups, roles | Yes | No | Quick start (`AmazonDynamoDBReadOnlyAccess`, 05#5) |
| **Identity-based: customer managed** | Users, groups, roles | Yes | No | Least privilege, reusable, versioned (04#2, 04#7) |
| **Identity-based: inline** | One user, group or role (1-to-1) | Yes | No | Strict 1-to-1 permissions that die with the identity. AWS prefers managed (04#2) |
| **Resource-based** | A resource (S3 bucket, SQS queue, KMS key, Lambda function…) | Yes | **Yes** | Cross-account access, letting a service call your resource |
| **Trust policy** (role trust policy) | An IAM role (it's the role's resource-based policy) | Only the right to **assume** the role | **Yes** | Who may call `sts:AssumeRole*` for this role |
| **Permission boundary** | A user or role | **No**, caps it | No | Let developers create roles without escalating privileges |
| **Service Control Policy (SCP)** | AWS Organizations root / OU / account | **No**, caps it | No | Block services, actions or Regions for whole accounts (99#2, 99#6) |
| **Resource Control Policy (RCP)** | AWS Organizations root / OU / account | **No**, caps it | Yes (applies to resources) | Cap what *resources* in the org allow, e.g. "no S3 access from outside the org" |
| **Session policy** | A temporary session (passed to `AssumeRole`, `GetFederationToken`) | **No**, caps it | No | Narrow a role further for one session |
| **Access Control Lists (ACLs)** | S3 buckets/objects (legacy), not JSON | Yes | Grantee list | Legacy S3 cross-account. Disabled by default now (Object Ownership = bucket owner enforced) |
| **VPC endpoint policy** | A VPC endpoint | **No**, caps it | Yes | "This endpoint may only reach bucket X" |
| **KMS key policy** | A KMS key | Yes | Yes | **Every key must have one.** Without it (or delegation to IAM), nobody can use the key |
| **KMS grant** | A KMS key (programmatic, not JSON) | Yes (temporary, specific operations) | Grantee principal | Services like EBS/RDS delegating key use |

> **Not IAM policies (don't mix them up):** Security groups and network ACLs control **network traffic** (IP/port), not API permissions. S3 **Block Public Access** is a setting that overrides public bucket policies/ACLs.

---

## 2. How AWS decides: the evaluation order

```
1. Any explicit DENY anywhere?                          → DENIED (always wins)
2. SCP / RCP allows it?                (if in an org)   → no → DENIED
3. Resource-based policy allows it?                     → same account: ALLOWED*
4. Permission boundary allows it?      (if set)         → no → DENIED
5. Session policy allows it?           (if passed)      → no → DENIED
6. Identity-based policy allows it?                     → yes → ALLOWED, no → DENIED (implicit deny)
```
\* simplified. The key rules:

| Situation | What's needed |
|---|---|
| **Same account** | Identity policy **OR** resource policy allows it (either one is enough) |
| **Cross-account** | Identity policy in the caller's account **AND** resource policy in the resource's account |
| **Guardrails** (SCP, RCP, boundary, session) | Access = **intersection**: must be allowed by the guardrail *and* by a granting policy |
| **KMS** | The **key policy** must allow it, or delegate to IAM with `"Principal": {"AWS": "arn:aws:iam::<acct>:root"}`. An IAM policy alone isn't enough |
| **Explicit `Deny`** | Beats every `Allow` in every policy type |

---

## 3. Services that have their own resource-based policy

If a service is on this list, **another account or AWS service can be let in by editing the resource's policy**. If it's not, you must use a role.

| Service | Name of its resource policy | Classic exam use |
|---|---|---|
| **S3** | **Bucket policy** (+ access point policies, legacy ACLs) | Enforce encryption `x-amz-server-side-encryption` (14#1), enforce HTTPS `aws:SecureTransport` (14#5, 14#7), cross-account, CloudFront OAC |
| **SQS** | **Queue policy** | Let an **SNS topic** or **S3 event notification** send to the queue |
| **SNS** | **Topic policy** | Let **S3**, CloudWatch alarms, or another account publish |
| **Lambda** | **Function policy** (resource-based policy) via `lambda add-permission` | Let **S3, SNS, API Gateway, EventBridge** invoke the function (21#34) |
| **KMS** | **Key policy** (mandatory) + grants | Who can use / administer the key (30#6) |
| **API Gateway** | **API resource policy** | Restrict by source IP / VPC / account; private APIs |
| **Secrets Manager** | **Secret resource policy** | Cross-account secret access |
| **ECR** | **Repository policy** | Other accounts pulling images |
| **EventBridge** | **Event bus policy** | Other accounts putting events on your bus (20#12) |
| **CloudWatch Logs** | **Resource policy / destination policy** | Let services (Route 53, EventBridge) write logs; cross-account subscriptions |
| **IAM role** | **Trust policy** | Who can assume the role |
| **Glacier, OpenSearch, Backup, CodeArtifact, Serverless Application Repository** | Vault / domain access / backup vault / repository / application policy | Rare on the exam |

**Not on the list (no resource policy): DynamoDB tables** are controlled by identity policies (with conditions like `dynamodb:LeadingKeys`, 22#9). EC2 instances and RDS instances also rely on identity policies only.

> DynamoDB has since added resource-based policies, but the exam and your quizzes treat DynamoDB access as **identity policy + conditions**.

---

## 4. Trust policy vs permissions policy (every role has both)

```
            ┌─────────────── IAM ROLE ───────────────┐
 WHO can    │ TRUST POLICY (resource-based)          │
 assume it  │   "Principal": {"Service":             │
 ─────────► │       "lambda.amazonaws.com"}          │
            │   "Action": "sts:AssumeRole"           │
            ├────────────────────────────────────────┤
 WHAT it    │ PERMISSIONS POLICIES (identity-based)  │
 can do     │   dynamodb:PutItem on table/Orders     │
 ─────────► │   logs:CreateLogStream, PutLogEvents   │
            └────────────────────────────────────────┘
```

| Who assumes the role | Trust policy `Principal` | STS API |
|---|---|---|
| An AWS service (Lambda, EC2, ECS…) | `"Service": "lambda.amazonaws.com"` | `AssumeRole` (done for you) |
| A user/role in another account | `"AWS": "arn:aws:iam::111122223333:root"` | `AssumeRole` (29#3) |
| Cognito identity pool users | `"Federated": "cognito-identity.amazonaws.com"` | `AssumeRoleWithWebIdentity` (27#4, 27#10) |
| Web/OIDC identity provider (Google, GitHub Actions) | `"Federated": "<oidc provider>"` | `AssumeRoleWithWebIdentity` |
| Corporate SAML directory | `"Federated": "arn:aws:iam::<acct>:saml-provider/X"` | `AssumeRoleWithSAML` (27#8) |

**`iam:PassRole`**: to *give* a role to a service (attach a role to an EC2 instance, a Lambda, a CloudFormation stack, an ECS task), the **person** doing it needs `iam:PassRole` on that role. This stops users from escalating privileges by handing a powerful role to a service.

---

## 5. Role types

| Role type | Who uses it | What it's for | Trusted service principal |
|---|---|---|---|
| **Service role** | An AWS service acting **on your behalf** | Generic term: any role you create for a service to assume | varies |
| **Service-linked role** | A specific service, created and owned by it | Predefined permissions you **can't edit**. Named `AWSServiceRoleFor…` (e.g. `AWSServiceRoleForAutoScaling`, `…ForECS`, `…ForElasticLoadBalancing`). **SCPs don't restrict them** | the service |
| **Lambda execution role** | Your Lambda function's code | What the function **can call**: CloudWatch Logs, DynamoDB, SQS, KMS… (21#5, 21#23, 21#32) | `lambda.amazonaws.com` |
| **EC2 instance role via instance profile** | Code running on an EC2 instance | Temporary credentials from the instance metadata service (16#2, 05#5) | `ec2.amazonaws.com` |
| **ECS task role** | **Your application** inside the container | What the **app code** can call (S3, DynamoDB…) (16#1, 16#16) | `ecs-tasks.amazonaws.com` |
| **ECS task execution role** | The **ECS agent / Fargate** | **Pull images from ECR**, **write to CloudWatch Logs**, fetch **Secrets Manager / SSM** values injected as env vars | `ecs-tasks.amazonaws.com` |
| **ECS container instance role** (EC2 launch type) | The ECS agent on the EC2 host | Register the instance with the cluster (`ecsInstanceRole`, delivered as an instance profile) | `ec2.amazonaws.com` |
| **Cross-account role** | Users/roles from another account | Temporary access instead of creating users (29#3) | other account |
| **Cognito identity pool roles** | App users (authenticated or guest) | One role for **authenticated**, one for **unauthenticated** identities (27#4, 27#10) | `cognito-identity.amazonaws.com` |
| **Federation / SAML / OIDC role** | Corporate or web identities | Log in with an external IdP and get AWS credentials (27#8) | federated provider |
| **IAM Identity Center permission set** | Workforce users across an org | Becomes a role in each account it's assigned to | managed by Identity Center |

### Instance profile: the one people confuse

- An **instance profile is a container** that holds exactly **one role** so EC2 can use it. EC2 can't take a role directly.
- Console: creating an EC2 role **automatically** creates an instance profile with the same name.
- CLI: you do it yourself (99#1):
  1. `aws iam create-instance-profile`
  2. `aws iam add-role-to-instance-profile`
  3. `aws ec2 associate-iam-instance-profile`
- Credentials come from **IMDS** (`http://169.254.169.254/...`) and rotate automatically.
- Credential chain order: **env vars → shared credentials file → container credentials → instance profile**. Leftover access keys in env vars beat the role (29#1).

### ECS: task role vs task execution role

| | **Task role** | **Task execution role** |
|---|---|---|
| Used by | **Your code** in the container | **ECS itself** (agent / Fargate) |
| Typical permissions | `s3:GetObject`, `dynamodb:PutItem`, `sqs:SendMessage` | `ecr:GetAuthorizationToken`, `ecr:BatchGetImage`, `logs:PutLogEvents`, `secretsmanager:GetSecretValue` |
| Symptom if missing | App gets `AccessDenied` calling AWS | Task **won't start**: can't pull image, no logs, secret injection fails |
| Credentials from | Container credentials endpoint (`AWS_CONTAINER_CREDENTIALS_RELATIVE_URI`) | Used before the container starts |

---

## 6. Per-service cheat sheet: which roles and policies each service uses

| Service | Roles it uses | Resource policies it has | Remember |
|---|---|---|---|
| **Lambda** | **Execution role** (what it calls) | **Function policy** (who invokes it) | See section 7 below. Push sources need the function policy, poll sources need the execution role |
| **EC2** | **Instance role via instance profile** | none | Never store keys on the instance |
| **ECS** | **Task role**, **task execution role**, container instance role (EC2 launch type), service-linked role | none (ECR has repository policies) | One task role per service for least privilege (16#16) |
| **Elastic Beanstalk** | **Service role** (`aws-elasticbeanstalk-service-role`: Beanstalk manages your environment) + **instance profile** (`aws-elasticbeanstalk-ec2-role`: your app on the instances) | none | Two roles: one for Beanstalk, one for your instances |
| **CodeDeploy** | **Service role** (CodeDeploy reads ASG/ELB/ECS/Lambda) + **EC2 instance profile** (agent downloads the revision from **S3**) | none | On-premises servers use an IAM user or role registered with CodeDeploy |
| **CodeBuild** | **Service role** (pull source, write logs, push to ECR/S3) | none | Push to ECR fails → check the CodeBuild service role |
| **CodePipeline** | **Service role** (start CodeBuild, CodeDeploy, read artifacts in S3) | none | |
| **CloudFormation / SAM / CDK** | Optional **service role** (`--role-arn`), else it uses the caller's permissions | none | Caller needs `iam:PassRole` for the service role |
| **Step Functions** | **State machine execution role** (`states.amazonaws.com`) to call Lambda, DynamoDB, etc. | none | |
| **API Gateway** | **CloudWatch logging role** (set once per Region in account settings); **integration credentials role** for AWS-service integrations (e.g. direct to SQS/DynamoDB) | **API resource policy** | Lambda integration → API Gateway uses the **Lambda function policy** instead of a role |
| **EventBridge** | **Target role** for some targets (Kinesis, Step Functions, ECS tasks, cross-account buses) | **Event bus policy** | Lambda/SNS/SQS targets use **their own resource policies** instead |
| **S3** | Replication role (for CRR/SRR) | **Bucket policy**, access point policies, ACLs | S3 → SQS/SNS/Lambda event notifications need the **target's** resource policy |
| **SQS / SNS** | none (they don't call other services) | **Queue policy / topic policy** | SNS → SQS fan-out needs a queue policy allowing the topic |
| **KMS** | none | **Key policy** (mandatory) + **grants** | Data key calls need `kms:GenerateDataKey` (30#6); SSE-KMS reads need `kms:Decrypt` |
| **Kinesis Data Firehose** | **Delivery role** (write to S3/Redshift/OpenSearch) | none | |
| **Cognito identity pools** | **Authenticated role** + **unauthenticated role** | none | Guest access = unauthenticated role (27#4, 27#10) |
| **DynamoDB** | none | (resource policies are new; exam uses identity policies) | Fine-grained access via `dynamodb:LeadingKeys` / `dynamodb:Attributes` conditions (22#9) |
| **AWS Organizations** | `OrganizationAccountAccessRole` in member accounts | **SCPs**, **RCPs** | SCPs don't affect the management account or service-linked roles |

---

## 7. The Lambda trap: push vs poll

This decides whether you need the **function policy** or the **execution role**.

| Event source | Who does the work | Permission goes in |
|---|---|---|
| **S3, SNS, API Gateway, EventBridge, CloudWatch Logs subscriptions, Cognito triggers** (push) | The **source service invokes** Lambda | Lambda **function (resource) policy** via `aws lambda add-permission` (21#34) |
| **SQS, Kinesis, DynamoDB Streams, MSK** (poll, "event source mapping") | **Lambda polls** the source | Lambda **execution role** (`sqs:ReceiveMessage`, `sqs:DeleteMessage`, `kinesis:GetRecords`, `dynamodb:GetRecords`…) (21#4) |
| **Destinations** (on-success / on-failure → SQS, SNS, EventBridge, Lambda) | Lambda sends the result | Lambda **execution role** (`sqs:SendMessage`, `sns:Publish`) (21#32) |
| **Writing logs** | Lambda | Execution role: `logs:CreateLogGroup`, `CreateLogStream`, `PutLogEvents` (21#5, 21#23) |

---

## 8. Exam-style "which one?" decisions

| Scenario | Answer |
|---|---|
| Allow another account to read your S3 bucket | **Bucket policy** with their account as `Principal` (plus an identity policy in their account) |
| Code on EC2/ECS/Lambda needs AWS access | **Role** (instance profile / task role / execution role), never access keys |
| Block every account in the org from using a Region or service | **SCP** |
| Stop org resources from being shared outside the org | **RCP** (or bucket policies with `aws:PrincipalOrgID`) |
| Developers may create roles but never exceed their own powers | **Permission boundary** |
| Temporary, narrowed access for one session | **Session policy** passed to `AssumeRole` |
| Force HTTPS / encryption on a bucket | **Bucket policy** with `Deny` + condition (14#1, 14#7) |
| Only allow access to a bucket through a VPC endpoint | **Bucket policy** with `aws:SourceVpce` and/or a **VPC endpoint policy** |
| Each user only gets their own S3 folder with one policy | **Policy variables** (`${aws:username}`) (04#10) |
| Each app user only gets their own DynamoDB items | Identity-pool role with a **`dynamodb:LeadingKeys`** condition (22#9, 22#34) |
| S3 event notification → SQS fails | **SQS queue policy** must allow `s3.amazonaws.com` |
| SNS → SQS fan-out, messages never arrive | **SQS queue policy** must allow the SNS topic |
| S3 → Lambda trigger | **Lambda function policy** (`add-permission`) (21#34) |
| Lambda reading from SQS fails | **Execution role** needs SQS receive/delete permissions |
| ECS task can't pull its image or write logs | **Task execution role** |
| ECS app gets `AccessDenied` from DynamoDB | **Task role** |
| Can't use a KMS key even though IAM allows it | **Key policy** doesn't allow or delegate to IAM |
| Guest users need to read an S3 bucket | **Cognito identity pool unauthenticated role** (27#10) |
| Dev account user needs access to prod | **Cross-account role** + `sts:AssumeRole` (29#3) |
| Access denied, message is encoded | `aws sts decode-authorization-message` (29#2) |
| API calls must use MFA | `sts:GetSessionToken` with the MFA code (12#3); condition `aws:MultiFactorAuthPresent` |
| Assign permissions to many users | **Groups** + **customer managed policies** (04#2, 04#7) |

---

## 9. Condition keys worth memorizing

| Condition key | Used for |
|---|---|
| `aws:SecureTransport` | Require HTTPS (14#5, 14#7) |
| `s3:x-amz-server-side-encryption` | Require SSE on uploads (14#1) |
| `aws:SourceIp` | Restrict by IP range |
| `aws:SourceVpce` / `aws:SourceVpc` | Only via a VPC endpoint / VPC |
| `aws:SourceArn` / `aws:SourceAccount` | Stop the "confused deputy" when a service invokes your resource (the `--source-arn` / `--source-account` in 21#34) |
| `aws:PrincipalOrgID` | Only principals from your AWS Organization |
| `aws:MultiFactorAuthPresent` | Require MFA |
| `aws:RequestedRegion` | Restrict Regions (common in SCPs) |
| `dynamodb:LeadingKeys` | Row-level (partition key) access (22#9) |
| `dynamodb:Attributes` | Column-level (attribute) access |
| `${aws:username}`, `${cognito-identity.amazonaws.com:sub}` | Policy variables: one policy, per-user paths (04#10) |
