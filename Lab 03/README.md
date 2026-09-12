# Lab 3 – Component Modelling & Architectural Pattern Selection

## Domain & SSL Certificate Expiry Alert System

**Student ID:** PES1UG24AM221  
**Lab:** Software Engineering – Lab 3  
**Topic:** Component Modelling & Architectural Pattern Selection

---

## 1. Objective

The objective of this lab is to evaluate different architectural styles, select the most appropriate architecture for the given system, and create a UML Component Diagram showing the major components, interfaces, dependencies, and interactions.

For this lab, the selected system is the **Domain & SSL Certificate Expiry Alert System**.

---

## 2. System Scenario

The Domain & SSL Certificate Expiry Alert System is designed to monitor registered domains and their SSL/TLS certificates.

The system performs regular audits to identify upcoming domain and certificate expirations and generates alerts when an expiration is approaching.

The system also maintains audit records and allows administrators or security officers to manage monitored domains and view monitoring results.

### Main Functions

- Monitor registered domains.
- Perform WHOIS audits.
- Perform SSL/TLS certificate audits.
- Detect domain and certificate expiration dates.
- Check expiration against a defined threshold.
- Generate expiration alerts.
- Notify responsible users.
- Maintain alert and audit records.
- Allow administrators to manage monitored domains.
- Provide secure access to the system.

---

## 3. Architectural Styles Considered

Three architectural styles were considered for the system.

### 3.1 Layered Architecture

Layered Architecture organizes the system into separate layers such as presentation, business logic, and data.

**Advantages:**
- Clear separation of concerns.
- Easy to understand and maintain.
- Suitable for traditional applications.

**Disadvantages:**
- Can introduce performance overhead.
- Components can become tightly coupled through layers.
- Individual monitoring functions are more difficult to scale independently.

---

### 3.2 Microservices Architecture

Microservices Architecture divides the system into smaller, independently deployable services.

**Advantages:**
- Individual services can be scaled independently.
- Provides fault isolation.
- Services can be developed and deployed independently.
- Suitable for separating WHOIS, SSL/TLS, expiry detection, and alert functions.

**Disadvantages:**
- More operational complexity.
- Communication between services can introduce network latency.
- Data consistency can be more difficult to manage.

---

### 3.3 Client-Server Architecture

Client-Server Architecture uses a centralized server that provides services to one or more clients.

**Advantages:**
- Centralized control.
- Simple deployment.
- Easier centralized data management.

**Disadvantages:**
- The server can become a bottleneck.
- The centralized server can become a single point of failure.
- Limited fault tolerance.

---

## 4. Selected Architecture

### Microservices Architecture

**Microservices Architecture** was selected for the Domain & SSL Certificate Expiry Alert System.

The system contains several independent functions that can naturally be separated into services. WHOIS auditing, SSL/TLS auditing, expiry detection, and alert management can operate independently.

This architecture also supports scalability and fault isolation as the number of monitored domains increases.

---

## 5. Major Components

The UML Component Diagram contains the following six major components:

### 1. Web Application (Admin Portal)

Provides the interface through which administrators and security officers can manage domains, view audit results, and view alerts.

### 2. Domain Monitoring Manager

Coordinates monitoring activities and manages domain-related operations.

### 3. WHOIS Audit Service

Performs WHOIS audits and retrieves domain registration and expiration information.

### 4. SSL/TLS Audit Service

Checks SSL/TLS certificates and retrieves certificate expiration information.

### 5. Expiry Detection & Alert Service

Analyses audit results, checks expiration thresholds, and generates alerts.

### 6. Audit Database

Stores domain information, audit information, alerts, and audit history.

---

## 6. Interfaces

The component diagram contains four major interfaces.

| Interface | Connected Components | Purpose |
|---|---|---|
| Domain Management API | Web Application ↔ Domain Monitoring Manager | Domain management operations |
| WHOIS Audit API | Domain Monitoring Manager ↔ WHOIS Audit Service | Request WHOIS audit operations |
| SSL/TLS Audit API | Domain Monitoring Manager ↔ SSL/TLS Audit Service | Request certificate audits |
| Alert API | Expiry Detection & Alert Service ↔ Web Application | Provide expiry alert information |

---

## 7. Data Flow

The major data flows in the system are:

```text
Web Application
       |
       | Domain Management API
       v
Domain Monitoring Manager
       |
       +----------------------+
       |                      |
       | WHOIS Audit API      | SSL/TLS Audit API
       v                      v
WHOIS Audit Service      SSL/TLS Audit Service
       |                      |
       | WHOIS Results        | Certificate Results
       +----------+-----------+
                  |
                  v
       Expiry Detection &
          Alert Service
                  |
                  +--------------------+
                  |                    |
                  v                    v
            Web Application      Audit Database
