from selenium import webdriver
from selenium.webdriver.common.by import By
import pickle

login_url = 'https://www.linkedin.com/' 
driver = webdriver.Firefox()
driver.get(login_url)

email = "something@gmail.com"
pswd = 'some_password'

email_input = driver.find_element(By.ID, "session_key")
pswd_input = driver.find_element(By.ID,  'session_password')
sign_btn = driver.find_elements(By.TAG_NAME, "button")[1]

email_input.send_keys(email)
pswd_input.send_keys(pswd)

input("Press Enter when you have successfully logged in!")

cookies = driver.get_cookies()

with open("cookies.pkl", "wb") as f:
    pickle.dump(cookies, f)

driver.quit()
