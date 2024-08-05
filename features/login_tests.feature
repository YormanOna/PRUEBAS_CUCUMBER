Feature: Login 

Scenario: Login exitoso
  Given I navigate to the login page
  When I enter valid credentials
  Then I should see a success message and navigate to the menu

Scenario: Campos vacios
  Given I navigate to the login page
  When I leave all fields empty
  Then I should see a message indicating fields are required

Scenario: Username invalido
  Given I navigate to the login page
  When I enter an invalid username
  Then I should see a username error message

Scenario: Contrasena invalida
  Given I navigate to the login page
  When I enter an invalid password
  Then I should see a password error message

Scenario: Credenciales invalidas
  Given I navigate to the login page
  When I enter invalid credentials
  Then I should see an invalid credentials error message