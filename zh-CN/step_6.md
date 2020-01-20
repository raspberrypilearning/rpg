## 添加敌人

这个游戏太简单了！ 让我们在，某些房间里添加一些玩家必须要躲避的敌人。

\--- task \---

Adding an enemy to a room is as easy as adding any other item. Let’s add a hungry monster to the kitchen:

## \--- code \---

language: python

## line_highlights: 11-12

# 连接房间与房间的数据字典

rooms = {

            '大厅' : {
                'south' : '厨房',
                'east' : '餐厅',
                'item' : '钥匙'
            },
    
            '厨房' : {
                'north' : '大厅',
                'item' : '怪物'
            },
    
            '餐厅' : {
                'west' : '大厅'
            }
    
        }
    

\--- /code \---

\--- /task \---

\--- task \---

You also want to make sure that the game ends if the player enters a room with a monster in. You can do this with the following code, which you should add to the end of the game:

## \--- code \---

language: python

## line_highlights: 6-9

        #否则，如果没有可拿的物品
        else:
            # 告诉玩家不能拿到物品
            print('不能' + move[1] + '!')
    
    #玩家如果进入一个有怪物的房间，则游戏失败
    if 'item' in rooms[currentRoom] and 'monster' in rooms[currentRoom]['item']:
        print('一个怪物抓住你了... 游戏结束!')
        break
    

\--- /code \---

This code checks whether there is an item in the room, and if so, whether that item is a monster. Notice that this code is indented, putting it in line with the code above it. This means that the game will check for a monster every time the player moves into a new room.

\--- /task \---

\--- task \---

Test out your code by going into the kitchen, which now contains a monster.

![screenshot](images/rpg-monster-test.png)

\--- /task \---