## Winning the game

Let’s give your player a mission, which needs to completed to win the game.

--- task ---

In this game, the player wins by getting to the garden and escaping the house. They also need to have the key with them, and the magic potion. Here’s a map of the game.

![screenshot](images/rpg-final-map.png)

--- /task ---

--- task ---

First, you need to add a garden to the south of the dining room. Remember to add doors, to link to other rooms in the house.

--- code ---
---
language: python
filename: main.py
line_numbers: true
line_number_start: 26
line_highlights: 38-43
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
    'Dining Room' : {
        'west' : 'Hall',
        'south' : 'Garden'
    },
    'Garden' : {
        'north' : 'Dining Room'
    }
}
--- /code ---

--- /task ---

--- task ---

Add a potion to the dining room (or another room in your house).

--- code ---
---
language: python
filename: main.py
line_numbers: true
line_number_start: 37
line_highlights: 39-40
---
    'Dining Room' : {
        'west' : 'Hall',
        'south' : 'Garden',
        'item' : 'potion'
    },
--- /code ---

--- /task ---

--- task ---

Add this code to allow the player to win the game when they get to the garden with the key and the potion:

--- code ---
---
language: python
filename: main.py
line_numbers: true
line_number_start: 91
line_highlights: 95-98
---
    #player loses if they enter a room with a monster
    if 'item' in rooms[currentRoom] and 'monster' in rooms[currentRoom]['item']:
        print('A monster has got you... GAME OVER!')
        break
    #player wins is they get to the garden with the key and potion
    if currentRoom == 'Garden' and 'key' in inventory and 'potion' in inventory:
        print('You escaped the house... YOU WIN!')
        break
--- /code ---

Make sure this code is indented, in line with the code above it. This code means that the message `You escaped the house...YOU WIN!` is displayed if the player is in room 4 (the garden) and if the key and the potion are in the inventory.

If you have more than 4 rooms, you may have to use a different room number for your garden in the code above.

--- /task ---

--- task ---

Test your game to make sure the player can win!

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
>get key
key got!
---------------------------
You are in the Hall
Inventory : ['key']
---------------------------
>go east
---------------------------
You are in the Dining Room
Inventory : ['key']
You see a potion
---------------------------
>get potion
potion got!
---------------------------
You are in the Dining Room
Inventory : ['key', 'potion']
---------------------------
>go south
You escaped the house... YOU WIN!
--- /code ---

--- /task ---

--- task ---

Finally, let’s add some instructions to your game, so that the player knows what they have to do. Edit the `showInstructions()` function to include more information.

--- code ---
---
language: python
filename: main.py
line_numbers: true
line_number_start: 1
line_highlights: 7-8
---
def showInstructions():
    #print a main menu and the commands
    print('''
          RPG Game
          ========
          
          Get to the Garden with a key and a potion
          Avoid the monsters!
          
          Commands:
          go [direction]
          get [item]
          ''')
--- /code ---

You will need to add instructions to tell the user what items they need to collect, and what they need to avoid!

--- /task ---

--- task ---

Test your game and you should see your new instructions.

--- code ---
---
language: text
filename: main.py
line_numbers: false
line_number_start: 
line_highlights: 
---
RPG Game
========

Get to the Garden with a key and a potion
Avoid the monsters!

Commands:
go [direction]
get [item]

--- /code ---

--- /task ---
