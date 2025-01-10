## Add a new room

--- task ---
Open the [starter project](https://editor.raspberrypi.org/en/projects/rpg-starter){:target="_blank"}.
--- /task ---


Here is a basic maze that represents a house with two rooms. The rooms are both empty for now. Here’s a map of the game:

![A map with two rooms - hall is in the North and kitchen is below it. There is a door between them.](images/rpg-map1.png)

--- task ---
Press **Run** to start the game. Type `go south` to move from the Hall to the Kitchen, and then `go north` to go back to the Hall again.
--- /task ---

--- task ---

What happens when you type in a direction that you cannot go? Type `go west` in the Hall.

--- collapse ---
---
title: Answer
---
You'll see a friendly error message, and a reminder of where you are plus any items in your inventory.

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


Look at the code and find the `rooms` variable. The map is coded as a **dictionary** of rooms:

--- code ---
---
language: python
line_numbers: true
line_number_start: 29
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

Add a Dining Room to your map, to the east of the Hall. **Don't forget to add a comma to the end of the previous line when you add a new direction.**

![A map with two rooms - hall is in the North and kitchen is below it. There is a door between them. A dining room has been added to the right of the hall.](images/rpg-dining.png)

--- code ---
---
language: python
line_numbers: true
line_number_start: 29
line_highlights: 32-33, 37-40
---
# A dictionary linking a room to other rooms
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

Click **Stop**, then click **Run** to try out the game with your new Dining Room code. 

Type `go east` from the Hall to move into to the Dining Room, and `go west` to move back to the Hall.

--- /task ---

