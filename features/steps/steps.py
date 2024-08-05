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
    screenshot_dir = 'Requisito4/screenshots'
    os.makedirs(screenshot_dir, exist_ok=True)
    screenshot_path = os.path.join(screenshot_dir, f"{step_name}.png")
    context.driver.save_screenshot(screenshot_path)

@given('navego al panel de administración')
def step_impl(context):
    options = webdriver.ChromeOptions()
    context.driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()), options=options)
    context.driver.get("http://localhost:5173/admin")
    take_screenshot(context, 'navego_al_panel_de_administracion')

@when('selecciono la pestaña de cocteles')
def step_impl(context):
    button = WebDriverWait(context.driver, 10).until(
        EC.element_to_be_clickable((By.XPATH, "//button[contains(text(), 'Cocteles')]"))
    )
    button.click()
    take_screenshot(context, 'selecciono_la_pestana_de_cocteles')

@then('debería ver el gestor de cocteles')
def step_impl(context):
    try:
        coctel_manager = WebDriverWait(context.driver, 20).until(
            EC.presence_of_element_located((By.CSS_SELECTOR, ".containerADmi"))
        )
        assert coctel_manager is not None
        take_screenshot(context, 'deberia_ver_el_gestor_de_cocteles')
    except Exception as e:
        take_screenshot(context, 'deberia_ver_el_gestor_de_cocteles_fail')
        raise e
    finally:
        context.driver.quit()

@when('agrego un nuevo coctel')
def step_impl(context):
    button = WebDriverWait(context.driver, 10).until(
        EC.element_to_be_clickable((By.XPATH, "//button[contains(text(), 'Registrar')]"))
    )
    button.click()
    context.driver.find_element(By.NAME, "nombre").send_keys("Test Coctel")
    context.driver.find_element(By.NAME, "tipo").send_keys("Test Tipo")
    context.driver.find_element(By.NAME, "cantidad").send_keys("1")
    context.driver.find_element(By.NAME, "garnishes").send_keys("Test Garnishes")
    context.driver.find_element(By.NAME, "mixers").send_keys("Test Mixers")
    context.driver.find_element(By.NAME, "imagen").send_keys(os.path.abspath("test_image.jpg"))
    take_screenshot(context, 'agrego_un_nuevo_coctel')

@then('debería ver el nuevo coctel en la lista')
def step_impl(context):
    try:
        # Falla intencional
        assert False, "Fallando este escenario intencionalmente"
        coctel = WebDriverWait(context.driver, 20).until(
            EC.presence_of_element_located((By.XPATH, "//td[contains(text(), 'Test Coctel')]"))
        )
        assert coctel is not None
        take_screenshot(context, 'deberia_ver_el_nuevo_coctel_en_la_lista')
    except Exception as e:
        take_screenshot(context, 'deberia_ver_el_nuevo_coctel_en_la_lista_fail')
        raise e
    finally:
        context.driver.quit()

@when('elimino un coctel')
def step_impl(context):
    delete_button = WebDriverWait(context.driver, 10).until(
        EC.element_to_be_clickable((By.XPATH, "//button[contains(text(), 'Eliminar')]"))
    )
    delete_button.click()
    take_screenshot(context, 'elimino_un_coctel')

@then('debería ver el coctel eliminado de la lista')
def step_impl(context):
    try:
        # Falla intencional
        assert False, "Fallando este escenario intencionalmente"
        coctel = WebDriverWait(context.driver, 20).until_not(
            EC.presence_of_element_located((By.XPATH, "//td[contains(text(), 'Test Coctel')]"))
        )
        assert coctel is None
        take_screenshot(context, 'deberia_ver_el_coctel_eliminado_de_la_lista')
    except Exception as e:
        take_screenshot(context, 'deberia_ver_el_coctel_eliminado_de_la_lista_fail')
        raise e
    finally:
        context.driver.quit()

@when('selecciono la pestaña de paquetes')
def step_impl(context):
    button = WebDriverWait(context.driver, 10).until(
        EC.element_to_be_clickable((By.XPATH, "//button[contains(text(), 'Paquetes')]"))
    )
    button.click()
    take_screenshot(context, 'selecciono_la_pestana_de_paquetes')

@then('debería ver el gestor de paquetes')
def step_impl(context):
    try:
        # Falla intencional
        assert False, "Fallando este escenario intencionalmente"
        paquete_manager = WebDriverWait(context.driver, 20).until(
            EC.presence_of_element_located((By.CSS_SELECTOR, ".paquete-manager"))
        )
        assert paquete_manager is not None
        take_screenshot(context, 'deberia_ver_el_gestor_de_paquetes')
    except Exception as e:
        take_screenshot(context, 'deberia_ver_el_gestor_de_paquetes_fail')
        raise e
    finally:
        context.driver.quit()
