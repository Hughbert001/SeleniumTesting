from selenium import webdriver 
# from shutil import which 
from selenium.webdriver.common.by import By 
from selenium.webdriver.support.ui import WebDriverWait 
from selenium.webdriver.support import expected_conditions 

@given(u'user is on the dashboard page') 
def step_impl(context): 
    context.browser.get("http://3.93.218.186:8081/dashboard") 

@when(u'user selects a specifc user by name') 
def step_impl(context): 
    button = By.XPATH, '//a[@title="User Details"]'
    search = By.XPATH, '//input[@type="search"]'
    WebDriverWait(context.browser,100).until( 
        expected_conditions.presence_of_element_located(button) 
    )
    context.browser.find_element(*button).click()
    srchfield = context.browser.find_element(*search) 
    srchfield.send_keys('Lena') 

@then(u'the components on the dashboard are search specific') 
def step_impl(context):
    false_counter = 0
    user_find = By.XPATH, '//span[contains(text(),"Lena R Perez")]' 
    if "Lena R Perez" not in context.browser.find_element(*user_find).text: 
        false_counter += 1 
    assert false_counter == 0

@when(u'user selects a specific user by customer number') 
def step_impl(context): 
    button = By.XPATH, '//a[@title="User Details"]'
    search = By.XPATH, '//input[@type="search"]'
    WebDriverWait(context.browser,100).until( 
        expected_conditions.presence_of_element_located(button) 
    )
    context.browser.find_element(*button).click()
    srchfield = context.browser.find_element(*search) 
    srchfield.send_keys('4323') 
