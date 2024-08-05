Feature: Funcionalidad del calendario

Scenario: Ver la información de la fecha seleccionada
  Given navego a la página del calendario
  When selecciono una fecha disponible
  Then debería ver la información de la fecha seleccionada

Scenario: Intentar seleccionar una fecha reservada
  Given navego a la página del calendario
  When intento seleccionar una fecha reservada
  Then debería ver un mensaje de error

Scenario: Seleccionar una fecha con disponibilidad limitada
  Given navego a la página del calendario
  When selecciono una fecha con disponibilidad limitada
  Then debería ver un mensaje de disponibilidad limitada

Scenario: Hacer clic en reservar ahora
  Given navego a la página del calendario
  When hago clic en reservar ahora
  Then debería ver la página de reserva
