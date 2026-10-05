# 🌱 Section 17: AWS Elastic Beanstalk — Study Guide

Slides 354–378 ([open slides](../../AWS_Certified_Developer_Slides_v45.pdf#page=354)) · Sections follow the slide order

---

## 🧠 The Mental Model (read this first)

> **Elastic Beanstalk = "give me your code, I'll build the ALB + ASG + EC2 (+ RDS) for you" — using CloudFormation under the hood.**

Almost every Beanstalk exam question is one of **four types**:

| # | Question type | What decides the answer | Section |
|---|---|---|---|
| 1 | **Which deployment policy?** | Downtime? Capacity? Cost? Rollback speed? New instances only? | 6️⃣ |
| 2 | **Where does a config file go?** | **`.ebextensions/` folder at the root** of the source bundle, `.config` extension | 🔟 |
| 3 | **How do I migrate / change something I can't change in place?** (LB type, decouple RDS, platform upgrade) | **New environment + CNAME swap** — "config = in place, architecture = new env" | 1️⃣3️⃣–1️⃣5️⃣ |
| 4 | **Web or worker? Single or HA?** | Long-running/background jobs → **worker tier (SQS)** | 4️⃣–5️⃣ |

### 🗂️ What a source bundle looks like

```
my-app.zip                         ← upload THIS (no parent folder inside!)
├── .ebextensions/                 ← ⭐ config files go here (root of the bundle)
│   ├── load-balancer.config       ←   YAML or JSON, MUST end in .config
│   ├── logging.config
│   └── resources.config           ←   extra AWS resources (CloudFormation)
├── application.py / app.js        ← your code
├── requirements.txt / package.json← dependencies (slide 371)
└── cron.yaml                      ← (worker tier periodic tasks — beyond slides)
```

---

## 1️⃣ Why Elastic Beanstalk? — slides [355](../../AWS_Certified_Developer_Slides_v45.pdf#page=355)–357

### The problem
- Typical **3-tier web app**: Route 53 → ELB → ASG of EC2 (multi-AZ) → RDS + ElastiCache
- Developers must manage infrastructure, deploy code, configure DBs/LBs, worry about scaling
- Most web apps have the **same architecture (ALB + ASG)** — developers just want their **code to run**, consistently across apps and environments

### The solution
- **Developer-centric** view of deploying on AWS
- Uses the components you know: **EC2, ASG, ELB, RDS**…
- **Managed service:** capacity provisioning, load balancing, scaling, health monitoring, instance configuration
- ⭐ **Only the application code is your responsibility** — but you still have **full control over the configuration**
- ⭐ **Beanstalk is free** — you pay for the underlying resources

---

## 2️⃣ Components — slide [358](../../AWS_Certified_Developer_Slides_v45.pdf#page=358)

| Component | What it is |
|---|---|
| **Application** | Collection of Beanstalk components (environments, versions, configurations…) |
| **Application Version** | One **iteration** of your code |
| **Environment** | AWS resources running **one application version at a time** |
| **Tier** | **Web Server** tier or **Worker** tier |

- Create multiple environments: **dev, test, prod**…
- Flow: **Create Application → Upload Version → Launch Environment → Manage Environment** (update version / deploy new version)

---

## 3️⃣ Supported Platforms — slide [359](../../AWS_Certified_Developer_Slides_v45.pdf#page=359)

Go, Java SE, Java with Tomcat, .NET Core on Linux, .NET on Windows Server, Node.js, PHP, Python, Ruby, Packer Builder, **Single Container Docker**, **Multi-container Docker**, **Preconfigured Docker**

> Platform not listed? → **Docker** (or Packer Builder for a custom platform).

---

## 4️⃣ Web Server Tier vs Worker Tier — slide [360](../../AWS_Certified_Developer_Slides_v45.pdf#page=360)

| | **Web Server Tier** | **Worker Tier** |
|---|---|---|
| Entry point | **ELB** + URL (`myapp.us-east-1.elasticbeanstalk.com`) | **SQS queue** |
| Instances | Web servers in an ASG | Workers that **pull messages** from SQS |
| Scales on | Traffic / CPU etc. | ⭐ **Number of SQS messages** |
| Use for | HTTP requests | ⭐ **Long-running / background / async jobs** |

- A web tier can **push messages to SQS** for the worker tier to process → **decouple**
- *(Beyond slides)* Periodic tasks for a worker → **`cron.yaml`** at the root of the bundle

**Keyword map:** "task takes a long time / offload processing / background jobs" → **Worker tier**.

---

## 5️⃣ Deployment Modes (Environment Types) — slide [361](../../AWS_Certified_Developer_Slides_v45.pdf#page=361)

| **Single Instance** | **High Availability with Load Balancer** |
|---|---|
| 1 EC2 with an **Elastic IP** (+ optional RDS master) | **ALB + ASG** across multiple AZs (+ RDS Multi-AZ) |
| ⭐ **Great for dev** | ⭐ **Great for prod** |

---

## 6️⃣ Deployment Options for Updates — slides [362](../../AWS_Certified_Developer_Slides_v45.pdf#page=362)–369

### The six policies

| Policy | How it works | Downtime | Capacity during deploy | Extra cost | Speed | Rollback |
|---|---|---|---|---|---|---|
| **All at once** | Deploy to **all instances at once** | ⚠️ **Yes** | Zero during deploy | **None** | ⭐ **Fastest** | Redeploy (manual) |
| **Rolling** | Update a **bucket** of instances at a time | No | ⚠️ **Below capacity** | **None** | Long | Redeploy (manual) |
| **Rolling with additional batches** | Like rolling, but **launches a new batch first** | No | ✅ **Full capacity** | **Small** | Longer | Redeploy (manual) |
| **Immutable** | New instances in a **temporary ASG**, then swap | No | ✅ Full (double) | ⚠️ **High (double)** | **Longest** | ⭐ **Quick — terminate the new ASG** |
| **Blue/Green** | **New environment**, then **swap URLs (CNAME)** or Route 53 weighted | No | ✅ Full | High (2 environments) | Manual | ⭐ Swap back |
| **Traffic Splitting** | **Canary:** new version in a temp ASG gets a **small % of traffic** | No | ✅ Full | High | Configurable | ⭐ **Automated, very quick** |

### Details worth knowing
- **All at once:** great for **quick iterations in dev**
- **Rolling:** you set the **bucket size**; both versions run **simultaneously**
- **Rolling with additional batches:** extra batch is **removed at the end**; **good for prod**
- **Immutable:** new code on **new instances only**; **great for prod**
- **Blue/Green:** ⚠️ **not a "direct feature"** of Beanstalk — you create the second environment yourself; Beanstalk **"swap URLs"** does the switch
- **Traffic Splitting:** deployment health is monitored → failure triggers **automated rollback**; new instances migrate into the original ASG; old version terminated

### 🎯 Keyword → policy (your questions)

| Question says… | Answer | Your question |
|---|---|---|
| "**fastest**", "dev", "downtime OK", "no extra cost" | **All at once** | — |
| "no extra cost", "can run below capacity" | **Rolling** | — |
| "**no reduction in performance/capacity**" + "**cost-effective**" | ⭐ **Rolling with additional batches** | **S17 Q1** |
| "**maintain full capacity**" + "**using existing instances**" | ⭐ **Rolling with additional batches** | **S16 Q8** |
| "**only to new EC2 instances**" | ⭐ **Immutable** + **Blue/Green** | **S17 Q2** |
| "**quickly roll back**" is the top priority | ⭐ **Immutable** | **S17 Q3** |
| "can't be offline if update fails", "**minimal impact, rollback ASAP**" | ⭐ **Immutable** | **S17 Q8** |
| "**platform upgrade**" (e.g. new Node.js version) with **no downtime** | ⭐ **Blue/Green (CNAME swap)** | **S17 Q5** |
| "send a **small % of traffic**", "canary" | **Traffic Splitting** | — |

> ⚠️ Trap: Immutable vs Rolling with additional batches — *both* keep full capacity. **"Existing instances" / "cost-effective" → Rolling with additional batches. "New instances" / "fast rollback" → Immutable.**

---

## 7️⃣ Elastic Beanstalk CLI — slide [370](../../AWS_Certified_Developer_Slides_v45.pdf#page=370)

The **EB CLI** makes Beanstalk easier from the command line and is helpful for **automated deployment pipelines**:

| Command | Does |
|---|---|
| `eb create` | Create an environment |
| `eb status` / `eb health` | Environment status / health |
| `eb events` / `eb logs` | Recent events / instance logs |
| `eb open` | Open the app in a browser |
| `eb deploy` | Deploy a new version |
| `eb config` | Edit the environment configuration |
| `eb terminate` | Terminate the environment |

---

## 8️⃣ Deployment Process & the Source Bundle — slide [371](../../AWS_Certified_Developer_Slides_v45.pdf#page=371)

1. **Describe dependencies:** `requirements.txt` (Python), `package.json` (Node.js)
2. **Package code as a zip**
3. **Console:** upload zip (creates a new **app version**) → deploy · **CLI:** create app version (uploads zip) → deploy
4. Beanstalk deploys the zip **on each EC2 instance**, **resolves dependencies**, and **starts the app**

### Source bundle requirements (your **S17 Q7**)
| Requirement | ✅ / ❌ |
|---|---|
| Single **ZIP** (or **WAR**) file | ✅ |
| ⭐ **Must not include a parent folder / top-level directory** (zip the *contents*, not the folder) | ✅ |
| ⭐ **Size limit** — your answer says **512 MB** (AWS docs state **500 MB**) | ✅ |
| Can include **subdirectories** (e.g. `.ebextensions/`) | ✅ |

---

## 9️⃣ Beanstalk Lifecycle Policy — slide [372](../../AWS_Certified_Developer_Slides_v45.pdf#page=372)

- ⭐ Beanstalk stores **at most 1000 application versions**
- Hit the limit → **you can't deploy anymore**
- Phase out old versions with a **lifecycle policy**:
  - **Based on time** (remove old versions)
  - **Based on space** (too many versions)
- **Versions in use are never deleted**
- Option to **keep the source bundle in S3** to prevent data loss

**Keyword map:** "can't deploy new versions / too many versions" → **lifecycle policy**.

---

## 🔟 ⭐ Elastic Beanstalk Extensions (`.ebextensions`) — slide [373](../../AWS_Certified_Developer_Slides_v45.pdf#page=373)

**What:** Everything you can set in the Beanstalk **console/UI** can be configured **as code** with files in your source bundle.

### The 3 rules (memorize)
| Rule | Detail |
|---|---|
| 📁 **Location** | In the **`.ebextensions/` directory** at the **root of the source code** |
| 📝 **Format** | **YAML or JSON** |
| 🏷️ **Extension** | Files must end in **`.config`** (e.g. `logging.config`, `load-balancer.config`) |

### What you can do
- **`option_settings`** → modify default settings (load balancer, ASG, environment variables…)
- **`Resources`** → add AWS resources: **RDS, ElastiCache, DynamoDB, S3**… (CloudFormation syntax)
- ⚠️ **Resources created by `.ebextensions` are deleted when the environment is deleted**

### Example: `.ebextensions/load-balancer.config`
```yaml
option_settings:
  aws:elasticbeanstalk:environment:process:default:
    HealthCheckPath: /health
  aws:elbv2:listener:443:
    ListenerEnabled: true
    Protocol: HTTPS
    SSLCertificateArns: arn:aws:acm:us-east-1:123456789012:certificate/abc-123
```

### Example: `.ebextensions/resources.config` (CloudFormation resource)
```yaml
Resources:
  SessionTable:
    Type: AWS::DynamoDB::Table
    Properties:
      AttributeDefinitions:
        - AttributeName: id
          AttributeType: S
      KeySchema:
        - AttributeName: id
          KeyType: HASH
      BillingMode: PAY_PER_REQUEST
```

### 🎯 Your question: **S17 Q4**
> *"Where should the Developer place the `load-balancer.config` file in the application source bundle?"* → ⭐ **In the `.ebextensions` folder**

**How to answer every variant of this question:**

| Question asks about… | Answer |
|---|---|
| Where does a `.config` file go? | **`.ebextensions/`** at the **root** of the bundle |
| What file extension? | **`.config`** (not `.yaml`, `.json`, `.yml`) |
| What format inside? | **YAML or JSON** |
| Configure LB / ASG / env vars / HTTPS as code? | **`option_settings`** in a `.ebextensions/*.config` |
| Add DynamoDB / ElastiCache / S3 / SNS to the environment? | **`Resources`** in a `.ebextensions/*.config` |
| What happens to those resources when the env is terminated? | **Deleted** with the environment |

### ⚠️ Wrong answers you'll see
- ❌ "In the root of the bundle" (must be **inside `.ebextensions/`**)
- ❌ "In a `.config/` folder" or "`ebextensions/`" without the dot
- ❌ "In the `.elasticbeanstalk/` folder" (that's the **EB CLI's local config**, not deployed settings)
- ❌ "Upload it to S3 and reference it"
- ❌ File named `load-balancer.yaml` / `.json` (must be **`.config`**)

### Beyond the slides (good to recognize)
| Key in a `.config` file | Does |
|---|---|
| `packages` | Install OS packages (yum…) |
| `files` | Create files on the instance |
| `commands` | Run commands **before** the app is extracted |
| `container_commands` | Run commands **after** the app is extracted, before it goes live — `leader_only: true` runs on **one instance** (e.g. DB migrations) |
| Precedence | Settings applied **directly in the console/API override** `.ebextensions` `option_settings` |
| Ordering | `.config` files are processed in **alphabetical order** (prefix `01-`, `02-`…) |

---

## 1️⃣1️⃣ Elastic Beanstalk Under the Hood — slide [374](../../AWS_Certified_Developer_Slides_v45.pdf#page=374)

- ⭐ **Beanstalk relies on CloudFormation** to provision everything
- Use case: define **CloudFormation resources in `.ebextensions`** to provision ElastiCache, an S3 bucket, **anything you want**
- That's why `.ebextensions` `Resources` use **CloudFormation syntax**

---

## 1️⃣2️⃣ Elastic Beanstalk Cloning — slide [375](../../AWS_Certified_Developer_Slides_v45.pdf#page=375)

- Clone an environment with the **exact same configuration** → great for a **"test"** version
- Preserved: **load balancer type & config**, **RDS database type** (⚠️ **but not the data**), **environment variables**
- You can change settings after cloning

---

## 1️⃣3️⃣ Migration: Load Balancer — slide [376](../../AWS_Certified_Developer_Slides_v45.pdf#page=376)

⚠️ **You cannot change the load balancer type after creating an environment** (only its configuration).

**To migrate (e.g. CLB → ALB):**
1. Create a **new environment** with the same config **except the LB** (⚠️ **can't clone** — cloning keeps the LB type)
2. Deploy the app onto the new environment
3. **CNAME swap** or **Route 53** update

---

## 1️⃣4️⃣ RDS with Elastic Beanstalk — slides [377](../../AWS_Certified_Developer_Slides_v45.pdf#page=377)–378

| RDS **inside** Beanstalk | RDS **outside** Beanstalk |
|---|---|
| Great for **dev / test** | ⭐ **Best for prod** |
| ⚠️ DB lifecycle **tied to the environment** (terminate env → lose DB) | Create RDS separately, give the app the **connection string** (env var) |

### Decoupling RDS from an existing environment (6 steps)
1. **Snapshot** the RDS DB (safeguard)
2. In the RDS console, **enable deletion protection**
3. Create a **new Beanstalk environment without RDS**, pointing to the existing DB
4. **CNAME swap** (blue/green) or Route 53 update; confirm it works
5. **Terminate the old environment** (RDS survives thanks to protection)
6. Delete the CloudFormation stack (stuck in **`DELETE_FAILED`**)

**Your S17 Q6:** managed provisioning + load balancing + auto scaling + PostgreSQL → **Elastic Beanstalk + Amazon RDS (PostgreSQL)**.

---

## 1️⃣5️⃣ ⭐ Migration Playbook: Changing What You Can't Change In Place — slides [367](../../AWS_Certified_Developer_Slides_v45.pdf#page=367), [375](../../AWS_Certified_Developer_Slides_v45.pdf#page=375)–378

> **Core idea:** Some environment settings are **locked at creation**. To change them you **never edit the old environment** — you **build a new one next to it, test it, then swap traffic** (CNAME swap or Route 53). This is the same mechanism as **Blue/Green**.

### ✅ vs ❌ — What can change on a running environment?

| ✅ **Change in place** (update the environment config) | ❌ **Locked → new environment + swap** |
|---|---|
| Instance type, AMI, key pair | ⭐ **Load balancer type** (e.g. CLB → ALB) — slide 376 |
| ASG min / max, scaling triggers | ⭐ **Decouple RDS** created inside the environment — slide 378 |
| Load balancer **configuration** (listeners, HTTPS cert, health check path) | ⭐ **Major platform upgrade with zero downtime** (e.g. new Node.js version) — your **S17 Q5** |
| Environment variables / environment properties | **Environment tier** (web ↔ worker) *(beyond slides)* |
| Deployment policy (all at once, rolling, immutable…) | **VPC** of the environment *(beyond slides)* |
| Application version (deploy new code) | |
| `.ebextensions` `option_settings` | |

> Memory trick: **"Config = in place. Architecture = new environment."** If it changes *what kind* of resource exists (LB type, tier, VPC, where the DB lives) → new environment.

### 🔁 The universal migration recipe

```
          ┌─────────────── OLD ("blue") ───────────────┐
Users ──▶ │ myapp.elasticbeanstalk.com  →  CLB / old v │   keep running!
          └────────────────────────────────────────────┘
                              │ 1. create NEW env (different setting)
                              ▼
          ┌─────────────── NEW ("green") ──────────────┐
          │ myapp-new.elasticbeanstalk.com → ALB / v2  │   2. deploy app  3. test via its own URL
          └────────────────────────────────────────────┘
                              │ 4. SWAP ENVIRONMENT URLs (CNAME swap)  — or Route 53 update
                              ▼
Users ──▶ myapp.elasticbeanstalk.com now points to GREEN
                              │ 5. wait for DNS TTL, confirm healthy
                              ▼
          6. terminate the OLD env   (rollback before this = swap back)
```

| Step | Detail |
|---|---|
| 1. **Create a new environment** | Same app, **same region**; either **clone** or **create from scratch** (see below) |
| 2. **Deploy** the app version | Same code, or the new code/platform |
| 3. **Test** the new environment | Using its **own URL** — users are unaffected |
| 4. **Swap** | Beanstalk **"Swap environment URLs"** (CNAME swap) — CLI `eb swap` — **or** Route 53 record update / **weighted** records for gradual shift |
| 5. **Wait & verify** | DNS caches → keep the old env running until traffic has moved |
| 6. **Terminate the old environment** | ⚠️ Protect anything you need first (e.g. RDS deletion protection) |

> ⭐ **Rollback = swap the URLs back** — as long as you haven't terminated the old environment.

### 🧬 Clone or create new?

| | **Clone** (slide 375) | **Create new environment** |
|---|---|---|
| Copies | **Everything**: LB **type & config**, RDS **type** (⚠️ not data), env variables | Only what you set |
| Use when | You want an **identical** copy (test env), or will only change in-place settings afterwards | You need a **different locked setting** |
| ⚠️ LB type change | ❌ **Can't clone** — it keeps the old LB type | ✅ Required |

### 🗺️ The three migrations from the slides

| Scenario | Steps | Why not in place? |
|---|---|---|
| **CLB → ALB** (slide 376) | New env with same config **except LB** (not a clone) → deploy → **CNAME swap** / Route 53 | LB type is fixed at creation |
| **Decouple RDS** (slide 378) | Snapshot → **RDS deletion protection** → new env **without RDS**, connection string to existing DB → **CNAME swap** → terminate old env → delete stack in **`DELETE_FAILED`** | RDS lifecycle is tied to the env (terminate env = delete DB) |
| **Platform upgrade, zero downtime** (S17 Q5) | New env on the **new platform version** + new code → test → **CNAME swap** | Avoids upgrading the live fleet in place |

### 🎯 Question patterns

| Question says… | Answer |
|---|---|
| "change the **load balancer type**" | **New environment** (not clone) + **CNAME swap** |
| "**upgrade the platform** / runtime version" + "**no downtime**" | **Blue/Green — CNAME swap** (S17 Q5) |
| "RDS must **survive** environment termination" / "move DB out of Beanstalk" | **Snapshot + deletion protection + new env + CNAME swap** |
| "**test** the new version in a separate environment before switching" | **Blue/Green + swap environment URLs** |
| "shift **a small % of traffic** to the new environment first" | **Route 53 weighted** records (blue/green) — or **Traffic Splitting** if same environment |
| "**fastest rollback** after swapping" | **Swap URLs back** (old env still running) |
| "copy an environment **exactly** for testing" | **Clone** |
| "environment **termination stuck**" after decoupling RDS | Delete the CloudFormation stack in **`DELETE_FAILED`** |

### ⚠️ Traps
1. **Clone ≠ migrate the LB** — a clone keeps the old load balancer type.
2. **Blue/Green is not a deployment policy** you select — you build the second environment and **swap URLs** yourself.
3. **Don't terminate the old environment immediately** — DNS caching; it's also your rollback.
4. **Cloning copies the RDS *type*, not its data.**
5. **CNAME swap** happens between environments in the **same region** — it changes DNS, not instances.

---

## 🎯 Master Cheat Sheet

| I need to… | Answer |
|---|---|
| Deploy code without managing infrastructure | **Elastic Beanstalk** |
| Fastest deploy, downtime OK (dev) | **All at once** |
| No extra cost, reduced capacity OK | **Rolling** |
| Full capacity, low extra cost, existing instances | **Rolling with additional batches** |
| New instances only + fastest rollback | **Immutable** |
| Test a whole new env / platform upgrade, zero downtime | **Blue/Green + swap URLs (CNAME)** |
| Canary % of traffic with automatic rollback | **Traffic Splitting** |
| Configure LB/ASG/env vars/HTTPS as code | **`.ebextensions/*.config`** → `option_settings` |
| Add DynamoDB/ElastiCache/S3 to the environment | **`.ebextensions/*.config`** → `Resources` (CloudFormation) |
| Background / long-running jobs | **Worker tier** (SQS) |
| Hit "can't deploy" due to many versions | **Lifecycle policy** (1000 version limit) |
| Copy an environment for testing | **Clone** |
| Change the load balancer type | **New environment + CNAME swap** (not clone) |
| Prod database | **RDS outside Beanstalk**, pass the connection string |

---

## 🌳 Decision Tree for Exam Questions

```
What is the question about?
│
├── Deploying a new version?
│    ├── downtime is OK / fastest / dev            ─▶ All at once
│    ├── no extra cost, reduced capacity OK         ─▶ Rolling
│    ├── full capacity + cost-effective / existing  ─▶ Rolling with additional batches
│    ├── new instances only / fastest rollback      ─▶ Immutable
│    ├── platform upgrade / separate env / swap     ─▶ Blue/Green (CNAME swap)
│    └── small % of traffic, auto rollback          ─▶ Traffic Splitting
│
├── A config file or extra resource?
│    ├── where does it go?                          ─▶ .ebextensions/ at the bundle root
│    ├── file extension / format?                   ─▶ .config, YAML or JSON
│    ├── change settings?                           ─▶ option_settings
│    └── add AWS resources?                         ─▶ Resources (CloudFormation)
│
├── Source bundle rules?                            ─▶ zip, no parent folder, size limit
├── Background processing?                          ─▶ Worker tier + SQS
├── Too many app versions?                          ─▶ Lifecycle policy
├── Change LB type?                                 ─▶ New env + CNAME swap (not clone)
├── Platform upgrade with zero downtime?            ─▶ Blue/Green: new env + swap environment URLs
├── Changed something locked (tier, VPC, LB type)?  ─▶ New env (not clone) + CNAME swap; rollback = swap back
└── Database for prod?                              ─▶ RDS outside Beanstalk (decouple via snapshot + protection + CNAME swap)
```

---

## 🚨 Top Exam Traps

1. **`.ebextensions/` must be at the ROOT of the source bundle**, files must end in **`.config`**, YAML or JSON.
2. **`.elasticbeanstalk/` ≠ `.ebextensions/`** — the first is local EB CLI config, the second is deployed configuration.
3. **Resources created in `.ebextensions` are deleted with the environment.**
4. **Source bundle: no parent folder inside the zip.**
5. **"Existing instances" + full capacity → Rolling with additional batches**; **"new instances" → Immutable / Blue-Green**.
6. **Fastest rollback → Immutable** (just terminate the temporary ASG).
7. **Blue/Green is not a built-in policy** — new environment + **swap URLs**.
8. **Platform upgrade with zero downtime → Blue/Green CNAME swap.**
9. **Can't change the load balancer type** after creation; **cloning keeps the LB type** → create a new env instead.
10. **RDS inside Beanstalk dies with the environment** → for prod, create RDS separately.
11. **1000 application version limit** → lifecycle policy.
12. **Worker tier scales on SQS queue depth** — use it for long-running tasks.
13. **Beanstalk is free; CloudFormation runs it under the hood.**
14. **Config = change in place; architecture (LB type, tier, VPC, RDS location) = new environment + CNAME swap.**
15. **Keep the old environment until the swap is verified** — swapping back is the fastest rollback.

---

## 💾 How to Use This Guide

1. Read the **Mental Model** and the **source bundle diagram**.
2. Memorize the **deployment policy table** and the **keyword → policy** map (5 of your 8 Beanstalk questions are deployment policy questions).
3. Know the **3 `.ebextensions` rules**: location, format, extension.
4. Finish with the **Decision Tree** and **Top Exam Traps**, then drill Section 17 in the quiz app.
