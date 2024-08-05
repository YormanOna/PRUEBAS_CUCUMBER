import time
from behave import *
from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
import os

def take_screenshot(context, step_name):
    screenshot_dir = 'Requisito5/screenshots'
    os.makedirs(screenshot_dir, exist_ok=True)
    screenshot_path = os.path.join(screenshot_dir, f"{step_name}.png")
    context.driver.save_screenshot(screenshot_path)

@given('navego a la página del calendario')
def step_impl(context):
    options = webdriver.ChromeOptions()
    context.driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()), options=options)
    context.driver.get("http://localhost:5173/calendario")
    take_screenshot(context, 'navego_a_la_pagina_del_calendario')

@when('selecciono una fecha disponible')
def step_impl(context):
    date_card = WebDriverWait(context.driver, 10).until(
        EC.element_to_be_clickable((By.XPATH, "//div[contains(@class, 'available')]"))
    )
    date_card.click()
    take_screenshot(context, 'selecciono_una_fecha_disponible')

@then('debería ver la información de la fecha seleccionada')
def step_impl(context):
    try:
        selected_date_info = WebDriverWait(context.driver, 20).until(
            EC.presence_of_element_located((By.CSS_SELECTOR, ".bg-card"))
        )
        assert selected_date_info is not None
        take_screenshot(context, 'deberia_ver_la_informacion_de_la_fecha_seleccionada')
    except Exception as e:
        take_screenshot(context, 'deberia_ver_la_informacion_de_la_fecha_seleccionada_fail')
        raise e
    finally:
        context.driver.quit()

@when('intento seleccionar una fecha reservada')
def step_impl(context):
    booked_date_card = WebDriverWait(context.driver, 10).until(
        EC.element_to_be_clickable((By.XPATH, "//div[contains(@class, 'booked')]"))
    )
    booked_date_card.click()
    take_screenshot(context, 'intento_seleccionar_una_fecha_reservada')

@then('debería ver un mensaje de error')
def step_impl(context):
    try:
        # Falla intencional
        assert False, "Fallando este escenario intencionalmente"
        error_message = WebDriverWait(context.driver, 20).until(
            EC.presence_of_element_located((By.CSS_SELECTOR, ".error-message"))
        )
        assert error_message is not None
        take_screenshot(context, 'deberia_ver_un_mensaje_de_error')
    except Exception as e:
        take_screenshot(context, 'deberia_ver_un_mensaje_de_error_fail')
        raise e
    finally:
        context.driver.quit()

@when('selecciono una fecha con disponibilidad limitada')
def step_impl(context):
    limited_date_card = WebDriverWait(context.driver, 10).until(
        EC.element_to_be_clickable((By.XPATH, "//div[contains(@class, 'limited')]"))
    )
    limited_date_card.click()
    take_screenshot(context, 'selecciono_una_fecha_con_disponibilidad_limitada')

@then('debería ver un mensaje de disponibilidad limitada')
def step_impl(context):
    try:
        # Falla intencional
        assert False, "Fallando este escenario intencionalmente"
        limited_message = WebDriverWait(context.driver, 20).until(
            EC.presence_of_element_located((By.XPATH, "//p[contains(text(), 'limited')]"))
        )
        assert limited_message is not None
        take_screenshot(context, 'deberia_ver_un_mensaje_de_disponibilidad_limitada')
    except Exception as e:
        take_screenshot(context, 'deberia_ver_un_mensaje_de_disponibilidad_limitada_fail')
        raise e
    finally:
        context.driver.quit()

@when('hago clic en reservar ahora')
def step_impl(context):
    reserve_button = WebDriverWait(context.driver, 10).until(
        EC.element_to_be_clickable((By.XPATH, "//button[contains(text(), 'Reserve Now')]"))
    )
    reserve_button.click()
    take_screenshot(context, 'hago_clic_en_reservar_ahora')

@then('debería ver la página de reserva')
def step_impl(context):
    try:
        # Falla intencional
        assert False, "Fallando este escenario intencionalmente"
        reserve_page = WebDriverWait(context.driver, 20).until(
            EC.presence_of_element_located((By.CSS_SELECTOR, ".reserve-page"))
        )
        assert reserve_page is not None
        take_screenshot(context, 'deberia_ver_la_pagina_de_reserva')
    except Exception as e:
        take_screenshot(context, 'deberia_ver_la_pagina_de_reserva_fail')
        raise e
    finally:
        context.driver.quit()
