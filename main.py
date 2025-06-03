# Link for project template:
# https://www.geeksforgeeks.org/automate-linkedin-connections-using-python/

# Kristian Tokos
# March 25th, 2025

# ----- Imports -----

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import  Keys
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.support.wait import WebDriverWait
from webdriver_manager.chrome import ChromeDriverManager
from telnetlib import EC
import time

# ----- Log in to LinkedIn -----

# Set up the browser
driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
driver.get("https://www.linkedin.com/login")

# Enter login credentials
username = driver.find_element(By.ID, "username")
password = driver.find_element(By.ID, "password")
username.send_keys("")
password.send_keys("")

# Click login button
login_button = driver.find_element(By.XPATH, "//button[@type='submit']")
login_button.click()

time.sleep(10)  # Wait for the page to load

# ----- Search for profiles -----

# Locate the search button
search_button = driver.find_element(By.XPATH, "//button[@aria-label='Click to start a search']")
search_button.click()

# Wait briefly for the search box to appear
time.sleep(2)  # Adjust based on site responsiveness

# Locate the search input field and enter text
search_input = driver.find_element(By.CLASS_NAME, "search-global-typeahead__input")
search_input.send_keys("Software Engineer")

# Submit the search
search_input.send_keys(Keys.RETURN)
time.sleep(5)

# ----- Send connection requests -----

# Filter the search results to show people
people = driver.find_elements(By.CLASS_NAME, "search-reusables__filter-pill-button")
people[3].click()  # Adjust the index if needed

# Allow the site to load
time.sleep(2)

try:
    while True:  # Loop to process profiles on the current page
        # Scroll to load profiles dynamically
        driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
        time.sleep(3)  # Wait for new profiles to load

        # Find all "Connect" buttons
        connect_buttons = driver.find_elements(By.XPATH, "//button[.//span[contains(@class, 'artdeco-button__text') and text()='Connect']]")

        if not connect_buttons:
            print("No 'Connect' buttons found on the current page.")
            break  # Exit the loop if no buttons are found

        for button in connect_buttons:
            try:
                # Scroll to the "Connect" button to bring it into view
                driver.execute_script("arguments[0].scrollIntoView(true);", button)
                time.sleep(1)  # Allow time for scrolling

                # Try normal click
                try:
                    button.click()
                except:
                    # Fallback to JavaScript click if intercepted
                    driver.execute_script("arguments[0].click();", button)

                time.sleep(2)  # Allow time for the pop-up to load

                # Click the "Send without a note" button in the pop-up
                try:
                    send_without_note_button = driver.find_element(By.XPATH, "//button[contains(@class, 'artdeco-button--primary')]")
                    send_without_note_button.click()
                    print("Connection request sent successfully.")
                    time.sleep(2)
                except Exception as send_error:
                    print(f"Error finding 'Send without a note' button: {send_error}")

            except Exception as button_error:
                print(f"Error clicking 'Connect' button: {button_error}")

except KeyboardInterrupt:
    print("Script stopped by user.")

# ----- Close the browser -----

driver.quit()
