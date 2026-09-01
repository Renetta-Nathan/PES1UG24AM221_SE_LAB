# Use-Case Flow Specification

## Use Case: Monitor Domain and SSL/TLS Certificate Expiration

### Use Case ID

UC-001

### Primary Actors

- SysAdmin
- Security Officer

### Goal

To automatically monitor domain registration and SSL/TLS certificate expiration dates and alert responsible personnel before expiration.

### Preconditions

1. The monitoring system is operational.
2. The domains to be monitored are registered in the system.
3. The system has network access required to perform WHOIS audits and SSL/TLS handshakes.
4. Alert recipients and the escalation ladder are configured.

### Postconditions

1. WHOIS and SSL/TLS audit results are recorded.
2. Domain registration and SSL/TLS certificate expiration dates are stored.
3. Required alerts are generated when an expiration threshold is reached.
4. Alert and escalation activities are recorded in the audit records.

### Main Success Scenario

1. The monitoring system initiates the scheduled daily monitoring process.
2. The system retrieves the list of monitored domains.
3. The system performs a WHOIS registration audit for each monitored domain.
4. The system performs an SSL/TLS handshake against each monitored domain.
5. The system extracts the domain registration and SSL/TLS certificate expiration dates.
6. The system compares the expiration dates against the configured thresholds.
7. The system identifies domains or certificates approaching expiration.
8. If an expiration date is 30, 15, or 3 days away, the system generates an alert.
9. The system sends the alert to the appropriate SysAdmin or Security Officer.
10. If escalation is required, the system escalates the alert according to the configured escalation ladder.
11. The system records the audit results, alert status, and escalation status.
12. The monitoring process completes successfully.

### Alternate Flow: Audit Failure

1. During the WHOIS or SSL/TLS audit, the system cannot reach a domain or retrieve the required information.
2. The system records the audit as unsuccessful.
3. The system records the reason for the audit failure.
4. The system continues the monitoring process for the remaining domains.
5. The failed audit is recorded for review by the SysAdmin or Security Officer.