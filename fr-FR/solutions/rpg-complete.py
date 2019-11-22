#!/bin/python3

def showInstructions():
    #affiche un menu principal et les commandes
    print('''
Jeu RPG
========

Atteins le Jardin avec une clé et la potion
Évite les montres!

Tu es fatigué, chaque fois que tu te déplaces, tu perds 1 point de santé. 

Commandes:
  aller [direction]
  prendre [objet]
''')

def showStatus():
  #affiche l'état actuel du joueur
  print('---------------------------')
  print(name + ' est dans le/la ' + currentRoom)
  print("Santé : " + str(health))
  #affiche l'inventaire actuel
  print("Inventaire : " + str(inventaire))
  #affiche un objet s'il y en a un
  if "objet" in rooms[currentRoom]:
    print('Tu vois un/une ' + rooms[currentRoom]['objet'])
  print("---------------------------")

#configure le jeu
name = None
health = 5
currentRoom = 'Hall'
inventory = []

#-# TON CODE VIENT ICI #-#
#Charge les donnée du fichier

#un dictionnaire liant une pièce aux autres positions de pièces
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

#demande au joueur leur nom
if name is None:
  name = input("Quel est ton nom d'Adventurier? ")
  showInstructions()

#loop forever
while True:

  showStatus()

  #obtenir la prochaine action du joueur
  #.split() le divise dans un tableau de liste
  #ex en tapant 'aller est' donnerais la liste:
  #['aller','est']
  move = ''
  while move == '':
    move = input('>')

  move = move.lower().split()

  #s'ils tapent 'aller' en premier
  if move[0] == 'aller':
    health = health - 1
    #vérifie qu'ils soient autorisés peu importe où ils souhaitent aller
    if move[1] in rooms[currentRoom]:
      #définis la pièce actuel à une autre pièce
      currentRoom = rooms[currentRoom][move[1]]
    #il n'y a pas de porte (lier) vers une autre pièce
    else:
      print('Tu ne peux pas aller par là!')

  #s'il tape 'prendre' en premier
  if move[0] == 'prendre' :
    #si la pièce contient un objet, et l'objet est celui qu'ils souhaitent avoir
    if 'objet' in rooms[currentRoom] and move[1] in rooms[currentRoom]['objet']:
      #ajoute l'objet à leur inventaire
      inventaire += [move[1]]
      #affiche un message utile
      print(move[1] + ' obtenue!')
      #supprime l'objet de la pièce
      del rooms[currentRoom]['objet']
    #sinon, si l'objet n'est pas là
    else:
      #leur indiquer qu'ils ne peuvent pas l'avoir
      print('Vous\ne pouvez pas l avoir ' + move[1] + '!')

  #le joueur perd s'il entre dans une pièce avec un monstre
  if 'objet' in rooms[currentRoom] and 'monstre' in rooms[currentRoom]['objet']:
    print('Un monstre t a eu... GAME OVER!')
    break

  if health == 0:
    print('Tu t effondres d'épuisement... GAME OVER!')

  #le joueur gagne s'il atteint le jardin avec la clé et la potion
  if currentRoom == 'Jardin' and 'clé' in inventaire and 'potion' in inventaire:
    print('Tu t es échappé de la maison... TU GAGNES!')
    break

  #-# TON CODE SE PLACE ICI #-#
  #sauve les données du jeu dans le fichier