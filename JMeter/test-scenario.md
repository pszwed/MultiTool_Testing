
# Test Scenario Description – JMeter

## Purpose
This test simulates a typical user journey through a web application — from registration to placing an order and logging out. It helps evaluate the application's performance and stability under load.

---

## Test Flow Summary

### 1. **User Registration**
- User credentials are loaded from a CSV file.
- A registration request is sent with a security question.
- The user ID is extracted from the response.

### 2. **User Login**
- User logs in using email and password.
- An authorization token is extracted and stored for future requests.

### 3. **Add Random Product to Basket**
- A random product is selected from the available products.
- It is then added to the shopping basket.

### 4. **Open Basket**
- The basket contents and related product info are retrieved.

### 5. **Delete Product from Basket**
- A random product from the basket is selected and removed.

### 6. **Checkout Process**
- A delivery address is created.
- A delivery method is selected.
- Payment card details are submitted.
- The order is placed and an order confirmation ID is saved.

### 7. **Track Order**
- The order status is checked using the confirmation ID.

### 8. **User Profile & Avatar Upload (optional)**
- The profile page is opened.
- A profile image is uploaded to the server.

### 9. **Logout**
- The user logs out and their IP address is logged.

---

## Test Configuration

| Parameter        | Default Value   | Description                                  |
|------------------|------------------|----------------------------------------------|
| Users            | 100              | Number of concurrent users                   |
| Ramp-up          | 60 seconds       | Time to start all threads                    |
| Duration         | 300 seconds      | How long the test runs                       |
| Think Time       | 1000 ms          | Pause between user actions                   |
| System Switch    | Windows/Linux    | Determines which OS command sampler to run   |

---

## Other Features
- Uses dynamic data and tokens (e.g. user ID, product ID, authorization).
- User credentials are provided via CSV file for user variability.
- Can be integrated into CI/CD pipelines.
- OS-dependent logic to simulate local command execution.

---

## Notes
You can run the test via JMeter GUI or CLI:
```sh
jmeter -n -t test_plan.jmx -l results/test_results.jtl
```

---
