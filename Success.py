from selenium import webdriver 
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

username = 'Automated.testt' 
password = 'Test.1399' 

driver = webdriver.Firefox() 
driver.get(r'https://gmail.com') 
driver.implicitly_wait(10) 
wait = WebDriverWait(driver, 10)

usernameField = wait.until(EC.element_to_be_clickable((By.ID, "identifierId")))
usernameField.send_keys(username) 

nextButton = wait.until(EC.element_to_be_clickable((By.ID, "identifierNext")))
nextButton.click()

passwordField = wait.until(EC.element_to_be_clickable((By.NAME, "password")))
passwordField.send_keys(password) 

nextButton = wait.until(EC.element_to_be_clickable((By.ID, "passwordNext")))
nextButton.click() 

wait.until(EC.title_contains('Inbox'))