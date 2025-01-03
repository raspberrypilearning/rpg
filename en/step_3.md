## Add items to collect

Add items in the rooms for the player to collect as they move through the maze.

--- task ---

To put an item in a room, you add it to a room's dictionary. Add a key in the hall.

--- code ---
---
language: python
line_numbers: true
line_number_start: 25
line_highlights: 29-30
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

Press **Stop** and then **Run**, and you can now see a key in the hall. You can even pick it up (by typing `get key`) which adds it to your inventory!

--- /task ---

--- task ---
Add an item to another room in your game. You can add anything that you think would be helpful in trying to escape the house! For example, a shield or a magic potion.
--- /task ---