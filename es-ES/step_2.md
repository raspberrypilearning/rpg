## Añadir nuevas habitaciones

+ Parte de los códigos de este juego son proporcionados. Escribe este trinket: <a href="http://jumpto.cc/rpg-go" target="_blank">jumpto.cc/rpg-go</a>. 

+ Este juego RPG es muy básico y solamente posee 2 habitaciones. Aquí tienes un mapa del juego:

  ![screenshot](images/rpg-map1.png)

  ¡Puedes escribir `go south` para moverte desde el pasillo a la cocina y, a continuación, `go north` para regresar al pasillo!

  ![screenshot](images/rpg-controls.png)

+ ¿Qué ocurre cuando anotas una dirección a la que no puedes dirigirte? Escribe `go west` en el pasillo y obtendrás un mensaje amistoso de error.

  ![screenshot](images/rpg-error.png)

+ Si encuentras la variable `rooms`, podrás ver que el mapa está codificado como un diccionario de habitaciones:

  ![screenshot](images/rpg-rooms.png)

  Cada habitación es un diccionario y las habitaciones están interconectadas mediante direcciones.  
  

+ Añadamos un comedor a tu mapa al este del pasillo.

  ![screenshot](images/rpg-dining.png)

  Necesitarás añadir una 3.ª habitación denominada `dining room`. También necesitarás enlazarla con el pasillo hacia el oeste. También necesitarás añadir datos al pasillo de modo que puedas moverte al comedor hacia el este.
  
  ![screenshot](images/rpg-dining-code.png)

+ Prueba el juego con tu nuevo comedor:

  ![screenshot](images/rpg-dining-test.png)

  Si no puedes entrar ni salir del comedor, comprueba si has añadido todo el código anterior (incluyendo las comas adicionales en las líneas anteriores).
