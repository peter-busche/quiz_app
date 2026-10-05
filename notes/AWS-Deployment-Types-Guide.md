# 🚀 AWS Deployment Types Study Guide

Master deployment strategies across ECS, Elastic Beanstalk, CodeDeploy, API Gateway & Lambda

---

## 📊 Master Comparison Chart

**Legend:** 🟢 = good for you · 🟡 = in between · 🔴 = the trade-off you pay · ➖ = not applicable

### Your 6 metrics

| Service | Deployment Type | 1. Deploy speed | 2. Rollback speed | 3. Cost | 4. New instances? | 5. Downtime? | 6. Reduced capacity during deploy? |
|---|---|---|---|---|---|---|---|
| **Elastic Beanstalk** | All at once | 🟢 **Fastest** | 🔴 Slow (redeploy old version) | 🟢 **Free** — no extra | 🟢 No | 🔴 **YES** | 🔴 **Yes — all instances at once** |
| | Rolling | 🔴 Slow (batch by batch) | 🔴 Slow (redeploy) | 🟢 **Free** — no extra | 🟢 No | 🟢 No | 🔴 **Yes — one batch out at a time** |
| | Rolling with additional batches | 🔴 Slower than rolling | 🔴 Slow (redeploy) | 🟡 **Small** extra (1 batch) | 🟡 Partly — 1 extra batch, rest are existing | 🟢 No | 🟢 **No — full capacity kept** |
| | Immutable | 🔴 **Slowest** | 🟢 **Fast** — terminate the temp ASG | 🔴 **High** — double capacity temporarily | 🔴 **Yes — all new** (temp ASG) | 🟢 No | 🟢 No (extra capacity) |
| | Traffic Splitting (canary) | 🔴 Slow (evaluation period) | 🟢 **Fast & automatic** | 🔴 High — temp ASG at full capacity | 🔴 **Yes — temp ASG** | 🟢 No | 🟢 No |
| | Blue/Green (swap URLs) | 🟡 Manual — build a whole new env | 🟢 **Instant** — swap URLs back | 🔴 **Highest** — 2 full environments | 🔴 **Yes — whole new environment** | 🟢 No | 🟢 No |
| **CodeDeploy (EC2 / on-prem)** | In-Place (AllAtOnce / HalfAtATime / OneAtATime) | 🟡 AllAtOnce fast → OneAtATime slow | 🔴 Slow (redeploy last good revision) | 🟢 **Free** — no extra | 🟢 No | 🔴 **Yes — each instance briefly** (all at once if AllAtOnce) | 🔴 **Yes** — instances offline while updating |
| | Blue/Green | 🟡 Moderate (provision new fleet) | 🟢 **Fast** — reroute to original fleet (if kept) | 🔴 High — two fleets | 🔴 **Yes** | 🟢 No | 🟢 No |
| **ECS** | Rolling | 🟡 Moderate | 🔴 Slow (redeploy previous task def; circuit breaker can auto-roll back) | 🟢 Free → 🟡 small (if max % > 100) | 🟡 **New tasks**, same cluster | 🟢 No | 🟡 **Depends** — yes if minimum healthy % < 100 |
| | Blue/Green (via CodeDeploy) | 🟡 Moderate | 🟢 **Fast** — shift traffic back | 🔴 High — 2 task sets | 🔴 **Yes — new task set** | 🟢 No | 🟢 No |
| **Lambda (via CodeDeploy / SAM)** | AllAtOnce | 🟢 **Instant** | 🟢 Fast if using an alias (repoint) | 🟢 Free — pay per request | ➖ New **version**, no instances | 🟢 No | 🟢 No (serverless scaling) |
| | Canary (e.g. 10% for 5 min) | 🟡 Minutes (canary window) | 🟢 **Fast & automatic** (CloudWatch alarms) | 🟢 Free — pay per request | ➖ New version | 🟢 No | 🟢 No |
| | Linear (e.g. 10% every 1 min) | 🔴 Slowest of Lambda options | 🟢 **Fast & automatic** | 🟢 Free — pay per request | ➖ New version | 🟢 No | 🟢 No |
| **API Gateway** | Canary (stage setting) | 🟡 As slow as you promote it | 🟢 **Fast** — set canary to 0% / delete it | 🟢 Free — config change only | ➖ New deployment on a stage | 🟢 No | 🟢 No |

### ➕ Extra metrics worth tracking

These five show up in exam wording more often than "speed" does:

| Service | Deployment Type | 7. Both versions live at once? | 8. Automatic rollback? | 9. Test new version before real traffic? | 10. Blast radius if broken | 11. Relies on DNS change? |
|---|---|---|---|---|---|---|
| **Elastic Beanstalk** | All at once | 🟢 No | 🔴 No | 🔴 No | 🔴 **100% of users** | 🟢 No |
| | Rolling | 🔴 **Yes** | 🔴 No | 🔴 No | 🟡 One batch at a time | 🟢 No |
| | Rolling with additional batches | 🔴 **Yes** | 🔴 No | 🔴 No | 🟡 One batch at a time | 🟢 No |
| | Immutable | 🟡 Briefly (health checks first) | 🟡 Fails health check → new ASG terminated | 🟡 Health checks only | 🟢 Small — old ASG untouched | 🟢 No |
| | Traffic Splitting | 🔴 **Yes** (by design) | 🟢 **Yes** — health monitored | 🟢 With real % of traffic | 🟢 **Small %** | 🟢 No |
| | Blue/Green | 🟢 No (separate envs) | 🔴 No (manual swap) | 🟢 **Yes — full env via its own URL** | 🟢 None until swap | 🔴 **Yes — CNAME swap / Route 53 (DNS caching)** |
| **CodeDeploy (EC2)** | In-Place | 🔴 Yes (during rollout) | 🟡 Optional (alarms / failed deployment) | 🔴 No | 🟡 Batch size (🔴 if AllAtOnce) | 🟢 No |
| | Blue/Green | 🟢 No | 🟡 Optional (alarms) | 🟢 Yes — before rerouting | 🟢 None until reroute | 🟢 No (load balancer) |
| **ECS** | Rolling | 🔴 Yes | 🟡 Deployment circuit breaker | 🔴 No | 🟡 New tasks gradually | 🟢 No |
| | Blue/Green | 🟢 No (test listener) | 🟢 Yes (CodeDeploy + alarms) | 🟢 **Yes — test listener** + lifecycle hooks | 🟢 None until shift | 🟢 No |
| **Lambda** | AllAtOnce | 🟢 No | 🟡 Alarms (but 100% already moved) | 🟡 Pre-traffic hook | 🔴 **100%** | 🟢 No |
| | Canary | 🔴 Yes | 🟢 **Yes — CloudWatch alarms** | 🟢 Pre/Post traffic hooks + canary % | 🟢 **Canary %** (e.g. 10%) | 🟢 No |
| | Linear | 🔴 Yes | 🟢 **Yes — CloudWatch alarms** | 🟢 Hooks + small steps | 🟢 One increment | 🟢 No |
| **API Gateway** | Canary | 🔴 Yes | 🟡 Manual or via alarms | 🟢 Canary % of real traffic | 🟢 **Canary %** | 🟢 No |

**Why these matter:**
- **7. Both versions live at once** → if old and new code can't coexist (breaking DB/schema or API change), avoid Rolling / Canary / Linear.
- **8. Automatic rollback** → "roll back without manual intervention" = Canary/Linear (Lambda, CodeDeploy alarms) or Beanstalk Traffic Splitting.
- **9. Test before real traffic** → "validate the new version before users see it" = Blue/Green (test URL / ECS test listener) or pre-traffic hooks.
- **10. Blast radius** → "minimize the number of users affected by a bad release" = Canary / Traffic Splitting.
- **11. DNS change** → Beanstalk Blue/Green swaps CNAMEs, so **clients with cached DNS may hit the old env for a while** — don't terminate it immediately.

### 🧠 One-line summary per type

| Type | Remember it as |
|---|---|
| **All at once** | Fast + free, but **downtime** |
| **Rolling** | Free + no downtime, but **less capacity** and slow |
| **Rolling + additional batches** | Rolling **at full capacity** for a little money |
| **Immutable** | **New instances only**, fastest Beanstalk rollback, costs double |
| **Traffic Splitting / Canary / Linear** | **Small % first**, automatic rollback |
| **Blue/Green** | **Separate environment**, test then swap, instant rollback, most expensive |
| **In-Place (CodeDeploy)** | Free, **brief downtime per instance** |

---

## 📋 Your Scenarios

### 💰 Cheapest Deployment

**Best Choice:** Rolling deployments

- **ECS** - Rolling
- **Elastic Beanstalk** - Rolling
- **CodeDeploy** - In-Place
- **Lambda** - All-at-once

**Why:** Reuses existing infrastructure—no extra instances/capacity needed

---

### 🚦 Minimal Traffic Impact

**Best Choice:** Blue/Green or Canary deployments

- **ECS** - Blue/Green
- **Elastic Beanstalk** - Blue/Green
- **CodeDeploy** - Blue/Green
- **API Gateway** - Canary
- **Lambda** - Canary / Linear

**Why:** New infrastructure deployed in parallel; instant or gradual traffic shift

---

### 🔄 Only New EC2 Instances

**Best Choice:** Immutable or Blue/Green

- **Elastic Beanstalk** - Immutable
- **Elastic Beanstalk** - Blue/Green
- **CodeDeploy** - Blue/Green (with new instances)

**Why:** Old instances never touched; clean environment for every deployment

---

### ⏮️ Fastest Rollback

**Best Choice:** Blue/Green deployments

- **ECS** - Blue/Green (instant switch)
- **Elastic Beanstalk** - Blue/Green (instant swap)
- **CodeDeploy** - Blue/Green (instant traffic shift)
- **Elastic Beanstalk** - **Immutable** (terminate the temporary ASG) — the exam's answer when the choice is among Beanstalk *deployment policies* (your S17 Q3, S17 Q8)

**Why:** Old environment/instances stay running untouched; one action reverts all traffic

---

## 🔍 Deployment Types by Service

| Service | Deployment Type | How It Works | Downtime | Rollback Speed |
|---------|-----------------|-------------|----------|----------------|
| **ECS** | Rolling | Gradually replaces tasks in the service. Removes old, starts new based on desired count. | None | Slow (redeploy) |
| | Blue/Green | Creates entirely new task set (Green) alongside old (Blue). Switches all traffic at once via ALB/NLB. | None | Instant (switch back) |
| **Elastic Beanstalk** | All At Once | Stops all instances, deploys to all at same time. | Yes | Slow (redeploy) |
| | Rolling | Takes down a few instances at a time, deploys, brings them back up. | None | Slow (redeploy) |
| | Rolling with Additional Batch | Like Rolling, but keeps full capacity by launching extra instances during deployment. | None | Slow (redeploy) |
| | Immutable | Launches new instances in a temporary ASG, tests them, then moves them into the original ASG. Old instances terminated. | None | Fast (terminate the temporary ASG) |
| | Traffic-Splitting | Canary: new version on NEW instances in a temporary ASG gets a small % of traffic for a set time; healthy → instances migrate to the original ASG. | None | Fast (automatic on failure) |
| | Blue/Green | Launches entire new environment, tests, then swaps via DNS/environment URLs. | None | Instant (swap) |
| **CodeDeploy** | In-Place | Stops app on existing instances, deploys new code, restarts. Goes through instances one/batch at a time. | Brief per instance | Slow (redeploy) |
| | Blue/Green | Launches new instances with new version, switches traffic (ALB/Classic ELB), terminates old. | None | Instant (traffic shift back) |
| **API Gateway** | Canary Deployment | Routes small % of traffic to new stage version, monitors, gradually increases if healthy. | None | Fast (reduce canary traffic) |
| **Lambda** | Canary | Routes 10% traffic to new version for 5 min, then 100%. Uses CloudWatch alarms to trigger rollback. | None | Fast (< 5 min to rollback) |
| | Linear | Gradually increases traffic to new version in equal increments (e.g., 10% per minute). | None | Fast (proportional) |
| | All-at-once | Immediately routes 100% traffic to new version. | None | Fast (if aliased; otherwise redeploy) |

---

## ⚡ Key Characteristics

### 🔴 Rolling Deployments

- Gradual instance-by-instance replacement
- No downtime, reduced capacity during deployment
- Slower overall deployment time
- Good for stateless apps
- Risk: mismatch between old/new versions in flight

### 🔵 Blue/Green Deployments

- Two complete, identical infrastructures
- Zero downtime, instant traffic switch
- Doubled infrastructure cost (temporary)
- Instant rollback to previous version
- Best for stateless apps & critical systems

### 🟢 Immutable Deployments

- Launches completely new instances
- Old instances never modified
- Clean environment for every deployment
- Good for avoiding config drift
- Slower than rolling, cheaper than blue/green

### 🟡 Canary Deployments

- Route small % of traffic to new version first
- Monitor metrics for errors/performance
- Automatic rollback if issues detected
- Risk: detecting issues requires good monitoring
- Great for API Gateway & Lambda

### 🟣 In-Place Deployments

- Deploy directly to existing instances
- Cheapest option (reuses infrastructure)
- Brief downtime per instance
- Instances modified, risk of config drift
- Fast rollback if keeping old revision handy

### ⚪ All-at-Once Deployments

- Immediate switch to new version (Lambda)
- Or stop-all-then-start (Elastic Beanstalk)
- Beanstalk version causes downtime
- Lambda version (if aliased) has zero downtime
- Risk: rapid failure affects all users

---

## 🎯 Additional Factors to Consider

> **💡 Tip:** These factors often matter MORE than the raw deployment type. Use them to narrow down your choice when multiple deployment types could work.

### 1. Stateful vs Stateless
Stateless apps = any blue/green strategy. Stateful apps = rolling or canary to avoid connection drops.

### 2. Database Changes
Backward-compatible schema = any strategy. Breaking changes = need canary or blue/green to detect issues fast.

### 3. Monitoring & Alarms
Good monitoring = use canary (automatic rollback). Poor monitoring = stick to blue/green (manual control).

### 4. Session/Connection State
Long-lived connections (WebSockets, gRPC) = avoid rolling. Blue/green better. Canary causes connection drops.

### 5. Deployment Frequency
Many deploys/day = prefer canary/traffic-split (catch regressions fast). Rare deploys = blue/green acceptable.

### 6. Budget Constraints
Tight budget = rolling or in-place. Flexible budget = blue/green for safety. Canary = middle ground.

### 7. Traffic Pattern & SLA
High-traffic 24/7 = blue/green or canary. Off-peak deployments = rolling/all-at-once acceptable.

### 8. Dependency on Third Parties
If external APIs called by your service = canary/rolling (detect 3rd party failures gradually).

### 9. Compliance & Audit Trail
Regulated environments = immutable deployments (provable clean environment) or blue/green (audit-friendly).

### 10. Easy Rollback Requirement
"Rollback ASAP" = blue/green (instant). "Good enough in 5 min" = canary (automatic). "Redeploy is OK" = rolling.

### 11. Container/Lambda Cold Starts
Containers = rolling reuses containers. Lambda canary = new concurrency (cold starts happen gradually).

### 12. Automatic vs Manual Decisions
Canary/traffic-split = automatic rollback (needs alarms). Blue/green = manual rollback (more control).

---

## 🌳 Simple Decision Tree

**1. Do you need zero downtime?**
- **NO** → All-at-once (Beanstalk) or In-Place (CodeDeploy) for lowest cost
- **YES** → Go to #2

**2. Can you afford 2× infrastructure temporarily?**
- **YES** → Blue/Green (instant rollback, safest)
- **NO** → Go to #3

**3. Do you have good monitoring & alarms?**
- **YES** → Canary/Linear (automatic rollback)
- **NO** → Rolling (safest with limited monitoring)

---

## 🎓 Quick Reference by Service

### ECS (Fargate/EC2)

| Aspect | Answer |
|--------|--------|
| Default Deployment | Rolling |
| Best for Safety | Blue/Green |

**Key Point:** Both strategies built-in to ECS. Rolling uses fewer resources, Blue/Green gives instant rollback.

---

### Elastic Beanstalk

| Aspect | Answer |
|--------|--------|
| Zero Downtime? | Rolling, Immutable, Blue/Green, or Traffic-Splitting |
| Cheapest? | Rolling |
| Instant Rollback? | Blue/Green (environment swap) |
| New Instances Always? | Immutable or Blue/Green |

**Key Point:** Most flexibility of all services. Choose based on your tolerance for old/new version coexistence.

---

### CodeDeploy (EC2/On-Premises)

| Aspect | Answer |
|--------|--------|
| Only 2 Choices | In-Place or Blue/Green |
| Typical Use | Pair with appspec.yml for granular control |

**Key Point:** Less opinionated than Beanstalk. Blue/Green requires separate instance group or will create instances automatically.

---

### API Gateway

| Aspect | Answer |
|--------|--------|
| Deployment Type | Canary (traffic-splitting only) |
| How It Works | Routes % of requests to new stage version |
| Monitoring? | CloudWatch metrics & custom alarms |
| Rollback | Manual (reduce traffic) or automatic (via alarms) |

**Key Point:** API Gateway deploys are fast/cheap (no compute cost). The "deployment" is a stage config change, not new resources.

---

### Lambda (via SAM/CodeDeploy)

| Aspect | Answer |
|--------|--------|
| Three Options | Canary, Linear, All-at-once |
| Fastest Rollback | Canary or Linear (automatic, within minutes) |
| No Downtime? | All three have zero downtime |
| Requires Aliases? | Yes (traffic shift only works with aliases) |

**Key Point:** Lambda alias + version = enables canary/linear. Plain function = all-at-once only. Automatic rollback via alarms is powerful here.

---

## 📚 AWS Developer Exam Tips

### ✅ Key Test Patterns

- **Zero downtime + instant rollback?** → Blue/Green (always correct for both)
- **Cheapest?** → Rolling or In-Place (Immutable costs more)
- **Gradual traffic shift?** → Canary (API Gateway) or Linear/Canary (Lambda)
- **Only affects new instances?** → Immutable (EB) or Blue/Green (must launch new)
- **Automatic rollback?** → Canary/Linear (Lambda) with alarms, or check monitoring setup
- **Database schema change?** → Canary or blue/green to detect breaking changes
- **Long-lived connections?** → Avoid rolling; use blue/green

---

## 📝 Study Notes

### Common Question Patterns on the Exam

1. **Scenario-based questions** usually ask "which deployment strategy would you use if..."
   - Know the 12 factors above to quickly eliminate wrong answers
   - Blue/Green is almost always a "safe" answer for production systems

2. **Cost optimization questions** will test whether you know rolling/in-place are cheapest

3. **High availability/SLA questions** test knowledge of which strategies have zero downtime

4. **Rollback questions** often ask for fastest or easiest rollback → Blue/Green wins

5. **Database migration questions** require understanding that you need gradual traffic shift (canary/linear) to detect schema compatibility issues

---

## 💾 How to Use This Guide

1. **Read through** all the characteristics and understand the visual differences
2. **Study the decision tree** - memorize the three yes/no questions
3. **Review each service section** - AWS loves questions about specific service deployment options
4. **Practice scenarios** - when you see exam questions, map them to the 12 factors
5. **Focus on overlaps** - where multiple services share similar deployment types (Blue/Green exists in ECS, Beanstalk, and CodeDeploy)

Good luck with your AWS Certified Developer exam! 🎓