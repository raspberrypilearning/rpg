## Ganar el juego

Demos a tu jugador una misión que necesita completar para ganar el juego.

\--- task \--- In this game, the player wins by getting to the garden and escaping the house. También van a necesitar tener una llave y una poción mágica con ellos. Aquí hay un mapa del juego.

![captura de pantalla](images/rpg-final-map.png) \--- /task \---

\--- task \--- First, you need to add a garden to the south of the dining room. Recuerda añadir puertas, para unirlo a otras habitaciones de la casa.

## \--- code \---

language: python

## line_highlights: 16-17,18-22

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
                'west' : 'Hall',
                'south' : 'Garden'
            },
    
            'Garden' : {
                'north' : 'Dining Room'
            }
    
        }
    

\--- /code \--- \--- /task \---

\--- task \--- Add a potion to the dining room (or another room in your house).

## \--- code \---

language: python

## line_highlights: 3-4

            'Dining Room' : {
                'west' : 'Hall',
                'south' : 'Garden',
                'item' : 'potion'
            },
    

\--- /code \--- \--- /task \---

\--- task \--- Add this code to allow the player to win the game when they get to the garden with the key and the potion:

## \--- code \---

language: python

## line_highlights: 6-9

# el jugador pierde si entra a una habitacion con un monstruo

if 'item' in rooms\[currentRoom] and 'monster' in rooms[currentRoom\]\['item'\]: print('A monster has got you... GAME OVER!') break

# player wins is they get to the garden with the key and potion

if currentRoom == 'Garden' and 'key' in inventory and 'potion' in inventory: print('You escaped the house... YOU WIN!') break \--- /code \---

Asegúrate de que el código tiene sangría, estando en línea con el código de arriba. Este código quiere decir que el mensaje `Te escapaste de la casa... ¡GANASTE!` si el jugador está en la habitación 4 (el jardín) y si la llave y la poción están en su inventario.

Si tienes más de 4 habitaciones, puedes utilizar un número diferente para tu jardín en el código de arriba. \--- /task \---

\--- task \--- Test your game to make sure the player can win!

![captura de pantalla](images/rpg-win-test.png) \--- /task \---

\--- task \--- Finally, let’s add some instructions to your game, so that the player knows what they have to do. Edita la función `showInstructions()` para incluir más información.

## \--- code \---

language: python

## line_highlights: 7-8

def showInstructions(): #print a main menu and the commands print('''

# Juego RPG

Get to the Garden with a key and a potion Avoid the monsters!

Commands: go [direction] get [item] ''') \--- /code \---

¡Vas a necesitar añadir instrucciones para decirle al usuario qué objetos necesitan recoger y qué necesitan evitar! \--- /task \---

\--- task \--- Test your game and you should see your new instructions.

![captura de pantalla](images/rpg-instructions-test.png) \--- /task \---