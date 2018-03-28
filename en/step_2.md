## Adding new rooms

--- task ---

Some code for this game has been provided for you. pen this trinket: <a href="http://jumpto.cc/rpg-go" target="_blank">jumpto.cc/rpg-go</a>. 

--- /task ---

--- task ---

This is a very basic RPG game that only has 2 rooms. Here’s a map of the game:

 ![screenshot](images/rpg-map1.png)

 You can type `go south` to move from the hall to the kitchen, and then `go north` to go back to the hall again!

 ![screenshot](images/rpg-controls.png)

--- /task ---

--- task ---

What happens when you type in a direction that you cannot go? Type `go west` in the hall and you’ll get a friendly error message.

 ![screenshot](images/rpg-error.png)

--- /task ---

--- task ---

If you find the `rooms` variable, you can see that the map is coded as a dictionary of rooms:

 ![screenshot](images/rpg-rooms.png)

 Each room is a dictionary and rooms are linked together using directions.  
 

--- /task ---

--- task ---

Let’s add a dining room to your map, to the east of the hall.

 ![screenshot](images/rpg-dining.png)

 You need to add a 3rd room, called the `dining room`. You also need to link it to the hall to the west. You also need to add data to the hall, so that you can move to the dining room to the east.
 
 ![screenshot](images/rpg-dining-code.png)

--- /task ---

--- task ---

Try out the game with your new dining room:

 ![screenshot](images/rpg-dining-test.png)

 If you can’t move in and out of the dining room, just check that you added all of the code above (including the extra commas to the lines above).

--- /task ---
