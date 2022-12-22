from base_page import Base_page
from browser import Browser
from pages.confirmation_page import Confirmation_page
from pages.signup_page import Signup_page


def before_all(context):
    context.base_page_object = Base_page()
    context.browser = Browser()
    context.signup_page = Signup_page()
    context.confirmation_page = Confirmation_page()

def after_all(context):
    context.browser.quit()
