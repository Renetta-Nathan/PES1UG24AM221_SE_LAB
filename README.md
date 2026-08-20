# PES1UG24AM221_SE_LAB01

## Lab 1 – Requirements Engineering & UML Use-Case Modelling

### Problem Statement #47

**Domain & SSL Certificate Expiry Alert System**

### Problem Overview

An IT operations utility that performs automated daily WHOIS registration and SSL/TLS handshake audits, alerting system administrators through escalation ladders before domain or certificate expiration.

### Target Actors

- SysAdmin
- Security Officer

## Repository Contents

### Requirements

Contains:

- 5 Functional Requirements (FR-001 to FR-005)
- 2 Non-Functional Requirements (NFR-001 to NFR-002)

See:

`requirements/requirements.md`

### UML Use-Case Diagram

The UML diagram models:

- SysAdmin
- Security Officer
- Domain monitoring
- WHOIS auditing
- SSL/TLS auditing
- Expiration checking
- Alert generation
- Alert escalation
- Audit records
- Domain management

See:

`uml/use-case-diagram.png`

PlantUML source:

`uml/use-case-diagram.puml`

### Use-Case Flow Specification

The document describes the domain and SSL/TLS certificate expiration monitoring use case, including:

- Preconditions
- Postconditions
- Main Success Scenario
- Alternate Flow

See:

`use-case-flow/certificate-expiry-monitoring.md`
