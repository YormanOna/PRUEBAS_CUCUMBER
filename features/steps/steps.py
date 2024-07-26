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
    screenshot_dir = 'reports/screenshots'
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
    context.driver.find_element("name", "nombre").send_keys("Silvia")
    context.driver.find_element("name", "apellido").send_keys("Añasco")
    context.driver.find_element("name", "cedula").send_keys("1753951076")
    context.driver.find_element("name", "domicilio").send_keys("Chillogallo")
    context.driver.find_element("name", "telefono").send_keys("0995227606")
    context.driver.find_element("name", "email").send_keys("sianasco@espe.edu.ec")
    context.driver.find_element("name", "fecha_nacimiento").send_keys("07-04-2024")
    
    context.driver.find_element(By.CSS_SELECTOR, "button").click()
    take_screenshot(context, 'I_enter_valid_data_for_each_field')

@then('I should see a confirmation message')
def step_impl(context):
    assert context.driver.find_element(By.CSS_SELECTOR, ".message").text == "Datos ingresado."
    take_screenshot(context, 'I_should_see_a_confirmation_message')
    context.driver.close()

@when('I leave all fields empty')
def step_impl(context):
    context.driver.find_element(By.CSS_SELECTOR, "button").click()
    take_screenshot(context, 'I_leave_all_fields_empty')

@then('I should see a message')
def step_impl(context):
    assert context.driver.find_element(By.CSS_SELECTOR, "label:nth-child(2) > p").text == "El nombre es requerido"
    take_screenshot(context, 'I_should_see_a_message')
    context.driver.close()

@when('I enter a name with numbers')
def step_impl(context):
    context.driver.find_element("name", "nombre").send_keys("Mari1234")
    context.driver.find_element("name", "apellido").send_keys("Añasco")
    context.driver.find_element("name", "cedula").send_keys("1753951076")
    context.driver.find_element("name", "domicilio").send_keys("Chillogallo")
    context.driver.find_element("name", "telefono").send_keys("0995227606")
    context.driver.find_element("name", "email").send_keys("sianasco@espe.edu.ec")
    context.driver.find_element("name", "fecha_nacimiento").send_keys("07-04-2024")
    
    context.driver.find_element(By.CSS_SELECTOR, "button").click()
    take_screenshot(context, 'I_enter_a_name_with_numbers')

@then('I should see a alert message')
def step_impl(context):
    assert context.driver.find_element(By.CSS_SELECTOR, ".message").text == "Complete la información correctamente."
    take_screenshot(context, 'I_should_see_a_alert_message')
    context.driver.close()

@when('I enter a lastname with numbers')
def step_impl(context):
    context.driver.find_element("name", "nombre").send_keys("Maria")
    context.driver.find_element("name", "apellido").send_keys("Lopez123")
    context.driver.find_element("name", "cedula").send_keys("1753951076")
    context.driver.find_element("name", "domicilio").send_keys("Chillogallo")
    context.driver.find_element("name", "telefono").send_keys("0995227606")
    context.driver.find_element("name", "email").send_keys("sianasco@espe.edu.ec")
    context.driver.find_element("name", "fecha_nacimiento").send_keys("07-04-2024")
    
    context.driver.find_element(By.CSS_SELECTOR, "button").click()
    take_screenshot(context, 'I_enter_a_lastname_with_numbers')

@when('I enter an excessively old birth date')
def step_impl(context):
    context.driver.find_element("name", "nombre").send_keys("Maria")
    context.driver.find_element("name", "apellido").send_keys("Lopez")
    context.driver.find_element("name", "cedula").send_keys("1753951076")
    context.driver.find_element("name", "domicilio").send_keys("Chillogallo")
    context.driver.find_element("name", "telefono").send_keys("0995227606")
    context.driver.find_element("name", "email").send_keys("sianasco@espe.edu.ec")
    context.driver.find_element("name", "fecha_nacimiento").send_keys("07-04-1800")
    
    context.driver.find_element(By.CSS_SELECTOR, "button").click()
    take_screenshot(context, 'I_enter_an_excessively_old_birth_date')

@when('I enter the birth date of a underage person')
def step_impl(context):
    context.driver.find_element("name", "nombre").send_keys("Maria")
    context.driver.find_element("name", "apellido").send_keys("Lopez")
    context.driver.find_element("name", "cedula").send_keys("1753951076")
    context.driver.find_element("name", "domicilio").send_keys("Chillogallo")
    context.driver.find_element("name", "telefono").send_keys("0995227606")
    context.driver.find_element("name", "email").send_keys("sianasco@espe.edu.ec")
    context.driver.find_element("name", "fecha_nacimiento").send_keys("07-04-2012")
    
    context.driver.find_element(By.CSS_SELECTOR, "button").click()
    take_screenshot(context, 'I_enter_the_birth_date_of_a_underage_person')


@when('I enter a negative number in id field')
def step_impl(context):
    context.driver.find_element("name", "nombre").send_keys("Maria")
    context.driver.find_element("name", "apellido").send_keys("Lopez")
    context.driver.find_element("name", "cedula").send_keys("-1")
    context.driver.find_element("name", "domicilio").send_keys("Chillogallo")
    context.driver.find_element("name", "telefono").send_keys("0995227606")
    context.driver.find_element("name", "email").send_keys("sianasco@espe.edu.ec")
    context.driver.find_element("name", "fecha_nacimiento").send_keys("07-04-2012")
    
    context.driver.find_element(By.CSS_SELECTOR, "button").click()
    take_screenshot(context, 'I_enter_a_negative_number_in_id_field')