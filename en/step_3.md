## Add items to collect

Add items in the rooms for the player to collect as they move through the maze.

--- task ---

To put an item in a room, you add it to a room's dictionary. Add a key in the Hall.

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
--- /code ---

Remember to put a comma after the line above the new item, or your program won’t run!

--- /task ---

--- task ---

Press **Stop** and then **Run**, and you can now see a key in the Hall. You can even pick it up (by typing `get key`) which adds it to your inventory!

--- /task ---

