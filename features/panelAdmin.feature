Feature: Panel de administración

Scenario: Ver el gestor de cocteles
  Given navego al panel de administración
  When selecciono la pestaña de cocteles
  Then debería ver el gestor de cocteles

Scenario: Agregar un nuevo coctel
  Given navego al panel de administración
  When selecciono la pestaña de cocteles
  And agrego un nuevo coctel
  Then debería ver el nuevo coctel en la lista

Scenario: Eliminar un coctel
  Given navego al panel de administración
  When selecciono la pestaña de cocteles
  And elimino un coctel
  Then debería ver el coctel eliminado de la lista

Scenario: Ver el gestor de paquetes
  Given navego al panel de administración
  When selecciono la pestaña de paquetes
  Then debería ver el gestor de paquetes
