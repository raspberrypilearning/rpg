## Add items to collect

Let’s leave items in the rooms for the player to collect as they move through the maze.

--- task ---

Adding an item into a room is easy, you can just add it to a room's dictionary. Let’s put a key in the hall.

Remember to put a comma after the line above the new item, or your program won’t run!

--- code ---
---
language: python
filename: main.py
line_numbers: true
line_number_start: 26
line_highlights: 31
---
#a dictionary linking a room to other rooms
rooms = {
    'Hall' : {
        'south' : 'Kitchen',
        'east' : 'Dining Room',
        'item' : 'key'
    },
--- /code ---

--- /task ---

--- task ---

If you run your game after adding the code above, you can now see a key in the hall, and you can even pick it up (by typing `get key`) which adds it to your inventory!

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
          Commands:
          go [direction]
          get [item]
          
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
>
--- /code ---

--- /task ---
