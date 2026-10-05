# 🚨 Section 15: CloudFront — Top Exam Traps

Slides 281–311 ([open slides](../../AWS_Certified_Developer_Slides_v45.pdf#page=281))

1. **S3 origin is secured with OAC + S3 bucket policy** — an S3 *static website* origin is a **custom (HTTP) origin**, not an S3 origin.
2. **Private ALB/NLB/EC2 → VPC Origin** (no internet exposure); **public** origin → security group must allow the **CloudFront edge public IPs**.
3. **CloudFront = static content cached everywhere (TTL)**; **S3 Cross-Region Replication = dynamic content, near real-time, in a few regions**.
4. **Default Cache Key = hostname + resource path** — add headers/cookies/query strings via a **Cache Policy**.
5. Anything in the Cache Key is **automatically forwarded** to the origin; need to forward something **without** caching on it → **Origin Request Policy**.
6. **More in the Cache Key = worse cache hit ratio** — "All" query strings = worst caching; "None" headers = best.
7. Updated the origin but users still see old content → **CreateInvalidation** (`/*` or `/images/*`) — otherwise wait for the **TTL**.
8. **Default cache behavior is always `/*` and always processed last**; route `/api/*` → ALB, `/*` → S3 via **cache behaviors**.
9. **Separate static and dynamic content** to maximize cache hits (no header/cookie caching rules on static).
10. **Geo Restriction** (allowlist / blocklist by country) → **copyright** use cases.
11. **Signed URL = one file; Signed Cookies = many files.**
12. **CloudFront Signed URL** (any origin, filters by IP/path/date, uses caching) ≠ **S3 Pre-Signed URL** (S3 only, acts as the signing IAM principal).
13. Signers: use **trusted key groups** (recommended, API + IAM) — **not** the root-account CloudFront key pair; **private key signs, CloudFront uses the public key to verify**.
14. **Price Class 100** = cheapest regions only; **200** = most regions minus most expensive; **All** = best performance.
15. **Origin Groups** (primary + secondary) = **failover / high availability**; **Cache Behaviors** = routing by path.
16. **Field-Level Encryption** = **asymmetric**, encrypts **up to 10 POST fields at the edge** with a public key — on top of HTTPS.
17. **Real-time logs → Kinesis Data Streams** (sampling rate, specific fields/behaviors).
18. **ACM certificate for CloudFront must be in us-east-1**; HTTPS is set by **Viewer/Origin Protocol Policy**, not Lambda@Edge.
