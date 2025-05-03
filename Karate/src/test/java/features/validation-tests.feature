Feature: Validation tests

  Background:
    * url baseUrl
    * def userData = read('classpath:testData/userData.json')
    * def validEmail = email
    * def validPassword = password

  Scenario Outline: Login with wrong email or password
    Given path 'rest/user/login'
    And request
    """
    {
      "email": <email>,
      "password": <password>
    }
    """
    When method POST
    Then status 401
    And match response == <response>

    Examples:
    | email         | password         | response                     |
    | 'wrongEmail'  | #(validPassword) | 'Invalid email or password.' |
    | #(validEmail) | "wrongPassword"  | 'Invalid email or password.' |


  Scenario: Add to basket sold out product
    Given path 'api/BasketItems'
    And request
    """
    {
      ProductId: 38,
      BasketId: #(basketId),
      quantity: 1
    }
    """
    When method POST
    Then status 400
    And match response.error == 'We are out of stock! Sorry for the inconvenience.'

  Scenario: Add more items than allowed for a product
    Given path 'api/BasketItems'
    And request
    """
    {
      ProductId: 33,
      BasketId: #(basketId),
      quantity: 4
    }
    """
    When method POST
    Then status 400
    And match response.error == 'You can order only up to 1 items of this product.'

  Scenario: Invalid card number type
    Given path 'api/Cards'
    * userData.requestCard.cardNum = 'Momomomo'
    And request userData.requestCard
    When method POST
    Then status 400
    And match response ==
    """
    {
        "message": "Validation error: Validation isInt on cardNum failed",
        "errors": [
            {
                "field": "cardNum",
                "message": "Validation isInt on cardNum failed"
            }
        ]
    }
    """