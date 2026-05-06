# Test Cases — OWASP Juice Shop API

**Target application:** OWASP Juice Shop  
**Tools:** Postman, Karate  

---

## TC01 — Registration

| ID          | Title                                | Preconditions           | Test Steps                                  | Expected Result                       | 
|-------------|--------------------------------------|-------------------------|---------------------------------------------|---------------------------------------|
| TC01-HP-01  | Register new user with valid data    | App running             | POST /api/Users with valid data             | 201, userId returned                  | 
| TC01-HP-02  | Fetch security questions list        | App running             | GET /api/SecurityQuestions                  | 200, non-empty list                   | 
| TC01-HP-03  | Fetch app configuration              | App running             | GET /rest/admin/application-configuration   | 200, config.application.domain exists | 
| TC01-NEG-01 | Register with already existing email | User already registered | POST /api/Users with duplicate email        | 409, duplicate error                  | 
| TC01-NEG-02 | Register without email field         | App running             | POST /api/Users — omit email                | 400                                   | 
| TC01-NEG-03 | Register without password field      | App running             | POST /api/Users — omit password             | 400                                   | 
| TC01-VAL-01 | Register with wrong passwordRepeat   | App running             | POST /api/Users with mismatched passwords   | 400, password mismatch error          | 
| TC01-VAL-02 | Register with invalid email format   | App running             | POST /api/Users with email='notanemail'     | 400                                   | 
| TC01-VAL-03 | Register with empty string as email  | App running             | POST /api/Users with email=''               | 400                                   | 

---

## TC02 — Login

| ID          | Title                        | Preconditions   | Test Steps                                                    | Expected Result                    | 
|-------------|------------------------------|-----------------|---------------------------------------------------------------|------------------------------------|
| TC02-HP-01  | Login with valid credentials | User registered | POST /rest/user/login with correct email and password         | 200, token and basketId returned   | 
| TC02-NEG-01 | Login with wrong password    | User registered | POST /rest/user/login with correct email, wrong password      | 401, "Invalid email or password."  | 
| TC02-NEG-02 | Login with wrong email       | User registered | POST /rest/user/login with wrong email, correct password      | 401, "Invalid email or password."  | 
| TC02-NEG-03 | Login without password field | User registered | POST /rest/user/login — omit password                         | 400/401                            | 
| TC02-NEG-04 | Login without email field    | User registered | POST /rest/user/login — omit email                            | 400/401                            | 
| TC02-VAL-01 | Login with empty body        | App running     | POST /rest/user/login with empty JSON {}                      | 400/401                            | 

---

## TC03 — Add Product to Basket

| ID          | Title                              | Preconditions                  | Test Steps                                           | Expected Result          | 
|-------------|------------------------------------|--------------------------------|------------------------------------------------------|--------------------------|
| TC03-HP-01  | Add existing product to basket     | User logged in                 | POST /api/BasketItems with valid data                | 200, item added          | 
| TC03-HP-02  | Add second product to basket       | User logged in, item in basket | POST /api/BasketItems with different ProductId       | 200                      | 
| TC03-NEG-01 | Add sold-out product               | User logged in                 | POST /api/BasketItems with   sold-out item (38)      | 400, proper message      | 
| TC03-NEG-02 | Add more than allowed quantity     | User logged in                 | POST /api/BasketItems with quantity > limit (PId=33) | 400, proper message      | 
| TC03-NEG-03 | Add product without auth token     | App running                    | POST /api/BasketItems without Authorization header   | 401                      | 
| TC03-NEG-04 | Add non-existent product           | User logged in                 | POST /api/BasketItems with ProductId=99999           | 400/404                  | 
| TC03-VAL-01 | Add product with negative quantity | User logged in                 | POST /api/BasketItems with quantity=-1               | 400                      | 
| TC03-VAL-02 | Add product with quantity = 0      | User logged in                 | POST /api/BasketItems with quantity=0                | 400                      | 
| TC03-VAL-03 | Add product without quantity field | User logged in                 | POST /api/BasketItems — omit quantity                | 400                      | 

---

## TC04 — View Basket

| ID          | Title                          | Preconditions                   | Test Steps                                         | Expected Result               | 
|-------------|--------------------------------|---------------------------------|----------------------------------------------------|-------------------------------|
| TC04-HP-01  | Get basket with products       | User logged in, items in basket | GET /rest/basket/{basketId}                        | 200, products list non-empty  | 
| TC04-HP-02  | Verify logged-in user identity | User logged in                  | GET /rest/user/whoami                         | 200, email matches registered user | 
| TC04-NEG-01 | Get basket without auth token  | App running                     | GET /rest/basket/{basketId} without Author. header | 401                           | 
| TC04-NEG-02 | Get basket of another user     | Two users registered            | GET /rest/basket/{otherUserBasketId}               | 401/403                       | 
| TC04-NEG-03 | Get non-existent basket        | User logged in                  | GET /rest/basket/99999                             | 404                           | 

---

## TC05 — Delete Item from Basket

| ID          | Title                            | Preconditions                   | Test Steps                                                | Expected Result     | 
|-------------|----------------------------------|---------------------------------|-----------------------------------------------------------|---------------------|
| TC05-HP-01  | Delete existing basket item      | User logged in, item in basket  | DELETE /api/BasketItems/{basketItemId}                    | 200, status success | 
| TC05-NEG-01 | Delete item without auth token   | App running                     | DELETE /api/BasketItems/{id} without Authorization header | 401                 | 
| TC05-NEG-02 | Delete non-existent basket item  | User logged in                  | DELETE /api/BasketItems/99999                             | 404                 | 
| TC05-VAL-01 | Delete item with invalid ID type | User logged in                  | DELETE /api/BasketItems/abc                               | 400                 | 

---

## TC06 — Delivery Address

| ID          | Title                                | Preconditions  | Test Steps                                      | Expected Result        | 
|-------------|--------------------------------------|----------------|-------------------------------------------------|------------------------|
| TC06-HP-01  | Add valid delivery address           | User logged in | POST /api/Addresss with all required fields     | 201, addressId returned| 
| TC06-NEG-01 | Add address without auth token       | App running    | POST /api/Addresss without Authorization header | 401                    | 
| TC06-VAL-01 | Add address without country field    | User logged in | POST /api/Addresss — omit country               | 400                    | 
| TC06-VAL-02 | Add address without fullName field   | User logged in | POST /api/Addresss — omit fullName              | 400                    | 
| TC06-VAL-03 | Add address without zipCode field    | User logged in | POST /api/Addresss — omit zipCode               | 400                    | 
| TC06-VAL-04 | Add address with mobileNum as string | User logged in | POST /api/Addresss with mobileNum='abc'         | 400                    | 

---

## TC07 — Delivery Methods

| ID          | Title                                   | Preconditions  | Test Steps                                      | Expected Result     | 
|-------------|-----------------------------------------|----------------|-------------------------------------------------|---------------------|
| TC07-HP-01  | Get available delivery methods          | User logged in | GET /api/Deliverys                              | 200, non-empty list | 
| TC07-NEG-01 | Get delivery methods without auth token | App running    | GET /api/Deliverys without Authorization header | 401                 | 

---

## TC08 — Payment / Cards

| ID          | Title                           | Preconditions              | Test Steps                                   | Expected Result                  | 
|-------------|---------------------------------|----------------------------|----------------------------------------------|----------------------------------|
| TC08-HP-01  | Add valid payment card          | User logged in             | POST /api/Cards with valid card data         | 201, paymentId returned          | 
| TC08-HP-02  | Get user's card list            | User logged in, card added | GET /api/Cards                               | 200, list contains added card    | 
| TC08-NEG-01 | Add card without auth token     | App running                | POST /api/Cards without Authorization header | 401                              | 
| TC08-VAL-01 | Add card with cardNum as string | User logged in             | POST /api/Cards with cardNum='Momomomo'      | 400, validation error on cardNum | 
| TC08-VAL-02 | Add card with expired year      | User logged in             | POST /api/Cards with expYear='2000'          | 400                              | 
| TC08-VAL-03 | Add card without cardNum field  | User logged in             | POST /api/Cards — omit cardNum               | 400                              | 
| TC08-VAL-04 | Add card without fullName field | User logged in             | POST /api/Cards — omit fullName              | 400                              | 

--- address and card added

## TC09 — Place Order

| ID          | Title                                   | Preconditions                      | Test Steps                                               | Expected Result  | 
|-------------|-----------------------------------------|------------------------------------|----------------------------------------------------------|------------------|
| TC09-HP-01  | Place order with valid data             | User logged in, basket non-empty,  | POST /rest/basket/{bid}/checkout with valid orderDetails | 200,             | 
| TC09-HP-02  | Track placed order                      | Order placed                       | GET /rest/track-order/{orderConfirmation}                | 200,             | 
| TC09-NEG-01 | Place order without auth token          | App running                        | POST /rest/basket/{bid}/checkout without Author. header  | 401              | 
| TC09-NEG-02 | Place order with empty basket           | User logged in, empty basket       | POST /rest/basket/{bid}/checkout                         | 400              | 
| TC09-NEG-03 | Track non-existent order                | User logged in                     | GET /rest/track-order/INVALID123                         | 404              | 
| TC09-VAL-01 | Place order with non-existent addressId | User logged in                     | POST checkout with addressId=99999                       | 400              | 
| TC09-VAL-02 | Place order with non-existent paymentId | User logged in                     | POST checkout with paymentId=99999                       | 400              | 

---

## TC10 — User Profile

| ID          | Title                              | Preconditions  | Test Steps                               | Expected Result  | 
|-------------|------------------------------------|----------------|------------------------------------------|------------------|
| TC10-HP-01  | Get profile page of logged-in user | User logged in | GET /profile with cookie token           | 200              | 
| TC10-HP-02  | Upload profile picture             | User logged in | POST /profile/image/file with image file | 200              | 
| TC10-NEG-01 | Get profile without auth token     | App running    | GET /profile without token cookie        | 401/302 redirect | 

---

## TC11 — Logout

| ID          | Title                     | Preconditions  | Test Steps                                         | Expected Result | 
|-------------|---------------------------|----------------|----------------------------------------------------|-----------------|
| TC11-HP-01  | Logout logged-in user     | User logged in | GET /rest/saveLoginIp with valid token             | 200             | 
| TC11-NEG-01 | Logout without auth token | App running    | GET /rest/saveLoginIp without Authorization header | 401             | 

---