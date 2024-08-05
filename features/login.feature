Feature: Registro de usuarios

  Scenario: Registro exitoso
    Given I navigate to the register page
    When I enter valid data for each field
    Then I should see a confirmation message

  Scenario: Campos en blanco
    Given I navigate to the register page
    When I leave all fields empty
    Then I should see a message

  Scenario: Nombre con números
    Given I navigate to the register page
    When I enter a name with numbers
    Then I should see a alert message

  Scenario: Apellido con números
    Given I navigate to the register page
    When I enter a lastname with numbers
    Then I should see a alert message

  Scenario: Fechas de nacimiento muy antiguas
    Given I navigate to the register page
    When I enter an excessively old birth date
    Then I should see a alert message

  Scenario: Edad menor a 18 años
    Given I navigate to the register page
    When I enter the birth date of an underage person
    Then I should see an underage validation message

  Scenario: Cedula con valor negativo
    Given I navigate to the register page
    When I enter a negative number in id field
    Then I should see an id validation message
