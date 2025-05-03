@ignore
Feature: Authentication Setup - Register and Login user

  Background:
    * def baseUrl = 'http://localhost:3000'
    * url baseUrl
    * def timestamp = new Date().getTime()
    * def email = 'user_' + timestamp + '@email.com'
    * def password = 'Pass1234!'

  Scenario: Register and login a user
  # Step 1: Get application configuration
    Given path 'rest/admin/application-configuration'
    When method GET
    Then status 200

  # Step 2: Get security questions
    Given path 'api/SecurityQuestions'
    When method GET
    Then status 200
    And match response.status == 'success'
    * def securityQuestionId = response.data[0].id
    * def securityQuestionText = response.data[0].question

  # Step 3: Register a new user
    Given path 'api/Users'
    And request
    """
    {
      "email": "#(email)",
      "password": "#(password)",
      "passwordRepeat": "#(password)",
      "securityQuestion": {
        "id": #(securityQuestionId),
        "question": "#(securityQuestionText)"
      },
      "securityAnswer": "John"
    }
    """
    When method POST
    Then status 201
    And match response.status == 'success'
    * def userId = response.data.id

  # Step 4: Submit security answer
    Given path 'api/SecurityAnswers'
    And request
    """
    {
      "UserId": #(userId),
      "answer": "John",
      "SecurityQuestionId": #(securityQuestionId)
    }
    """
    When method POST
    Then status 201

  # Step 5: Login user
    Given path 'rest/user/login'
    And request
    """
    {
      "email": "#(email)",
      "password": "#(password)"
    }
    """
    When method POST
    Then status 200
    And match response.authentication.token != null
    * def authToken = response.authentication.token
    * def basketId = response.authentication.bid

    * karate.set('token', authToken)
    * karate.set('basketId', basketId)
    * karate.set('email', email)
    * karate.set('password', password)