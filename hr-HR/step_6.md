## Dodavanje neprijatelja

Ova igra je prejednostavna! Dodajmo u neke od prostorija neprijatelje koje će igrač izbjegavati.

\--- task \---

Adding an enemy to a room is as easy as adding any other item. Let’s add a hungry monster to the kitchen:

## \--- code \---

language: python

## line_highlights: 11-12

# rječnik koji povezuje prostorije jednu s drugom

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
    

\--- /code \---

\--- /task \---

\--- task \---

You also want to make sure that the game ends if the player enters a room with a monster in. You can do this with the following code, which you should add to the end of the game:

## \--- code \---

language: python

## line_highlights: 6-9

        #u suprotnom, ako predmet nije tu za nabaviti
        else:
            #tell them they can't get it
            print('Can\'t get' + move[1] + '!')
    
    #igrač gubi ako uđe u sobu s čudovištem
    if 'item' in rooms[currentRoom] and 'monster' in rooms[currentRoom]['item']:
        print('Čudovište te uhvatilo... IGRA JE GOTOVA!')
        break
    

\--- /code \---

This code checks whether there is an item in the room, and if so, whether that item is a monster. Notice that this code is indented, putting it in line with the code above it. This means that the game will check for a monster every time the player moves into a new room.

\--- /task \---

\--- task \---

Test out your code by going into the kitchen, which now contains a monster.

![screenshot](images/rpg-monster-test.png)

\--- /task \---