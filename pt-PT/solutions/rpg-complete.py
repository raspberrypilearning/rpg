#!/bin/python3

def mostraInstrucoes():
    #imprime um menu principal e os comandos
    print('''
Jogo RPG
========

Chega ao jardim com uma chave e uma garrafa de poçāo
Evita os monstros!

Estás a ficar cansado, cada vez que te moves perdes 1 ponto de vida. 

Comandos:
  vai [direçāo]
  apanha [item]
''')

def mostraEstado():
  #imprime o estado corrente do jogador
  print('---------------------------')
  print(nome + ' está na ' + divAtual)
  print("Saúde : " + str(saude))
  #Imprime o inventário atual
  print("Inventário : " + str(inventario))
  #imprime um item se houver um
  if "item" in divisoes[divAtual]:
    print('Estás a ver uma ' + divisoes[divAtual]['item'])
  print("---------------------------")

# configurar o jogo
nome = None
saude = 5
divAtual = 'Entrada'
inventario = []

#-# O TEU CÓDIGO FICA AQUI #-#
# Carregar os dados do jogo para o arquivo

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

# perguntar ao jogador o seu nome
if nome is None:
  nome = input("Qual é o teu nome Aventureiro? ")
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
    saude = saude -1
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

  if saude == 0:
    print('Desmaias-te de exaustão... FIM DO JOGO!')

  #o jogador ganha se entrar no jardim com a chave e a garrafa de poçāo
  if divAtual == 'Jardim' and 'chave' in inventario and 'garrafa' in inventario:
    print('Fugiste da casa... GANHASTE!')
    break

  #-# O TEU CÓDIGO FICA AQUI #-#
  # Carregar os dados do jogo para o arquivo