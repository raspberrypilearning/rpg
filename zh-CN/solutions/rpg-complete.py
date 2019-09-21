#!/bin/python3

def showInstructions():
    # 显示主菜单和可用命令
    print('''
RPG游戏
========

找到一把钥匙和一瓶魔法药水并到达花园
同时躲避怪物！

你正变得疲惫，你每移动一次你的生命值将减少一分。 

命令：
  go [direction]
  get [item]
''')

def showStatus():
  # 显示玩家的当前状态
  print('---------------------------')
  print(name + ' 正在 ' + currentRoom)
  print("生命值：" + str(health))
  # 显示当前已获得物品
  print('物品 ： ' + str(inventory))
  # 显示物品（如果存在）
  if "item" in rooms[currentRoom]:
    print('你看见一个 ' + rooms[currentRoom]['item'])
  print("---------------------------")

# 初始化游戏设置
name = None
health = 5
currentRoom = '大厅'
inventory = []

#-# 这里放入你的代码 #-#
# 从文件中加载数据

# 连接房间与房间的数据字典
rooms = {

            'Hall' : { 'south' : 'Kitchen',
                  'east'  : 'Dining Room',
                  'item'  : 'key'
                },

            'Kitchen' : { 'north' : 'Hall',
                  'item'  : 'monster'
                },

            'Dining Room' : { 'west'  : 'Hall',
                  'south' : 'Garden',
                  'item'  : 'potion'

                },

            'Garden' : { 'north' : 'Dining Room' }

         }

# 询问玩家名字
if name is None:
  name = input("冒险家，你叫什么名字？ ")
  showInstructions()

# 永久循环
while True:

  showStatus()

  # 取得玩家的下一个行动
  #.split()方法分隔对象到列表中
  # 例如：输入"go east“将产生如下列表:
  # ['go','east']
  move = ''
  while move == '':
    move = input('>')

  move = move.lower().split()

  # 如果玩家输入'go'指令
  if move[0] == 'go':
    health = health - 1
    # 检查玩家是否被允许走入他们所输入的方向
    if move[1] in rooms[currentRoom]:
      # 将当前房间换成新进入的房间
      currentRoom = rooms[currentRoom][move[1]]
    # 那里没有通向另一房间的门（连接）
    else:
      print('你不能往那里走！')

  # 如果玩家输入'get'指令
  if move[0] == 'get' :
    # 如果房间里有一件物品，那这件物品是玩家想要拿到的
    if 'item' in rooms[currentRoom] and move[1] in rooms[currentRoom]['item']:
      # 将物品加入玩家的物品清单
      inventory += [move[1]]
      # 显示一条有用的消息
      print('拿到了 ' + move[1] + '！')
      # 将物品从房间里去除
      del rooms[currentRoom]['item']
    # 否则，如果没有可拿的物品
    else:
      # 告诉玩家不能拿到物品
      print('无法拿到 ' + move[1] + '！')

  #玩家如果进入一个有怪物的房间，则游戏失败
  if 'item' in rooms[currentRoom] and '怪物' in rooms[currentRoom]['item']:
    print('一个怪物抓住你了... 游戏结束！')
    break

  if health == 0:
    print('你力竭而死... 游戏结束!')

  #如果玩家得到钥匙和魔法药水并到达花园，就赢了
  if currentRoom == 'Garden' and 'key' in inventory and 'potion' in inventory:
    print('你成功逃离房子... 你赢了！')
    break

  #-# 这里放入你的代码 #-#
  # 将游戏数据存入文件