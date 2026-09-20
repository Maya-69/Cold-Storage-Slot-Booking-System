# Cold Storage Slot Booking System (CSBS)
**Enterprise Cloud-Native Logistics & Perishable Food Preservation Platform**

[![CI Build Status](https://img.shields.io/badge/build-passing-brightgreen.svg)]()
[![Java Version](https://img.shields.io/badge/java-21%2B-blue.svg)]()
[![Spring Boot](https://img.shields.io/badge/spring--boot-3.3.4-green.svg)]()
[![Database](https://img.shields.io/badge/database-Embedded%20H2-orange.svg)]()
[![DevOps Quality Gate](https://img.shields.io/badge/quality--gate-passed-success.svg)]()

---

## 1. Academic & Student Metadata
* **Student Name:** Mayuresh Sawant
* **Roll Number:** 23102A0029
* **Program & Branch:** B.E. Semester VII – Computer Engineering
* **Subject:** DevOps Lab
* **Subject In-charge / Evaluator:** Dr. Snehal Andhare
* **Assigned Project Title:** Jenkins Deployment for a Cold Storage Slot Booking System

---

## 2. Project Executive Overview
The **Cold Storage Slot Booking System (CSBS)** is a cloud-ready web application engineered to resolve acute post-harvest produce spoilage across agricultural and cold-chain supply networks. By digitizing cold chamber availability across certified temperature zones, the platform enables farmers, commodity traders, and logistics operators to make deterministic slot reservations, eliminating dockside transit delays and produce dump losses.

### Core MVP Capabilities:
1. **User / Farmer Authentication:** Account management for farmers, traders, and facility managers.
2. **Multi-Temperature Chamber Directory:** Interactive availability matrix across Deep Freeze (-18°C to -25°C), Chilled (0°C to 4°C), and Controlled Atmosphere (10°C to 15°C) zones.
3. **Slot Booking & Cost Engine:** Instant reservation flow capturing commodity type, crate quantity, and check-in / check-out dates.
4. **Lifecycle State Machine:** Enforcing transitions: `PENDING` $\rightarrow$ `CONFIRMED` $\rightarrow$ `CHECKED_IN` $\rightarrow$ `COMPLETED` / `CANCELLED`.
5. **Observability & Health Probes:** Real-time capacity KPIs and Spring Boot Actuator endpoint (`/actuator/health`).

---

## 3. Technology Stack & Prerequisites
* **Language & Framework:** Java 21+ with Spring Boot 3.3.4 (Spring MVC, Spring Data JPA, Spring Validation)
* **Build Automation:** Apache Maven 3.9.x with Maven Wrapper (`mvnw` / `mvnw.cmd`)
* **Persistence Tier:** Embedded in-memory H2 Database (`jdbc:h2:mem:coldstoragedb`)
* **Frontend UI:** Server-side Thymeleaf + Bootstrap 5.3 + Bootstrap Icons
* **Automated Testing:** Selenium WebDriver 4.25 + JUnit 5 + WebDriverManager
* **CI/CD Pipeline:** Declarative Jenkinsfile on Jenkins 2.450+
* **Containerization:** Multi-stage Dockerfile with Eclipse Temurin JRE runtime
* **Configuration Management:** Ansible inventory (`hosts.ini`) and playbook (`playbook.yml`)

---

## 4. Git Branching Policy & Contribution Standards
To maintain enterprise-grade version control integrity across sprints, all contributions must strictly conform to the following branching strategy:

### Branch Structure:
* `main`: Protected production-ready branch. Receives merged releases and tagged baselines (e.g., `v1.0.0`).
* `dev`: Primary integration branch for daily development. Feature branches are merged here via Pull Requests.
* `feature/<feature-name>`: Dedicated feature branch created from `dev` (e.g., `feature/slot-view`, `feature/booking-engine`).
* `fix/<defect-name>`: Hotfix branch addressing specific test failures or defects.

### Conventional Commit Standard:
Commit messages must follow the Conventional Commits specification:
* `feat:` A new feature or business capability (e.g., `feat(booking): add date overlap validation logic`)
* `fix:` A bug fix or defect correction (e.g., `fix(slot): prevent negative available slot counter`)
* `docs:` Documentation changes only (e.g., `docs: update README with API specifications`)
* `test:` Adding or correcting unit/Selenium tests (e.g., `test(selenium): add critical booking user journey`)
* `ci:` Changes to CI/CD pipeline scripts or configs (e.g., `ci(jenkins): add test quality gate stage`)

---

## 5. Local Setup & Execution Guide

### Prerequisites:
* JDK 21 or higher installed (`java -version`)
* Maven installed or using the bundled Maven in `maven/`

### 1. Compile and Test:
```powershell
cd cold-storage-app
mvn clean test
```

### 2. Package Executable JAR:
```powershell
mvn package -DskipTests
```

### 3. Run Locally:
```powershell
java -jar target/coldstorage-app.jar
```
Access the application on: `http://localhost:8080/`

### 4. Health Check Probe:
```powershell
curl.exe -s http://localhost:8080/actuator/health
```
Expected output:
```json
{"status":"UP","components":{"db":{"status":"UP"}}}
```

---

## 6. Project Directory Architecture
```
E:\Dev\DevOPS\
├── .github/
│   ├── ISSUE_TEMPLATE/
│   │   ├── bug_report.md
│   │   └── feature_request.md
│   └── pull_request_template.md
├── cold-storage-app/
│   ├── pom.xml
│   └── src/
│       ├── main/java/com/coldstorage/
│       │   ├── controller/
│       │   ├── model/
│       │   ├── repository/
│       │   └── service/
│       ├── main/resources/
│       │   ├── application.properties
│       │   └── templates/
│       └── test/java/com/coldstorage/
├── docs/
│   ├── DevOps_Task1_MayureshSawant_23102A0029.docx
│   ├── DevOps_Task2_MayureshSawant_23102A0029.docx
│   ├── DevOps_Task3_MayureshSawant_23102A0029.docx
│   └── prev/
├── scripts/
│   ├── doc_helper.py
│   ├── generate_task1.py
│   ├── generate_task2.py
│   └── generate_task3.py
├── templates/
│   ├── template_task1.docx
│   └── template_standard.docx
├── .gitignore
├── ASSIGNMENT.md
├── GEMINI.md
└── README.md
```
