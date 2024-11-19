import os
import pandas as pd
from dotenv import load_dotenv
from selenium import webdriver
from selenium.webdriver.firefox.service import Service
from selenium.webdriver.firefox.options import Options


if __name__ == "__main__":
    df = pd.read_excel("responsiva-refr.xlsx", header=0)

    print(f"Excel table shape: {df.shape}")
    print(f"Table head: \n{df.head()} \n\nTable tail: \n{df.tail()}")

    # Configure the user agent
    # Load environment variables from .env file
    load_dotenv()

    # Get the user agent from the environment variables
    user_agent = os.getenv("USER_AGENT")

    # Specify the path to the geckodriver
    firefox_driver_path = "/usr/local/bin/geckodriver"
    firefox_service = Service(executable_path=firefox_driver_path)

    # Configure Firefox options
    firefox_options = Options()
    firefox_options.set_preference("general.useragent.override", user_agent)

    # Specify the path to the Firefox binary
    firefox_options.binary_location = os.getenv("FIREFOX_BINARY_PATH")

    # Start the Firefox browser
    try:
        browser = webdriver.Firefox(service=firefox_service, options=firefox_options)
        browser.get(os.getenv("WEB_URL"))
    except Exception as e:
        print(f"An error occurred: {e}")
    finally:
        # Close the browser at the end (optional)
        # browser.quit()
        pass
