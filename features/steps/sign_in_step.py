from selenium import webdriver 
# from shutil import which 
from selenium.webdriver.common.by import By 
from selenium.webdriver.support.ui import WebDriverWait 
from selenium.webdriver.support import expected_conditions 

@given(u'user is on the landing page') 
def step_impl(context): 
    context.browser.get("http://3.93.218.186:8081/") 

@when(u'user clicks on launch button') 
def step_impl(context): 
    button = By.XPATH, '//button'
    WebDriverWait(context.browser,100).until( 
        expected_conditions.presence_of_element_located(button) 
    )
    context.browser.find_element(*button).click()

@then(u'user gets redirected to the dashboard') 
def step_impl(context):
    wait = WebDriverWait(context.browser, 3) 
    assert context.browser.current_url == "http://3.93.218.186:8081/login" 
     
