#!/bin/python3

# Replace RPG starter project with this code when new instructions are live

def toonInstructies():
  #laat een hoofdmenu en de commando's zien
  print('''
RPG Spel
========
Commando‘s:
  ga [richting]
  pak [voorwerp]
''')

def toonStatus():
  #laat de huidige status van de speler zien
  print('---------------------------')
  print('Je bent in de ' + dezeKamer)
  #laat de huidige inventaris zien
  print("inventaris : " + str(inventaris))
  #laat een voorwerp zien als er een is
  if "voorwerp" in kamers[dezeKamer]:
    print('Je ziet een ' + kamers[dezeKamer]['voorwerp'])
  print("---------------------------")

#een lege inventaris
inventaris = []

#een woordenboek die een kamer verbindt met andere kamers
kamers = {

            'Hal' : { 
                  'zuid' : 'Keuken'
                },

            'Keuken' : {
                  'noord' : 'Hal'
                }

         }

#laat de speler in de hal beginnen
dezeKamer = 'Hal'

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

