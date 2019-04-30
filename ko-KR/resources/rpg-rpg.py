#!/bin/python3

# Replace RPG starter project with this code when new instructions are live

def showInstructions():
  #메인메뉴와 명령어 출력
  print('''
RPG 게임
========
명령어:
  go [방향]
  get [아이템]
''')

def showStatus():
  #플레이어의 현재 상태 출력
  print('---------------------------')
  print('이곳은 ' + currentRoom + '입니다')
  #플레이어의 현재 인벤토리 출력
  print("인벤토리: " + str(inventory))
  #아이템이 있다면 출력
  if "item" in rooms[currentRoom]:
    print(rooms[currentRoom]['item'] + '를 발견했습니다.')
  print("---------------------------")

#인벤토리 리스트 자료형
inventory = []

#room 딕셔너리
rooms = {

            'Hall' : { 
                  'south' : 'Kitchen'
                },

            'Kitchen' : {
                  'north' : 'Hall'
                }

         }

#플레이어는 Hall에서 시작함
currentRoom = 'Hall'

showInstructions()

#무한 반복
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
    if "item" in rooms[currentRoom] and move[1] in rooms[currentRoom]['item']:
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

