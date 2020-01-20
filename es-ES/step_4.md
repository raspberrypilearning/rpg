## Agregar elementos para recoger

Dejemos objetos en las habitaciones para que el jugador recoja a medida que se mueve por el laberinto.

\--- task \---

Adding an item into a room is easy, you can just add it to a room's dictionary. Let’s put a key in the hall.

Remember to put a comma after the line above the new item, or your program won’t run!

## \--- code \---

language: python

## line_highlights: 6-7

# un diccionario que une una habitacion a las posiciones de las otras habitaciones

rooms = {

            'Sala' : {
                'sur' : 'Cocina',
                'este' : 'Comedor',
                'objeto' : 'llave'
            },
    
            'Cocina' : {
                'norte' : 'Sala'
            },
    
            'Comedor' : {
                'oeste' : 'Sala'
            }
    
        }
    

\--- /code \---

\--- /task \---

\--- task \---

If you run your game after adding the code above, you can now see a key in the hall, and you can even pick it up (by typing `get key`) which adds it to your inventory!

![screenshot](images/rpg-key-test.png)

\--- /task \---