Feature: Catalogo de servicios

Scenario: Ver la imagen de inicio del menú de bartender
  Given navego a la página del menú
  When selecciono el servicio de bartender
  Then debería ver la imagen de inicio del menú de bartender

Scenario: Ver la imagen de fin del menú de bartender
  Given navego a la página del menú
  When selecciono el servicio de bartender
  And navego a la última página del menú de bartender
  Then debería ver la imagen de fin del menú de bartender

Scenario: Volver a la imagen de inicio del menú de bartender desde la última página
  Given navego a la página del menú
  When selecciono el servicio de bartender
  And navego a la última página del menú de bartender
  And vuelvo a la primera página del menú de bartender desde la última página
  Then debería ver nuevamente la imagen de inicio del menú de bartender

Scenario: Ver el componente de catering
  Given navego a la página del menú
  When selecciono el servicio de catering y navego a la sección de catering
  Then debería ver el componente de catering
