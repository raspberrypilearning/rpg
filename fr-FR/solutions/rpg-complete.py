#!/bin/python3

def showInstructions():
    #affiche un menu principal et les commandes
    print('''
Jeu RPG
========

Atteint le Jardin avec une clé et la potion
Évite les montres!

Commandes:
  aller [direction]
  prendre [objet]
''')

def showStatus():
  #affiche l'état actuel du joueur
  print('---------------------------')
  print('Tu es dans le/la ' + currentRoom)
  #affiche l'inventaire actuel
  print("Inventaire : " + str(inventaire))
  #affiche un objet s'il y en a un
  if "objet" in rooms[currentRoom]:
    print('Tu vois un/une ' + rooms[currentRoom]['objet'])
  print("---------------------------")

#un inventaire, qui est initialement vide
inventaire = []

#un dictionnaire liant une pièce d'autres positions de pièces
rooms = {

            'Hall' : { 'sud' : 'Cuisine',
                  'est'  : 'Salle a manger',
                  'objet'  : 'clé'
                },

            'Cuisine' : { 'nord' : 'Hall',
                  'objet'  : 'monstre'
                },

            'Salle a manger' : { 'ouest'  : 'Hall',
                  'sud' : 'Jardin',
                  'objet'  : 'potion'

                },

            'Jardin' : { 'nord' : 'Salle à manger' }

         }

#démarre le joueur dans le Hall
currentRoom = 'Hall'

showInstructions()

#loop forever
while True:

  showStatus()

  #obtenir la prochaine action du joueur
  #.split() le diviste dans un tableau de liste
  #ex en tapant 'aller est' donnerais la liste:
  #['aller','est']
  move = ''
  while move == '':
    move = input('>')

  move = move.lower().split()

  #s'ils tapent 'aller' en premier
  if move[0] == 'aller':
    #vérifie qu'ils soient autorisé peu importe où ils souhaitent aller
    if move[1] in rooms[currentRoom]:
      #définit la pièce actuel à une autre pièce
      currentRoom = rooms[currentRoom][move[1]]
    #il n'y a pas d'autre porte (lier) à une autre pièce
    else:
      print('Tu ne peux pas aller par là!')

  #s'il tape 'prendre' en premier
  if move[0] == 'prendre' :
    #si la pièce contient un objet, et l'objet est celui qu'ils souhaitent avoir
    if 'objet' in rooms[currentRoom] and move[1] in rooms[currentRoom]['objet']:
      #ajoute l'objet à leur inventaire
      inventaire += [move[1]]
      #affiche un message d'aide
      print(move[1] + ' obtenue!')
      #supprime l'objet de la pièce
      del rooms[currentRoom]['objet']
    #au sinon, si l'objet n'est pas là
    else:
      #leur indiquer qu'ils ne peuvent pas l'avoir
      print('Vous\ne pouvez pas l avoir ' + move[1] + '!')

  #le joueur perd s'il entre dans une pièce avec un monstre
  if 'objet' in rooms[currentRoom] and 'monstre' in rooms[currentRoom]['objet']:
    print('Un monstre t a eu... GAME OVER!')
    break

  #le joueur gagne s'il atteint le jardin avec la clé et la potion
  if currentRoom == 'Jardin' and 'clé' in inventaire and 'potion' in inventaire:
    print('Tu t es échappé de la maison... TU GAGNES!')
    break
