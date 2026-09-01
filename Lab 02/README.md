# Lab 2: Agile Backlog Creation & Sprint Simulation in Jira

## Student Details

- **Name:** Renetta Nathan
- **USN:** PES1UG24AM221
- **Lab:** Software Engineering Lab 2
- **Project:** Domain SSL Alert System
- **Tool Used:** Jira
- **Methodology:** Agile Scrum

---

## 1. Aim

To create and prioritize an Agile product backlog in Jira, estimate user stories using Story Points, conduct mock Scrum sprints, track sprint progress, and analyze the sprint using Jira's Burndown Chart.

---

## 2. Objectives

- Create Epics and User Stories in Jira.
- Organize User Stories under their respective Epics.
- Estimate User Stories using Story Points.
- Prioritize and rank the Product Backlog.
- Create and execute Scrum Sprints.
- Simulate progress using the To Do → In Progress → Done workflow.
- Add comments to completed work items.
- Generate and analyze Burndown Charts.
- Understand the Agile Scrum workflow using Jira.

---

## 3. Project Description

The project is a **Domain SSL Alert System** designed to monitor domains and SSL/TLS certificates, detect upcoming expirations, generate alerts, escalate critical alerts, and maintain audit records.

The project backlog was organized into three major Epics:

1. Domain & Certificate Monitoring
2. Alert & Escalation Management
3. Audit & System Management

---

## 4. Epics

### Epic 1: Domain & Certificate Monitoring

Responsible for monitoring domains and SSL/TLS certificates and detecting expiration-related information.

### Epic 2: Alert & Escalation Management

Responsible for generating notifications and escalating alerts when domain or certificate issues require attention.

### Epic 3: Audit & System Management

Responsible for maintaining audit records, managing domains, and providing secure access to the system.

---

## 5. User Stories

| ID | User Story | Epic | Story Points |
|----|------------|------|--------------|
| DSAS-4 | Daily WHOIS Audit | Domain & Certificate Monitoring | 5 |
| DSAS-5 | Daily SSL/TLS Audit | Domain & Certificate Monitoring | 5 |
| DSAS-6 | Expiration Date Detection | Domain & Certificate Monitoring | 3 |
| DSAS-7 | Expiration Threshold Check | Domain & Certificate Monitoring | 3 |
| DSAS-8 | Expiration Alerts | Alert & Escalation Management | 5 |
| DSAS-9 | Alert Notification | Alert & Escalation Management | 3 |
| DSAS-10 | Alert Escalation | Alert & Escalation Management | 5 |
| DSAS-11 | Audit Record Management | Audit & System Management | 5 |
| DSAS-12 | Domain Management | Audit & System Management | 3 |
| DSAS-13 | Secure Access | Audit & System Management | 5 |

**Total Story Points: 42**

---

## 6. Story Point Estimation

Story Points were assigned using the Fibonacci-based estimation approach.

The estimation considered:

- Complexity of the work
- Amount of work involved
- Risk
- Uncertainty

The assigned Story Points were:

- 3 points – relatively small/moderate tasks
- 5 points – larger or more complex tasks

Planning Poker was considered as the estimation technique for discussing and reaching agreement on the effort required for each User Story.

---

## 7. Backlog Prioritization

The Product Backlog was prioritized according to the importance and business value of the User Stories.

### Priority Order

1. Expiration Alerts – Highest
2. Daily SSL/TLS Audit – High
3. Daily WHOIS Audit – High
4. Expiration Date Detection – High
5. Expiration Threshold Check – High
6. Alert Notification – High
7. Alert Escalation – High
8. Audit Record Management – Medium
9. Domain Management – Medium
10. Secure Access – Medium

The backlog was reordered in Jira according to this priority.

---

## 8. Sprint 1

### Sprint Goal

> Implement core domain and SSL/TLS monitoring and expiration alert functionality.

### Duration

**1 week**

### Sprint Backlog

| User Story | Story Points |
|------------|--------------|
| Expiration Alerts | 5 |
| Daily SSL/TLS Audit | 5 |
| Daily WHOIS Audit | 5 |
| Expiration Date Detection | 3 |
| Expiration Threshold Check | 3 |
| Alert Notification | 3 |

**Sprint 1 Total: 24 Story Points**

### Sprint Progress

The stories were simulated through the Scrum workflow:

```text
To Do → In Progress → Done
