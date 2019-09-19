## 赢得胜利

让我们给予玩家一项任务，使他们必须完成这项任务才能获得游戏的胜利。

--- task --- 在这个游戏中，玩家如果逃离房子并到达花园时，就赢得了胜利。 他们还需要拿到钥匙和魔法药水。 以下是游戏的地图。

![screenshot](images/rpg-final-map.png) --- /task ---

--- task --- 首先，你需要在餐厅的南面添加一个花园。 记住要添加“门”来将其关联到另外一个房间。

--- code ---
---
language: python 
line_highlights: 16-17,18-22
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
                'west' : 'Hall',
                'south' : 'Garden'
            },
    
            'Garden' : {
                'north' : 'Dining Room'
            }
    
        }
    

--- /code --- --- /task ---

--- task --- 在餐厅中添加一瓶魔法药水（或任何其他一个房间）。

--- code ---
---
language: python 
line_highlights: 3-4
---

            'Dining Room' : {
                'west' : 'Hall',
                'south' : 'Garden',
                'item' : 'potion'
            },
    

--- /code --- --- /task ---

--- task --- 添加以下代码，可以让玩家在得到钥匙和魔法药水，并到达花园时赢得胜利。

--- code ---
---
language: python 
line_highlights: 6-9
---
# 玩家如果进入一个有怪物的房间，则游戏失败
if 'item' in rooms\[currentRoom] and 'monster' in rooms[currentRoom\]\['item'\]: 
  print('A monster has got you... GAME OVER!') 
  break

# 如果玩家得到钥匙和魔法药水并到达花园，就赢了
if currentRoom == 'Garden' and 'key' in inventory and 'potion' in inventory: 
  print('You escaped the house... YOU WIN!') 
  break 
--- /code ---

注意这段代码也是缩进的，应当与上面的代码对齐。 这段代码表示当玩家在第4个房间（花园）中，并且在他们的物品袋中有钥匙和魔法药水时，就显示“你已逃离房子...你赢了！”的消息。

如果你已经有了4个或更多的房间了，你可能需要在你的代码中给花园一个不同的房间号。 --- /task ---

--- task --- 测试你的游戏，确保玩家有可能获得胜利！

![screenshot](images/rpg-win-test.png) --- /task ---

--- task --- 最后，让我们在游戏中添加一些说明来让玩家知道怎样来操作。 修改`showInstructions()`函数来添加更多的说明信息。

--- code ---
---
language: python 
line_highlights: 7-8
---

def showInstructions(): 
  # 显示主菜单和可用命令 
  print('''
RPG游戏

找到一把钥匙和一瓶魔法药水并到达花园
同时躲避怪物！

命令： 
go [direction] 
get [item] 
''') 
--- /code ---

你需要添加说明来告诉玩家他们需要收集哪些物品，并需要避开什么！ --- /task ---

--- task --- 测试你的游戏，你应该能够看到你新加的游戏说明。

![screenshot](images/rpg-instructions-test.png) --- /task ---
