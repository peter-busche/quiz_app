# 🗄️ Section 22: AWS Serverless: DynamoDB — Study Guide

Slides 602–655 ([open slides](../../AWS_Certified_Developer_Slides_v45.pdf#page=602)) · Sections follow the slide order

---

## 🧠 The Mental Model (read this first)

DynamoDB questions fall into **five buckets**. Identify the bucket, then the answer is usually one keyword:

| Bucket | The question is about… | Topics | Slides |
|---|---|---|---|
| 🧱 **Model** | How data is keyed and found | Primary keys, LSI, GSI, write sharding | 606–609, 631–633, 648 |
| ⚡ **Capacity** | How much throughput, what happens when exceeded | RCU/WCU math, modes, partitions, throttling, DAX | 610–617, 636–637 |
| 🛠️ **API** | Which call reads/writes the data correctly | Put/Update/Get/Query/Scan, Batch, Conditional, Transactions, PartiQL | 618–630, 634–635, 643–646 |
| 🔔 **Events & lifecycle** | Reacting to changes / expiring data | Streams, TTL | 638–642 |
| 🔐 **Security & ops** | Access, backup, copying, multi-region | IAM, VPC endpoint, PITR, Global Tables, fine-grained access | 652–655 |

### 🔢 The math you MUST know (slide 646: "Important for the exam!")

```
WCU  = writes/sec × ceil(item size / 1 KB)
RCU  = reads/sec  × ceil(item size / 4 KB)          ← strongly consistent
RCU  = reads/sec  × ceil(item size / 4 KB) ÷ 2      ← eventually consistent (default)
Transactional  = ×2  (on both RCU and WCU)
```

> Memory trick: **"W = 1, R = 4"** — writes in **1 KB** chunks, reads in **4 KB** chunks. Always **round size UP** first.

---

## 1️⃣ NoSQL & DynamoDB Overview — slides [603](../../AWS_Certified_Developer_Slides_v45.pdf#page=603)–605

| Traditional RDBMS (RDS) | NoSQL (DynamoDB) |
|---|---|
| SQL, strict data model | Non-relational, distributed |
| **Joins, aggregations** (SUM, AVG), complex computations | ⚠️ **No joins** (or limited), **no aggregations** — all data for a query is in **one row** |
| Vertical scaling + read replicas | **Horizontal scaling** |

### DynamoDB at a glance
- **Fully managed, highly available**, replicated across **multiple AZs**
- Scales to **millions of requests/sec, trillions of rows, 100s of TB**
- Fast, **consistent low latency**
- **IAM** for security, authorization, administration
- **DynamoDB Streams** → event-driven programming
- Low cost, **auto-scaling**
- Table classes: **Standard** & **Infrequent Access (IA)**

---

## 2️⃣ Basics & Primary Keys — slides [606](../../AWS_Certified_Developer_Slides_v45.pdf#page=606)–609

### Basics
- **Tables** → **items** (rows, unlimited) → **attributes** (can be added over time, can be null)
- **Primary key must be decided at creation time**
- ⭐ **Max item size = 400 KB**
- Data types:

| Category | Types |
|---|---|
| Scalar | String, Number, Binary, Boolean, Null |
| Document | List, Map |
| Set | String Set, Number Set, Binary Set |

### Two primary key options
| Option | Uniqueness | Example |
|---|---|---|
| **Partition Key (HASH)** | Partition key **unique per item** | `User_ID` in a users table |
| **Partition Key + Sort Key (HASH + RANGE)** | **Combination** unique; data **grouped by partition key** | `User_ID` + `Game_ID` in a users-games table |

### Choosing a partition key
- Must be **diverse / high cardinality** so data spreads across partitions
- Movie database exercise: ✅ **`movie_id`** (highest cardinality) · ❌ `movie_language` (few values, skewed to English)

> ⚠️ Trap: two items with the same partition key and no sort key → the second write **overwrites** (or fails a condition). Fix → **composite key (partition + sort)**.

---

## 3️⃣ Read/Write Capacity Modes — slides [610](../../AWS_Certified_Developer_Slides_v45.pdf#page=610)–611, [617](../../AWS_Certified_Developer_Slides_v45.pdf#page=617)

| | **Provisioned** | **On-Demand** (default) |
|---|---|---|
| You set | **RCU / WCU** per second | Nothing — auto scales |
| Planning | Plan capacity beforehand | **No capacity planning** |
| Billing | Pay for provisioned capacity | Pay per use: **RRU / WRU** |
| Cost | Cheaper | **2.5× more expensive** |
| Scaling | Optional **auto-scaling**; **Burst Capacity** for temporary spikes | Unlimited, **no throttling** |
| Exceeded? | `ProvisionedThroughputExceededException` → **exponential backoff** | — |
| Use case | **Predictable** traffic | **Unknown / unpredictable** workloads |

- ⭐ You can **switch modes once every 24 hours**
- RRU ≈ RCU, WRU ≈ WCU (same units, different billing)

---

## 4️⃣ WCU & RCU Calculations — slides [612](../../AWS_Certified_Developer_Slides_v45.pdf#page=612)–614

### Write Capacity Units (WCU)
**1 WCU = 1 write/sec for an item up to 1 KB**

| Example | Math | Answer |
|---|---|---|
| 10 writes/s, 2 KB | 10 × 2 | **20 WCU** |
| 6 writes/s, 4.5 KB | 6 × **5** (round up) | **30 WCU** |
| 120 writes/**minute**, 2 KB | (120 ÷ 60) × 2 | **4 WCU** |

### Strongly vs Eventually Consistent Reads
| | **Eventually consistent** (default) | **Strongly consistent** |
|---|---|---|
| After a write | May read **stale** data (replication lag) | Always **correct** data |
| How | Default | **`ConsistentRead = true`** on GetItem, BatchGetItem, Query, Scan |
| Cost | **½** the RCU | **2×** the RCU of eventual |

### Read Capacity Units (RCU)
**1 RCU = 1 strongly consistent read/sec OR 2 eventually consistent reads/sec, for an item up to 4 KB**

| Example | Math | Answer |
|---|---|---|
| 10 strong reads/s, 4 KB | 10 × (4/4) | **10 RCU** |
| 16 eventual reads/s, 12 KB | (16 ÷ 2) × (12/4) | **24 RCU** |
| 10 strong reads/s, 6 KB | 10 × (**8**/4) (round 6 → 8 KB) | **20 RCU** |

> ⚠️ Rounding traps: WCU rounds to the next **1 KB**; RCU rounds to the next **4 KB**. "Per minute" → **divide by 60 first**.

---

## 5️⃣ Partitions & Throttling — slides [615](../../AWS_Certified_Developer_Slides_v45.pdf#page=615)–616

### Partitions
- Data is stored in **partitions**; the partition key goes through a **hash function** to pick one
- ⭐ **RCUs and WCUs are spread evenly across partitions**

```
# partitions by capacity = (RCUs / 3000) + (WCUs / 1000)
# partitions by size     = Total size / 10 GB
# partitions             = ceil( max(by capacity, by size) )
```

### Throttling
**Error:** `ProvisionedThroughputExceededException`

| Causes | Solutions |
|---|---|
| **Hot keys** — one partition key read too often (popular item) | **Exponential backoff** (already built into the SDK) |
| **Hot partitions** | **Distribute partition keys** as much as possible |
| **Very large items** (RCU/WCU depend on size) | **RCU problem → DAX** |

---

## 6️⃣ Writing, Deleting & Batch Operations — slides [618](../../AWS_Certified_Developer_Slides_v45.pdf#page=618), [622](../../AWS_Certified_Developer_Slides_v45.pdf#page=622)–623

### Writing
| API | Does |
|---|---|
| **`PutItem`** | **Creates** a new item or **fully replaces** an old one (same primary key) |
| **`UpdateItem`** | **Edits** attributes, or adds the item if missing — ⭐ **atomic counters** (unconditionally increment a number) |
| **Conditional writes** | Write/update/delete **only if conditions are met** — helps with concurrency, **no performance impact** |

### Deleting
| API | Does |
|---|---|
| **`DeleteItem`** | Delete one item (can be **conditional**) |
| **`DeleteTable`** | ⭐ Delete the whole table — **much faster** than DeleteItem on every item |

### Batch operations
- Save **latency** by reducing API calls; items processed **in parallel**
- ⚠️ **Part of a batch can fail** → retry the failed items

| API | Limits | Failed items |
|---|---|---|
| **`BatchWriteItem`** | Up to **25** Put/Delete, **16 MB** total, 400 KB/item — ⚠️ **can't update** (use UpdateItem) | **`UnprocessedItems`** → exponential backoff or add **WCU** |
| **`BatchGetItem`** | Up to **100** items, **16 MB**, one or more tables | **`UnprocessedKeys`** → exponential backoff or add **RCU** |

---

## 7️⃣ Reading Data: GetItem, Query, Scan — slides [619](../../AWS_Certified_Developer_Slides_v45.pdf#page=619)–621

| | **GetItem** | **Query** | **Scan** |
|---|---|---|---|
| Finds | **One item** by full primary key | Items with **one partition key** (+ optional sort key condition) | **Every item** in the table, then filters |
| Efficiency | ✅ Best | ✅ Efficient | ❌ **Inefficient**, consumes a lot of RCU |
| Returns | 1 item | Up to **Limit** items or **1 MB** (paginate) | Up to **1 MB** (paginate) |
| Works on | Table | Table, **LSI**, **GSI** | Table, indexes |

### Query details
- **`KeyConditionExpression`**:
  - **Partition key — required, `=` only**
  - Sort key — optional: `=, <, <=, >, >=, BETWEEN, begins_with`
- **`FilterExpression`**: extra filtering **after** the Query, **non-key attributes only**
- **`ProjectionExpression`**: return only certain attributes

### Scan details
- Limit impact with **`Limit`** or smaller results + pauses
- ⭐ **Parallel Scan** → multiple workers scan segments at once → **faster but more RCU**
- `ProjectionExpression` / `FilterExpression` **do not reduce RCU** (filtering happens after reading)

> ⚠️ Trap: **FilterExpression doesn't save RCU** — the data is still read. To read less, use a better **key or index** (Query instead of Scan).

---

## 8️⃣ PartiQL — slides [624](../../AWS_Certified_Developer_Slides_v45.pdf#page=624), [634](../../AWS_Certified_Developer_Slides_v45.pdf#page=634)

- **SQL-compatible** query language for DynamoDB
- Supports **SELECT, INSERT, UPDATE, DELETE** (not all SQL — still **no joins**)
- Query across **multiple tables**; supports **batch** operations
- Run from: Console, **NoSQL Workbench**, DynamoDB APIs, CLI, SDK

---

## 9️⃣ Conditional Writes & Optimistic Locking — slides [625](../../AWS_Certified_Developer_Slides_v45.pdf#page=625)–630, [635](../../AWS_Certified_Developer_Slides_v45.pdf#page=635)

### Condition expressions
For **PutItem, UpdateItem, DeleteItem, TransactWriteItems**:

| Function | Checks |
|---|---|
| `attribute_exists` / `attribute_not_exists` | Attribute has / has no value |
| `attribute_type` | Attribute's type |
| `contains` | String contains a substring |
| `begins_with` | String prefix |
| `IN`, `BETWEEN` | e.g. `ProductCategory IN (:cat1, :cat2) and Price between :low and :high` |
| `size` | String length |

> ⭐ **Filter expression = reads. Condition expression = writes.**

### Don't overwrite an existing item
- `attribute_not_exists(partition_key)` → item isn't overwritten
- `attribute_not_exists(partition_key) and attribute_not_exists(sort_key)` → partition + sort combination isn't overwritten

### Optimistic locking
```
Item: User_ID=7791…  Name=Michael  Version=1

Client 1: Update Name=John  only if Version = 1   ✅ succeeds → Version=2
Client 2: Update Name=Lisa  only if Version = 1   ❌ fails (Version is now 2)
```
- Each item has a **version number** attribute; update only if it hasn't changed
- Built on **conditional writes**

---

## 🔟 Secondary Indexes: LSI & GSI — slides [631](../../AWS_Certified_Developer_Slides_v45.pdf#page=631)–633

| | **Local Secondary Index (LSI)** | **Global Secondary Index (GSI)** |
|---|---|---|
| What | **Alternative sort key** | **Alternative primary key** (HASH or HASH+RANGE) |
| Partition key | ⭐ **Same as the base table** | **Different** from the base table |
| Key types | One scalar (String, Number, Binary) | Scalars (String, Number, Binary) |
| When created | ⚠️ **Only at table creation** | ✅ **Can add/modify after creation** |
| Limit | Up to **5 per table** | — |
| Capacity | Uses the **base table's RCU/WCU** | ⚠️ **Provision its own RCU/WCU** |
| Projections | KEYS_ONLY, INCLUDE, ALL | KEYS_ONLY, INCLUDE, ALL |
| Use | Query same partition, sorted differently | Query by a **non-key attribute** |

### Throttling with indexes
- ⚠️ **GSI writes throttled → the MAIN table is throttled too**, even if the table's WCU are fine → choose the **GSI partition key** and **WCU** carefully
- **LSI** uses the table's capacity → no special throttling considerations

**Keyword map:** "query by another attribute, table already exists" → **GSI**. "Same partition key, different sort order" → **LSI** (only if at creation).

---

## 1️⃣1️⃣ DynamoDB Accelerator (DAX) — slides [636](../../AWS_Certified_Developer_Slides_v45.pdf#page=636)–637

- **Fully managed, highly available, in-memory cache** for DynamoDB
- ⭐ **Microsecond** latency for cached reads & queries
- ⭐ **No application logic changes** — compatible with DynamoDB APIs
- Solves the **hot key** problem (too many reads)
- Default cache **TTL = 5 minutes**
- Up to **10 nodes**; Multi-AZ (**3 nodes minimum** recommended for prod)
- Secure: KMS at rest, VPC, IAM, CloudTrail

### DAX vs ElastiCache
| **DAX** | **ElastiCache** |
|---|---|
| Individual **objects** cache | Store **aggregation results** (computed data) |
| **Query & Scan** cache | Anything your app decides to cache |
| No code changes | Heavy code changes |

---

## 1️⃣2️⃣ DynamoDB Streams — slides [638](../../AWS_Certified_Developer_Slides_v45.pdf#page=638)–641

- **Ordered** stream of **item-level** changes (create / update / delete)
- Consumers: **Kinesis Data Streams**, **Lambda**, **Kinesis Client Library** apps
- ⭐ **Retention up to 24 hours**
- Use cases: react in real time (**welcome email**), analytics, derivative tables, **OpenSearch**, **cross-region replication**

### What gets written (stream view type)
| Option | Contains |
|---|---|
| `KEYS_ONLY` | Only key attributes |
| `NEW_IMAGE` | Item **after** the change |
| `OLD_IMAGE` | Item **before** the change |
| `NEW_AND_OLD_IMAGES` | Both |

- Made of **shards** (like Kinesis) — **provisioned automatically** by AWS
- ⚠️ **Not retroactive** — records only start after you enable the stream

### Streams + Lambda
```
Table ──▶ DynamoDB Streams ◀──poll── Event Source Mapping ──invoke (sync, batch)──▶ Lambda
```
- Requires an **Event Source Mapping**
- Lambda needs **permissions** to read the stream (`AWSLambdaDynamoDBExecutionRole`)
- Lambda is invoked **synchronously**

---

## 1️⃣3️⃣ Time To Live (TTL) — slide [642](../../AWS_Certified_Developer_Slides_v45.pdf#page=642)

- **Automatically delete items** after an expiry timestamp
- ⭐ **No WCU consumed** (no extra cost)
- TTL attribute must be a **Number** with a **Unix epoch timestamp**
- Expired items deleted **within a few days** — ⚠️ until then they **still appear** in reads/queries/scans (filter them out)
- Deleted from **LSIs and GSIs** too
- Each TTL delete enters **DynamoDB Streams** (can help recover expired items)
- Use cases: keep only current items (**session data**), regulatory obligations

---

## 1️⃣4️⃣ DynamoDB CLI — Good to Know — slide [643](../../AWS_Certified_Developer_Slides_v45.pdf#page=643)

| Option | Does |
|---|---|
| `--projection-expression` | Retrieve only certain attributes |
| `--filter-expression` | Filter items before they're returned |
| `--page-size` | Still gets the full list, but in **more, smaller API calls** (default 1000) — avoids timeouts |
| `--max-items` | Max items shown; returns a **`NextToken`** |
| `--starting-token` | Continue from the last `NextToken` |

> ⚠️ Trap: CLI call **timing out** on a big table → **`--page-size`**. Want to **show** fewer results → `--max-items`.

---

## 1️⃣5️⃣ DynamoDB Transactions — slides [644](../../AWS_Certified_Developer_Slides_v45.pdf#page=644)–646

- **All-or-nothing** add/update/delete across **multiple items and tables** → **ACID**
- Read modes: Eventual, Strong, **Transactional** · Write modes: Standard, **Transactional**
- ⭐ **Consumes 2× WCU & RCU** (prepare + commit)
- APIs:
  - **`TransactGetItems`** — one or more GetItem
  - **`TransactWriteItems`** — one or more Put/Update/Delete
- Use cases: **financial transactions**, orders, multiplayer games (e.g. update `AccountBalance` **and** put into `BankTransactions` — both or neither)

### Transaction capacity math
| Example | Math | Answer |
|---|---|---|
| 3 transactional writes/s, 5 KB | 3 × 5 × **2** | **30 WCU** |
| 5 transactional reads/s, 5 KB | 5 × (**8**/4) × **2** | **20 RCU** |

---

## 1️⃣6️⃣ Design Patterns — slides [647](../../AWS_Certified_Developer_Slides_v45.pdf#page=647)–651

### Session state cache — slide 647
DynamoDB is commonly used to store **session state**:

| vs | Why DynamoDB / why not the other |
|---|---|
| ElastiCache | Both key/value; ElastiCache is **in-memory**, DynamoDB is **serverless** |
| EFS | EFS must be **attached to EC2** as a network drive |
| EBS / Instance Store | **Local caching only**, not shared |
| S3 | **Higher latency**, not meant for small objects |

### Write sharding — slide 648
- Voting app with 2 candidates → partition key `Candidate_ID` = only **2 partitions** → **hot partition**
- Fix: **add a suffix** to the partition key (`Candidate_A-11`, `Candidate_B-17`…)
  - **Random suffix** or **calculated suffix**

### Write types — slide 649
| Type | Behavior |
|---|---|
| **Concurrent writes** | Second write **overwrites** the first |
| **Atomic writes** | Both succeed — "increase by 1" + "increase by 2" → **+3** |
| **Conditional writes** | First accepted, **second fails** (condition no longer true) |
| **Batch writes** | Write/update many items at once |

### Large objects — slide 650
⭐ Items max **400 KB** → store the **object in S3**, store the **metadata + S3 URL** in DynamoDB.

### Indexing S3 object metadata — slide 651
```
Upload to S3 ──▶ Lambda ──▶ store metadata in DynamoDB ──▶ API to search by date, customer storage, attributes…
```

---

## 1️⃣7️⃣ DynamoDB Operations — slide [652](../../AWS_Certified_Developer_Slides_v45.pdf#page=652)

| Task | Option | Verdict |
|---|---|---|
| **Table cleanup** | Scan + DeleteItem | ❌ Slow, consumes RCU & WCU, expensive |
| | **Drop table + recreate** | ✅ **Fast, efficient, cheap** |
| **Copy a table** | **AWS Backup** | ✅ |
| | **AWS Glue** (ETL job) | ✅ |
| | Scan + PutItem / BatchWriteItem | Write your own code |

---

## 1️⃣8️⃣ Security & Other Features — slide [653](../../AWS_Certified_Developer_Slides_v45.pdf#page=653)

| Feature | Detail |
|---|---|
| **VPC Endpoints** | Access DynamoDB **without the internet** |
| **IAM** | Access fully controlled by IAM |
| **Encryption** | At rest with **KMS**, in transit with **SSL/TLS** |
| **Backup & Restore** | Including **Point-in-Time Recovery (PITR)**, **no performance impact** |
| **Global Tables** | ⭐ **Multi-region, multi-active**, fully replicated (built on Streams) |
| **DynamoDB Local** | Develop/test **locally without internet** |
| **AWS DMS** | Migrate **to** DynamoDB from MongoDB, Oracle, MySQL, S3… |

---

## 1️⃣9️⃣ Users Access DynamoDB Directly & Fine-Grained Access — slides [654](../../AWS_Certified_Developer_Slides_v45.pdf#page=654)–655

```
Web/Mobile user ──login──▶ Identity provider (Cognito User Pools, Google, Facebook, OIDC)
                ──▶ Cognito Identity Pool ──▶ temporary AWS credentials (IAM role)
                ──▶ DynamoDB table directly
```

### Fine-grained access control
- Users get AWS credentials via **Web Identity Federation** or **Cognito Identity Pools**
- Assign an **IAM role with Conditions** to limit API access:

| Condition key | Limits |
|---|---|
| ⭐ **`dynamodb:LeadingKeys`** | **Row-level** access — users only touch items whose **partition key = their identity** |
| **`dynamodb:Attributes`** | **Column-level** — which attributes the user can see |

---

## 🎯 Master Cheat Sheet

### APIs
| I need to… | Use |
|---|---|
| Create or fully replace an item | `PutItem` |
| Change some attributes / increment a counter | `UpdateItem` (atomic counter) |
| Write only if something is true | Condition expression |
| Prevent overwriting an existing item | `attribute_not_exists(pk)` |
| Detect concurrent updates | Optimistic locking (version attribute) |
| Get one item by full key | `GetItem` |
| Get items for one partition key | `Query` |
| Read the whole table | `Scan` (faster: Parallel Scan) |
| Return only some attributes | `ProjectionExpression` |
| Write/delete up to 25 items in one call | `BatchWriteItem` |
| Read up to 100 items in one call | `BatchGetItem` |
| All-or-nothing across items/tables | `TransactWriteItems` / `TransactGetItems` |
| SQL syntax | PartiQL |
| Delete everything fast | `DeleteTable` + recreate |

### Numbers
| Number | Meaning |
|---|---|
| **400 KB** | Max item size |
| **1 KB / 4 KB** | WCU / RCU unit size |
| **×½** | Eventually consistent reads |
| **×2** | Strongly consistent (vs eventual) · Transactions |
| **2.5×** | On-demand cost vs provisioned |
| **24 h** | Mode switch interval · Streams retention |
| **25 / 16 MB** | BatchWriteItem items / size |
| **100 / 16 MB** | BatchGetItem items / size |
| **1 MB** | Query/Scan page size |
| **5** | LSIs per table |
| **5 min** | DAX default TTL |
| **10 nodes / 3 min (prod)** | DAX cluster |
| **3000 RCU / 1000 WCU / 10 GB** | Per-partition limits (partition formula) |

---

## 🌳 Decision Tree for Exam Questions

```
Is the question about...
│
├── Capacity math?                    ─▶ WCU = n × ceil(KB/1) · RCU = n × ceil(KB/4) (÷2 eventual, ×2 transactional)
│
├── ProvisionedThroughputExceededException?
│    ├── general                      ─▶ Exponential backoff (SDK does it)
│    ├── one hot item, read-heavy     ─▶ DAX
│    ├── few partition key values     ─▶ Better partition key / write sharding (suffix)
│    ├── GSI under-provisioned        ─▶ Raise GSI WCU (it throttles the main table!)
│    └── unpredictable traffic        ─▶ On-Demand mode
│
├── Need to query by another attribute?
│    ├── same partition key, table not created yet ─▶ LSI
│    └── different key / table already exists      ─▶ GSI
│
├── Reads must reflect the latest write?          ─▶ ConsistentRead = true (2× RCU)
│
├── Concurrency?
│    ├── don't overwrite                          ─▶ attribute_not_exists
│    ├── detect someone else changed it           ─▶ Optimistic locking (version)
│    ├── increment safely                         ─▶ Atomic counter (UpdateItem)
│    └── multiple items all-or-nothing            ─▶ Transactions (2× capacity)
│
├── React to changes / replicate?                 ─▶ DynamoDB Streams (+ Lambda via event source mapping)
├── Auto-expire sessions/data for free?           ─▶ TTL (Number, epoch)
├── Microsecond reads, no code change?            ─▶ DAX
├── Cache aggregation results?                    ─▶ ElastiCache
├── Item > 400 KB?                                ─▶ S3 + metadata in DynamoDB
├── Multi-region active-active?                   ─▶ Global Tables
├── Users only see their own rows?                ─▶ IAM condition dynamodb:LeadingKeys
├── CLI timing out on large table?                ─▶ --page-size
└── Delete all items / copy table?                ─▶ Drop & recreate / AWS Backup or Glue
```

---

## 🚨 Top Exam Traps

1. **Round item size UP first** — 1 KB for WCU, **4 KB** for RCU; "per minute" → **÷ 60**.
2. **Eventually consistent is the default** and costs **half**; strong = `ConsistentRead=true`.
3. **Transactions cost 2×** RCU/WCU.
4. **LSI only at table creation** and shares table capacity; **GSI anytime** with its **own** capacity.
5. **Throttled GSI throttles the main table.**
6. **FilterExpression / ProjectionExpression don't reduce RCU** — Scan still reads everything.
7. Query **partition key must use `=`**; FilterExpression only on **non-key** attributes.
8. **BatchWriteItem can't update** — use UpdateItem; handle **UnprocessedItems / UnprocessedKeys**.
9. **Filter expression = reads; condition expression = writes.**
10. **DAX = no code changes, object/query cache**; **ElastiCache = aggregations, code changes**.
11. **Streams retain 24 h and aren't retroactive**; Lambda needs an **event source mapping**.
12. **TTL is free (no WCU)** but expired items may **still show up for days**.
13. **Items max 400 KB** → large objects in **S3**.
14. **Delete all data → drop and recreate the table** (not Scan + DeleteItem).
15. **On-demand = 2.5× cost, no throttling**; switch modes **once per 24 h**.
16. **`LeadingKeys`** = row-level, **`Attributes`** = column-level fine-grained access.

---

## 💾 How to Use This Guide

1. Read the **Mental Model** and memorize **"W = 1, R = 4"**.
2. Do the WCU/RCU and transaction examples yourself without looking.
3. Go section by section; click the slide links for the original diagrams.
4. Finish with the **Decision Tree** and **Top Exam Traps**, then drill Section 22 in the quiz app.
