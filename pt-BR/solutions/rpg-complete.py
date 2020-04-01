#!/bin/python3

def mostrarInstrucoes():
    #exibe o menu principal e os possíveis comandos
    print('''
Jogo RPG
========

Vá para o Jardim com uma chave e uma poção
Evite os monstros!

Você está ficando cansado, você perderá 1 ponto de vida a cada movimento. 

Comandos:
  para [direção]
  pegar [item]
''')

def mostrarEstado():
  #exibe o estado atual do jogador
  print('---------------------------')
  print(nome + ' está na ' + comodoAtual)
  print("Saúde : " + str(saude))
  #exibe o inventário atual
  print("Inventário : " + str(inventario))
  #exibe um item se houver um
  if "item" in comodos[comodoAtual]:
    print('Você vê um(a) ' + comodos[comodoAtual]['item'])
  print("---------------------------")

#configurar o jogo
nome = None
saude = 5
comodoAtual = 'Saguão'
inventario = []

#-# O TEU CÓDIGO FICA AQUI #-#
# Carrega os dados do jogo para o arquivo

#dicionário ligando um cômodo aos demais cômodos
comodos = {

            'Saguão' : {'baixo' : 'Cozinha',
                  'direita' : 'Sala de Jantar',
                  'item' : 'chave'
                },

            'Cozinha': {'cima' : 'Saguão',
                  'item' : 'monstro'
                },

            'Sala de Jantar' : { 'esquerda' : 'Saguão',
                  'baixo' : 'Jardim',
                  'item' : 'poção'

                },

            'Jardim' : {'cima' : 'Sala de Jantar' }

         }

#pergunta ao jogador qual é o nome dele
if nome is None:
  nome = input("Qual é o teu nome Aventureiro? ")
  mostrarInstrucoes()

#repita infinitamente
while True:

  mostrarEstado()

  #pega o próximo 'movimento' do jogador
  #.split() quebra o texto em uma lista com cada palavra
  #ex. digitar 'para direita' resultaria na lista:
  #['para','direita']
  movimento = ''
  while movimento == '':
    movimento = input('>')

  movimento = movimento.lower().split()

  #se o jogador digitar primeiro 'para'
  if movimento[0] == 'para':
    saude = saude -1
    #verifica se eles podem ir aonde querem
    if movimento[1] in comodos[comodoAtual]:
      #define o novo cômodo como o atual
      comodoAtual = comodos[comodoAtual][movimento[1]]
    #não há porta (conexão) para o novo cômodo
    else:
      print('Você não pode ir para esse lado')

  #se eles digitarem 'pegar' primeiro
  if movimento[0] == 'pegar':
    #se o cômodo tiver um item, e o item é o qual eles desejam pegar
    if "item" in comodos[comodoAtual] and movimento[1] in comodos[comodoAtual]['item']:
      #adiciona o item ao inventário
      inventario += [movimento[1]]
      #exiba uma mensagem útil
      print('Pegou ' + movimento[1] + '!')
      #deleta o item do cômodo
      del comodos[comodoAtual]['item']
    #caso contrário, se o item não estiver lá
    else:
      #fale para o jogador que ele não pode pegar
      print('Não pode pegar o(a) ' + movimento[1] + '!')

  #o jogador perde se entrar em um cômodo com um monstro
  if "item" in comodos[comodoAtual] and 'monstro' in comodos[comodoAtual]['item']:
    print('O monstro te pegou... FIM DE JOGO!')
    break

  if saude == 0:
    print('Você ficou exausto... FIM DE JOGO!')

  #o jogador ganha se entrar no jardim com a chave e a poçāo
  if comodoAtual == 'Jardim' and 'chave' in inventario and 'poção' in inventario:
    print('Você conseguiu escapar... VOCÊ VENCEU!')
    break

  #-# O TEU CÓDIGO FICA AQUI #-#
  # Carregar os dados do jogo para o arquivo