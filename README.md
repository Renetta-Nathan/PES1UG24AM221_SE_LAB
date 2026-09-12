# Software Engineering Lab

## Domain & SSL Certificate Expiry Alert System

**SRN:** PES1UG24AM221

This repository contains the work completed for the Software Engineering Laboratory based on the **Domain & SSL Certificate Expiry Alert System**.

---

## Lab 01 – Requirements Engineering & UML Use-Case Modelling

This lab focused on requirements engineering and UML use-case modelling for the **Domain & SSL Certificate Expiry Alert System**. The requirements were identified and documented as functional and non-functional requirements, followed by identifying the system actors and use cases. A UML use-case diagram was created to represent the interactions between the **SysAdmin**, **Security Officer**, and the system. A detailed use-case flow was also documented for monitoring domain and SSL/TLS certificate expiration, including the main success scenario and an alternate flow for audit failure.

### Topics Covered

- Functional and Non-Functional Requirements
- Requirements Specification
- Actors and Use Cases
- UML Use-Case Diagrams
- `<<include>>` and `<<extend>>` relationships
- Main and Alternate Use-Case Flows

---

## Lab 02 – Agile Backlog Creation & Sprint Simulation

This lab focused on applying Agile Scrum practices to the **Domain & SSL Certificate Expiry Alert System** using **Jira**. The requirements from Lab 01 were converted into Epics and User Stories and organized into a prioritized Product Backlog. Story Points were assigned using Fibonacci-based estimation, and the backlog was divided into two mock Scrum sprints. The progress of each sprint was simulated using the **To Do → In Progress → Done** workflow. Jira Burndown Charts were also generated to track the remaining work and sprint progress.

### Topics Covered

- Agile Scrum Methodology
- Jira Project and Scrum Board
- Epics and User Stories
- Product Backlog Creation
- Story Point Estimation
- Planning Poker
- Backlog Prioritization and Ranking
- Sprint Planning
- Sprint Execution
- To Do → In Progress → Done Workflow
- Sprint Comments and Tracking
- Burndown Charts
- Agile Sprint Reflection

### Sprint Summary

| Sprint | Stories | Story Points | Status |
|--------|---------|--------------|--------|
| Sprint 1 | 6 | 24 | Completed |
| Sprint 2 | 4 | 18 | Completed |
| **Total** | **10** | **42** | **Completed** |

---

## Lab 03 – Component Modelling & Architectural Pattern Selection

### Summary

This lab focused on evaluating architectural styles and selecting the most appropriate architecture for the **Domain & SSL Certificate Expiry Alert System**. **Layered, Microservices, and Client-Server architectures** were compared based on their advantages and disadvantages.

**Microservices Architecture** was selected because the system contains independent functions such as WHOIS auditing, SSL/TLS auditing, expiry detection, and alert management. These functions can be separated into independent services, allowing the system to achieve better modularity, scalability, and fault isolation.

A UML component diagram was created to represent the major components, interfaces, dependencies, and data flow within the system. The major components identified were the **Web Application (Admin Portal), Domain Monitoring Manager, WHOIS Audit Service, SSL/TLS Audit Service, Expiry Detection & Alert Service, and Audit Database**.

### Topics Covered

- Architectural Style Evaluation
- Layered Architecture
- Microservices Architecture
- Client-Server Architecture
- Architectural Pattern Selection
- UML Component Modelling
- UML Components and Interfaces
- Provided and Required Interfaces
- Component Dependencies
- Data Flow and Component Interactions
- Security Considerations
- Performance Considerations
- Architectural Documentation
- Component Diagram Creation

### Selected Architecture

**Microservices Architecture**

The Microservices Architecture was selected because:

1. **Independent Monitoring Services**  
   WHOIS auditing and SSL/TLS certificate auditing can operate as independent services without tightly coupling their implementation.

2. **Scalability and Fault Isolation**  
   Individual services can be scaled according to their workload, and a failure in one monitoring service does not necessarily stop the other services from operating.

### Main Components

| Component | Responsibility |
|-----------|----------------|
| Web Application (Admin Portal) | Provides the administrative interface for managing domains and viewing alerts |
| Domain Monitoring Manager | Coordinates domain monitoring and audit activities |
| WHOIS Audit Service | Performs WHOIS audits and retrieves domain expiry information |
| SSL/TLS Audit Service | Checks SSL/TLS certificates and retrieves certificate expiry information |
| Expiry Detection & Alert Service | Analyses audit results, checks expiry thresholds, and generates alerts |
| Audit Database | Stores domain data, audit records, alerts, and audit history |

### Main Interfaces

| Interface | Purpose |
|-----------|---------|
| Domain Management API | Connects the Web Application with the Domain Monitoring Manager |
| WHOIS Audit API | Connects the Domain Monitoring Manager with the WHOIS Audit Service |
| SSL/TLS Audit API | Connects the Domain Monitoring Manager with the SSL/TLS Audit Service |
| Alert API | Connects the Expiry Detection & Alert Service with the Web Application |

### Security Consideration

The architecture separates security responsibilities between services. Administrative access can be protected using authenticated HTTPS communication, while domain and audit information can be isolated within the appropriate services and database.

### Performance Consideration

WHOIS and SSL/TLS audits can operate independently and potentially in parallel. This allows multiple domains to be monitored efficiently and reduces the time required to perform monitoring operations.

---

## Lab 03 Deliverables

The Lab 03 work includes:

- UML Component Diagram
- Architectural Selection and Justification
- Lab Reflection
- README Documentation

### Files

```text
Lab 03/
│
├── README.md
│
├── PES1UG24AM221_Lab3_Component_Diagram.pdf
│
├── PES1UG24AM221_Lab3_Component_Diagram.png
│
├── PES1UG24AM221_Lab3_Architecture_Justification.pdf
│
└── PES1UG24AM221_Lab3_Lab_Reflection.pdf
