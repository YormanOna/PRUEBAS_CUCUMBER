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
    screenshot_dir = 'Requisito6/screenshots'
    os.makedirs(screenshot_dir, exist_ok=True)
    screenshot_path = os.path.join(screenshot_dir, f"{step_name}.png")
    context.driver.save_screenshot(screenshot_path)

@given('navego a la página de cotización')
def step_impl(context):
    options = webdriver.ChromeOptions()
    context.driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()), options=options)
    context.driver.get("http://localhost:5173/cotizacion")
    take_screenshot(context, 'navego_a_la_pagina_de_cotizacion')

@when('selecciono un servicio y una fecha y genero la cotización')
def step_impl(context):
    service_select = WebDriverWait(context.driver, 10).until(
        EC.element_to_be_clickable((By.ID, "service"))
    )
    service_select.send_keys("Bartending")
    date_input = context.driver.find_element(By.ID, "date")
    date_input.send_keys("2023-06-20")
    generate_button = context.driver.find_element(By.ID, "generate-quote")
    generate_button.click()
    take_screenshot(context, 'selecciono_un_servicio_y_una_fecha_y_genero_la_cotizacion')

@then('debería ver la cotización detallada')
def step_impl(context):
    try:
        quote_result = WebDriverWait(context.driver, 20).until(
            EC.presence_of_element_located((By.ID, "quote-result"))
        )
        assert quote_result is not None
        take_screenshot(context, 'deberia_ver_la_cotizacion_detallada')
    except Exception as e:
        take_screenshot(context, 'deberia_ver_la_cotizacion_detallada_fail')
        raise e
    finally:
        context.driver.quit()

@when('no lleno todos los campos y genero la cotización')
def step_impl(context):
    generate_button = WebDriverWait(context.driver, 10).until(
        EC.element_to_be_clickable((By.ID, "generate-quote"))
    )
    generate_button.click()
    take_screenshot(context, 'no_lleno_todos_los_campos_y_genero_la_cotizacion')

@then('debería ver un mensaje de error')
def step_impl(context):
    try:
        alert = WebDriverWait(context.driver, 10).until(
            EC.alert_is_present()
        )
        alert_text = alert.text
        assert "Por favor, complete todos los campos." in alert_text
        take_screenshot(context, 'deberia_ver_un_mensaje_de_error')
        alert.accept()
    except Exception as e:
        take_screenshot(context, 'deberia_ver_un_mensaje_de_error_fail')
        raise e
    finally:
        context.driver.quit()

@when('selecciono extras y genero la cotización')
def step_impl(context):
    service_select = WebDriverWait(context.driver, 10).until(
        EC.element_to_be_clickable((By.ID, "service"))
    )
    service_select.send_keys("Catering")
    date_input = context.driver.find_element(By.ID, "date")
    date_input.send_keys("2023-06-20")
    dj_checkbox = context.driver.find_element(By.ID, "dj")
    dj_checkbox.click()
    lighting_checkbox = context.driver.find_element(By.ID, "lighting")
    lighting_checkbox.click()
    generate_button = context.driver.find_element(By.ID, "generate-quote")
    generate_button.click()
    take_screenshot(context, 'selecciono_extras_y_genero_la_cotizacion')

@then('debería ver la cotización detallada con los extras')
def step_impl(context):
    try:
        # Falla intencional
        assert False, "Fallando este escenario intencionalmente"
        quote_result = WebDriverWait(context.driver, 20).until(
            EC.presence_of_element_located((By.ID, "quote-result"))
        )
        assert "DJ, Iluminación" in quote_result.text
        take_screenshot(context, 'deberia_ver_la_cotizacion_detallada_con_los_extras')
    except Exception as e:
        take_screenshot(context, 'deberia_ver_la_cotizacion_detallada_con_los_extras_fail')
        raise e
    finally:
        context.driver.quit()

@when('genero la cotización sin seleccionar servicio')
def step_impl(context):
    date_input = WebDriverWait(context.driver, 10).until(
        EC.element_to_be_clickable((By.ID, "date"))
    )
    date_input.send_keys("2023-06-20")
    generate_button = context.driver.find_element(By.ID, "generate-quote")
    generate_button.click()
    take_screenshot(context, 'genero_la_cotizacion_sin_seleccionar_servicio')

@then('debería ver un mensaje de error por falta de servicio')
def step_impl(context):
    try:
        # Falla intencional
        assert False, "Fallando este escenario intencionalmente"
        alert = WebDriverWait(context.driver, 10).until(
            EC.alert_is_present()
        )
        alert_text = alert.text
        assert "Por favor, complete todos los campos." in alert_text
        take_screenshot(context, 'deberia_ver_un_mensaje_de_error_por_falta_de_servicio')
        alert.accept()
    except Exception as e:
        take_screenshot(context, 'deberia_ver_un_mensaje_de_error_por_falta_de_servicio_fail')
        raise e
    finally:
        context.driver.quit()
