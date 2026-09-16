---
name: ndr-monitoring
description: Detect network threats from authorized traffic telemetry.
version: 0.1.0
author: Thomas Yiu (@tomtyiu), Hermes Agent
license: MIT
category: security
platforms: [linux, macos, windows]
metadata:
  hermes:
    tags: [security, ndr, network, traffic, detection]
    category: security
    related_skills: [security-log-detection, edr-monitoring]
---

# NDR Monitoring Skill

Analyze authorized network-detection-and-response (NDR) telemetry, flow records, DNS logs, proxy logs, Zeek records, or Suricata alerts for threats. The default posture is metadata-first and read-only: do not capture content, probe hosts, block traffic, or modify network controls without explicit authorization.

## When to Use

- Reviewing NDR alerts, NetFlow/IPFIX, DNS, proxy, Zeek, or Suricata exports.
- Detecting scanning, command-and-control patterns, lateral movement, exfiltration, and policy violations.
- Correlating network observations with endpoint and identity telemetry.

Do not use for unauthorized packet capture, active scanning, interception, evasion, or disruptive blocking.

## Prerequisites

- Written authorization covering interfaces, VLANs, tenants, destinations, and retention.
- A bounded time window, timezone, sensor list, network zones, asset inventory, and approved read-only query or MCP access.
- Flow, DNS, proxy, TLS metadata, or alert data; collect full payloads only under a separate approved process.
- Use `read_file`, `search_files`, and `terminal` for sanitized exports and approved read-only validation.

## How to Run

1. Define monitored zones, expected services, sensitive assets, and an explicit no-action boundary.
2. Validate sensor coverage, clock alignment, NAT mapping, and retention gaps.
3. Establish baselines by asset, protocol, destination, volume, and time of day.
4. Run detections, preserve source event IDs, and correlate with EDR and security logs.
5. Report evidence, confidence, likely impact, and the approved next query; route response through network operations.

## Quick Reference

| Signal | Correlate | Validate |
|---|---|---|
| Beaconing | Periodicity, rare destination, process, DNS | Is it a known agent, update service, or monitoring tool? |
| Scanning | Source, ports, zones, asset role, rate | Is it approved inventory or vulnerability scanning? |
| DNS anomaly | Entropy, NXDOMAIN, age, resolver, host | Is it CDN, software update, or split-horizon DNS? |
| Lateral movement | Auth, SMB/RDP/WinRM/SSH, source role | Is the path expected for administration? |
| Exfiltration | Volume, destination, protocol, identity | Is it backup, replication, or approved transfer? |

## Procedure

1. Confirm that the event is observable through the available telemetry and record blind spots such as encryption, asymmetric routing, NAT, or sensor loss.
2. Detect reconnaissance from unusual fan-out, sequential ports, denied-connection bursts, or new east-west paths, while excluding approved scanners.
3. Detect command-and-control candidates from periodic low-volume flows, rare destinations, unusual DNS patterns, proxy policy violations, and mismatched protocol or port use.
4. Detect lateral movement from new administrative paths, remote-service bursts, credential reuse across zones, and endpoint corroboration.
5. Detect possible exfiltration from unusual volume, compression or archive timing, destination novelty, long-lived sessions, and identity or endpoint context. Treat encrypted payloads as metadata-only evidence.
6. Correlate source and destination with asset inventory, EDR process data, authentication logs, and change windows. Use at least two independent indicators before high-confidence escalation where possible.
7. Recommend containment, blocking, sinkholing, or capture only through an approved change or incident process. Preserve timestamps, sensor IDs, query text, and chain-of-custody metadata.

## Pitfalls

- Confusing CDN, backup, vulnerability-scanner, monitoring, or NAT behavior with malicious traffic.
- Treating an IP reputation result as sufficient evidence without asset and time context.
- Capturing payloads or personal data by default when flow metadata answers the question.
- Probing a suspected host or blocking a destination during detection without authorization.
- Ignoring IPv6, encrypted traffic, asymmetric routing, clock drift, and sensor blind spots.

## Verification

- Run detections against sanitized benign traffic and reviewed positive fixtures.
- Reconcile event and byte counts with the source sensor and document NAT or sampling effects.
- Confirm every finding includes source, destination, protocol, time window, sensor, evidence, confidence, and blind spots.
- Verify high and medium findings have a human owner, approved next action, and a non-disruptive validation query.
