# MultiTool Testing Project

A multi-tool testing project targeting the **OWASP Juice Shop** — a deliberately vulnerable web application designed for security and QA practice.

---

## Target Application

**OWASP Juice Shop** — an intentionally insecure web application that covers a wide range of vulnerabilities found in modern applications. Used here as a safe and legal target for test automation practice.

- Docker image: `bkimminich/juice-shop`
- Default port: `3000`
- Repository: https://github.com/juice-shop/juice-shop

---

## Tools

| Tool       | Purpose                                          |
|------------|--------------------------------------------------|
| **Postman  | Functional API tests — happy path flows          |
| **Karate** | API tests — validation & negative path scenarios |
| **JMeter** | Performance & load testing                       |

---

## Project Structure

```
├── Postman/
│   ├── juice-shop-collection.json   # Postman test collection
│   └── postman-env.json             # Environment variables
│
├── Karate/
│   └── src/test/java/
│       ├── features/
│       │   ├── e2e.feature          # End-to-end happy path scenarios
│       │   └── validation-tests.feature  # Negative & validation scenarios
│       ├── setup/
│       │   └── authentication.feature   # Login setup (reused across tests)
│       └── testData/
│           └── userData.json        # Test data
│
├── JMeter/
│   ├── performance_test.jmx         # JMeter test plan
│   ├── test_data/                   # Input data for performance tests
│   ├── test_results/                # Generated reports
│   └── monitoring/                  # Grafana + Telegraf config for dashboards
│
├── TEST_CASES.md                    # Full test case specification
└── .github/workflows/               # GitHub Actions CI pipelines
```

---

## Test Cases

All test cases are documented in [`TEST_CASES.md`](TEST_CASES.md), organized by feature and covering three scenario types:

- ✅ **Happy Path** — expected successful flows
- ❌ **Negative** — invalid inputs, missing auth, non-existent resources
- 🔍 **Validation** — field-level validation rules (types, formats, required fields)

---

## Running Tests Locally

### Prerequisites
- Docker
- Java 17+ (Karate)
- Maven (Karate)
- Node.js + Newman (Postman)
- JMeter (performance tests)

### 1. Start OWASP Juice Shop

```bash
docker run -d -p 3000:3000 bkimminich/juice-shop
```

### 2. Run Postman tests

```bash
npm install -g newman newman-reporter-htmlextra
newman run Postman/juice-shop-collection.json \
  --environment Postman/postman-env.json \
  --reporters cli,htmlextra \
  --reporter-htmlextra-export report.html
```

### 3. Run Karate tests

```bash
cd Karate
mvn test -Dkarate.env=local
```

### 4. Run JMeter tests

```bash
jmeter -n -t JMeter/performance_test.jmx \
  -Jhost=localhost -Jport=3000 \
  -l JMeter/test_results/results.csv \
  -e -o JMeter/test_results/reports/
```

---

## CI/CD

Tests are automated via **GitHub Actions** and triggered manually (`workflow_dispatch`):

| Workflow      | File                                 |
|---------------|--------------------------------------|
| Postman tests | `.github/workflows/postman-tests.yml`|
| Karate tests  | `.github/workflows/karate-tests.yml` |
| JMeter tests  | `.github/workflows/jmeter-tests.yml` |

HTML reports are uploaded as artifacts after each run.

## About Me

I am a Test Engineer expanding my skills in test automation.   
Feel free to explore and reach out if you have any questions.