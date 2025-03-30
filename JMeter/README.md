# Juice Shop – Performance Test Plan (JMeter)

This repository contains a JMeter test plan for simulating end-to-end user interactions with the OWASP Juice Shop web application under load.

## 🔧 Requirements

- [Apache JMeter](https://jmeter.apache.org/) 5.5 or later
- Java 8+
- (Optional) JMeter Plugin Manager
- Tested with Juice Shop running on `localhost:3000`

## 🚀 How to Run the Test

### GUI mode

1. Open Apache JMeter.
2. Load `test_plan.jmx`.
3. Adjust variables in the top-level "User Defined Variables" if needed:
   - `users`, `ramp_up`, `duration`, etc.
4. Click **Start** to run the test.

### CLI mode

```bash
jmeter -n -t test_plan.jmx -l results/test_results.jtl -e -o results/report
```

This will generate a full HTML report in the `results/report/` directory.

## 🔍 What the Test Does

The test simulates real user behavior, including:

1. **Registration** – creates new users using data from `users.csv`.
2. **Login** – logs in with valid credentials.
3. **Browse and add product** – searches products and adds random ones to the basket.
4. **Basket operations** – opens, modifies, deletes items from basket.
5. **Checkout** – performs a full checkout flow.
6. **Delivery and payment** – selects delivery method and adds a card.
7. **Order confirmation** – confirms and tracks the order.
8. **Profile (optional)** – accesses user profile and uploads an image.
9. **Logout**

➡️ See [test-scenario.md](./test-scenario.md) for a detailed step-by-step description.

## 📈 Results & Reports

- Run results are stored in the `results/` directory.
- Use JMeter's built-in or third-party listeners (e.g., Aggregate Report, Summary Report).
- Optional integration with Grafana, InfluxDB, or Jenkins pipelines.

## 🧠 Tips

- Use `-Jusers=50` or `-Jduration=300` to override default parameters.
- Use the "Switch Controller" to execute OS-dependent commands based on `system` variable.
- All headers (e.g., `Authorization`, `Origin`) are dynamically set.

## 👤 Author

Created by Patryk Szwed – QA Engineer
