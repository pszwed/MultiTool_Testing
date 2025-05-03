Feature: Full E2E flow

  Background:
    * url baseUrl
    * def userData = read('classpath:testData/userData.json')

  Scenario: Full end-to-end user flow

  # TC03 - Add product to basket
    Given path 'api/BasketItems'
    And request
    """
    {
      ProductId: 1,
      BasketId: #(basketId),
      quantity: 2
    }
    """
    When method POST
    Then status 200

  # TC04 - View basket
    Given path 'rest/basket/' + basketId
    When method GET
    Then status 200
    And match response.data.Products[0].name == 'Apple Juice (1000ml)'
    And match response.data.Products[0].BasketItem.quantity == 2
    And assert response.data.Products.length > 0
    And match response.data.id == basketId
    * def basketItemId = response.data.Products[0].BasketItem.id

  # TC05 - Delete item
    Given path 'api/BasketItems/' + basketItemId
    When method DELETE
    Then status 200
    And match response ==
    """
    {
      status: 'success',
      data: '#object'
    }
    """

  # TC06 - Checkout (Address)
    Given path '/api/Addresss'
    And request userData.requestAddress
    When method POST
    Then status 201
    * def addressId = response.data.id

  # TC07 - Delivery
    Given path 'api/Deliverys'
    When method GET
    Then status 200

  # TC08 - Payment
    Given path 'api/Cards'
    And request userData.requestCard
    When method POST
    Then status 201
    * def paymentId = response.data.id

    Given path 'api/Cards'
    When method GET
    Then status 200

  # TC09 - Order
    Given path '/rest/basket/' + basketId + '/checkout'
    And request
    """
    {
      "couponData": "bnVsbA==",
      "orderDetails": {
        "paymentId": #(paymentId),
        "addressId": #(addressId),
        "deliveryMethodId": "1"
      }
    }
    """
    When method POST
    Then status 200
    * def orderConfirmation = response.orderConfirmation

    Given path '/rest/track-order/' + orderConfirmation
    When method GET
    Then status 200
    And match response.data[0].addressId == addressId
    And match response.data[0].paymentId == paymentId

  # TC10 - Logout
    Given path '/rest/saveLoginIp'
    When method GET
    Then status 200
    And match response.email == email