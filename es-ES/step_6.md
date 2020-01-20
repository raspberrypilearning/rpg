## Añadir enemigos

¡Este juego es muy fácil! Agreguemos enemigos a algunas habitaciones, que el jugador deberá evitar.

\--- task \---

Adding an enemy to a room is as easy as adding any other item. Let’s add a hungry monster to the kitchen:

## \--- code \---

language: python

## line_highlights: 11-12

# un diccionario que une una habitacion a las posiciones de las otras habitaciones

rooms = {

            'Sala': {
            'sur': 'Cocina',
            'este': 'Comedor',
            'objeto': 'llave'
        },
    
        'Cocina': {
            'norte': 'Sala',
            'objeto': 'monstruo'
        },
    
        'Comedor': {
            'oeste': 'Sala'
        }
    
    
    }
    

\--- /code \---

\--- /task \---

\--- task \---

You also want to make sure that the game ends if the player enters a room with a monster in. You can do this with the following code, which you should add to the end of the game:

## \--- code \---

language: python

## line_highlights: 6-9

        #Por el contrario, si el objeto que se quiere no esta en la habitación
        else:
        #diles que no pueden cogerlo
        print('¡No puedes coger el/la ' + movimiento[1] + '!')
    
    #el jugador pierde si entra en una habitación con un monstruo
    if 'objeto' in habitaciones[habitacionActual] and 'monstruo' in habitaciones[habitacionActual]['objeto']:
        print('Te ha pillado el monstruo... JUEGO TERMINADO!')
        break
    

\--- /code \---

This code checks whether there is an item in the room, and if so, whether that item is a monster. Notice that this code is indented, putting it in line with the code above it. This means that the game will check for a monster every time the player moves into a new room.

\--- /task \---

\--- task \---

Test out your code by going into the kitchen, which now contains a monster.

![screenshot](images/rpg-monster-test.png)

\--- /task \---