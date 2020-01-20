## 添加可收集的物品

让我们在房间中添置一些物品，让玩家在穿越迷宫的时候收集。

\--- task \---

Adding an item into a room is easy, you can just add it to a room's dictionary. Let’s put a key in the hall.

Remember to put a comma after the line above the new item, or your program won’t run!

## \--- code \---

language: python

## line_highlights: 6-7

# 连接房间与房间的数据字典

rooms = {

            '大厅' : {
                'south' : '厨房',
                'east' : '餐厅',
                'item' : '钥匙'
            },
    
            '厨房' : {
                'north' : '大厅'
            },
    
            '餐厅' : {
                'west' : '大厅'
            }
    
        }
    

\--- /code \---

\--- /task \---

\--- task \---

If you run your game after adding the code above, you can now see a key in the hall, and you can even pick it up (by typing `get key`) which adds it to your inventory!

![screenshot](images/rpg-key-test.png)

\--- /task \---