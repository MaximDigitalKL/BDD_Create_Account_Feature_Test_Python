from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait

class Browser():
    chrome = webdriver.Chrome()
    chrome.maximize_window()
    chrome.get('https://transfermate.io/en/register.asp')
    chrome.implicitly_wait(4)

    def close(self):
        self.chrome.close()
