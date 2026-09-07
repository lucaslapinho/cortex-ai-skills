# Findings and detection handoff

## Contents

1. Investigation-object boundaries
2. Conclusion criteria
3. Detection-opportunity gate
4. Handoff contract
5. Downstream routing

## 1. Investigation-object boundaries

Treat finding, alert, issue, case, event, and rule as distinct objects. Their relationships and availability are product/version/tenant-sensitive.

- A finding can be a lead or contextual object.
- An alert or issue reflects product logic and configuration, not a final analyst verdict.
- A case can organize work and evidence; it is not itself proof.
- A generating BIOC or IOC rule supplies provenance for a detection path; its label still does not prove compromise.

Use current XSIAM and XDR terminology only for the applicable product/release. Preserve legacy object names when the source artifact uses them and label their version scope. Use DEPRECATED only when current official evidence identifies deprecation; a still-supported legacy API identifier or historical label is not automatically deprecated.

## 2. Conclusion criteria

Tie confidence to explicit criteria:

- primary evidence meets the hypothesis observable;
- evidence provenance and time are adequate;
- necessary population/coverage is verified;
- material alternatives were tested;
- independent corroboration exists where risk warrants it;
- contradicting evidence and gaps are disclosed.

Do not raise confidence merely because multiple records originated from the same producer or detection rule.

## 3. Detection-opportunity gate

A detection opportunity is justified when:

- the behavior is repeatable and has a stable observable;
- the target telemetry is available with acceptable coverage;
- the signal is distinguishable from known legitimate activity;
- a baseline and candidate threshold/logic can be tested;
- expected false positives and blind spots are described;
- the handoff has an owner and validation plan.

A single IOC, one-off incident artifact, unverified schema, or unexplained anomaly is usually a hunting lead rather than a production detection.

## 4. Handoff contract

DET-nnn must include:

1. behavior and risk;
2. source hunt/evidence IDs;
3. applicable product/surface/version;
4. required telemetry and schema evidence;
5. candidate analytic logic in prose;
6. baseline and exclusions;
7. expected signal and false-positive families;
8. coverage and evasion limits;
9. ATT&CK interpretation with version/date if used;
10. safe test dataset and acceptance criteria;
11. precision/recall assumptions, never efficacy claims;
12. owner, review, deployment, monitoring, and rollback needs;
13. status and tenant qualifiers.

Do not create a production-ready rule unless a separately authorized detection-engineering workflow validates the schema, logic, performance, governance, and rollout.

## 5. Downstream routing

- Schema/XQL unresolved: send a query handoff packet to an XQL-capable workflow.
- Repeatable detection candidate: send DET-nnn to detection engineering.
- Active compromise evidence: recommend incident-response escalation; do not contain.
- Case/issue documentation needed: provide evidence IDs, timeline, confidence, gaps, and next actions.
- Missing integration or collection: route the gap to platform/integration owners.
- Malware or artifact semantics: route preserved evidence to the appropriate specialist.
