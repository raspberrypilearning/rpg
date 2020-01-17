## Agregar elementos para recoger

Dejemos objetos en las habitaciones para que el jugador recoja a medida que se mueve por el laberinto.

\--- task \--- Agregar un objeto a una habitación es fácil, simplemente agrégalo al diccionario de la habitación. Pongamos una llave en la sala.

¡Recuerda poner una coma después de la línea de objeto nuevo, o tu programa no va a funcionar!

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

\--- task \--- Si ejecutas tu programa después de añadir el código de arriba, vas a poder ver una llave en la sala, e incluso podrás cogerla (escribiendo `coger llave`) lo que la añadirá a tu inventario!

![captura de pantalla](images/rpg-key-test.png) \--- /task \---