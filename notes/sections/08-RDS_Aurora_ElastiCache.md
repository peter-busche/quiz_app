# 🚨 Section 8: AWS Fundamentals: RDS + Aurora + ElastiCache — Top Exam Traps

Slides 138–164 ([open slides](../../AWS_Certified_Developer_Slides_v45.pdf#page=138))

1. **RDS is managed — you can't SSH in** (except **RDS Custom**); OS patching, backups, Point-in-Time Restore are handled for you.
2. **Storage Auto Scaling needs a Maximum Storage Threshold** — triggers at **< 10% free, lasting 5 min, 6 h since last change**.
3. **Read Replicas = ASYNC = eventually consistent reads**, up to **15**, for **scaling reads** (SELECT only).
4. **Apps must update the connection string** to use read replicas.
5. **Reporting/analytics without impacting prod → Read Replica**.
6. **Replica in same region (different AZ) = free replication traffic**; **cross-region = $$$**.
7. **Multi-AZ = SYNC, one DNS name, automatic failover = disaster recovery — NOT for scaling** (standby serves no reads).
8. **Read Replicas can be set up as Multi-AZ** for DR.
9. **Single-AZ → Multi-AZ = zero downtime** (click "modify": snapshot → restore in new AZ → sync).
10. **Aurora: 6 copies across 3 AZs** (4/6 for writes, 3/6 for reads), **15 replicas**, **< 30 s failover**, storage grows in **10 GB** steps.
11. **Aurora Writer Endpoint → master; Reader Endpoint → load-balances across replicas** (connections, not queries).
12. **Aurora Backtrack** = restore to any point in time **without backups**.
13. **Encryption at rest must be set at launch**; **unencrypted master → replicas can't be encrypted**; to encrypt an existing DB → **snapshot → restore as encrypted**.
14. **IAM Authentication** = connect with IAM roles instead of username/password; **network access = Security Groups**.
15. **Lambda + RDS "too many connections" → RDS Proxy** (pools connections, **66% faster failover**, IAM auth + Secrets Manager, **VPC only — never public**, no code changes).
16. **ElastiCache = Redis or Memcached**, requires **heavy application code changes**.
17. **Make the app stateless → store user sessions in ElastiCache**.
19. **Lazy Loading (cache-aside):** only requested data cached, node failure not fatal — cons: **3 round trips on miss, stale data**.
20. **Write-Through:** never stale — cons: **missing data until written, cache churn**; combine with Lazy Loading.
21. **TTL is a good idea except with pure Write-Through**; too many memory evictions (LRU) → **scale up or out**.
22. **Cache anti-pattern: rapidly changing data or huge key space**; good fit: slow-changing data, few hot keys.
