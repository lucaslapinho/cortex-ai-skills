# Example: OpenCTI integration mismatch

## Symptom

A team reports that some OpenCTI object types do not become Cortex indicators after an upgrade.

## Evidence status

- Report: `UNVERIFIED / PROJECT-ASSERTED / TENANT-UNVERIFIED`.
- Product/version, OpenCTI server version, installed Cortex integration, mappings, logs, and sample objects: not supplied.
- Official baseline: `VERSION-DEPENDENT / OFFICIAL-CURRENT`.

The current OpenCTI Feed 4.x integration reference reviewed for this Skill lists XSOAR and XSIAM availability and names an OpenCTI compatibility baseline. Its out-of-box indicator-type list and automatic-creation wording explicitly name XSOAR, so XSIAM mapping remains `UNVERIFIED`. The older OpenCTI Feed 3.x reference is deprecated in favor of 4.x. Those facts make version/mapping mismatch plausible; they do not prove the root cause.

## Competing hypotheses

| Hypothesis | Read-only evidence |
|---|---|
| OpenCTI server and installed integration are incompatible | Sanitized version inventory and current integration reference |
| The tenant still uses deprecated OpenCTI 3.x integration | Exact installed integration name/version |
| A source object type has no applicable out-of-box mapping | Named Cortex product plus one sanitized source object and installed mapping/type configuration; do not reuse the XSOAR list as XSIAM evidence |
| Pattern/type validation rejects the object | Sanitized processing error/rejection evidence |
| Pagination/checkpoint skipped an update | Source IDs/revisions and page/checkpoint logs |
| Marking/exclusion policy prevents the expected processing | Sanitized marking and applicable exclusion configuration |
| Object is represented as context/relationship rather than an indicator | Source and Cortex readback for one object |

## Safe diagnostic sequence

1. Inventory product/build, license, OpenCTI server, content pack, exact integration/version, engine, and permissions.
2. Re-open the current OpenCTI 4.x and deprecated 3.x references.
3. Choose one sanitized missing object and one known-good object from the same UTC window.
4. Trace source availability, page/checkpoint, mapping/type validation, managed readback, and relationships.
5. Classify the first divergent stage before proposing a change.

For pagination, the current official 4.x page has conflicting output-path prose and example nesting, plus a no-output declaration. Resolve that conflict with applicable installed metadata or pinned implementation and bounded readback; no pagination path is established by this example.

## Change boundary

Do not upgrade, reset fetch history, broaden mappings, ignore validation, or replay the full source without approval, exact scope, expected volume, before state, rollback, and duplicate/capacity analysis.

## Conclusion

Most defensible current conclusion: `UNVERIFIED`. Version or mapping incompatibility is a supported hypothesis, not a diagnosis. No migration, fetch, import, or tenant result is claimed.

## Local references

- [Troubleshooting](../../references/troubleshooting.md)
- [Interoperability and distribution](../../references/interoperability-and-distribution.md)
