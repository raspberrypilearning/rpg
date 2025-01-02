## Adding new rooms

--- task ---
Open the [starter project](https://editor.raspberrypi.org/en/projects/rpg-starter){:target="_blank"}.
--- /task ---


This is a very basic RPG game that only has 2 rooms. Here’s a map of the game:

![A map with two rooms - hall is in the North and kitchen is below it. There is a door between them.](images/rpg-map1.png)

--- task ---
Press **Run** to start the game. Type `go south` to move from the hall to the kitchen, and then `go north` to go back to the hall again.
--- /task ---

--- task ---

What happens when you type in a direction that you cannot go? Type `go west` in the hall.

--- collapse ---
---
title: Answer
---
You'll see a friendly error message.

--- code ---
---
language: text
line_numbers: false
line_number_start: 
line_highlights: 
---
go west
You can't go that way!
---------------------------
You are in the Hall
Inventory : []
---------------------------
>
--- /code ---

--- /collapse ---
--- /task ---



Find the `rooms` variable, and you can see that the map is coded as a dictionary of rooms:

--- code ---
---
language: python
filename: main.py
line_numbers: true
line_number_start: 26
line_highlights: 
---
# A dictionary linking a room to other rooms
rooms = {
    'Hall' : {
        'south' : 'Kitchen'
    },
    'Kitchen' : {
        'north' : 'Hall'
    }
}
--- /code ---

Each room is a dictionary, and rooms are linked together using directions.  


--- task ---

Add a dining room to your map, to the east of the hall.

![A map with two rooms - hall is in the North and kitchen is below it. There is a door between them. A dining room has been added to the right of the hall.](images/rpg-dining.png)

--- code ---
---
language: python
filename: main.py
line_numbers: true
line_number_start: 26
line_highlights: 30, 34-37
---
#a dictionary linking a room to other rooms
rooms = {
    'Hall' : {
        'south' : 'Kitchen',
        'east' : 'Dining Room'
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

Try out the game with your new dining room:

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
---------------------------
>go east
---------------------------
You are in the Dining Room
Inventory : []
---------------------------
>go west
---------------------------
You are in the Hall
Inventory : []
---------------------------
>
--- /code ---

If you can’t move in and out of the dining room, just check that you added all of the code above (including the extra commas to the lines above).

--- /task ---
