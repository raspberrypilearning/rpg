## Adding new rooms

--- task ---

Open the Python starter project.

**Online**: open the [starter project](https://editor.raspberrypi.org/en/projects/rpg-starter){:target="_blank"}.

**Offline**: open the [starter project](https://rpf.io/p/en/rpg-go){:target="_blank"} in the offline editor.

--- /task ---

--- task ---

This is a very basic RPG game that only has 2 rooms. Here’s a map of the game:

![screenshot](images/rpg-map1.png)

You can type `go south` to move from the hall to the kitchen, and then `go north` to go back to the hall again!

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
>
--- /code ---

--- /task ---

--- task ---

What happens when you type in a direction that you cannot go? Type `go west` in the hall and you’ll get a friendly error message.

--- code ---
---
language: text
filename: main.py
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

--- /task ---

--- task ---

If you find the `rooms` variable, you can see that the map is coded as a dictionary of rooms:

--- code ---
---
language: python
filename: main.py
line_numbers: true
line_number_start: 26
line_highlights: 
---
#a dictionary linking a room to other rooms
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

--- /task ---

--- task ---

Let’s add a dining room to your map, to the east of the hall.

![screenshot](images/rpg-dining.png)

You need to add a 3rd room, called the `dining room`, and link it to the hall (to the west). You also need to add data to the hall, so that you can move to the dining room to the east.

**Don't forget that you'll also need to add commas to lines before your new code.**

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
