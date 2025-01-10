## Add enemies

Add enemies to some rooms that the player must avoid.

--- task ---

Adding an enemy to a room is the same as adding an item. Add a monster to the Kitchen:

--- code ---
---
language: python
line_numbers: true
line_number_start: 29
line_highlights: 33-34
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

If the player enters a room with a monster in, the game ends. Test out your code by going into the Kitchen, which now contains a monster.

--- task ---
Click **Stop** then click **Run** and type `go south`.

--- code ---
---
language: text
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
