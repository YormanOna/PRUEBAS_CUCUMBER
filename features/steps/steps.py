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
    screenshot_dir = 'reports_Requisito2/screenshots'
    os.makedirs(screenshot_dir, exist_ok=True)
    screenshot_path = os.path.join(screenshot_dir, f"{step_name}.png")
    context.driver.save_screenshot(screenshot_path)

@given('I navigate to the register page')
def step_impl(context):
    options = webdriver.ChromeOptions()
    context.driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()), options=options)
    context.driver.get("http://localhost:5173/registro")
    take_screenshot(context, 'I_navigate_to_the_register_page')

@when('I enter valid data for each field')
def step_impl(context):
    context.driver.find_element(By.NAME, "nombre").send_keys("Silvia")
    context.driver.find_element(By.NAME, "apellido").send_keys("Anasco")
    context.driver.find_element(By.NAME, "cedula_ciudadania").send_keys("1753951076")
    context.driver.find_element(By.NAME, "domicilio").send_keys("Chillogallo")
    context.driver.find_element(By.NAME, "telefono").send_keys("0995227606")
    context.driver.find_element(By.NAME, "email").send_keys("sianasco@espe.edu.ec")
    context.driver.find_element(By.NAME, "fecha_nacimiento").send_keys("07-04-2004")
    context.driver.find_element(By.NAME, "user").send_keys("sianasco1")
    context.driver.find_element(By.NAME, "password").send_keys("password123")
    
    context.driver.find_element(By.CSS_SELECTOR, "button").click()
    take_screenshot(context, 'I_enter_valid_data_for_each_field')

@then('I should see a confirmation message')
def step_impl(context):
    message = WebDriverWait(context.driver, 10).until(
        EC.presence_of_element_located((By.CSS_SELECTOR, ".success-message"))
    ).text
    assert message == "Datos ingresados correctamente."
    take_screenshot(context, 'I_should_see_a_confirmation_message')
    context.driver.quit()

@when('I leave all fields empty')
def step_impl(context):
    context.driver.find_element(By.CSS_SELECTOR, "button").click()
    take_screenshot(context, 'I_leave_all_fields_empty')

@then('I should see a message')
def step_impl(context):
    error_message = WebDriverWait(context.driver, 10).until(
        EC.presence_of_element_located((By.CSS_SELECTOR, ".errors-custom"))
    ).text
    assert error_message == "El nombre es requerido"
    take_screenshot(context, 'I_should_see_a_message')
    context.driver.quit()

@when('I enter a name with numbers')
def step_impl(context):
    context.driver.find_element(By.NAME, "nombre").send_keys("Mari1234")
    context.driver.find_element(By.NAME, "apellido").send_keys("Anasco")
    context.driver.find_element(By.NAME, "cedula_ciudadania").send_keys("1753951076")
    context.driver.find_element(By.NAME, "domicilio").send_keys("Chillogallo")
    context.driver.find_element(By.NAME, "telefono").send_keys("0995227606")
    context.driver.find_element(By.NAME, "email").send_keys("sianasco@espe.edu.ec")
    context.driver.find_element(By.NAME, "fecha_nacimiento").send_keys("07-04-2004")
    context.driver.find_element(By.NAME, "user").send_keys("sianasco2")
    context.driver.find_element(By.NAME, "password").send_keys("password456")
    
    context.driver.find_element(By.CSS_SELECTOR, "button").click()
    take_screenshot(context, 'I_enter_a_name_with_numbers')

@then('I should see a alert message')
def step_impl(context):
    error_message = WebDriverWait(context.driver, 10).until(
        EC.presence_of_element_located((By.CSS_SELECTOR, ".errors-custom"))
    ).text
    assert error_message == "Solo se permiten letras"
    take_screenshot(context, 'I_should_see_a_alert_message')
    context.driver.quit()

@when('I enter a lastname with numbers')
def step_impl(context):
    context.driver.find_element(By.NAME, "nombre").send_keys("Maria")
    context.driver.find_element(By.NAME, "apellido").send_keys("Lopez123")
    context.driver.find_element(By.NAME, "cedula_ciudadania").send_keys("1753951076")
    context.driver.find_element(By.NAME, "domicilio").send_keys("Chillogallo")
    context.driver.find_element(By.NAME, "telefono").send_keys("0995227606")
    context.driver.find_element(By.NAME, "email").send_keys("sianasco@espe.edu.ec")
    context.driver.find_element(By.NAME, "fecha_nacimiento").send_keys("07-04-2004")
    context.driver.find_element(By.NAME, "user").send_keys("sianasco3")
    context.driver.find_element(By.NAME, "password").send_keys("password789")
    
    context.driver.find_element(By.CSS_SELECTOR, "button").click()
    take_screenshot(context, 'I_enter_a_lastname_with_numbers')

@when('I enter an excessively old birth date')
def step_impl(context):
    context.driver.find_element(By.NAME, "nombre").send_keys("Maria")
    context.driver.find_element(By.NAME, "apellido").send_keys("Lopez")
    context.driver.find_element(By.NAME, "cedula_ciudadania").send_keys("1753951076")
    context.driver.find_element(By.NAME, "domicilio").send_keys("Chillogallo")
    context.driver.find_element(By.NAME, "telefono").send_keys("0995227606")
    context.driver.find_element(By.NAME, "email").send_keys("sianasco@espe.edu.ec")
    context.driver.find_element(By.NAME, "fecha_nacimiento").send_keys("07-04-1800")
    context.driver.find_element(By.NAME, "user").send_keys("sianasco4")
    context.driver.find_element(By.NAME, "password").send_keys("password321")
    
    context.driver.find_element(By.CSS_SELECTOR, "button").click()
    take_screenshot(context, 'I_enter_an_excessively_old_birth_date')

@when('I enter the birth date of an underage person')
def step_impl(context):
    context.driver.find_element(By.NAME, "nombre").send_keys("Maria")
    context.driver.find_element(By.NAME, "apellido").send_keys("Lopez")
    context.driver.find_element(By.NAME, "cedula_ciudadania").send_keys("1753951076")
    context.driver.find_element(By.NAME, "domicilio").send_keys("Chillogallo")
    context.driver.find_element(By.NAME, "telefono").send_keys("0995227606")
    context.driver.find_element(By.NAME, "email").send_keys("sianasco@espe.edu.ec")
    context.driver.find_element(By.NAME, "fecha_nacimiento").send_keys("07-04-2012")
    context.driver.find_element(By.NAME, "user").send_keys("sianasco5")
    context.driver.find_element(By.NAME, "password").send_keys("password654")
    
    context.driver.find_element(By.CSS_SELECTOR, "button").click()
    take_screenshot(context, 'I_enter_the_birth_date_of_an_underage_person')

@when('I enter a negative number in id field')
def step_impl(context):
    context.driver.find_element(By.NAME, "nombre").send_keys("Maria")
    context.driver.find_element(By.NAME, "apellido").send_keys("Lopez")
    context.driver.find_element(By.NAME, "cedula_ciudadania").send_keys("-1")
    context.driver.find_element(By.NAME, "domicilio").send_keys("Chillogallo")
    context.driver.find_element(By.NAME, "telefono").send_keys("0995227606")
    context.driver.find_element(By.NAME, "email").send_keys("sianasco@espe.edu.ec")
    context.driver.find_element(By.NAME, "fecha_nacimiento").send_keys("07-04-2004")
    context.driver.find_element(By.NAME, "user").send_keys("sianasco6")
    context.driver.find_element(By.NAME, "password").send_keys("password987")
    
    context.driver.find_element(By.CSS_SELECTOR, "button").click()
    take_screenshot(context, 'I_enter_a_negative_number_in_id_field')

@then('I should see an id validation message')
def step_impl(context):
    error_message = WebDriverWait(context.driver, 10).until(
        EC.presence_of_element_located((By.CSS_SELECTOR, ".errors-custom"))
    ).text
    assert error_message == "El número de cédula es requerido"
    take_screenshot(context, 'I_should_see_an_id_validation_message')
    context.driver.quit()
