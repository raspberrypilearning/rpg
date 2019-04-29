## 添加新房间

+ 我们已经为你提供了这个游戏的部分代码。 请打开这个Trinket：<a href="http://jumpto.cc/rpg-go" target="_blank">jumpto.cc/rpg-go</a>.

+ 这是个仅包含2个房间的基本的RPG游戏。 以下是游戏的地图：
    
    ![screenshot](images/rpg-map1.png)
    
    你可以输入`go south`指令从大厅走到厨房，然后输入`go north`指令再返回大厅！
    
    ![screenshot](images/rpg-controls.png)

+ 当你输入一个无法到达的方向时将会发生什么？ 当你在大厅时，输入`go west`指令，你将得到一个友善的错误消息。
    
    ![screenshot](images/rpg-error.png)

+ 当你在代码中找到`rooms`变量时，你会发现游戏地图实际上是用一个包含房间信息的数据字典来实现的。
    
    ![screenshot](images/rpg-rooms.png)
    
    每个房间是字典中的一项数据，然后用方向来将房间与房间关联起来。

+ 让我们在地图上添加一个餐厅，将其放在大厅的东面。
    
    ![screenshot](images/rpg-dining.png)
    
    You need to add a 3rd room, called the `dining room`. You also need to link it to the hall to the west. You also need to add data to the hall, so that you can move to the dining room to the east.
    
    ![screenshot](images/rpg-dining-code.png)

+ Try out the game with your new dining room:
    
    ![screenshot](images/rpg-dining-test.png)
    
    If you can’t move in and out of the dining room, just check that you added all of the code above (including the extra commas to the lines above).