import os
import pandas as pd
from dotenv import load_dotenv
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.firefox.options import Options
from selenium.webdriver.firefox.service import Service
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait
import time


def extract_element_data(row):
    serie = row["SERIE"]
    activo = row["ACTIVO"]
    modelo = row["MODELO"]
    cliente = row["CLIENTE"]
    sap = row["SAP"]
    direccion = row["DIRECCIÓN"]

    return serie, activo, modelo, cliente, sap, direccion


if __name__ == "__main__":
    # Load environment variables from .env file
    load_dotenv()

    # Read the Excel file and create a DataFrame for fail elements
    df = pd.read_excel(os.getenv("DATA_PATH"), header=0)
    fail_elements = pd.DataFrame(
        columns=["Serie", "Activo", "Modelo", "Cliente", "SAP", "Dirección"]
    )

    # print(f"Excel table shape: {df.shape}")
    # print(f"Table head: \n{df.head(3)} \n\nTable tail: \n{df.tail(3)}")

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
        # browser = webdriver.Firefox(service=firefox_service, options=firefox_options)
        # browser.get(os.getenv("WEB_URL"))

        # # PREVENTA
        # checkbox_preventa = WebDriverWait(browser, 10).until(
        #     EC.element_to_be_clickable((By.XPATH, "//label[.//span[text()='207']]"))
        # )
        # checkbox_preventa.click()

        # if 'N2RpBe' in checkbox_preventa.get_attribute('class'):
        #     print("✅ Checkbox selected successfully!")
        # else:
        #     print("❌ Checkbox not selected.")

        # # SERIE
        # textarea_serie = WebDriverWait(browser, 15).until(
        #     EC.visibility_of_element_located((By.XPATH, "//textarea[@class='KHxj8b tL9Q4c']"))
        # )
        # textarea_serie.clear()
        # textarea_serie.send_keys("TEST SERIE")

        # # ACTIVO
        # input_activo = WebDriverWait(browser, 15).until(
        #     EC.visibility_of_element_located((By.XPATH, "//input[@class='whsOnd zHQkBf']"))
        # )
        # input_activo.clear()
        # input_activo.send_keys("TEST ACTIVO")

        # # MODELO
        # input_modelo = WebDriverWait(browser, 15).until(
        #     EC.visibility_of_element_located((By.XPATH, "//input[@class='whsOnd zHQkBf' and @aria-labelledby='i46 i49']"))
        # )
        # input_modelo.clear()
        # input_modelo.send_keys("TEST MODELO")

        # # CLIENTE
        # span_cliente = WebDriverWait(browser, 15).until(
        #     EC.visibility_of_element_located((By.XPATH, "//span[contains(text(), 'CLIENTE')]"))
        # )
        # input_cliente = browser.find_element(By.XPATH, "//span[contains(text(), 'CLIENTE')]/ancestor::div[contains(@class, 'geS5n')]//input[@class='whsOnd zHQkBf']")
        # input_cliente.clear()
        # input_cliente.send_keys("TEST CLIENTE")

        # # SAP
        # span_sap = WebDriverWait(browser, 15).until(
        #     EC.visibility_of_element_located((By.XPATH, "//span[contains(text(), 'SAP')]"))
        # )
        # input_sap = browser.find_element(By.XPATH, "//span[contains(text(), 'SAP')]/ancestor::div[contains(@class, 'geS5n')]//input[@class='whsOnd zHQkBf']")
        # input_sap.clear()
        # input_sap.send_keys("TEST SAP")

        # # DIRECCIÓN
        # span_direccion = WebDriverWait(browser, 15).until(
        #     EC.visibility_of_element_located((By.XPATH, "//span[contains(text(), 'DIRECCIÓN')]"))
        # )
        # input_direccion = browser.find_element(By.XPATH, "//span[contains(text(), 'DIRECCIÓN')]/ancestor::div[contains(@class, 'geS5n')]//input[@class='whsOnd zHQkBf']")
        # input_direccion.clear()
        # input_direccion.send_keys("TEST DIRECCIÓN")

        # # Enviar formulario
        # button_enviar = WebDriverWait(browser, 15).until(
        #     EC.element_to_be_clickable((By.XPATH, "//div[@role='button' and @aria-label='Submit']"))
        # )
        # button_enviar.click()

        # Verifica que se haya cargado la página de confirmación
        # WebDriverWait(browser, 15).until(
        #     EC.visibility_of_element_located((By.XPATH, "//div[contains(text(), 'Se registró tu respuesta.')]"))
        # )

        # # Verifica la presencia del enlace "Enviar otra respuesta"
        # enlace_enviar_otra_respuesta = WebDriverWait(browser, 15).until(
        #     EC.visibility_of_element_located((By.XPATH, "//a[contains(text(), 'Enviar otra respuesta')]"))
        # )

        # # Si ambos elementos están presentes, imprime un mensaje de éxito
        # if enlace_enviar_otra_respuesta:
        #     formulario_enviado_count += 1  # Incrementa el contador
        #     print(f"Formulario enviado exitosamente. Total de formularios enviados: {formulario_enviado_count}")

        #     # Haz clic en el enlace para enviar otra respuesta
        #     enlace_enviar_otra_respuesta.click()

        # Create a new DataFrame from row 15 onwards
        new_df = df.iloc[14:].drop(columns=["PREVENTA"]).reset_index(drop=False)

        # print(f"\n\nNew DataFrame shape: {new_df.shape}")
        print(f"\nNew DataFrame head: \n{new_df.head(3)}")

        pause_duration = 7

        # Using for and iterrows
        # TODO: Remove head(3) to process all rows
        for index, row in new_df.head(3).iterrows():
            serie, activo, modelo, cliente, sap, direccion = extract_element_data(row)
            print(f"\n\nRow {index + 14} | elements:")
            print(f"Serie: {serie}")
            print(f"Activo: {activo}")
            print(f"Modelo: {modelo}")
            print(f"Cliente: {cliente}")
            print(f"SAP: {sap}")
            print(f"Dirección: {direccion}")

            # TODO: Remove head(3) to process all rows
            if index != len(new_df.head(3)) - 1:
                time.sleep(pause_duration)

    except Exception as e:
        print(f"Fail with element: {index + 14} | Error: \n{e}")
        fail_elements = fail_elements.append(
            {
                "Serie": serie,
                "Activo": activo,
                "Modelo": modelo,
                "Cliente": cliente,
                "SAP": sap,
                "Dirección": direccion,
            },
            ignore_index=True,
        )

    finally:
        if len(fail_elements) > 0:
            print("\n\nSome elements were not sent.")
            print(f"\nFailed elements: {fail_elements}")
            fail_elements.to_excel("failed_elements.xlsx", index=False)
        else:
            print("\n\nAll elements were successfully sent.")
            # browser.quit()
            # print("\nBrowser closed.")
