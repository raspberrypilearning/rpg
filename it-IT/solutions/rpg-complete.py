#!/bin/python3

def mostraIstruzioni():
    #stampa un menu principale e i comandi
    print('''
Gioco RPG
========

Raggiungi il giardino con una chiave e una pozione
Evita i mostri!

You are getting tired, each time you move you loose 1 health point. 

Comandi:
  vai [direzione]
  prendi [oggetto]
''')

def mostraPosizione():
  #stampa la posizione corrente del giocatore
  print('---------------------------')
  print(name + ' is in the ' + currentRoom)
  print("Health : " + str(health))
  #stampa il contenuto dell'inventario
  print('inventario : ' + str(inventario))
  #stampa un oggetto se presente nell'inventario
  if 'oggetto' in stanze[stanzaCorrente]:
    print('Vedi quest\'oggetto: ' + stanze[stanzaCorrente]['oggetto'])
  print('---------------------------')

# setup the game
name = None
health = 5
currentRoom = 'Hall'
inventory = []

#-# YOUR CODE GOES HERE #-#
# Load data from the file

#un dizionario collega una stanza alle altre
stanze = {

            'Ingresso' : { 'sud' : 'Cucina',
                  'est'  : 'Sala da pranzo',
                  'oggetto'  : 'chiave'
                },

            'Cucina' : { 'nord' : 'Ingresso',
                  'oggetto'  : 'mostro'
                },

            'Sala da pranzo' : { 'ovest'  : 'Ingresso',
                  'sud' : 'Giardino',
                  'oggetto'  : 'pozione'

                },

            'Giardino' : { 'nord' : 'Sala da pranzo'}

         }

# ask the player their name
if name is None:
  name = input("What is your name Adventurer? ")
  mostraIstruzioni()

#ciclo infinito
while True:

  mostraPosizione()

  #prende la prossima 'istruzione' del giocatore
  #e .split() la divide in una lista
  #per esempio digitando 'vai est' si ottiene la seguente lista:
  #['vai','est']
  istruzione = ''
  while istruzione == '':
    istruzione = input('>')

  istruzione = istruzione.lower().split()

  #se la prima parola digitata è 'vai'
  if istruzione[0] == 'vai':
    health = health - 1
    #verifica se la direzione inserita è consentita
    if istruzione[1] in stanze[stanzaCorrente]:
      #imposta la stanza corrente alla nuova inserita
      stanzaCorrente = stanze[stanzaCorrente][istruzione[1]]
    #altrimenti, se non c'è nessuna porta (collegamento) in quella direzione
    else:
      print('Non puoi andare da quella parte!')

  #se la prima parola digitata è 'prendi'
  if istruzione[0] == 'prendi' :
    #se la stanza contiene un oggetto ed è quello che si vuole raccogliere
    if 'oggetto' in stanze[stanzaCorrente] and istruzione[1] in stanze[stanzaCorrente]['oggetto']:
      #aggiungi l'oggetto all'inventario
      inventario += [istruzione[1]]
      #visualizza un messaggio di conferma
      print('Ho raccolto: ' + istruzione[1])
      #cancella l'oggetto dalla stanza
      del stanze[stanzaCorrente]['oggetto']
    #altrimenti, se non c'è nessun oggetto da prendere
    else:
      #informa che non si può prendere
      print('Impossibile prendere ' + istruzione[1] + '!')

  #il giocatore perde se nella stanza c'è un mostro
  if 'oggetto' in stanze[stanzaCorrente] and 'mostro' in stanze[stanzaCorrente]['oggetto']:
    print('Una creatura mostruosa ti ha catturato... GAME OVER!')
    break

  if health == 0:
    print('You collapse from exhaustion... GAME OVER!')

  #il giocatore vince se raggiunge il giardino con una chiave e un pozione
  if stanzaCorrente == 'Giardino' and 'chiave' in inventario and 'pozione' in inventario:
    print('Sei scappato dalla casa... HAI VINTO!')
    break

  #-# YOUR CODE GOES HERE #-#
  # Save game data to the file