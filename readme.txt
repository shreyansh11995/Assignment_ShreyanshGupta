# Automated Testing with Selenium 

## Overview

The automated testing solution implemented using Selenium WebDriver for web application testing. The solution is designed to perform a series of automated interactions on a web application hosted at https://ecs-qa.kloudship.com.

### Prerequisites
- Ensure Python is installed on your system.
- Install the Selenium WebDriver for Python.
- Download the appropriate ChromeDriver executable and update the service = Service('C:/WebDriver/chromedriver.exe') line in the script to point to its location on your system.

### Execution Steps
1. Clone or download the repository containing the Python script (TestCase_2.py) and the README file.
2. Open a terminal or command prompt.
3. Navigate to the directory where TestCase_2.py is located.
4. Run the Python script using the following command:
5. The script will automate the described actions on the specified web application.
6. Monitor the terminal for any errors or the final output indicating whether the test case passed.

## Design Decisions and Approach

- *Use of Selenium WebDriver*: Chosen for its cross-browser compatibility and ability to interact with web elements programmatically.

- *Element Locators*: XPath and ID were primarily used for locating elements, ensuring robustness against UI changes.

- *Error Handling*: Incorporated try...except...finally blocks to manage exceptions gracefully, ensuring proper cleanup even in case of errors.

- *Dynamic Element Identification*: Where possible, elements were identified using common properties (class, role, etc.) rather than specific text values to increase flexibility and robustness.

- *Logging and Debugging*: Basic exception handling and print statements were used for logging purposes, aiding in debugging and understanding script execution flow.

