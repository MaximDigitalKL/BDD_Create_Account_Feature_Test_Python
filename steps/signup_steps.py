from behave import *

@given("The user is a Educational institute")
def step_impl(context):
    context.signup_page.navigate_to_signup_page()
    context.base_page_object.accept_cookies()
    context.signup_page.select_education_button()

@given("The user is an individual")
def step_impl(context):
    context.signup_page.navigate_to_signup_page()
    context.base_page_object.accept_cookies()
    context.signup_page.select_individual_button()

@given("The user is a Corporation")
def step_impl(context):
    context.signup_page.navigate_to_signup_page()
    context.base_page_object.accept_cookies()
    context.signup_page.select_corporation_button()

@given("The user does not select any account type")
def step_impl(context):
    context.signup_page.navigate_to_signup_page()
    context.base_page_object.accept_cookies()

@given("The user tries to create an account without accepting terms and conditions")
def step_impl(context):
    context.signup_page.navigate_to_signup_page()
    context.base_page_object.accept_cookies()
    context.signup_page.select_individual_button()

@given("The user tries to create an account without solving the equation (captcha)")
def step_impl(context):
    context.signup_page.navigate_to_signup_page()
    context.base_page_object.accept_cookies()
    context.signup_page.select_individual_button()

@given("The user tries to create an account and provides invalid First Name (1 character)")
def step_impl(context):
    context.signup_page.navigate_to_signup_page()
    context.base_page_object.accept_cookies()
    context.signup_page.select_individual_button()

@given("The user tries to create an account and provides invalid First Name (31 character)")
def step_impl(context):
    context.signup_page.navigate_to_signup_page()
    context.base_page_object.accept_cookies()
    context.signup_page.select_individual_button()

@given("The user tries to create an account and provides invalid First Name (special character)")
def step_impl(context):
    context.signup_page.navigate_to_signup_page()
    context.base_page_object.accept_cookies()
    context.signup_page.select_individual_button()

@given("The user tries to create an account and provides invalid email address format")
def step_impl(context):
    context.signup_page.navigate_to_signup_page()
    context.base_page_object.accept_cookies()
    context.signup_page.select_individual_button()

@given("The user tries to create an account and provides invalid phone number")
def step_impl(context):
    context.signup_page.navigate_to_signup_page()
    context.base_page_object.accept_cookies()
    context.signup_page.select_individual_button()

@given("The user tries to create an account and provides invalid country country-id combination")
def step_impl(context):
    context.signup_page.navigate_to_signup_page()
    context.base_page_object.accept_cookies()
    context.signup_page.select_individual_button()


@when('Filling in all parameters POZ "{country}", "{FirstName}", "{LastName}","{email}", "{phone_id}", "{phone}" in the form with valid information')
def step_impl(context, country, FirstName, LastName, email, phone_id, phone):
    context.signup_page.drop_down_country(country)
    context.signup_page.insert_FirstName(FirstName)
    context.signup_page.insert_LastName(LastName)
    context.signup_page.insert_email(email)
    context.signup_page.drop_down_prefix(phone_id)
    context.signup_page.insert_phone(phone)
    context.signup_page.select_terms_of_use()
    context.signup_page.select_news_letter()
    context.signup_page.calculate_captcha()



@when('Filling in all parameters NEG "{country}", "{FirstName}", "{LastName}","{email}", "{phone_id}", "{phone}" in the form with valid information')
def step_impl(context, country, FirstName, LastName, email, phone_id, phone):
    context.signup_page.drop_down_country(country)
    context.signup_page.insert_FirstName(FirstName)
    context.signup_page.insert_LastName(LastName)
    context.signup_page.insert_email(email)
    context.signup_page.drop_down_prefix(phone_id)
    context.signup_page.insert_phone(phone)
    context.signup_page.select_terms_of_use()  #- comment line for second scenario in Negative Testing batch
    context.signup_page.select_news_letter()
    context.signup_page.calculate_captcha()    #- comment line for third scenario in Negative Testing batch

@when('Filling in all parameters NEG2 "{country}", "{FirstName}", "{LastName}","{email}", "{phone_id}", "{phone}" in the form with valid information')
def step_impl(context, country, FirstName, LastName, email, phone_id, phone):
    context.signup_page.drop_down_country(country)
    context.signup_page.insert_FirstName(FirstName)
    context.signup_page.insert_LastName(LastName)
    context.signup_page.insert_email(email)
    context.signup_page.drop_down_prefix(phone_id)
    context.signup_page.insert_phone(phone)
    context.signup_page.select_news_letter()
    context.signup_page.calculate_captcha()

@when('Filling in all parameters NEG3 "{country}", "{FirstName}", "{LastName}","{email}", "{phone_id}", "{phone}" in the form with valid information')
def step_impl(context, country, FirstName, LastName, email, phone_id, phone):
    context.signup_page.drop_down_country(country)
    context.signup_page.insert_FirstName(FirstName)
    context.signup_page.insert_LastName(LastName)
    context.signup_page.insert_email(email)
    context.signup_page.drop_down_prefix(phone_id)
    context.signup_page.insert_phone(phone)
    context.signup_page.select_terms_of_use()
    context.signup_page.select_news_letter()

@when('Filling in all parameters EQB "{country}", "{FirstName}", "{LastName}","{email}", "{phone_id}", "{phone}" in the form with valid information')
def step_impl(context, country, FirstName, LastName, email, phone_id, phone):
    context.signup_page.drop_down_country(country)
    context.signup_page.insert_FirstName(FirstName)
    context.signup_page.insert_LastName(LastName)
    context.signup_page.insert_email(email)
    context.signup_page.drop_down_prefix(phone_id)
    context.signup_page.insert_phone(phone)
    context.signup_page.select_terms_of_use()
    context.signup_page.select_news_letter()
    context.signup_page.calculate_captcha()

@when('Filling in all parameters SAN "{country}", "{FirstName}", "{LastName}","{email}", "{phone_id}", "{phone}" in the form with valid information')
def step_impl(context, country, FirstName, LastName, email, phone_id, phone):
    context.signup_page.drop_down_country(country)
    context.signup_page.insert_FirstName(FirstName)
    context.signup_page.insert_LastName(LastName)
    context.signup_page.insert_email(email)
    context.signup_page.drop_down_prefix(phone_id)
    context.signup_page.insert_phone(phone)
    context.signup_page.select_terms_of_use()
    context.signup_page.select_news_letter()
    context.signup_page.calculate_captcha()

@when('I click the create account button')
def step_impl(context):
    context.signup_page.select_create_account()

@then('Account is created, end user receives confirmation message "{expected_message}"')
def step_impl(context,expected_message):
        context.base_page_object.accept_cookies()
        context.confirmation_page.check_successful_account_creation(expected_message)

@then('Account is not created - Account Type user alerted of mandatory field "{error_message}"')
def step_impl(context, error_message):
    context.signup_page.check_account_type_error(error_message)

@then('Account is not created - Terms&conditions user alerted of mandatory field "{error_message}"')
def step_impl(context, error_message):
    context.signup_page.check_terms_and_conditions_error(error_message)

@then('Account is not created - Captcha user alerted of mandatory field "{error_message}"')
def step_impl(context, error_message):
    context.signup_page.check_captch_error(error_message)

@then('Account is not created - FirstName user alerted of mandatory field "{error_message}"')
def step_impl(context, error_message):
    context.signup_page.check_first_name_error(error_message)

@then('Account is not created - Email user alerted of mandatory field "{error_message}"')
def step_impl(context, error_message):
    context.signup_page.check_email_address_error(error_message)

@then('Account is not created - Phone user alerted of mandatory field "{error_message}"')
def step_impl(context, error_message):
    context.signup_page.check_phone_number_error(error_message)

@then('Account is not created - C_ID user alerted of mandatory field "{error_message}"')
def step_impl(context, error_message):
    context.signup_page.check_contry_ID_error(error_message)