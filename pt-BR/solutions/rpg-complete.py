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
# Carregar os dados do jogo para o arquivo

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

# perguntar ao jogador o nome dele
if nome is None:
  nome = input("Qual é o teu nome Aventureiro? ")
  mostrarInstrucoes()

#repita infinitamente
while True:

  mostrarEstado()

  #pega o próximo 'movimento' do jogador
  #.split() quebra a entrada em uma lista vetor
  #ex. digitar 'va leste' resultaria na lista:
  #['va','leste']
  movimento = ''
  while movimento == '':
    movimento = input('>')

  movimento = movimento.lower().split()

  #se eles digitarem primeiro 'va'
  if movimento[0] == 'va':
    saude = saude -1
    #verifica se eles podem ir onde pretendem
    if movimento[1] in comodos[comodoAtual]:
      #define o novo cômodo como o atual
      comodoAtual = comodos[comodoAtual][movimento[1]]
    #não há porta (conexão) para o novo cômodo
    else:
      print('Você não pode ir para esse lado')

  #se eles digitarem 'pegar' primeiro
  if movimento[0] == 'pegar':
    #se o quarto tiver um item, e o item é o qual eles desejam pegar
    if "item" in comodos[comodoAtual] and movimento[1] in comodos[comodoAtual]['item']:
      #adicionar o item ao inventário
      inventario += [movimento[1]]
      #exiba uma mensagem útil
      print('Pegou' + movimento[1] + '!')
      #deletar o item do cômodo
      del comodos[comodoAtual]['item']
    #caso contrário, se o item não estiver lá
    else:
      #fale para o jogador que ele não pode pegar
      print('Não pode pegar o(a)' + movimento[1] + '!')

  #o jogador perde se entrar em um cômodo com um monstro
  if "item" in comodos[comodoAtual] and 'monstro' in comodos[comodoAtual]['item']:
    print('Um monstro pegou você... FIM DE JOGO!')
    break

  if saude == 0:
    print('Você ficou exausto... FIM DE JOGO!')

  #o jogador ganha se entrar no jardim com a chave e a poçāo
  if comodoAtual == 'Jardim' and 'Chave' in inventario and 'Poção' in inventario:
    print('Você conseguiu escapar... VOCÊ VENCEU!')
    break

  #-# O TEU CÓDIGO FICA AQUI #-#
  # Carregar os dados do jogo para o arquivo