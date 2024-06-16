from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time
import random

def test_case_1():
    # Path to your ChromeDriver
    service = Service('C:/WebDriver/chromedriver.exe')
    driver = webdriver.Chrome(service=service)

    try:
        # Open the URL
        driver.get('https://ecs-qa.kloudship.com/signin')

        # Wait for the page to load and the login elements to be present
        WebDriverWait(driver, 10).until(
            EC.presence_of_element_located((By.ID, 'login-email'))
        )

        # Find the email and password input fields
        email_input = driver.find_element(By.ID, 'login-email')
        password_input = driver.find_element(By.ID, 'login-password')

        # Set the values for email and password
        email_input.send_keys('kloudship.qa.automation@mailinator.com')
        password_input.send_keys('Password1')

        # Find the login button and click it
        login_button = driver.find_element(By.ID, 'login-btn')
        login_button.click()


        WebDriverWait(driver, 10).until(
            EC.presence_of_element_located((By.CLASS_NAME, 'count-card'))
        )

        # Find the Login Button and click it
        mat_card = driver.find_element(By.XPATH, "//mat-card[.//span[text()='Package Types']]")
        mat_card.click()
        

        WebDriverWait(driver, 10).until(
            EC.presence_of_element_located((By.XPATH, "//span[@class='mat-button-wrapper']//mat-icon[text()='add']"))
        )

        # Find the 'add' button and click it
        add_icon_span = driver.find_element(By.XPATH, "//span[@class='mat-button-wrapper']//mat-icon[text()='add']")
        add_icon_span.click()        


        name_input = driver.find_element(By.ID, 'mat-input-2')
        length_input = driver.find_element(By.ID, 'mat-input-3')
        width_input = driver.find_element(By.ID, 'mat-input-4')
        height_input = driver.find_element(By.ID, 'mat-input-5')
        
        # Clear previous values if any
        name_input.clear()
        length_input.clear()
        width_input.clear()
        height_input.clear()

        # Generate random values
        random_length = random.randint(1, 21)  # Random number between 1 and 18 (inclusive)
        random_width = random.randint(1, 21)   # Random number between 1 and 18 (inclusive)
        random_height = random.randint(1, 21)  # Random number between 1 and 18 (inclusive)
        print(random_length, random_width, random_height)

        # Set the values for name and Dimensions
        name_input.send_keys('Shreyansh_Gupta')
        length_input.send_keys(random_length)
        width_input.send_keys(random_width)
        height_input.send_keys(random_height)
        
        # Find the 'check' button and click it
        check_icon_span = driver.find_element(By.XPATH, "//span[@class='mat-button-wrapper']//mat-icon[text()='check']")
        check_icon_span.click()

        # Wait for the 'more_vert' icon to be clickable
        WebDriverWait(driver, 10).until(
            EC.element_to_be_clickable((By.XPATH, "//span[@class='mat-button-wrapper']//mat-icon[text()='more_vert']"))
        )

        # Find the three dots icon and click it
        more_vert_icon_span = driver.find_element(By.XPATH, "//span[@class='mat-button-wrapper']//mat-icon[text()='more_vert']")
        more_vert_icon_span.click()

        # Find the logout button and click it
        logout_button = driver.find_element(By.XPATH, "//button[@role='menuitem' and .//mat-icon[text()='power_settings_new']]")
        logout_button.click()

        time.sleep(5) 
        return "Test Case 1 Passed!"
    finally:
        # Close the browser
        driver.quit()

