## Winning the game

Let’s give your player a mission, which needs to be completed to win the game.



In this game, the player wins by getting to the garden and escaping the house. They also need to have the key with them, and the magic potion. Here’s a map of the game.

![A map showing the hall containing a key, witih the dining room to the East containing a potion. The kitchen is South of the hall and contains a monster. The garden is East of the kitchen and South of the dining room.](images/rpg-final-map.png)



--- task ---

Add a garden to the south of the dining room. Remember to add a door to the garden from the dining room.

--- code ---
---
language: python
line_numbers: true
line_number_start: 29
line_highlights: 41-42, 43-46
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

Add a potion to the dining room.

--- code ---
---
language: python
line_numbers: true
line_number_start: 39
line_highlights: 41-42
---
    'Dining Room' : {
        'west' : 'Hall',
        'south' : 'Garden',
        'item' : 'potion'
    },
--- /code ---

--- /task ---

--- task ---

Add this code right at the end of the Python file to allow the player to win the game when they get to the garden with the key and the potion. Make sure the code is indented, in line with the code above it. 

--- code ---
---
language: python
line_numbers: true
line_number_start: 96
line_highlights: 96-99
---
    if currentRoom == 'Garden' and 'key' in inventory and 'potion' in inventory:
        print('You escaped the house... YOU WIN!')
        break
--- /code ---

--- /task ---

--- task ---

Click **Stop** then click **Run** to test your game to make sure the player can win!

--- code ---
---
language: text
line_numbers: false
line_number_start: 
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

--- /task ---

--- task ---

Test your game and you should see your new instructions.

--- /code ---

--- /task ---
