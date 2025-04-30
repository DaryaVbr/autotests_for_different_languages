import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By
import time



link = "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/"

def test_presence_add_button(browser):
    browser.get(link)
    time.sleep(30)
    # add_but = browser.find_element(By.CSS_SELECTOR, "button.btn.btn-lg.btn-primary.btn-add-to-basket")

    assert browser.find_elements(By.CSS_SELECTOR, "button.btn.btn-lg.btn-primary.btn-add-to-basket"), "add button not found"
