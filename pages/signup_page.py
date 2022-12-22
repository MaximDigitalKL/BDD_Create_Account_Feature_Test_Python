import time

from base_page import Base_page
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select


class Signup_page(Base_page):
    EDUCATION_BUTTON = (By.XPATH, '//label[@class="check-radio-label" and @for="account_type_education"]')
    INDIVIDUAL_BUTTON = (By.XPATH, '//label[@class="check-radio-label" and @for="account_type_individual"]')
    CORPORATION_BUTTON = (By.XPATH, '//label[@class="check-radio-label" and @for="account_type_corporate"]')
    COUNTRY_DD = (By.XPATH, '//select[@name="country"]')
    FIRST_NAME = (By.XPATH, '//input[@name="first_name"]')
    LAST_NAME = (By.XPATH, '//input[@name="last_name"]')
    EMAIL = (By.XPATH, '//input[@name="email"]')
    PREFIX_DD = (By.XPATH,'//select[@name="__pin_mobile_number_international_dialing_code"]')
    PHONE_NR = (By.XPATH, '//input[@name="__pin_mobile_number_mobile_phone"]')
    TERMS_CONDITIONS = (By.XPATH, '//label[@class="check-radio-label"] [@for="terms_of_use_agree"]')
    NEWS_LETTER = (By.XPATH, '//label[@class="check-radio-label" and @for="newsletter_and_privacy_policy_agree"]')
    CREATE_ACCOUNT = (By.XPATH, '//input[@type="submit"]')
    CAPTCHA = (By.XPATH, '//div[@id="cal_captcha_f10_question"]')
    DROP_DOWN_C = (By.XPATH, '//select[@name="country"]')
    DROP_DOWN_P = (By.XPATH, '//select[@name="__pin_mobile_number_international_dialing_code"]')
    ERROR_MESSAGE_ACT = (By.ID, 'register_account_type_individual_error')
    ERROR_MESSAGE_TERMS = (By.XPATH, '//div[@id="register_terms_of_use_agree_error"]')
    ERROR_MESSAGE_CAPTCHA = (By.XPATH,'//div[@id="register___calc_captcha_text_error"]')
    ERROR_MESSAGE_FN = (By.ID, 'register_first_name_error')
    ERROR_MESSAGE_EM = (By.XPATH, '//div[@id="register_email_error"]')
    ERROR_MESSAGE_PH = (By.XPATH, '//div[@id="register___pin_mobile_number_mobile_phone_error"]')
    ERROR_MESSAGE_CID= (By.XPATH, '//select[@id="__pin_mobile_number_international_dialing_code"]')


    def navigate_to_signup_page(self):
        self.chrome.get('https://transfermate.io/en/register.asp')

    def select_education_button(self):
        self.chrome.find_element(*self.EDUCATION_BUTTON).click()

    def select_individual_button(self):
        self.chrome.find_element(*self.INDIVIDUAL_BUTTON).click()

    def select_corporation_button(self):
        self.chrome.find_element(*self.INDIVIDUAL_BUTTON).click()

    def insert_FirstName(self, FirstName):
        self.chrome.find_element(*self.FIRST_NAME).send_keys(FirstName)

    def insert_LastName(self, LastName):
        self.chrome.find_element(*self.LAST_NAME).send_keys(LastName)

    def insert_email(self,email):
        self.chrome.find_element(*self.EMAIL).send_keys(email)

    def insert_phone(self,phone):
        self.chrome.find_element(*self.PHONE_NR).send_keys(phone)

    def select_terms_of_use(self):
        self.chrome.find_element(*self.TERMS_CONDITIONS).click()

    def select_news_letter(self):
        self.chrome.find_element(*self.NEWS_LETTER).click()

    def calculate_captcha(self):
        equation = self.chrome.find_element(*self.CAPTCHA).text.split(' ')
        if equation[1] == "+":
            answer = int(equation[0])+int(equation[2])
        else:
            answer = int(equation[0])-int(equation[2])
        self.chrome.find_element(By.XPATH,'//input[@name="__calc_captcha_text"]').send_keys(answer)

    def drop_down_country(self,d_country):  #Romania / France
        drop_down = self.chrome.find_element(*self.DROP_DOWN_C)
        country = Select(drop_down)
        country.select_by_visible_text(d_country)

    def drop_down_prefix(self,d_prefix): #Romania +40 / Angola +244
        drop_down = self.chrome.find_element(*self.DROP_DOWN_P)
        prefix = Select(drop_down)
        prefix.select_by_visible_text(d_prefix)

    def select_create_account(self):
        button = self.chrome.find_element(*self.CREATE_ACCOUNT)
        self.chrome.execute_script("arguments[0].click();", button)

    def check_account_type_error(self, expected_message):
        test_error = "Account type not selected error message"
        actual_message = self.chrome.find_element(*self.ERROR_MESSAGE_ACT).text
        self.check_error_message(expected_message, actual_message,test_error)

    def check_terms_and_conditions_error(self, expected_message):
        test_error = "Select Terms and Conditions error message"
        actual_message = self.chrome.find_element(*self.ERROR_MESSAGE_TERMS).text
        self.check_error_message(expected_message, actual_message,test_error)

    def check_captch_error(self, expected_message):
        test_error = "Resolve Captcah Equation error message"
        actual_message = self.chrome.find_element(*self.ERROR_MESSAGE_CAPTCHA).text
        self.check_error_message(expected_message, actual_message,test_error)

    def check_first_name_error(self, expected_message):
        test_error = "Invalid First Name error message"
        actual_message = self.chrome.find_element(*self.ERROR_MESSAGE_FN).text
        self.check_error_message(expected_message, actual_message,test_error)

    def check_email_address_error(self, expected_message):
        test_error = "Invalid email address error message"
        actual_message = self.chrome.find_element(*self.ERROR_MESSAGE_EM).text
        self.check_error_message(expected_message, actual_message,test_error)

    def check_phone_number_error(self, expected_message):
        test_error = "Invalid phone number error message"
        actual_message = self.chrome.find_element(*self.ERROR_MESSAGE_PH).text
        self.check_error_message(expected_message, actual_message, test_error)

    def check_contry_ID_error(self, expected_message):
        test_error = "Invalid contry and country ID combination error message"
        actual_message = self.chrome.find_element(*self.ERROR_MESSAGE_CID).text
        self.check_error_message(expected_message, actual_message, test_error)