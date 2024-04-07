from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.service import Service as ChromeService
from selenium.webdriver.support.select import Select
from selenium.webdriver.common.by import By
from selenium.webdriver import ActionChains, Keys
import time

# Function to perform login
def perform_login(driver):
    driver.get("https://www.like4like.org/login/")
    driver.maximize_window()
    driver.find_element(By.ID, "username").send_keys("Preetkumar")
    driver.find_element(By.ID, "password").send_keys('Fakeerparo99')
    # Click the login button or perform any other actions needed for login
    driver.find_element(By.XPATH, "//*[@id='login']/fieldset/table/tbody/tr[8]/td/span").click()
    time.sleep(5)

# Create the WebDriver session
driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))

# Perform login
perform_login(driver)

# Loop for other tasks
while True:  
    element = driver.find_element(By.CSS_SELECTOR, "a[title='Free Credits']")
    actions = ActionChains(driver)
    actions.move_to_element(element).perform()
    
    time.sleep(3)
    driver.find_element(By.CSS_SELECTOR, "a[title='Free Credits By Instagram Followers']").click()
    time.sleep(5) 

    driver.find_element(By.CLASS_NAME, 'earn_pages_button').click()

    # I sopped working on that because website is not working more
    