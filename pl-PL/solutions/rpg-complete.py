#!/bin/python3

def pokazInstrukcje():
    #wyświetl menu główne i polecenia
    print('''
Gra przygodowa (RPG)
========

Dostań się do ogrodu z kluczem i miksturą
Unikaj potworów!

To będzie męczące, za każdym razem gdy się poruszysz stracisz 1 punkt zdrowia. 

Polecenia:
  rusz-na [kierunek]
  bierz [przedmiot]
''')

def pokazStatus():
  #wyświetl aktualny status gracza
  print('---------------------------')
  print(nazwa + ' jest tu: ' + aktualnyPokoj)
  print("Zdrowie: " + str(zdrowie))
  #wyświetl aktualny ekwipunek
  print('Masz w ekwipunku: ' + str(ekwipunek))
  #Wyświetl przedmiot jeśli jakiś tam jest
  if "przedmiot" in pokoje[aktualnyPokoj]:
    print('Widzisz ' + pokoje[aktualnyPokoj]['przedmiot'])
  print("---------------------------")

# konfiguracja gry
nazwa = None
zdrowie = 5
aktualnyPokoj = 'Korytarz'
ekwipunek = []

#-# TWÓJ KOD ZACZYNA SIĘ TUTAJ #-#
# Wczytaj dane z pliku

#słownik łączący pokój z innymi pokojami
pokoje = {

            'Korytarz' : { 'południe' : 'Kuchnia',
                  'wschód'  : 'Jadalnia',
                  'przedmiot'  : 'klucz'
                },

            'Kuchnia' : { 'północ' : 'Korytarz',
                  'przedmiot'  : 'potwór'
                },

            'Jadalnia' : { 'zachód'  : 'Korytarz',
                  'południe' : 'Ogród',
                  'przedmiot'  : 'mikstura'

                },

            'Ogród' : { 'północ' : 'Jadalnia' }

         }

# zapytaj gracza o jego imię
if nazwa is None:
  nazwa = input("Jak masz na imię miłośniku przygód? ")
  pokazInstrukcje()

#pętla nieskończona
while True:

  pokazStatus()

  #sprawdź następny „ruch” gracza
  #.split() rozdziela ją na tablicę napisów
  #np. wpisanie 'rusz-na wschód' dałoby taką listę:
  #['rusz-na','wschód']
  ruch = ''
  while ruch == '':
    ruch = input('>')

  ruch = ruch.lower().split()

  #jeśli gracz wpisze najpierw 'rusz-na'
  if ruch[0] == 'rusz-na':
    zdrowie = zdrowie - 1
    #sprawdź, czy może iść tam gdzie zamierza
    if ruch[1] in pokoje[aktualnyPokoj]:
      #ustaw aktualny pokój na nowy pokój
      aktualnyPokoj = pokoje[aktualnyPokoj][ruch[1]]
    #nie ma drzwi (połączenia) do nowego pokoju
    else:
      print('Nie możesz iść tędy!')

  #jeśli gracz wpisze najpierw 'bierz'
  if ruch[0] == 'bierz' :
    #jeśli pomieszczenie zawiera przedmiot i jest to ten sam przedmiot, który gracz zamierza wziąć
    if 'przedmiot' in pokoje[aktualnyPokoj] and ruch[1] in pokoje[aktualnyPokoj]['przedmiot']:
      #dodaj przedmiot do ekwipunku
      ekwipunek += [ruch[1]]
      #wyświetl komunikat pomocniczy
      print('Wziąłeś: ' + ruch[1] + '!')
      #usuń przedmiot z pokoju
      del pokoje[aktualnyPokoj]['przedmiot']
    #w przeciwnym wypadku, jeśli przedmiotu nie można wziąć bo go nie ma
    else:
      #powiedz, że nie da się tego wziąć
      print('Tego nie możesz wziąć: ' + ruch[1] + '!')

  #gracz przegrywa jeśli wejdzie do pokoju z potworem
  if 'przedmiot' in pokoje[aktualnyPokoj] and 'potwór' in pokoje[aktualnyPokoj]['przedmiot']:
    print('Dorwał cię potwór... PRZEGRYWASZ!')
    break

  if zdrowie == 0:
    print('Upadasz z wyczerpania... PRZEGRYWASZ!')

  #gracz wygrywa jeśli dostanie się do ogrodu z kluczem i miksturą
  if aktualnyPokoj == 'Ogród' and 'klucz' in ekwipunek and 'mikstura' in ekwipunek:
    print('Wydostałeś się z domu... WYGRYWASZ!')
    break

  #-# TWÓJ KOD ZACZYNA SIĘ TUTAJ #-#
  # Zapisz dane gry do pliku