# Executive recommendation (one page)

## Decision: Re-scope the transformation; continue safe repo migration, constrain pipeline cutovers
Repository migration ahead of plan is not the end-state: converted pipelines, developer usability, safe execution and trustworthy telemetry are the critical path. Do not pause all work or accelerate all waves. Continue low-risk repositories with proven validation; shift pipeline capacity to conversion archetypes and legacy-runner paths. Stage security enforcement so critical protections are immediate, but broad required checks follow pilot reliability and remediation support.

### Priorities for the next 90 days
1. **Control risk and regain pipeline throughput:** inventory owners, classify pipeline archetypes, run 20–30 representative pilots, dual-run critical paths, protect rollback and artifact parity. Create segregated Windows/x86 runner path for approved legacy products.
2. **Reduce developer friction:** measure time-to-feedback, blocked PRs, failure causes and satisfaction; fix top workflow pain points; publish docs and office hours; use exception process with expiry rather than shadow pipelines.
3. **Establish metric trust before targets:** publish DORA definitions, lineage, source coverage and quality status. Workbook profiling found 164 commits, 350 builds, 11 incidents, two projects; commit/build key and deployment semantics require validation, builds show no explicit outcome, only three incidents are marked deployment-caused, and one incident resolution precedes start. Therefore do not represent the workbook as an authoritative DORA baseline.

### Investment choices
Fund a platform product squad (workflow/migration automation and developer enablement), secure runner engineering for legacy workloads, and a small Fabric data product team. Accept temporary dual-run and runner costs to reduce cutover risk. Defer mass rewrites, full ADO retirement, universal AI agents, team-level DORA targets, and broad mandatory controls on unsupported paths.

### Executive decisions required
- Name accountable sponsor and service/pipeline owners; prioritize business-critical waves.
- Approve minimum org-wide security baseline and risk-tiered rollout, exception authority/expiry, and runner isolation funding.
- Confirm Azure Boards remains in one ADO org and fund integration/identity ownership.
- Approve Fabric source access, data stewardship, metric contract, and a “no ranking until quality gate” policy.
- Set stop/go criteria: parity evidence, CI reliability, rollback rehearsal, security controls, developer friction and metric coverage.

**Success at day 90:** pilot cohorts meet agreed parity/security/rollback gates; conversion throughput is measured and improving; exception inventory has owners/dates; developers report friction trend; DORA dashboard displays only qualified metrics with lineage and explicit gaps.
