## Añadir enemigos

¡Este juego es muy fácil! Agreguemos enemigos a algunas habitaciones, que el jugador deberá evitar.

+ Añadir un enemigo a una habitación es tan fácil como agregar cualquier otro objeto. Añadamos un monstruo hambriento a la cocina:
    
    ![captura de pantalla](images/rpg-monster-dict.png)

+ También quieres asegurarte de que el juego termine si el jugador entra a una habitación que contiene un monstruo. Puedes hacerlo con el siguiente código, que debes añadir al final del juego:
    
    ![captura de pantalla](images/rpg-monster-code.png)
    
    Este código verifica si hay un objeto en la habitación, y en caso afirmativo, si ese objeto es un monstruo. Date cuenta que el código tiene sangría, poniéndolo en línea con el código encima de él. Esto significa que el juego va a verificar si hay un monstruo cada vez que el jugador entra a una nueva habitación.

+ Prueba tu código yendo a la cocina, que ahora contiene un monstruo.
    
    ![captura de pantalla](images/rpg-monster-test.png)