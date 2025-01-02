## Add enemies

Add enemies to some rooms that the player must avoid.

--- task ---

Adding an enemy to a room is the same as adding an item. Add a hungry monster to the kitchen:

--- code ---
---
language: python
line_numbers: true
line_number_start: 26
line_highlights: 35
---
# A dictionary linking a room to other rooms
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

If the player enters a room with a monster in, the game ends. Add this code to the end of the game:

--- code ---
---
language: python
line_numbers: true
line_number_start: 83
line_highlights: 86-89
---
        else:
            # Tell them they can't get it
            print('Can\'t get ' + move[1] + '!')
    # Player loses if they enter a room with a monster
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
