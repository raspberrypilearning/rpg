#!/bin/python3

def showInstructions():
    # 显示主菜单和可用命令
    print('''
RPG游戏
========

找到一把钥匙和一瓶魔法药水并到达花园
同时躲避怪物！

命令：
  go [方向]
  get [物品]
''')

def showStatus():
  # 显示玩家的当前状态
  print('---------------------------')
  print('你现在在 ' + currentRoom)
  # 显示当前已获得物品
  print('物品 ： ' + str(inventory))
  # 显示物品（如果存在）
  if "item" in rooms[currentRoom]:
    print('你看见一个 ' + rooms[currentRoom]['item'])
  print("---------------------------")

# 已获得物品清单，初始为空
inventory = []

# 连接房间与房间的数据字典
rooms = {

            '大厅' : { 'south' : '厨房',
                  'east'  : '餐厅',
                  'item'  : '钥匙'
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

#start the player in the Hall
currentRoom = 'Hall'

showInstructions()

#loop forever
while True:

  showStatus()

  #get the player's next 'move'
  #.split() breaks it up into an list array
  #eg typing 'go east' would give the list:
  #['go','east']
  move = ''
  while move == '':  
    move = input('>')
    
  move = move.lower().split()

  #if they type 'go' first
  if move[0] == 'go':
    #check that they are allowed wherever they want to go
    if move[1] in rooms[currentRoom]:
      #set the current room to the new room
      currentRoom = rooms[currentRoom][move[1]]
    #there is no door (link) to the new room
    else:
      print('You can\'t go that way!')

  #if they type 'get' first
  if move[0] == 'get' :
    #if the room contains an item, and the item is the one they want to get
    if 'item' in rooms[currentRoom] and move[1] in rooms[currentRoom]['item']:
      #add the item to their inventory
      inventory += [move[1]]
      #display a helpful message
      print(move[1] + ' got!')
      #delete the item from the room
      del rooms[currentRoom]['item']
    #otherwise, if the item isn't there to get
    else:
      #tell them they can't get it
      print('Can\'t get ' + move[1] + '!')

  # player loses if they enter a room with a monster
  if 'item' in rooms[currentRoom] and 'monster' in rooms[currentRoom]['item']:
    print('A monster has got you... GAME OVER!')
    break

  # player wins if they get to the garden with a key and a potion
  if currentRoom == 'Garden' and 'key' in inventory and 'potion' in inventory:
    print('You escaped the house... YOU WIN!')
    break
  
