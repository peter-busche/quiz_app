# 🚨 Section 7: AWS Fundamentals: ELB + ASG — Top Exam Traps

Slides 92–137 ([open slides](../../AWS_Certified_Developer_Slides_v45.pdf#page=92))

1. **EBS is locked to one AZ** — move it with **snapshot → restore in the new AZ**; **EFS** = many Linux instances across AZs sharing files.
2. **EFS cost savings → lifecycle policy to IA / Archive**; **One Zone-IA** = cheapest (dev, single AZ).
3. **Vertical = bigger instance (scale up/down)**; **Horizontal = more instances (scale out/in)**; **High availability = at least 2 AZs**.
4. **ALB = Layer 7 (HTTP/HTTPS/WebSocket)**, **NLB = Layer 4 (TCP/UDP/TLS)**, **GWLB = Layer 3 (IP, GENEVE port 6081)** for 3rd-party firewalls/IDS.
5. **Only NLB has a static IP per AZ / Elastic IP** — "whitelist a fixed IP" → **NLB** (put an **ALB behind the NLB** if you also need HTTP routing).
6. **ALB routes by path, hostname, query string, headers** → one ALB for many microservices (CLB would need one per app).
7. **ALB targets: EC2, ECS tasks, Lambda (HTTP → JSON event), private IPs** — health checks are at the **target group** level.
8. **Client IP behind ALB is in `X-Forwarded-For`** (port in `X-Forwarded-Port`, protocol in `X-Forwarded-Proto`) — the app sees the ALB's private IP.
9. **Instance security group should allow traffic from the load balancer's security group**, not 0.0.0.0/0.
10. **Health check non-200 = unhealthy** → LB stops sending traffic (the **ASG** is what replaces the instance).
11. **Sticky sessions** work on CLB, ALB, NLB — fix "users lose session" quickly, but can **unbalance load**; reserved cookie names **AWSALB, AWSALBAPP, AWSALBTG** (CLB: **AWSELB**).
12. **Cross-zone: ALB = on by default, free**; **NLB/GWLB = off by default, you pay inter-AZ**; **CLB = off by default, free**.
13. **SSL offload to the load balancer** (not the EC2 instances) to save instance CPU; certificates via **ACM**.
14. **Multiple certificates on one LB → SNI** — works on **ALB, NLB, CloudFront**, **NOT CLB** (CLB = one cert, need multiple CLBs).
15. **Legacy clients with old TLS → security policy on the HTTPS listener**.
16. **Connection Draining (CLB) = Deregistration Delay (ALB/NLB)**: 1–3600 s, **default 300 s**, 0 disables — **lower it for short requests**.
17. **ASGs are free** (pay for EC2); **Launch Templates** replace deprecated Launch Configurations (AMI, instance type, user data, SGs, IAM role…).
18. **Target Tracking** = "keep CPU at ~40%"; **Step/Simple** = CloudWatch alarm thresholds; **Scheduled** = known pattern (Fridays 5 PM); **Predictive** = forecast.
19. **Good scaling metrics:** CPUUtilization, **RequestCountPerTarget**, Network In/Out, custom CloudWatch metrics.
20. **Cooldown (default 300 s)** blocks new scaling actions — shorten it with a **pre-baked AMI**.
21. **New AMI on all instances → Instance Refresh** (min healthy %, warm-up time).
