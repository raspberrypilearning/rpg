## Ajoute des adversaires

Ce jeu est trop facile! Ajoutons des adversaires à quelques unes des pièces que le joueur doit éviter.

\--- task \---

Adding an enemy to a room is as easy as adding any other item. Let’s add a hungry monster to the kitchen:

## \--- code \---

language: python

## line_highlights: 11-12

# un dictionnaire liant une pièce à d'autres pièces

rooms = {

            'Hall' : {
                'sud' : 'Cuisine',
                'est' : 'Salle a manger',
                'objet' : 'clé'
            },
    
            'Cuisine' : {
                'nord' : 'Hall',
                'objet' : 'monstre'
            },
    
            'Salle a manger' : {
                'ouest' : 'Hall'
            }
    
        }
    

\--- /code \---

\--- /task \---

\--- task \---

You also want to make sure that the game ends if the player enters a room with a monster in. You can do this with the following code, which you should add to the end of the game:

## \--- code \---

language: python

## line_highlights: 6-9

        #sinon, si l'objet n'est pas là à obtenir
        else:
            #dis leur qu'ils ne peuvent pas l'obtenir
            print('Tu ne peux pas l avoir' + move[1] + '!')
    
    #le joueur perd s'ils entrent dans une pièce avec un monstre
    if 'objet' in rooms[currentRoom] and 'monstre' in rooms[currentRoom]['objet']:
        print('Un monstre t a attrapé... GAME OVER!')
        break
    

\--- /code \---

This code checks whether there is an item in the room, and if so, whether that item is a monster. Notice that this code is indented, putting it in line with the code above it. This means that the game will check for a monster every time the player moves into a new room.

\--- /task \---

\--- task \---

Test out your code by going into the kitchen, which now contains a monster.

![screenshot](images/rpg-monster-test.png)

\--- /task \---