from base_page import Base_page
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select


class Confirmation_page(Base_page):
    CONFIRMATION_MESSAGE = (By.XPATH, '//div/h2[@class="font-weight-normal mb-3"]')

    def check_successful_account_creation(self, expected_message):
        self.chrome.get('https://transfermate.io/en/register_mail_verification.html?frwd_frb_country=0')
        test_error = "Account was not created"
        actual_message = self.chrome.find_element(*self.CONFIRMATION_MESSAGE).text
        self.check_error_message(expected_message, actual_message,test_error)