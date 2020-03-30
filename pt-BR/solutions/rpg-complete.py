#!/bin/python3

def mostrarInstrucoes():
    #exibe um menu principal e os comandos possiveis
    print('''
Jogo RPG
========

Vá para o Jardim com uma chave e uma poção
Evite os monstros!

Você está ficando cansado, você perderá 1 ponto de vida a cada movimento. 

Comandos:
  va [direção]
  pegar [item]
''')

def mostrarEstado():
  #exibe o estado atual do jogador
  print('---------------------------')
  print(nome + ' está na ' + comodoAtual)
  print("Saúde : " + str(saude))
  #exibe o inventário atual
  print("Inventário :" + str(inventario))
  #exibe um item se houver um
  if "item" in comodos[comodoAtual]:
    print('Você vê um(a) ' + comodos[comodoAtual]['item'])
  print("---------------------------")

# configurar o jogo
nome = None
saude = 5
comodoAtual = 'Saguão'
inventario = []

#-# O TEU CÓDIGO FICA AQUI #-#
# Carrega os dados do jogo para o arquivo

#um dicionário ligando um cômodo aos demais cômodos
comodos= {

            'Saguão' : {'sul' : 'Cozinha',
                  'leste' : 'Sala de Jantar',
                  'item' : 'Chave'
                },

            'Cozinha': {'norte' : 'Saguão',
                  'item' : 'Monstro'
                },

            'Sala de Jantar' : { 'oeste' : 'Saguão',
                  'sul' : 'Jardim',
                  'item' : 'Poção'

                },

            'Jardim' : {'norte' : 'Sala de Jantar' }

         }

# ask the player their name
if name is None:
  name = input("What is your name Adventurer? ")
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
    health = health - 1
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

  #player loses if they enter a room with a monster
  if 'item' in rooms[currentRoom] and 'monster' in rooms[currentRoom]['item']:
    print('A monster has got you... GAME OVER!')
    break

  if health == 0:
    print('You collapse from exhaustion... GAME OVER!')

  #player wins if they get to the garden with a key and a potion
  if currentRoom == 'Garden' and 'key' in inventory and 'potion' in inventory:
    print('You escaped the house... YOU WIN!')
    break

  #-# YOUR CODE GOES HERE #-#
  # Save game data to the file