#!/bin/python3

def showInstructions():
    #메인메뉴와 명령어 출력
    print('''
RPG 게임
========

괴물에게 잡히지 말고, 
key와 potion을 가지고 Garden으로 탈출하십시오!

You are getting tired, each time you move you loose 1 health point. 

명령어:
  go [direction]
  get [item]
''')

def showStatus():
  #플레이어의 현재 상태 출력
  print('---------------------------')
  print(name + ' is in the ' + currentRoom)
  print("Health : " + str(health))
  #플레이어의 현재 인벤토리 출력
  print("인벤토리: " + str(inventory))
  #아이템이 있다면 출력
  if "item" in rooms[currentRoom]:
    print(rooms[currentRoom]['item'] + '를 발견했습니다.')
  print("---------------------------")

# setup the game
name = None
health = 5
currentRoom = 'Hall'
inventory = []

#-# YOUR CODE GOES HERE #-#
# Load data from the file

#room 딕셔너리
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

# ask the player their name
if name is None:
  name = input("What is your name Adventurer? ")
  showInstructions()

#무한 반복
while True:

  showStatus()

  #플레이어를 'move'로 이동함
  #.split() 함수는 문자열을 구분함
  #e.g. 'go east'는 아래와 같이 리스트에 삽입됨:
  #['go','east']
  move = ''
  while move == '':
    move = input('>')

  move = move.lower().split()

  #만약에 'go'가 입력되면
  if move[0] == 'go':
    health = health - 1
    #go 다음에 입력된 문자열이 올바른 방인지를 체크
    if move[1] in rooms[currentRoom]:
      #현재 방을 새로운 방으로 옮김
      currentRoom = rooms[currentRoom][move[1]]
    #만약 방을 해당 방향으로 옮길 수 없다면,
    else:
      print('이곳으로 갈 수 없습니다!')

  #만약에 'get'이 입력되면
  if move[0] == 'get' :
    #만약 방 안에 아이템이 있고, 플레이어가 입력한 아이템이 존재한다면
    if 'item' in rooms[currentRoom] and move[1] in rooms[currentRoom]['item']:
      #아이템을 인벤토리에 추가함
      inventory += [move[1]]
      #플레이어에게 메시지 출력
      print(move[1] + '를 받았습니다!')
      #아이템을 방에서 제거
      del rooms[currentRoom]['item']
    #만약에 아이템이 없다면
    else:
      #아이템이 없다라고 메시지 출력
      print(move[1] + '아이템을 획득할 수 없습니다!')

  #몬스터가 있는 방으로 들어가면 게임이 끝난다
  if 'item' in rooms[currentRoom] and 'monster' in rooms[currentRoom]['item']:
    print('괴물에게 잡혔습니다... GAME OVER!')
    break

  if health == 0:
    print('You collapse from exhaustion... GAME OVER!')

  #키와 포션을 가지고 Garden으로 가면 탈출 성공
  if currentRoom == 'Garden' and 'key' in inventory and 'potion' in inventory:
    print('괴물의 집에서 탈출하셨습니다! YOU WIN!')
    break

  #-# YOUR CODE GOES HERE #-#
  # Save game data to the file