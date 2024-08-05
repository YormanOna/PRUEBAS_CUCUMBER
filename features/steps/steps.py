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
    screenshot_dir = 'Requisito1/screenshots'
    os.makedirs(screenshot_dir, exist_ok=True)
    screenshot_path = os.path.join(screenshot_dir, f"{step_name}.png")
    context.driver.save_screenshot(screenshot_path)

@given('navego a la página del menú')
def step_impl(context):
    options = webdriver.ChromeOptions()
    context.driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()), options=options)
    context.driver.get("http://localhost:5173/menu")
    take_screenshot(context, 'navego_a_la_pagina_del_menu')

@when('selecciono el servicio de bartender')
def step_impl(context):
    button = WebDriverWait(context.driver, 10).until(
        EC.element_to_be_clickable((By.XPATH, "//button[contains(text(), 'Servicio de Bartender')]"))
    )
    button.click()
    take_screenshot(context, 'selecciono_el_servicio_de_bartender')

@then('debería ver la imagen de inicio del menú de bartender')
def step_impl(context):
    try:
        page_image = WebDriverWait(context.driver, 20).until(
            EC.presence_of_element_located((By.CSS_SELECTOR, "img[alt='Inicio']"))
        )
        assert page_image is not None
        take_screenshot(context, 'deberia_ver_la_imagen_de_inicio_del_menu_de_bartender')
    except Exception as e:
        take_screenshot(context, 'deberia_ver_la_imagen_de_inicio_del_menu_de_bartender_fail')
        raise e
    finally:
        context.driver.quit()

@when('navego a la última página del menú de bartender')
def step_impl(context):
    next_button = WebDriverWait(context.driver, 10).until(
        EC.element_to_be_clickable((By.CSS_SELECTOR, ".nav-button.right"))
    )
    for _ in range(7):  # Navegar hasta la última página
        next_button.click()
        time.sleep(1)
    take_screenshot(context, 'navego_a_la_ultima_pagina_del_menu_de_bartender')

@then('debería ver la imagen de fin del menú de bartender')
def step_impl(context):
    try:
        # Falla intencional
        assert False, "Fallando este escenario intencionalmente"
        page_image = WebDriverWait(context.driver, 20).until(
            EC.presence_of_element_located((By.CSS_SELECTOR, "img[alt='Fin']"))
        )
        assert page_image is not None
        take_screenshot(context, 'deberia_ver_la_imagen_de_fin_del_menu_de_bartender')
    except Exception as e:
        take_screenshot(context, 'deberia_ver_la_imagen_de_fin_del_menu_de_bartender_fail')
        raise e
    finally:
        context.driver.quit()

@when('vuelvo a la primera página del menú de bartender desde la última página')
def step_impl(context):
    prev_button = WebDriverWait(context.driver, 10).until(
        EC.element_to_be_clickable((By.CSS_SELECTOR, ".nav-button.left"))
    )
    for _ in range(7):  # Volver a la primera página
        prev_button.click()
        time.sleep(1)
    take_screenshot(context, 'vuelvo_a_la_primera_pagina_del_menu_de_bartender_desde_la_ultima_pagina')

@then('debería ver nuevamente la imagen de inicio del menú de bartender')
def step_impl(context):
    try:
        # Falla intencional
        assert False, "Fallando este escenario intencionalmente"
        page_image = WebDriverWait(context.driver, 20).until(
            EC.presence_of_element_located((By.CSS_SELECTOR, "img[alt='Inicio']"))
        )
        assert page_image is not None
        take_screenshot(context, 'deberia_ver_nuevamente_la_imagen_de_inicio_del_menu_de_bartender')
    except Exception as e:
        take_screenshot(context, 'deberia_ver_nuevamente_la_imagen_de_inicio_del_menu_de_bartender_fail')
        raise e
    finally:
        context.driver.quit()

@when('selecciono el servicio de catering y navego a la sección de catering')
def step_impl(context):
    button = WebDriverWait(context.driver, 10).until(
        EC.element_to_be_clickable((By.XPATH, "//button[contains(text(), 'Servicio de Catering')]"))
    )
    button.click()
    take_screenshot(context, 'selecciono_el_servicio_de_catering_y_navego_a_la_seccion_de_catering')

@then('debería ver el componente de catering')
def step_impl(context):
    try:
        # Falla intencional
        assert False, "Fallando este escenario intencionalmente"
        catering_component = WebDriverWait(context.driver, 20).until(
            EC.presence_of_element_located((By.CSS_SELECTOR, ".catering-section"))
        )
        assert catering_component is not None
        take_screenshot(context, 'deberia_ver_el_componente_de_catering')
    except Exception as e:
        take_screenshot(context, 'deberia_ver_el_componente_de_catering_fail')
        raise e
    finally:
        context.driver.quit()
