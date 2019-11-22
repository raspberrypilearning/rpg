#!/bin/python3

def showInstructions():
    #drukuj menu główne i polecenia
    print('''
Gra przygodowa (RPG)
========

Dostań się do ogrodu z kluczem i miksturą
Unikaj potworów!

To będzie męczące, za każdym razem gdy się poruszysz stracisz 1 punkt zdrowia. 

Polecenia:
  rusz.na [kierunek]
  bierz [przedmiot]
''')

def showStatus():
  #drukuj aktualny status gracza
  print('---------------------------')
  print(name + ' jest tu: ' + currentRoom)
  print("Zdrowie: " + str(health))
  #drukuj aktualny ekwipunek
  print('Masz w ekwipunku: ' + str(inventory))
  #drukuj przedmiot jeśli jakiś tam jest
  if "item" in rooms[currentRoom]:
    print('Widzisz ' + rooms[currentRoom]['item'])
  print("---------------------------")

# inicjuj grę
name = None
health = 5
currentRoom = 'Korytarz'
inventory = []

#-# TWÓJ KOD ZACZYNA SIĘ TUTAJ #-#
# Wczytaj dane z pliku

#słownik łączący pokój z innymi pokojami
rooms = {

            'Korytarz' : { 'południe' : 'Kuchnia',
                  'wschód'  : 'Jadalnia',
                  'item'  : 'klucz'
                },

            'Kuchnia' : { 'północ' : 'Korytarz',
                  'item'  : 'potwór'
                },

            'Jadalnia' : { 'zachód'  : 'Korytarz',
                  'południe' : 'Ogród',
                  'item'  : 'miksturę'

                },

            'Ogród' : { 'północ' : 'Jadalnia' }

         }

# zapytaj gracza o jego imię
if name is None:
  name = input("Jak masz na imię miłośniku przygód? ")
  showInstructions()

#pętla nieskończona
while True:

  showStatus()

  #sprawdź następny 'ruch' gracza
  #.split() rozdziela ja na tablicę napisów
  #np. wpisując 'rusz.na wschód' dałoby taką listę:
  #['rusz.na','wschód']
  move = ''
  while move == '':
    move = input('>')

  move = move.lower().split()

  #jeśli wpisze najpierw 'rusz.na'
  if move[0] == 'rusz.na':
    health = health - 1
    #sprawdź, czy może iść tam gdzie zamierza
    if move[1] in rooms[currentRoom]:
      #ustaw bieżący pokój na nowy pokój
      currentRoom = rooms[currentRoom][move[1]]
    #nie ma drzwi (połączenia) do nowego pokoju
    else:
      print('Nie możesz iść tędy!')

  #jeśli wpisze najpierw 'bierz'
  if move[0] == 'bierz' :
    #jeśli pomieszczenie zawiera przedmiot, i jeśli to jest ten sam, który zamierza wziąć
    if 'item' in rooms[currentRoom] and move[1] in rooms[currentRoom]['item']:
      #dodaj przedmiot do ekwipunku
      inventory += [move[1]]
      #wyświetl komunikat potwierdzający
      print('Wziąłeś ' + move[1] + '!')
      #usuń przedmiot z pokoju
      del rooms[currentRoom]['item']
    #w przeciwnym wypadku, jeśli przedmiotu nie można wziąć bo go nie ma
    else:
      #powiedz, że nie da się tego wziąć
      print('Tego nie możesz wziąć: ' + move[1] + '!')

  #gracz przegrywa jeśli wejdzie do pokoju z potworem
  if 'item' in rooms[currentRoom] and 'potwór' in rooms[currentRoom]['item']:
    print('Dorwał cię potwór... PRZEGRYWASZ!')
    break

  if health == 0:
    print('Upadasz z wyczerpania... PRZEGRYWASZ!')

  #gracz wygrywa jeśli dostanie się do ogrodu z kluczem i miksturą
  if currentRoom == 'Ogród' and 'klucz' in inventory and 'miksturę' in inventory:
    print('Wydostałeś się z domu... WYGRYWASZ!')
    break

  #-# TWÓJ KOD ZACZYNA SIĘ TUTAJ #-#
  # Zapisz dane gry do pliku