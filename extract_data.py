import os
import pandas as pd
from dotenv import load_dotenv
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.firefox.options import Options
from selenium.webdriver.firefox.service import Service
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait


if __name__ == "__main__":
    df = pd.read_excel("responsiva-refr.xlsx", header=0)

    # print(f"Excel table shape: {df.shape}")
    # print(f"Table head: \n{df.head()} \n\nTable tail: \n{df.tail()}")

    # Load environment variables from .env file
    load_dotenv()

    # Get environment variables
    user_agent = os.getenv("USER_AGENT")
    firefox_driver_path = "/usr/local/bin/geckodriver"
    firefox_profile_path = os.getenv("FIREFOX_PROFILE_PATH")
    firefox_binary_path = os.getenv("FIREFOX_BINARY_PATH")

    # Configure Firefox options
    firefox_options = Options()
    firefox_options.set_preference("general.useragent.override", user_agent)
    firefox_options.binary_location = firefox_binary_path
    firefox_options.profile = firefox_profile_path

    # Specify the path to the geckodriver
    firefox_service = Service(executable_path=firefox_driver_path)

    # Start the Firefox browser
    try:
        browser = webdriver.Firefox(service=firefox_service, options=firefox_options)
        browser.get(os.getenv("WEB_URL"))

        # Wait until the checkbox is available
        checkbox_label = WebDriverWait(browser, 10).until(
            EC.element_to_be_clickable((By.XPATH, "//label[.//span[text()='207']]"))
        )
        checkbox_label.click()

        if 'N2RpBe' in checkbox_label.get_attribute('class'):
            print("✅ Checkbox selected successfully!")
        else:
            print("❌ Checkbox not selected.")

    except Exception as e:
        print(f"An error occurred: {e}")
    finally:
        # Close the browser at the end (optional)
        # browser.quit()
        pass
