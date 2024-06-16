from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time
import random

def test_case_2():
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

        # Find the Package type and click it
        mat_card = driver.find_element(By.XPATH, "//mat-card[.//span[text()='Package Types']]")
        mat_card.click()
        # -----------------
# Wait for the mat-card elements to be present
        WebDriverWait(driver, 10).until(
            EC.presence_of_element_located((By.CLASS_NAME, 'card-list'))
        )

        # Find the first mat-card element with class 'card-list'
        card_element = driver.find_element(By.CLASS_NAME, 'card-list')

        # Hover over the element to make the delete icon visible
        ActionChains(driver).move_to_element(card_element).perform()


# -----------------
        # Find and click the delete icon
        delete_icon = WebDriverWait(driver, 10).until(
            EC.element_to_be_clickable((By.XPATH, "//div[@appdialog='alert' and @dialogicon='delete']"))
        )
        delete_icon.click()


        # Wait for the "Delete Package Type" button to appear and become clickable
        delete_package_type_button = WebDriverWait(driver, 20).until(
            EC.element_to_be_clickable((By.XPATH, "//button[contains(@class, 'mat-raised-button') and contains(., 'Delete Package Type')]"))
        )

        # Click the "Delete Package Type" button
        delete_package_type_button.click()


        # -----------------
        time.sleep(5) 
        return "Test Case 2 Passed!"
    finally:
        # Close the browser
        driver.quit()

