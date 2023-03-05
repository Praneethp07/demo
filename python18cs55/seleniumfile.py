from selenium import webdriver
import time

from selenium.webdriver import ActionChains
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
browser = webdriver.Firefox()
try:
    browser.get('http://instagram.com')
except Exception as exe:
    print(f"Exception occured:{exe}")


# Clicking on the link
username = browser.find_element(By.NAME,'username').send_keys("buzzingabuzzathome")
password = browser.find_element(By.NAME,'password').send_keys("praneeth@123")
searchbtn = browser.find_element(By.CSS_SELECTOR,"._acan _acap _acas _aj1-")

searchbtn.click()

# actions = ActionChains(browser)
# actions.send_keys(Keys.ENTER)
# searchbtn.click()
# actions.perform()


