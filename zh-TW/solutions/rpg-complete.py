#!/bin/python3

def showInstructions():
    #印出主選單和指令
    print('''
角色扮演遊戲
========

帶著鑰匙和藥水抵達花園
避開怪物！

你會感到疲倦，每次移動都會失去1個健康點數。 

指令：
  往 [方向]
  拿 [物品]
''')

def showStatus():
  ＃印出玩家的目前狀態
  print('---------------------------')
  print(name +'正在'+ currentRoom)
  print("健康 : " + str(health))
  ＃印出物品欄
  print("物品欄：” + str(inventory))
  ＃如果物品欄中有物品就印出
  if "物品" in rooms[currentRoom]:
    print('你看到一個' + rooms[currentRoom]['物品'])
  print('---------------------------')

＃設置遊戲
name = None
health = 5
currentRoom = '大廳'
inventory = []

＃-＃你的程式碼從這裡開始＃-＃
＃從檔案讀取資料

#將一個房間連接到其他房間的字典
rooms = {

            '大廳 ': { '南' : '廚房',
                  '東'  : '飯廳',
                  '物品' : '鑰匙'
                },

            '廚房' : {'北' : '大廳',
                  '物品' : '怪物'
                },

            '飯廳' : {'西' : '大廳',
                  '南' : '花園',
                  '物品' : '藥水'

                },

            '花園'： { '北' : '飯廳' }

         }

＃詢問玩家名稱
if name is None:
  name = input("冒險家，你的名字是？ ")
  showInstructions()

＃重複無限次。
while True:

  showStatus()

  ＃獲取玩家的下一個「行動」
  ＃使用字串分割 .split() 將字串分解放入串列（list）
  #例如 輸入'往 東'將列出：
  #['往','東']
  move = ''
  while move == '':
    move = input('>')

  move = move.lower().split()

  #假設先輸入'往'
  if move[0] == '往':
    health = health - 1
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

  #如果玩家進入有怪物的房間就輸了
  if '物品’ in rooms[currentRoom] and '怪物' in rooms[currentRoom]['物品']:
    print('怪物抓到你了… 遊戲結束!')
    break

  if health == 0:
    print('你已經精疲力盡了… 遊戲結束!')

  #如果玩家帶著鑰匙和藥水進入花園則獲勝
  if currentRoom == '花園' and '鑰匙' in inventory and '藥水' in inventory:
    print('成功逃離房屋… 你贏了!')
    break

  ＃-＃你的程式碼到這裡結束＃-＃
  ＃將遊戲記錄存檔