# Lab 01: Requirements Engineering & UML Use-Case Modelling

## Problem Statement #47: Domain & SSL Certificate Expiry Alert System

### Objective

The objective of this lab is to perform requirements engineering for a Domain & SSL Certificate Expiry Alert System and model its behaviour using UML use-case modelling.

The system automatically monitors domain registration and SSL/TLS certificate expiration dates and alerts responsible personnel before expiration.

---

## 1. Requirements Specification

### Functional Requirements

| ID | Type | Description | Priority |
|---|---|---|---|
| FR-001 | Functional | The system shall initiate TLS handshakes against monitored domains daily, extract certificate expiration dates, and trigger alerts at 30, 15, and 3 days before expiry. | High |
| FR-002 | Functional | The system shall perform daily WHOIS registration audits for all monitored domains and retrieve their domain registration expiration dates. | High |
| FR-003 | Functional | The system shall compare domain and SSL/TLS certificate expiration dates against the configured expiration thresholds. | High |
| FR-004 | Functional | The system shall send alerts to the appropriate SysAdmin or Security Officer according to the configured escalation ladder. | High |
| FR-005 | Functional | The system shall maintain an audit record containing the monitored domain, audit date, expiration information, alert status, and escalation status. | Medium |

### Non-Functional Requirements

| ID | Type | Description | Priority |
|---|---|---|---|
| NFR-001 | Performance | The monitoring engine shall scan a list of 1,000 domains and SSL endpoints in under 3 minutes. | High |
| NFR-002 | Security | The system shall protect monitoring and audit information from unauthorized access and restrict alert-management operations to authorized users. | High |

---

## 2. Actors

The system has two primary actors:

- **SysAdmin**
  - Manages monitored domains
  - Views audit records
  - Receives alerts
  - Handles escalated alerts

- **Security Officer**
  - Receives generated alerts
  - Handles escalated alerts
  - Reviews monitoring and security information

---

## 3. Use Cases

The major use cases identified for the system are:

- **UC-01:** Monitor Domains
- **UC-02:** Manage Monitored Domains
- **UC-03:** Perform WHOIS Audit
- **UC-04:** Perform SSL/TLS Audit
- **UC-05:** Check Expiration Threshold
- **UC-06:** Generate Alert
- **UC-07:** Escalate Alert
- **UC-08:** View Audit Records

---

## 4. UML Use-Case Relationships

The following relationships are represented in the use-case diagram:

### Include Relationships

- **Monitor Domains** `<<include>>` **Perform WHOIS Audit**
- **Monitor Domains** `<<include>>` **Perform SSL/TLS Audit**
- **Perform WHOIS Audit** `<<include>>` **Check Expiration Threshold**
- **Perform SSL/TLS Audit** `<<include>>` **Check Expiration Threshold**

The `<<include>>` relationship represents functionality that is performed as part of the main use case.

### Extend Relationship

- **Generate Alert** `<<extend>>` **Escalate Alert**

Escalation is performed when the configured escalation conditions require it.

---

## 5. Use-Case Flow

### Use Case: Monitor Domain and SSL/TLS Certificate Expiration

**Use Case ID:** UC-001

**Primary Actors:**
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

---

## 6. System Constraints

- Domain and SSL/TLS expiration dates must be monitored daily.
- Alerts must be generated at configured expiration thresholds.
- Default alert thresholds include 30, 15, and 3 days before expiration.
- The system requires network access for WHOIS audits and SSL/TLS handshakes.
- Monitoring and audit information must be protected from unauthorized access.
- Alert-management operations must be restricted to authorized users.
- The monitoring engine must scan 1,000 domains and SSL endpoints in under 3 minutes.

---

## 7. Deliverables

The following deliverables are included in this lab:

1. Requirements Specification containing functional and non-functional requirements.
2. UML Use-Case Diagram showing actors, use cases, system boundary, and `<<include>>` / `<<extend>>` relationships.
3. Use-Case Flow Specification for **UC-001: Monitor Domain and SSL/TLS Certificate Expiration**.

---

## 8. Conclusion

This lab demonstrates the process of identifying and documenting functional and non-functional requirements, identifying system actors and use cases, modelling system behaviour using UML use-case diagrams, and specifying the main and alternate flows of a key use case.

The resulting model provides a structured representation of a system that monitors domain and SSL/TLS certificate expiration and alerts responsible personnel before expiration.
