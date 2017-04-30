from behave import *
from selenium import webdriver
from pyvirtualdisplay import Display
import django


def before_all(context):
    django.setup()
    display = Display(visible=0, size=(800, 600))
    display.start()
    context.browser = webdriver.Chrome()

def after_all(context):
    context.browser.quit()
