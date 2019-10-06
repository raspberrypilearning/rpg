#!/bin/python3

# Substitua o projeto inicial de RPG por este código quando novas instruções estiverem ativas

def mostraInstrucoes():
  #imprime um menu principal e os comandos
  print('''
Jogo RPG
========
Comandos:
  vai [direçāo]
  apanha [item]
''')

def mostraEstado():
  #imprime o estado corrente do jogador
  print('---------------------------')
  print('Estás na ' + divAtual)
  #Imprime o inventário currente
  print("Inventário : " + str(inventario))
  #imprime um item se houver um
  if "item" in divisoes[divAtual]:
    print('Estás a ver uma ' + divisoes[divAtual]['item'])
  print("---------------------------")

#um inventário, que inicialmente está vazio
inventario = []

#um dicionário a ligar uma divisāo a outras divisões
divisoes = {

            'Entrada' : { 
                  'sul' : 'Cozinha'
                },

            'Cozinha' : {
                  'norte' : 'Entrada'
                }

         }

#começa com o jogador na Entrada
divAtual = 'Entrada'

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

