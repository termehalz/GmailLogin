from selenium import webdriver 
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

username = 'Automated.testt' 
password = 'Test.1300' 

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

wait.until(EC.text_to_be_present_in_element((By.XPATH, '/html/body/div[1]/div[1]/div[2]/div/div[2]/div/div/div[2]/div/div[1]/div/form/span/section/div/div/div[1]/div[2]/div[2]/span'),'Wrong password. Try again or click Forgot password to reset it.'))