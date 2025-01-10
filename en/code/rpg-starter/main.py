def showInstructions():
    # Print a main menu and the commands
    print(
        """
          RPG Game
          ========
          Commands:
          go [direction]
          get [item]
          """
    )


def showStatus():
    # Print the player's current status
    print("---------------------------")
    print("You are in the " + currentRoom)
    # Print the current inventory
    print("Inventory : " + str(inventory))
    # Print an item if there is one
    if "item" in rooms[currentRoom]:
        print("You see a " + rooms[currentRoom]["item"])
    print("---------------------------")


# An inventory, which is initially empty
inventory = []

# A dictionary linking a room to other rooms
rooms = {
    "Hall": {
        "south": "Kitchen"
    }, 
    "Kitchen": {
        "north": "Hall"
    }
}

# Start the player in the Hall
currentRoom = "Hall"

showInstructions()

# Loop forever
while True:

    showStatus()

    # Get the player's next 'move'
    # .split() breaks it up into an list array
    # e.g. typing 'go east' would give the list:
    # ['go','east']
    move = ""
    while move == "":
        move = input(">")

    move = move.lower().split()

    # If they type 'go' first
    if move[0] == "go":
        # Check that they are allowed wherever they want to go
        if move[1] in rooms[currentRoom]:
            # Set the current room to the new room
            currentRoom = rooms[currentRoom][move[1]]
        else:
            print("You can't go that way!")

    # If they type 'get' first
    if move[0] == "get":
        # If the room contains an item, and the item is the one they want to get
        if "item" in rooms[currentRoom] and move[1] in rooms[currentRoom]["item"]:
            # Add the item to their inventory
            inventory += [move[1]]
            print("You picked up the " + move[1])
            # Delete the item from the room
            del rooms[currentRoom]["item"]
        # Otherwise, the item isn't there
        else:
            # Tell them they can't get it
            print("There is no " + move[1] + " here!")

    # Player loses if they enter a room with a monster
    if "item" in rooms[currentRoom] and "monster" in rooms[currentRoom]["item"]:
        print("A monster has got you... GAME OVER!")
        break
