## About Project

This project automates the submission of data through a web form using Selenium and data extracted from an Excel file. The data is read from an Excel file specified in a .env file, and is submitted through a Firefox browser configured with a specific profile and user agent. The project includes error handling and generates an Excel file with the items that could not be submitted.

## Technologies implemented

### **Selenium:**

Selenium is a web browser automation tool that allows developers to interact with web pages programmatically. It is especially useful for automated testing and repetitive tasks in web applications. Selenium supports multiple browsers and provides an interface to control the browser, interact with page elements, and wait for certain conditions to be met.

**Key Selenium Components**

- **WebDriver**: Controls the web browser and simulates user actions.
- **By**: Methods to locate elements on the page (ID, NAME, XPATH, etc.).
- **Options**: Configures browser options, such as the profile and user agent.
- **Service**: Configures the browser driver service.
- **expected_conditions (EC)**: Predefined conditions to wait for certain states or events on the page.
- **WebDriverWait**: Waits until a specific condition is met before continuing.
