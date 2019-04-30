## 添加新房间

+ 我们已经为你提供了这个游戏的部分代码。 请打开这个Trinket：<a href="http://jumpto.cc/rpg-go" target="_blank">jumpto.cc/rpg-go</a>.

+ 这是个仅包含2个房间的基本的RPG游戏。 以下是游戏的地图：
    
    ![截图](images/rpg-map1.png)
    
    你可以输入`go south`指令从大厅走到厨房，然后输入`go north`指令再返回大厅！
    
    ![截图](images/rpg-controls.png)

+ 当你输入一个无法到达的方向时将会发生什么？ 当你在大厅时，输入`go west`指令，你将得到一个友善的错误消息。
    
    ![截图](images/rpg-error.png)

+ 当你在代码中找到`rooms`变量时，你会发现游戏地图实际上是用一个包含房间信息的数据字典来实现的。
    
    ![截图](images/rpg-rooms.png)
    
    每个房间是字典中的一项数据，然后用方向来将房间与房间关联起来。

+ 让我们在地图上添加一个餐厅，将其放在大厅的东面。
    
    ![截图](images/rpg-dining.png)
    
    你需要添加一个房间并称其为`餐厅`。 你还需要将它的西侧关联到大厅。 你还需要向大厅添加额外信息，以使你可以从那里向东走到餐厅。
    
    ![截图](images/rpg-dining-code.png)

+ 加完新的餐厅后，试着运行一下游戏。
    
    ![截图](images/rpg-dining-test.png)
    
    如果你不能走进或走出餐厅，检查你是否已经添加了如上所示的所有代码（包括在上一行已有代码行末尾添加额外的逗号）。