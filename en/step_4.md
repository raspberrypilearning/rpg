## Adding items to collect

Let’s leave items in the rooms for the player to collect as they move through the maze.

--- task ---

Adding an item into a room is easy, you can just add it to a room's dictionary. Let’s put a key in the hall.

Remember to put a comma after the line above the new item, or your program won’t run!

--- code ---
---
language: python
line_highlights: 6-7
---
#a dictionary linking a room to other rooms
rooms = {

            'Hall' : {
                'south' : 'Kitchen',
                'east' : 'Dining Room',
                'item' : 'key'
            },

            'Kitchen' : {
                'north' : 'Hall'
            },

            'Dining Room' : {
                'west' : 'Hall'
            }

        }
--- /code ---

--- /task ---

--- task ---

If you run your game after adding the code above, you can now see a key in the hall, and you can even pick it up (by typing `get key`) which adds it to your inventory!

![screenshot](images/rpg-key-test.png)

--- /task ---
