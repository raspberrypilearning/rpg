## Ganar el juego

Demos a tu jugador una misión que necesita completar para ganar el juego.

+ En este juego, el jugador gana al llegar al jardín y escapar de la casa. También van a necesitar tener una llave y una poción mágica con ellos. Aquí hay un mapa del juego.
    
    ![captura de pantalla](images/rpg-final-map.png)

+ Primero, necesitas agregar un jardín al sur del comedor. Recuerda añadir puertas, para unirlo a otras habitaciones de la casa.
    
    ![captura de pantalla](images/rpg-garden.png)

+ Agrega una poción al comedor (u otra habitación de tu casa).
    
    ![captura de pantalla](images/rpg-potion.png)

+ Agrega este código para permitir que el jugador gane cuando llegue al jardín con la llave y la poción:
    
    ![captura de pantalla](images/rpg-win-code.png)
    
    Asegúrate de que el código tiene sangría, estando en línea con el código de arriba. Este código quiere decir que el mensaje `Te escapaste de la casa... ¡GANASTE!` si el jugador está en la habitación 4 (el jardín) y si la llave y la poción están en su inventario.
    
    Si tienes más de 4 habitaciones, puedes utilizar un número diferente para tu jardín en el código de arriba.

+ ¡Prueba tu juego para asegurarte de que el jugador puede ganar!
    
    ![captura de pantalla](images/rpg-win-test.png)

+ Finalmente, agreguemos instrucciones al juego, así el jugador sabe qué tiene que hacer. Edita la función `showInstructions()` para incluir más información.
    
    ![captura de pantalla](images/rpg-instructions-code.png)
    
    ¡Vas a necesitar añadir instrucciones para decirle al usuario qué objetos necesitan recoger y qué necesitan evitar!

+ Prueba tu juego y vas a ver tus nuevas instrucciones.
    
    ![captura de pantalla](images/rpg-instructions-test.png)