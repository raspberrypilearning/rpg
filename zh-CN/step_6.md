## 添加敌人

这个游戏太简单了！ 让我们在，某些房间里添加一些玩家必须要躲避的敌人。

+ 在一个房间中添加一个敌人和添加一个物品一样简单。 让我们在厨房中添加一只饥饿的怪物：
    
    ![screenshot](images/rpg-monster-dict.png)

+ 你还要确保当玩家进入一个有怪物的房间时，游戏就以失败而结束。 你可以在游戏的末尾添加如下的代码：
    
    ![screenshot](images/rpg-monster-code.png)
    
    This code checks whether there is an item in the room, and if so, whether that item is a monster. Notice that this code is indented, putting it in line with the code above it. This means that the game will check for a monster every time the player moves into a new room.

+ Test out your code by going into the kitchen, which now contains a monster.
    
    ![screenshot](images/rpg-monster-test.png)