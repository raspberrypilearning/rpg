#!/bin/python3

# Zamień projekt startowy RPG tym kodem, kiedy użyte będą nowe instrukcje

def showInstructions():
  #drukuj menu główne i polecenia
  print('''
Gra przygodowa (RPG)
========
Polecenia:
  rusz.na [kierunek]
  bierz [przedmiot]
''')

def showStatus():
  #drukuj aktualny status gracza
  print('---------------------------')
  print('Jesteś tu: ' + currentRoom)
  #drukuj aktualny ekwipunek
  print('Masz w ekwipunku: ' + str(inventory))
  #drukuj przedmiot jeśli jakiś tam jest
  if "item" in rooms[currentRoom]:
    print('Widzisz ' + rooms[currentRoom]['item'])
  print("---------------------------")

#ekwipunek, początkowo pusty
inventory = []

#słownik łączący pokój z innymi pokojami
rooms = {

            'Korytarz' : { 
                  'południe' : 'Kuchnia'
                },

            'Kuchnia' : {
                  'północ' : 'Korytarz'
                }

         }

#ustaw gracza na początku w korytarzu
currentRoom = 'Korytarz'

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

  #jeśli wpisze najpierw 'ruszaj.na'
  if move[0] == 'rusz.na':
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
    if "item" in rooms[currentRoom] and move[1] in rooms[currentRoom]['item']:
      #dodaj przedmiot do ekwipunku
      inventory += [move[1]]
      #wyświetl komunikat pomocy
      print('Wziąłeś ' + move[1] + '!')
      #usuń przedmiot z pokoju
      del rooms[currentRoom]['item']
    #w przeciwnym wypadku, jeśli przedmiotu nie można wziąć bo go nie ma
    else:
      #powiedz, że nie da się tego wziąć
      print('Tego nie możesz wziąć: ' + move[1] + '!')

