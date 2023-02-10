from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains
import time

driver = webdriver.Chrome()

driver.get("https://www.google.com")
driver.find_element(By.NAME,"q").send

driver.close()
driver.quit()