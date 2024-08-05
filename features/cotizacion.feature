Feature: Cotización Automatica

Scenario: Generar una cotización detallada
  Given navego a la página de cotización
  When selecciono un servicio y una fecha y genero la cotización
  Then debería ver la cotización detallada

Scenario: Generar una cotización sin llenar todos los campos
  Given navego a la página de cotización
  When no lleno todos los campos y genero la cotización
  Then debería ver un mensaje de error

Scenario: Generar una cotización con extras
  Given navego a la página de cotización
  When selecciono un servicio, una fecha, y extras y genero la cotización
  Then debería ver la cotización detallada con los extras

Scenario: Generar una cotización sin seleccionar servicio
  Given navego a la página de cotización
  When genero la cotización sin seleccionar servicio
  Then debería ver un mensaje de error por falta de servicio
