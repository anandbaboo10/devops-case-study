# DevOps & Analytics Transformation — Strategy Package

## 1. Executive intent and decision
**Re-scope, do not pause the whole program or accelerate blindly.** Keep repo migration moving where safe; move pipeline conversion to a risk-based, service-tiered factory with explicit Windows/x86 exceptions. Temporarily gate enforcement on a small set of critical controls and pilot developer-friendly remediation before broad mandatory rollout. Treat disputed DORA metrics as a data product quality issue—not a performance management issue.

## 2. Target architecture
GitHub Enterprise is the source-control and CI/CD strategic control plane; Azure Boards stays in the designated ADO organization for work tracking with verified commit/PR linking. Standard reusable workflows/composite actions expose paved roads; central policy-as-code and org rulesets enforce minimums. Hosted runners cover standard workloads; segmented ephemeral self-hosted Windows/x86 runner pools serve documented legacy constraints. OIDC/federated identity preferred to long-lived secrets; environment approvals for production. Fabric Lakehouse Bronze (immutable authorized extracts), Silver (typed/deduped/conformed), Gold (versioned metric contract), Power BI semantic model and dashboard. Catalog lineage, access controls and quality status accompany every metric.

## 3. Operating model / IDP product
Central platform team owns paved-road templates, runner fleet, workflow security, platform SLOs, migration tooling, developer portal/catalog, and support. Domain teams own service metadata, tests, deployment definition, incident attribution, and adoption. Product model: funded roadmap, internal customers, service tiers, published docs/changelog, support channel, usage/adoption telemetry, reliability/cost measures. Federated champions provide onboarding and exception feedback. Golden path is opt-in and easy first; required controls are proportionate to service risk.

## 4. Migration waves and controls
Inventory and classify all 5 orgs / ~1,000 repos / ~1,500 pipelines by business criticality, language/runtime, dependencies, permissions, agent demands, release coupling, and owner. Wave 0: ownership/data discovery, pilot, controls and restore rehearsal. Wave 1: low-risk stateless repos/pipelines; dual-run validation. Wave 2: common build patterns and dependent repos in service-aligned batches. Wave 3: legacy/native/regulated workloads with bespoke runners and signed exceptions. Wave 4: decommission old pipelines only after parity, access, artifact, audit, and rollback criteria pass. Freeze only affected cutovers if criteria fail. Keep Boards migration out of scope except integration validation.

## 5. Security, governance and exceptions
Org-level baseline: SSO/SCIM, least privilege, protected branches/rulesets, CODEOWNERS, required review/checks, secret scanning, dependency alerts, audit-log retention, approved actions pinning, artifact provenance/retention, environment protection, runner isolation, SBOM/signing where justified. Central workflow changes reviewed/versioned; pin third-party actions to immutable SHAs through approved allowlist. Exception record includes owner, asset, risk, compensating control, approver, expiry, remediation date; review monthly. Avoid blanket required checks before reliability and support are ready. Separate developer identity from automation identities; rotate/revoke tokens.

## 6. Trusted metric product
Publish a data contract and metric dictionary with deployment definition, service/environment scope, event-time timezone, attribution window, dedupe keys, exclusions, denominator, null behavior, freshness SLA, ownership and lineage. Reconcile source counts with teams before executive use. Do not score individuals or compare unlike services. Show coverage and quality flags. DORA should be used for system improvement and trends with context, not simplistic targets.

## 7. Twelve-month roadmap
**Q1 (months 1–3):** discover inventory/owners; pilot golden path and 2–3 migration cohorts; unblock runner exception design; baseline developer friction; define metric contract and source gaps; quality dashboard prototype.
**Q2 (4–6):** scale templates and training; migrate common pipeline archetypes; central runner pools; GitHub–Boards linkage; implement Fabric Bronze/Silver and audited Gold pilot; security enforcement stage 1.
**Q3 (7–9):** service-aligned waves; sunset redundant pipelines only after parity; expand metric coverage, lineage and semantic model; reliability/error-budget reviews; enforcement stage 2 for supported repos.
**Q4 (10–12):** consolidate remaining exceptions with business cases; retire obsolete org assets; optimize runner/cost and platform SLOs; independent controls/metric audit; assess AI pilot outcomes and next-year roadmap.

## 8. Prioritized 90-day plan
Days 0–30: appoint exec sponsor and product owners; freeze inventory schema; establish repo/pipeline owner and criticality; profile pipeline archetypes and x86/native demand; agree success measures; validate security baseline and rollback; interview developer cohorts; metric source mapping and incident timestamp anomalies.
Days 31–60: pilot ~20–30 representative repos across standard and exception paths; build reusable workflow/action; implement workflow parity checks and evidence bundles; dual-run where feasible; build DQ gates and lineage prototype; weekly friction office hours; risk review with security.
Days 61–90: expand first low-risk wave on exit criteria; turn on graduated branch protections for validated repos; close priority exception designs; publish dashboard as provisional with caveats; decision gate for next wave based on migration throughput, CI success, rollback readiness, developer friction and data quality.

## 9. Measures, investment and trade-offs
Track owner coverage, migration throughput and rollback rate; CI success/time-to-feedback; reusable workflow adoption; runner availability/cost; critical vulnerability remediation; exception age; developer satisfaction/task completion; DORA source coverage/freshness/quality. Invest in platform product engineers, migration automation, Windows runner isolation, identity/security engineering, Fabric data engineering, enablement and observability. Defer mass rewrite, forced Boards migration, universal self-hosted fleet, premature AI agents, team ranking, and decommissioning before parity. Trade-off: a short dual-run/cost period reduces delivery and audit risk.

## 10. Risk register and AI
| Risk | Response |
|---|---|
| Pipeline lag blocks release parity | Archetype factory, focused conversion squads, wave gates, visible backlog/owner. |
| x86/native product incompatibility | Isolated supported Windows runners, inventory, containment, funded modernization exceptions. |
| Security friction/unsafe bypasses | Risk-based progressive enforcement, fast exception path, measure blocked PRs and false positives. |
| Metric dispute / bad linkage | Contract, lineage, reconciliation, quarantining, publish coverage before benchmarks. |
| Migration outage / artifact loss | Dual-run, immutable artifact retention, tested rollback and cutover checklist. |
| AI code/data leakage or unsafe automation | Approved enterprise tools only, no secrets/regulated content, human approval, audit, limited read-only pilots. |

AI opportunities: policy/documentation Q&A grounded in approved platform docs; pipeline failure summarization; suggested YAML conversion with deterministic validation; anomaly triage. Later, tightly scoped agent can open a PR, never merge/deploy autonomously initially. Measure accepted suggestions, escape defects, toil saved, and security incidents; stop pilots without measurable benefit.

## Assumptions and implementation boundary
Scale and maturity figures are scenario-provided, not independently verified. The included code is a working small sample; Fabric notebook is a proposed portable implementation sketch, not a live workspace deployment. Supplied workbook is schema/data-profiling input only; no raw workbook or direct identifiers included. The package makes no claim of hosted GitHub Actions or Fabric execution evidence.
