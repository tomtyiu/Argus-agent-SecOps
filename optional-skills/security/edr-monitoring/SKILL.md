---
name: edr-monitoring
description: Triage endpoint telemetry for suspicious activity.
version: 0.1.0
author: Thomas Yiu (@tomtyiu), Hermes Agent
license: MIT
category: security
platforms: [linux, macos, windows]
metadata:
  hermes:
    tags: [security, edr, endpoint, detection, triage]
    category: security
    related_skills: [security-log-detection, ndr-monitoring]
---

# EDR Monitoring Skill

Triage authorized endpoint-detection-and-response (EDR) telemetry for suspicious processes, persistence, credential access, and defense evasion. “ERC” is treated here as EDR; if ERC means a different product or control in your environment, map its exported fields before running detections.

## When to Use

- Reviewing EDR alerts or read-only endpoint telemetry exports.
- Correlating process trees, user sessions, files, services, and endpoint network connections.
- Preparing an evidence-backed endpoint triage or escalation report.

Do not use for unauthorized endpoint access, malware deployment, evasion, or automatic containment without approval.

## Prerequisites

- Authorization for the endpoint fleet, tenant, and time window.
- Read-only EDR console access, export, or approved MCP server; never place API tokens in a skill or report.
- Endpoint names, operating-system coverage, sensor health, clock source, and retention limits.
- Use `read_file` and `search_files` for exports; use `terminal` only for approved read-only inspection.

## How to Run

1. Record tenant, host scope, sensor status, time window, timezone, and EDR schema.
2. Start with alerts and process trees, then pivot to identity, persistence, file, and network context.
3. Preserve event IDs, hashes, signer data, command-line metadata, and timestamps while redacting secrets.
4. Separate observed facts from analyst inference and document missing telemetry.
5. Escalate response actions through the authorized incident workflow.

## Quick Reference

| Endpoint signal | Useful pivots | Validate |
|---|---|---|
| Suspicious process | Parent, signer, hash, user, prevalence | Is it approved software or a known-good update? |
| Persistence change | Service, task, startup, run key, launch agent | Was there a change ticket or deployment? |
| Credential access | Process, target, privilege, sensor alert | Is the access expected for this role and tool? |
| Sensor tampering | Actor, policy, stop event, gap | Was maintenance scheduled and documented? |
| Host egress | Process, destination, DNS, proxy, identity | Does NDR or proxy telemetry corroborate it? |

## Procedure

1. Validate sensor health and collection gaps before interpreting silence as clean.
2. Review process ancestry for unusual interpreters, office-to-shell chains, unsigned binaries, user-writable execution paths, and rare parent-child relationships.
3. Review persistence and privilege changes, including services, scheduled tasks, startup locations, launch agents, new local administrators, and token or policy changes.
4. Review file and memory-related alerts using only telemetry the EDR already exposes. Do not dump credentials, memory, or private data as part of routine triage.
5. Correlate endpoint events with identity and NDR data using stable host, user, process, hash, and timestamp keys.
6. Assign severity and confidence based on exposure, privilege, execution, corroboration, and business context. Mark detections as hypotheses when telemetry is incomplete.
7. Recommend isolation, kill, quarantine, or credential action only as a human-approved next step; record rollback and evidence-preservation requirements.

## Pitfalls

- Treating a command line as proof of intent without parent, signer, user, and deployment context.
- Trusting a hash or vendor name without checking signer, prevalence, path, and collection time.
- Killing a process or isolating a host before preserving volatile evidence and confirming impact.
- Exposing command-line secrets, access tokens, or personal data in tickets.
- Ignoring sensor health, policy changes, clock drift, or offline hosts.

## Verification

- Test the procedure with sanitized benign and suspicious telemetry fixtures.
- Confirm process-tree and host pivots return the original event IDs and timestamps.
- Reconcile alert counts with the EDR export or query result and record unsupported fields.
- Verify every recommended response has an owner, approval gate, evidence-preservation step, and rollback path.
