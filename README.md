# Software Engineering Lab

## Domain & SSL Certificate Expiry Alert System

**SRN:** PES1UG24AM221

This repository contains the work completed for the Software Engineering Laboratory, including requirements engineering, Agile planning, architectural modelling, database design, and static code analysis.

---

## Lab 01 – Requirements Engineering & UML Use-Case Modelling

This lab focused on identifying functional and non-functional requirements for the **Domain & SSL Certificate Expiry Alert System**. System actors, use cases, and UML use-case diagrams were created to represent system interactions and document the main and alternate use-case flows.

### Topics Covered

- Functional and Non-Functional Requirements
- Requirements Specification
- Actors and Use Cases
- UML Use-Case Diagrams
- `<<include>>` and `<<extend>>` Relationships
- Use-Case Flows

---

## Lab 02 – Agile Backlog Creation & Sprint Simulation

This lab focused on applying **Agile Scrum practices using Jira**. Requirements were converted into Epics and User Stories, prioritized in a Product Backlog, estimated using Fibonacci-based Story Points, and organized into two mock sprints. Sprint progress was tracked using workflows and Burndown Charts.

### Topics Covered

- Agile Scrum and Jira
- Epics and User Stories
- Product Backlog and Prioritization
- Story Point Estimation
- Sprint Planning and Execution
- Workflow Management
- Burndown Charts

### Sprint Summary

| Sprint | Stories | Story Points | Status |
|---|---:|---:|---|
| Sprint 1 | 6 | 24 | Completed |
| Sprint 2 | 4 | 18 | Completed |
| **Total** | **10** | **42** | **Completed** |

---

## Lab 03 – Component Modelling & Architectural Pattern Selection

This lab focused on comparing Layered, Microservices, and Client-Server architectures for the **Domain & SSL Certificate Expiry Alert System**. Microservices Architecture was selected to support modularity, independent monitoring services, scalability, and fault isolation. A UML component diagram was created to represent the system's components, interfaces, and dependencies.

### Topics Covered

- Architectural Style Evaluation
- Microservices Architecture
- UML Component Diagrams
- Components and Interfaces
- Dependencies and Data Flow
- Security and Performance Considerations

---

## Lab 04 – Database Design and Implementation

This lab focused on designing and implementing a database by identifying entities, attributes, relationships, and constraints. An ER diagram was developed to represent the data model, followed by relational database design and implementation using tables, keys, and SQL queries.

### Topics Covered

- Database Requirements
- Entity-Relationship Modelling
- ER Diagrams
- Relational Database Design
- Primary and Foreign Keys
- SQL Table Creation and Queries
- Data Integrity and Constraints

---

## Lab 05 – Static Code Analysis

This lab focused on improving the quality, security, and maintainability of the **Vehicle Service Management System** Python program. Pylint, Bandit, and Flake8 were used to identify code-quality issues, potentially insecure coding practices, and formatting violations. Corrections were made and verified through before-and-after reports.

### Topics Covered

- Static Code Analysis
- Pylint Code Quality Checks
- Bandit Security Analysis
- Flake8 Style Checks
- Code Refactoring and Issue Documentation
- Before-and-After Reports
- Git Version Control and Commits

### Analysis Summary

| Tool | Purpose | Final Result |
|---|---|---|
| Pylint | Code quality | 10.00/10 |
| Bandit | Security analysis | No issues identified |
| Flake8 | Code style and formatting | To be verified |

---
### Lab 6 – Code and Branch Coverage Analysis

This lab focused on analysing code coverage and branch coverage for a Password Policy Checker application using Python's `pytest` and `coverage.py` tools. Test cases were developed to cover password length validation, common passwords, character-type requirements, password strength evaluation, and password fix suggestions. Separate test suites were created for code coverage and branch coverage, achieving 100% code coverage and evaluating branch coverage against the required 90% target.

**Topics Covered:**
- Code Coverage Analysis
- Branch Coverage Analysis
- Automated Testing using Pytest
- Coverage Measurement using Coverage.py
- Test Case Design and Execution
- Testing Conditional Statements and Branches
