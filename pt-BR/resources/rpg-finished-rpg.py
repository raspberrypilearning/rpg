#!/bin/python3

def mostrarInstrucoes():
    #exibe um menu principal e os comandos possiveis
    print('''
Jogo RPG
========

Vá para o Jardim com uma chave e uma poção
Evite os monstros!

Comandos:
  va[direcao]
  pegar[item]
''')

def mostrarEstado():
  #exibe o estado atual do jogador
  print('---------------------------')
  print('Você esta no ' + quartoAtual)
  #exibe o inventário atual
  print("Inventário :" + str(inventario))
  #exibe um item se houver um
  if "item" in quartos[quartoAtual]:
    print('Você vê um(a) ' + quartos[quartoAtual]['item'])
  print("---------------------------")

#um inventário que está inicialmente vazio
inventario = []

#um dicionário ligando um quarto as posições de outros quartos
quartos = {

            'Salao' : {'sul' : 'Cozinha',
                  'leste' : 'Sala de Jantar',
                  'item' : 'chave'
                },        

            'Cozinha': {'norte' : 'Salao',
                  'item' : 'monstro'
                },
                
            'Sala de Jantar' : { 'oeste' : 'Salao',
                  'sul' : 'Jardim',
                  'item' : 'poção'
              
                },
                
            'Jardim' : {'norte' : 'Sala de Jantar' }

         }

#começa o jogador no Salao
quartoAtual = 'Salao'

mostrarInstrucoes()

#repita infinitamente
while True:

  mostrarEstado()

  #pega o próximo 'movimento' do jogador
  #.split() quebra a entrada em uma lista vetor
  #eg digitar 'va leste' resultaria na lista:
  #['va','leste']
  movimento = ''
  while movimento == '':  
    movimento = input('>')
    
  movimento = movimento.lower().split()

  #se eles digitarem primeiro 'va'
  if movimento[0] == 'va':
    #verifica se eles podem ir onde pretendem
    if movimento[1] in quartos[quartoAtual]:
      #torna o novo quarto o quarto atual
      quartoAtual = quartos[quartoAtual][movimento[1]]
    #não há porta (conexão) para um novo quarto
    else:
      print('Você não pode ir para esse lado')

  #se eles digitarem 'pegar' primeiro
  if movimento[0] == 'pegar':
    #se o quarto contém um item, e o item é o qual eles desejam pegar
    if 'item' in quartos[quartoAtual] and movimento[1] in quartos[quartoAtual]['item']:
      #adicionar o item ao inventário
      inventario += [movimento[1]]
      #exiba uma mensagem útil
      print(movimento[1] + ' pego!')
      #deletar o item do quarto
      del quartos[quartoAtual]['item']
    #caso contrário, se o item não estiver lá
    else:
      #fale para eles que não podem pegar
      print('Não pode pegar' + movimento[1] + '!')

  # o jogador perde se ele entrar em um quarto que tem um monstro
  if 'item' in quartos[quartoAtual] and 'monstro' in quartos[quartoAtual]['item']:
    print('Um monstro pegou você... FIM DE JOGO!')
    break

  # o jogador ganha se ele chegar ao jardim com uma chave e uma poção
  if quartoAtual == 'Jardim' and 'chave' in inventario and 'poção' in inventario:
    print('Você escapou a casa... VOCÊ VENCEU!')
    break
  
