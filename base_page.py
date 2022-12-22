from browser import Browser
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select

class Base_page(Browser):

    ACCEPT_COOKIES = (By.XPATH,'//a[@id="cookies-read-more-link"]')

    def check_error_message(self, expected_message, actual_message, test_error):
        assert expected_message == actual_message, test_error

    def accept_cookies(self):
        try:
            self.chrome.find_element(*self.ACCEPT_COOKIES).click()
        except:
            pass
