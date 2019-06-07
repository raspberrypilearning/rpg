## Agregar elementos para recoger

Dejemos objetos en las habitaciones para que el jugador recoja a medida que se mueve por el laberinto.

\--- task \--- Adding an item into a room is easy, you can just add it to a room's dictionary. Pongamos una llave en la sala.

¡Recuerda poner una coma después de la línea de objeto nuevo, o tu programa no va a funcionar!

## \--- code \---

language: python

## line_highlights: 6-7

# un diccionario que une una habitacion a las posiciones de las otras habitaciones

rooms = {

            'Hall' : {
                'south' : 'Kitchen',
                'east' : 'Dining Room',
                'item' : 'key'
            },
    
            'Kitchen' : {
                'north' : 'Hall'
            },
    
            'Dining Room' : {
                'west' : 'Hall'
            }
    
        }
    

\--- /code \---

\--- /task \---

\--- task \--- If you run your game after adding the code above, you can now see a key in the hall, and you can even pick it up (by typing `get key`) which adds it to your inventory!

![captura de pantalla](images/rpg-key-test.png) \--- /task \---