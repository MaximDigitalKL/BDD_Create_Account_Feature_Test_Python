Feature: Check the functionality of the login page

  #-----------------------------Functional positive testing for each type of user--------------------------

  Scenario: Form Completion under Educational institute
    Given The user is a Educational institute
    When Filling in all parameters POZ "Romania", "Univerisity", "NYU","UniverityNYU02@bdd.io", "Romania +40", "729456945" in the form with valid information
    When I click the create account button
    Then Account is created, end user receives confirmation message "Check your mail"

  Scenario: Form Completion under Individual
    Given The user is an individual
    When Filling in all parameters POZ "Romania", "Petre", "Tutuca","Petre_Tutuca03@bdd.io", "Romania +40", "729456945" in the form with valid information
    When I click the create account button
    Then Account is created, end user receives confirmation message "Check your mail"

  Scenario: Form Completion under Corporation
    Given The user is a Corporation
    When Filling in all parameters POZ "Romania", "Auto", "Parts","autoparts02@bdd.io", "Romania +40", "729456945" in the form with valid information
    When I click the create account button
    Then Account is created, end user receives confirmation message "Check your mail"

  #----------------------------Functional negative testing-----------------------------------

  @Negative_Testing
  Scenario: Form completion without selecting type of account
    Given The user does not select any account type
    When Filling in all parameters NEG "Romania", "Without", "Account","withoutaccount02@bdd.io", "Romania +40", "729456945" in the form with valid information
    When I click the create account button
    Then Account is not created - Account Type user alerted of mandatory field "Please Select Account Type"

  @Negative_Testing
  Scenario: Form completion without agreeing to terms and conditions checkbox
    Given The user tries to create an account without accepting terms and conditions
    When Filling in all parameters NEG2 "Romania", "Without", "Account","withoutaccount03@bdd.io", "Romania +40", "729456945" in the form with valid information
    When I click the create account button
    Then Account is not created - Terms&conditions user alerted of mandatory field "Click OK to return and check the box that you have read and agree with our Terms of Use"

  @Negative_Testing
  Scenario: Form completion without entering the right equation result (captcha)
    Given The user tries to create an account without solving the equation (captcha)
    When Filling in all parameters NEG3 "Romania", "Without", "Account","withoutaccount04@bdd.io", "Romania +40", "729456945" in the form with valid information
    When I click the create account button
    Then Account is not created - Captcha user alerted of mandatory field "Please enter correct information!"

  #----------------------------Functional equivalence/boundary testing-----------------------------------

  Scenario: Form Completion with invalid First Name (1 character)
    Given The user tries to create an account and provides invalid First Name (1 character)
    When Filling in all parameters EQB "Romania", "A", "Popescu","AntonPopescu01@bdd.io", "Romania +40", "729456945" in the form with valid information
    When I click the create account button
    Then Account is not created - FirstName user alerted of mandatory field "Please enter correct information!"

  Scenario: Form Completion with invalid First Name (31 characters)
    Given The user tries to create an account and provides invalid First Name (31 character)
    When Filling in all parameters EQB "Romania", "AntonqwertasdfgzxcvbAntonqwerta", "Popescu","AntonPopescu05@bdd.io", "Romania +40", "729456945" in the form with valid information
    When I click the create account button
    Then Account is not created - FirstName user alerted of mandatory field "Please enter correct information!"

    Scenario: Form Completion with invalid First Name (special character)
     Given The user tries to create an account and provides invalid First Name (special character)
     When Filling in all parameters EQB "Romania", "An#on", "Popescu","AntonPopescu05@bdd.io", "Romania +40", "729456945" in the form with valid information
     When I click the create account button
     Then Account is not created - FirstName user alerted of mandatory field "Please enter correct information!"

   #-------------------------------------------Random sanity tests-----------------------------------------------------

   Scenario: Form completion with incorrect email adress format
    Given The user tries to create an account and provides invalid email address format
    When Filling in all parameters SAN "Romania", "Mary", "Stuart","Mary_Stuart%bdd.io", "Romania +40", "729456945" in the form with valid information
    When I click the create account button
    Then Account is not created - Email user alerted of mandatory field "Please enter correct information!"

   Scenario: Form completion with incorrect phone number
    Given The user tries to create an account and provides invalid phone number
    When Filling in all parameters SAN "Romania", "Mary", "Stuart","Mary_Stuart01@bdd.io", "Romania +40", "12365478965422566345678976567890876546789334565666" in the form with valid information
    When I click the create account button
    Then Account is not created - Phone user alerted of mandatory field "Please enter correct information!"

   Scenario: Form completion with country and Country ID not matching
    Given The user tries to create an account and provides invalid country country-id combination
    When Filling in all parameters SAN "Romania", "Mary", "Stuart","Mary_Stuart04@bdd.io", "Angola +244", "729456945" in the form with valid information
    When I click the create account button
    Then Account is not created - C_ID user alerted of mandatory field "Please enter correct information!"