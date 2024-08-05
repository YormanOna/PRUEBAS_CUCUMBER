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
    screenshot_dir = 'Requisito3/screenshots'
    os.makedirs(screenshot_dir, exist_ok=True)
    screenshot_path = os.path.join(screenshot_dir, f"{step_name}.png")
    context.driver.save_screenshot(screenshot_path)

@given('I navigate to the login page')
def step_impl(context):
    options = webdriver.ChromeOptions()
    context.driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()), options=options)
    context.driver.get("http://localhost:5173/login")
    take_screenshot(context, 'I_navigate_to_the_login_page')

@when('I enter valid credentials')
def step_impl(context):
    context.driver.find_element(By.NAME, "nombreUsuario").send_keys("MIGUEL")
    context.driver.find_element(By.NAME, "password").send_keys("4321")
    take_screenshot(context, 'I_enter_valid_credentials')
    submit_button = context.driver.find_element(By.ID, "login-submit-btn")
    WebDriverWait(context.driver, 10).until(EC.element_to_be_clickable((By.ID, "login-submit-btn")))
    submit_button.click()

@then('I should see a success message and navigate to the menu')
def step_impl(context):
    try:
        message = WebDriverWait(context.driver, 20).until(
            EC.presence_of_element_located((By.CSS_SELECTOR, ".butteruptoast.success .message"))
        ).text
        assert "Bienvenido al panel de administración." in message
        take_screenshot(context, 'I_should_see_a_success_message')
    except Exception as e:
        take_screenshot(context, 'I_should_see_a_success_message_fail')
        raise e
    finally:
        context.driver.quit()

@when('I leave all fields empty')
def step_impl(context):
    take_screenshot(context, 'I_leave_all_fields_empty')
    submit_button = context.driver.find_element(By.ID, "login-submit-btn")
    WebDriverWait(context.driver, 10).until(EC.element_to_be_clickable((By.ID, "login-submit-btn")))
    submit_button.click()

@then('I should see a message indicating fields are required')
def step_impl(context):
    try:
        # Intentional failure
        assert False, "Failing this scenario intentionally"
        error_messages = WebDriverWait(context.driver, 20).until(
            EC.presence_of_all_elements_located((By.CSS_SELECTOR, ".errors"))
        )
        assert any("El usuario es requerido" in error.text for error in error_messages), "El usuario es requerido error message not found"
        assert any("La contraseña es requerida" in error.text for error in error_messages), "La contraseña es requerida error message not found"
        take_screenshot(context, 'I_should_see_a_message_indicating_fields_are_required')
    except Exception as e:
        take_screenshot(context, 'I_should_see_a_message_indicating_fields_are_required_fail')
        raise e
    finally:
        context.driver.quit()

@when('I enter an invalid username')
def step_impl(context):
    context.driver.find_element(By.NAME, "nombreUsuario").send_keys("invalidUser")
    context.driver.find_element(By.NAME, "password").send_keys("4321")
    take_screenshot(context, 'I_enter_an_invalid_username')
    submit_button = context.driver.find_element(By.ID, "login-submit-btn")
    WebDriverWait(context.driver, 10).until(EC.element_to_be_clickable((By.ID, "login-submit-btn")))
    submit_button.click()

@then('I should see a username error message')
def step_impl(context):
    try:
        # Intentional failure
        assert False, "Failing this scenario intentionally"
        error_message = WebDriverWait(context.driver, 20).until(
            EC.presence_of_element_located((By.CSS_SELECTOR, ".butteruptoast.error .message"))
        ).text
        assert "Usuario o contraseña incorrectos." in error_message, "Usuario o contraseña incorrectos error message not found"
        take_screenshot(context, 'I_should_see_a_username_error_message')
    except Exception as e:
        take_screenshot(context, 'I_should_see_a_username_error_message_fail')
        raise e
    finally:
        context.driver.quit()

@when('I enter an invalid password')
def step_impl(context):
    context.driver.find_element(By.NAME, "nombreUsuario").send_keys("MIGUEL")
    context.driver.find_element(By.NAME, "password").send_keys("invalidPassword")
    take_screenshot(context, 'I_enter_an_invalid_password')
    submit_button = context.driver.find_element(By.ID, "login-submit-btn")
    WebDriverWait(context.driver, 10).until(EC.element_to_be_clickable((By.ID, "login-submit-btn")))
    submit_button.click()

@then('I should see a password error message')
def step_impl(context):
    try:
        # Intentional failure
        assert False, "Failing this scenario intentionally"
        error_message = WebDriverWait(context.driver, 20).until(
            EC.presence_of_element_located((By.CSS_SELECTOR, ".butteruptoast.error .message"))
        ).text
        assert "Usuario o contraseña incorrectos." in error_message, "Usuario o contraseña incorrectos error message not found"
        take_screenshot(context, 'I_should_see_a_password_error_message')
    except Exception as e:
        take_screenshot(context, 'I_should_see_a_password_error_message_fail')
        raise e
    finally:
        context.driver.quit()

@when('I enter invalid credentials')
def step_impl(context):
    context.driver.find_element(By.NAME, "nombreUsuario").send_keys("invalidUser")
    context.driver.find_element(By.NAME, "password").send_keys("invalidPassword")
    take_screenshot(context, 'I_enter_invalid_credentials')
    submit_button = context.driver.find_element(By.ID, "login-submit-btn")
    WebDriverWait(context.driver, 10).until(EC.element_to_be_clickable((By.ID, "login-submit-btn")))
    submit_button.click()

@then('I should see an invalid credentials error message')
def step_impl(context):
    try:
        # Intentional failure
        assert False, "Failing this scenario intentionally"
        error_message = WebDriverWait(context.driver, 20).until(
            EC.presence_of_element_located((By.CSS_SELECTOR, ".butteruptoast.error .message"))
        ).text
        assert "Usuario o contraseña incorrectos." in error_message, "Usuario o contraseña incorrectos error message not found"
        take_screenshot(context, 'I_should_see_an_invalid_credentials_error_message')
    except Exception as e:
        take_screenshot(context, 'I_should_see_an_invalid_credentials_error_message_fail')
        raise e
    finally:
        context.driver.quit()
