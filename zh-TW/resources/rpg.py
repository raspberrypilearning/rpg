#!/bin/python3

# 當新指令啟用時, 用這個程式碼取代角色扮演遊戲入門專案

def showInstructions():
  #印出主選單和指令
  print('''
角色扮演遊戲
========
指令：
  往 [方向]
  拿 [物品]
''')

def showStatus():
  ＃印出玩家的目前狀態
  print('---------------------------')
  print('你正在' + currentRoom)
  ＃印出物品欄
  print("物品欄：” + str(inventory))
  ＃如果物品欄中有物品就印出
  if "物品" in rooms[currentRoom]:
    print('你看到一個' + rooms[currentRoom]['物品'])
  print("---------------------------")

#物品欄（inventory）為空的初始值
inventory = []

#將一個房間連接到其他房間的字典
rooms = {

            '大廳' : { 
                  '南' : '廚房'
                },

            '廚房' : {
                  '北' : '大廳'
                }

         }

＃玩家從大廳開始
currentRoom = '大廳'

showInstructions()

＃重複無限次。
while True:

  showStatus()

  ＃獲取玩家的下一個「行動」
  ＃使用字串分割 .split() 將字串分解放入串列（list）
  #例如 輸入'往 東'列出：
  #['往','東']
  move = ''
  while move == '':  
    move = input('>')
    
  move = move.lower().split()

  #假設先輸入'往'
  if move[0] == '往':
    ＃檢查他們想去的地方是否被允許
    if move[1] in rooms[currentRoom]:
      ＃將目前房間設置為新房間
      currentRoom = rooms[currentRoom][move[1]]
    ＃沒有門(連結)通往新房間
    else:
        print('你不能往那走!')

  ＃假設先輸入“拿”
  if move[0] == '拿' :
    ＃如果房間中有他們想要得到的物品
    if '物品' in rooms[currentRoom] and move[1] in rooms[currentRoom]['物品']:
      ＃新增物品至物品欄
      inventory += [move[1]]
      ＃顯示訊息
      print(move[1] + ' 取得!')
      ＃把取得的物品從房間中刪除
      del rooms[currentRoom]['物品']
    ＃反之，如果想取得的物品不在那
    else:
      ＃告訴他們無法取得物品
      print('無法取得' + move[1] + '!')

