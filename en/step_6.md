## Adding enemies

This game is too easy! Let’s add enemies to some rooms that the player must avoid.

--- task ---

Adding an enemy to a room is as easy as adding any other item. Let’s add a hungry monster to the kitchen:

--- code ---
---
language: python
filename: main.py
line_numbers: true
line_number_start: 26
line_highlights: 35
---
#a dictionary linking a room to other rooms
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
--- /code ---

--- /task ---

--- task ---

You also want to make sure that the game ends if the player enters a room with a monster in. You can do this with the following code, which you should add to the end of the game:

--- code ---
---
language: python
filename: main.py
line_numbers: true
line_number_start: 83
line_highlights: 86-89
---
        else:
            #tell them they can't get it
            print('Can\'t get ' + move[1] + '!')
    #player loses if they enter a room with a monster
    if 'item' in rooms[currentRoom] and 'monster' in rooms[currentRoom]['item']:
        print('A monster has got you... GAME OVER!')
        break
--- /code ---

This code checks whether there is an item in the room, and if so, whether that item is a monster. Notice that this code is indented, putting it in line with the code above it. This means that the game will check for a monster every time the player moves into a new room.

--- /task ---

--- task ---

Test out your code by going into the kitchen, which now contains a monster.

--- code ---
---
language: text
filename: main.py
line_numbers: false
line_number_start: 
line_highlights: 
---
---------------------------
You are in the Hall
Inventory : []
You see a key
---------------------------
>go south

A monster has got you... GAME OVER!
--- /code ---

--- /task ---
