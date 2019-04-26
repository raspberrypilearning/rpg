## Winning the game

Let’s give your player a mission, which needs to completed to win the game.

+ In this game, the player wins by getting to the garden and escaping the house. They also need to have the key with them, and the magic potion. Here’s a map of the game.
    
    ![captura de pantalla](images/rpg-final-map.png)

+ First, you need to add a garden to the south of the dining room. Remember to add doors, to link to other rooms in the house.
    
    ![captura de pantalla](images/rpg-garden.png)

+ Add a potion to the dining room (or another room in your house).
    
    ![captura de pantalla](images/rpg-potion.png)

+ Add this code to allow the player to win the game when they get to the garden with the key and the potion:
    
    ![captura de pantalla](images/rpg-win-code.png)
    
    Make sure this code is indented, in line with the code above it. This code means that the message `You escaped the house...YOU WIN!` is displayed if the player is in room 4 (the garden) and if the key and the potion are in the inventory.
    
    If you have more than 4 rooms, you may have to use a different room number for your garden in the code above.

+ Test your game to make sure the player can win!
    
    ![captura de pantalla](images/rpg-win-test.png)

+ Finally, let’s add some instructions to your game, so that the player knows what they have to do. Edit the `showInstructions()` function to include more information.
    
    ![captura de pantalla](images/rpg-instructions-code.png)
    
    You will need to add instructions to tell the user what items they need to collect, and what they need to avoid!

+ Test your game and you should see your new instructions.
    
    ![captura de pantalla](images/rpg-instructions-test.png)