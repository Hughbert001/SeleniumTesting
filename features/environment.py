from selenium import webdriver 
from selenium.webdriver.firefox.options import Options as FirefoxOptions 
from selenium.webdriver.chrome.options import Options as ChromeOptions 
 
def before_all(context): 
    # options = FirefoxOptions() 
    # options.headless = True 
    # context.browser = webdriver.Firefox(options=options) 
    chrome_options = ChromeOptions() 
    chrome_options.add_argument('--headless') 
    chrome_options.add_argument('--no-sandbox') 
    chrome_options.add_argument('--disable-dev-shm-usage') 
    context.browser = webdriver.Chrome(chrome_options=chrome_options) 
     
def after_all(context): 
    context.browser.quit() 