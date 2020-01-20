## Ganhar o jogo

Vamos dar ao teu jogador uma missão, que precisa ser concluída para ganhar o jogo.

\--- task \---

In this game, the player wins by getting to the garden and escaping the house. They also need to have the key with them, and the magic potion. Here’s a map of the game.

![screenshot](images/rpg-final-map.png)

\--- /task \---

\--- task \---

First, you need to add a garden to the south of the dining room. Remember to add doors, to link to other rooms in the house.

## \--- code \---

language: python

## line_highlights: 16-17,18-22

# um dicionário a ligar uma divisāo a outras divisões

rooms = {

            'Entrada' : {
                'sul' : 'Cozinha',
                'este' : 'Sala Jantar',
                'item' : 'chave'
            },
    
            'Cozinha' : {
                'norte' : 'Entrada',
               'item' : 'monstro'
            },
    
            'Sala Jantar' : {
                'oeste' : 'Entrada',
                'sul' : 'Jardim"
            },
    
           'Jardim' : {
                'norte' : 'Sala Jantar'
           }
    
        }
    

\--- /code \---

\--- /task \---

\--- task \---

Add a potion to the dining room (or another room in your house).

## \--- code \---

language: python

## line_highlights: 3-4

            'Sala Jantar' : {
                'oeste' : 'Entrada',
                'sul' : 'Jardim",
                'item' : 'garrafa'
            },
    

\--- /code \---

\--- /task \---

\--- task \---

Add this code to allow the player to win the game when they get to the garden with the key and the potion:

## \--- code \---

language: python

## line_highlights: 6-9

# o jogador perde se entrar numa divisāo com um monstro

if 'item' in rooms\[currentRoom] and 'monster' in rooms[currentRoom\]\['item'\]: print('A monster has got you... GAME OVER!') break

# o jogador ganha se entrar no jardim com a chave e a garrafa de poçāo

if currentRoom == 'Garden' and 'key' in inventory and 'potion' in inventory: print('You escaped the house... YOU WIN!') break \--- /code \---

Make sure this code is indented, in line with the code above it. This code means that the message `You escaped the house...YOU WIN!` is displayed if the player is in room 4 (the garden) and if the key and the potion are in the inventory.

If you have more than 4 rooms, you may have to use a different room number for your garden in the code above.

\--- /task \---

\--- task \---

Test your game to make sure the player can win!

![screenshot](images/rpg-win-test.png)

\--- /task \---

\--- task \---

Finally, let’s add some instructions to your game, so that the player knows what they have to do. Edit the `showInstructions()` function to include more information.

## \--- code \---

language: python

## line_highlights: 7-8

def showInstructions(): #print a main menu and the commands print('''

# Jogo RPG

Get to the Garden with a key and a potion Avoid the monsters!

Commands: go [direction] get [item] ''') \--- /code \---

You will need to add instructions to tell the user what items they need to collect, and what they need to avoid!

\--- /task \---

\--- task \---

Test your game and you should see your new instructions.

![screenshot](images/rpg-instructions-test.png)

\--- /task \---