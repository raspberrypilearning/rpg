#!/bin/python3

def zeigeAnweisungen():
    #Zeige ein Hauptmenü und die möglichen Befehle
    print('''
RPG Spiel (Labyrinth)
========

Suche den Schlüssel und den Zaubertrank und versuche dann, in den Garten zu entkommen.
Lass dich nicht von den Monstern fressen!

Du wirst müde, jedes mal, wenn du einen Schritt machst, verlierst du 1 Gesundheitspunkt. 

Befehle:
  gehenach [Richtung]
  nimm [Gegenstand]
''')

def zeigeZustand():
  #Zeige den aktuellen Zustand des Spielers
  print('---------------------------')
  print(name + ' ist im Zimmer: ' + aktuellesZimmer)
  print("Gesundheit : " + str(gesundheit))
  #Zeige das aktuelle Inventar
  print('Inventar : ' + str(inventar))
  #Zeige einen Gegenstand an, wenn einer im Zimmer vorhanden ist
  if "Gegenstand" in zimmer[aktuellesZimmer]:
    print('Du siehst einen ' + zimmer[aktuellesZimmer]['Gegenstand'])
  print("---------------------------")

# bereite das Spiel vor
name = None
gesundheit = 5
aktuellesZimmer = 'Diele'
inventar = []

#-# HIER KOMMT DEIN CODE #-#
# Lade Daten aus der Datei

#Ein Dictionary (Wörterbuch) verbindet ein Zimmer mit anderen Zimmern
zimmer = {

            'Diele' : { 'süden' : 'Küche',
                  'osten'  : 'Esszimmer',
                  'Gegenstand' : 'Schlüssel'
                },

            'Küche' : { 'norden' : 'Diele',
                  'Gegenstand'  : 'Monster'
                },

            'Esszimmer' : { 'westen'  : 'Diele',
                  'süden' : 'Garten',
                  'Gegenstand'  : 'Zaubertrank'

                },

            'Garten' : { 'norden' : 'Esszimmer' }

         }

# frag den Spieler nach seinem Namen
if name is None:
  name = input("Wie ist dein Name, Abenteurer? ")
  zeigeAnweisungen()

#Ewige Schleife
while True:

  zeigeZustand()

  #Warte auf den 'nächsten Spielzug (die nächste Bewegung)' des Spielers
  #.split() teilt ihn in ein Array auf
  #Wenn du z.B. 'gehenach osten' eintippst, erhältst du folgende Liste:
  #['gehenach','osten']
  spielzug = ''
  while spielzug == '':
    spielzug = input('>')

  spielzug = spielzug.split()
#please do not change - in German the object names start with uppercase letter

  #Wenn das Eingetippte mit 'gehenach' beginnt
  if spielzug[0] == 'gehenach':
    gesundheit = gesundheit - 1
    #Prüfe, ob der Spieler auch dorthin gehen kann, wo er hin will
    if spielzug[1] in zimmer[aktuellesZimmer]:
      #Mache das neue Zimmer zum aktuellen Zimmer
      aktuellesZimmer = zimmer[aktuellesZimmer][spielzug[1]]
    #Es gibt keine Tür (Verbindung) zum neuen Zimmer
    else:
      print('Du kannst nicht in diese Richtung gehen!')

  #Wenn das Eingetippte mit 'nimm' beginnt
  if spielzug[0] == 'nimm' :
    #Wenn das Zimmer einen Gegenstand enthält, und du genau diesen Gegenstand nehmen willst
    if "Gegenstand" in zimmer[aktuellesZimmer] and spielzug[1] in zimmer[aktuellesZimmer]['Gegenstand']:
      #Füge den Gegenstand dem Inventar des Spielers hinzu
      inventar += [spielzug[1]]
      #Zeige eine hilfreiche Mitteilung
      print(spielzug[1] + ' wurde genommen!')
      #Lösche den Gegenstand vom Zimmer
      del zimmer[aktuellesZimmer]['Gegenstand']
    #Andernfalls ist der Gegenstand nicht vorhanden und kann auch nicht genommen werden
    else:
      #Sage dem Spieler, dass er diesen Gegenstand nicht nehmen kann
      print('Du kannst ' + spielzug[1] + ' nicht nehmen!')

  #Der Spieler verliert, wenn er ein Zimmer mit einem Monster betritt
  if "Gegenstand" in zimmer[aktuellesZimmer] and 'Monster' in zimmer[aktuellesZimmer]['Gegenstand']:
    print('Du wurdest von einem hungrigen Monster gefressen... DAS SPIEL IST AUS!')
    break

  if gesundheit == 0:
    print('Du brichst vor Erschöpfung zusammen... DAS SPIEL IST AUS!')

  #Der Spieler gewinnt, wenn er mit dem Schlüssel und dem Zaubertrank den Garten erreicht
  if aktuellesZimmer == 'Garten' and 'Schlüssel' in inventar and 'Zaubertrank' in inventar:
    print('Du bist aus dem Haus entkommen... DU HAST GEWONNEN!')
    break

  #-# HIER KOMMT DEIN CODE #-#
  # speichere die Spiel-Daten in die Datei