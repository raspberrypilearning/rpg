## 添加敌人

这个游戏太简单了！ 让我们在，某些房间里添加一些玩家必须要躲避的敌人。

--- task --- 在一个房间中添加一个敌人和添加一个物品一样简单。 让我们在厨房中添加一只饥饿的怪物：

--- code ---
---
language: python line_highlights: 11-12
---
# 连接房间与房间的数据字典

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
                'west' : 'Hall'
            }
    
        }
    

--- /code --- --- /task ---

--- task --- 你还要确保当玩家进入一个有怪物的房间时，游戏就以失败而结束。 你可以在游戏的末尾添加如下的代码：

--- code ---
---
language: python line_highlights: 6-9
---

        #otherwise, if the item isn't there to get
        else:
            #tell them they can't get it
            print('Can\'t get' + move[1] + '!')
    
    #player loses if they enter a room with a monster
    if 'item' in rooms[currentRoom] and 'monster' in rooms[currentRoom]['item']:
        print('A monster has got you... GAME OVER!')
        break
    

--- /code ---

这些代码检查房间中是否有一个物品，如果是的话，那个物品是不是一个怪物。 注意这段代码也是缩进的，应当与上面的代码对齐。 这个缩进表示每当玩家进入一个新的房间时，游戏都会检测那个房间中是不是有怪物。 --- /task ---

--- task --- 测试你的代码，并试着进入现在有怪物的餐厅。

![screenshot](images/rpg-monster-test.png) --- /task ---