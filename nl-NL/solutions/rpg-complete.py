#!/bin/python3

def toonInstructies():
    #laat een hoofdmenu en de commando's zien
    print('''
RPG Spel
========

Ga naar de Tuin met een sleutel en een toverdrank
Vermijd de monsters!

You are getting tired, each time you move you loose 1 health point. 

Commando's:
  ga [richting]
  pak [voorwerp]
''')

def toonStatus():
  #laat de huidige status van de speler zien
  print('---------------------------')
  print(name + ' is in the ' + currentRoom)
  print("Health : " + str(health))
  #laat de huidige inventaris zien
  print("inventaris : " + str(inventaris))
  #laat een voorwerp zien als er een is
  if "voorwerp" in kamers[dezeKamer]:
    print('Je ziet een ' + kamers[dezeKamer]['voorwerp'])
  print("---------------------------")

# setup the game
name = None
health = 5
currentRoom = 'Hall'
inventory = []

#-# YOUR CODE GOES HERE #-#
# Load data from the file

#een woordenboek die een kamer verbindt met andere kamers
kamers = {

            'Hal' : { 'zuid' : 'Keuken',
                  'oost'  : 'Eetkamer',
                  'voorwerp'  : 'sleutel'
                },

            'Keuken' : { 'noord' : 'Hal',
                  'voorwerp'  : 'monster'
                },

            'Eetkamer' : { 'west'  : 'Hal',
                  'zuid' : 'Tuin',
                  'voorwerp'  : 'toverdrank'

                },

            'Tuin' : { 'noord' : 'Eetkamer' }

         }

# ask the player their name
if name is None:
  name = input("What is your name Adventurer? ")
  toonInstructies()

#Voor altijd herhalen
while True:

  toonStatus()

  #vraag de volgende stap van de speler op
  #.split() splitst het op in een gerangschikte lijst
  #zo zal 'ga oost' deze lijst geven:
  #['ga','oost']
  beweeg = ''
  while beweeg == '':
    beweeg = input('>')

  beweeg = beweeg.lower().split()

  #als eerst 'ga' wordt getypt
  if beweeg[0] == 'ga':
    health = health - 1
    #kijk dan of alle richtingen beschikbaar zijn
    if beweeg[1] in kamers[dezeKamer]:
      #de huidige kamer wordt de nieuwe kamer
      dezeKamer = kamers[dezeKamer][beweeg[1]]
    #er is geen deur (verbinding) naar de nieuwe kamer
    else:
      print('Je kunt zo niet gaan!')

  #als eerst 'pak' wordt getypt
  if beweeg[0] == 'pak' :
    #als de kamer een voorwerp bevat en het je wilt het hebben
    if 'voorwerp' in kamers[dezeKamer] and beweeg[1] in kamers[dezeKamer]['voorwerp']:
      #voeg het voorwerp toe aan de inventaris
      inventaris += [beweeg[1]]
      #laat een verklarend berichtje zien
      print(beweeg[1] + ' hebbes!')
      #haal het voorwerp uit de kamer
      del kamers[dezeKamer]['voorwerp']
    #of, als er geen voorwerp is
    else:
      #geef aan dat er niks te pakken is
      print('Kan' + beweeg[1] + 'niet pakken!')

  #de speler verliest als er een monster in de kamer is
  if 'voorwerp' in kamers[dezeKamer] and 'monster' in kamers[dezeKamer]['voorwerp']:
    print('Een monster heeft je te pakken... GAME OVER!')
    break

  if health == 0:
    print('You collapse from exhaustion... GAME OVER!')

  #de speler wint als die in de tuin komt met een sleutel en een toverdrank
  if dezeKamer == 'Tuin' and 'sleutel' in inventaris and 'toverdrank' in inventaris:
    print('Je bent ontsnapt... JIJ WINT!')
    break

  #-# YOUR CODE GOES HERE #-#
  # Save game data to the file