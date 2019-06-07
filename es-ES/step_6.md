## Añadir enemigos

¡Este juego es muy fácil! Agreguemos enemigos a algunas habitaciones, que el jugador deberá evitar.

\--- task \--- Adding an enemy to a room is as easy as adding any other item. Añadamos un monstruo hambriento a la cocina:

## \--- code \---

language: python

## line_highlights: 11-12

# un diccionario que une una habitacion a las posiciones de las otras habitaciones

rooms = {

            'Hall' : {
                'south' : 'Kitchen',
                'east' : 'Dining Room',
                'item' : 'key'
            },
    
            'Kitchen' : {
                'north' : 'Hall',
                'item' : 'monster'
            },
    
            'Dining Room' : {
                'west' : 'Hall'
            }
    
        }
    

\--- /code \--- \--- /task \---

\--- task \--- You also want to make sure that the game ends if the player enters a room with a monster in. Puedes hacerlo con el siguiente código, que debes añadir al final del juego:

## \--- code \---

language: python

## line_highlights: 6-9

        #otherwise, if the item isn't there to get
        else:
            #tell them they can't get it
            print('Can\'t get' + move[1] + '!')
    
    #player loses if they enter a room with a monster
    if 'item' in rooms[currentRoom] and 'monster' in rooms[currentRoom]['item']:
        print('A monster has got you... GAME OVER!')
        break
    

\--- /code \---

Este código verifica si hay un objeto en la habitación, y en caso afirmativo, si ese objeto es un monstruo. Date cuenta que el código tiene sangría, poniéndolo en línea con el código encima de él. Esto significa que el juego va a verificar si hay un monstruo cada vez que el jugador entra a una nueva habitación. \--- /task \---

\--- task \--- Test out your code by going into the kitchen, which now contains a monster.

![captura de pantalla](images/rpg-monster-test.png) \--- /task \---