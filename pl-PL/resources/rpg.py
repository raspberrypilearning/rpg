#!/bin/python3

# Zastąp projekt startowy RPG tym kodem, kiedy użyte będą nowe instrukcje

def pokazInstrukcje():
  #wyświetl menu główne i polecenia
  print('''
Gra przygodowa (RPG)
========
Polecenia:
  rusz-na [kierunek]
  bierz [przedmiot]
''')

def pokazStatus():
  #wyświetl aktualny status gracza
  print('---------------------------')
  print('Jesteś tu: ' + aktualnyPokoj)
  #wyświetl aktualny ekwipunek
  print('Masz w ekwipunku: ' + str(ekwipunek))
  #wyświetl przedmiot jeśli jakiś tam jest
  if "przedmiot" in pokoje[aktualnyPokoj]:
    print('Widzisz: ' + pokoje[aktualnyPokoj]['przedmiot'])
  print("---------------------------")

#ekwipunek, początkowo pusty
ekwipunek = []

#słownik łączący pokój z innymi pokojami
pokoje = {

            'Korytarz' : { 
                  'południe' : 'Kuchnia'
                },

            'Kuchnia' : {
                  'północ' : 'Korytarz'
                }

         }

#ustaw gracza na początku w korytarzu
aktualnyPokoj = 'Korytarz'

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
    if "przedmiot" in pokoje[aktualnyPokoj] and ruch[1] in pokoje[aktualnyPokoj]['przedmiot']:
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

