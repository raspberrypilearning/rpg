#!/bin/python3

def mostraInstrucoes():
    #imprime um menu principal e os comandos
    print('''
Jogo RPG
========

Chega ao jardim com uma chave e uma garrafa de poçāo
Evita os monstros!

You are getting tired, each time you move you loose 1 health point. 

Comandos:
  vai [direçāo]
  apanha [item]
''')

def mostraEstado():
  #imprime o estado corrente do jogador
  print('---------------------------')
  print(name + ' is in the ' + currentRoom)
  print("Health : " + str(health))
  #Imprime o inventário currente
  print("Inventário : " + str(inventario))
  #imprime um item se houver um
  if "item" in divisoes[divAtual]:
    print('Estás a ver uma ' + divisoes[divAtual]['item'])
  print("---------------------------")

# setup the game
name = None
health = 5
currentRoom = 'Hall'
inventory = []

#-# YOUR CODE GOES HERE #-#
# Load data from the file

#um dicionário a ligar uma divisāo a outras divisões
divisoes = {

            'Entrada' : { 'sul' : 'Cozinha',
                  'este'  : 'Sala de Jantar',
                  'item'  : 'chave'
                },

            'Cozinha' : { 'norte' : 'Entrada',
                  'item'  : 'monstro'
                },

            'Sala Jantar' : { 'oeste'  : 'Entrada',
                  'sul' : 'Jardim',
                  'item'  : 'garrafa'

                },

            'Jardim' : { 'norte' : 'Sala Jantar' }

         }

# ask the player their name
if name is None:
  name = input("What is your name Adventurer? ")
  mostraInstrucoes()

#ciclo perpétuo
while True:

  mostraEstado()

  #recebe a próxima 'jogada'
  #.split() divide-a numa matriz de listas
  #por exemplo digitar 'vai este' resulta na lista:
  #['vai', 'este']
  jogada = ''
  while jogada == '':
    jogada = input ('>')

  jogada = jogada.lower().split()

  #se digitarem 'vai' primeiro
  if jogada[0] == 'vai':
    health = health - 1
    #verifica que o jogador pode ir na direcāo que está a pedir
    se jogada[1] in divisoes[divAtual]:
      #altera a divisāo actual para a nova divisāo
      divAtual = divisoes[divActua][jogada[1]]
    #nāo há porta (ligaçāo) para a nova divisāo
    else:
      print('Nāo podes ir nessa direçāo!')

  #se digitarem 'apanha' primeiro
  if jogada[0] == 'apanha' :
    #se a divisāo tiver um item, e o jogador quiser apanhar esse item
    if "item" in divisoes[divAtual] and jogada[1] in divisoes[divAtual]['item']:
      #adicionar o item ao inventário
      inventario += [jogada[1]]
      #mostra uma mensagem informativa
      print('Apanhaste uma ' + jogada[1] + '!')
      #apaga o item da divisāo
      del divisoes[divAtual]['item']
    #senāo, se nāo houver item para apanhar
    else:
      #diz ao jogador que nāo pode apanhar o item
      print('Nāo podes apanhar uma ' + jogada[1] + '!')

  #o jogador perde se entrar numa divisāo com um monstro
  if "item" in divisoes[divAtual] and 'monstro' in divisoes[divAtual]['item']:
    print('O monstro apanhou-te... PERDESTE!')
    break

  if health == 0:
    print('You collapse from exhaustion... GAME OVER!')

  #o jogador ganha se entrar no jardim com a chave e a garrafa de poçāo
  if divAtual == 'Jardim' and 'chave' in inventario and 'garrafa' in inventario:
    print('Fugiste da casa... GANHASTE!')
    break

  #-# YOUR CODE GOES HERE #-#
  # Save game data to the file