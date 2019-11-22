#!/bin/python3

def prikaziUpute():
    #ispis glavnog izbornika i naredbi
    print('''
RPG Igra
========

Otiđi do vrta s ključem i napitkom
Izbjegni čudovišta!

Postaješ umoran, svaki put kad se pomakneš izgubiš 1 točku zdravlja. 

Naredbe:
  go [direction]
  get [item]
''')

def prikaziStatus():
  #ispis igračevog trenutnog statusa
  print('---------------------------')
  print(name + ' je u ' + currentRoom)
  print("Zdravlje : " + str(health))
  #ispis trenutnog stanja inventara
  print('Inventar : ' + str(inventar))
  #ispis predmeta ako postoji
  if "predmet" in prostorije[currentRoom]:
    print('Vidiš ' + rooms[currentRoom]['predmet'])
  print("---------------------------")

# podešavanje igre
name = Prazno
zdravlje = 5
currentRoom = 'Hall'
inventory = []

#-# VAŠ KOD DOLAZI OVDJE #-#
# Učitaj podatke iz datoteke

#rječnik koji povezuje lokaciju prostorije jednu s drugom
prostorije = {

            'Hodnik' : { 'jug' : 'Kuhinja',
                  'istok'  : 'Blagovaonica',
                  'predmet'  : 'ključ'
                },

            'Kuhinja' : { 'sjever' : 'Hodnik',
                  'predmet'  : 'čudovište'
                },

            'Blagovaonica' : { 'zapad'  : 'Hodnik',
                  'jug' : 'Vrt',
                  'predmet'  : 'napitak'

                },

            'Vrt' : { 'north' : 'Dining Room' }

         }

# pitaj igrača njegovo ime
ako je ime None:
  name = input("Koja je tvoja avantura? ")
  prikaziUpute()

#petlja se neprestano ponavlja
while True:

  prikaziStatus()

  #igračev sljedeći 'potez'
  #.split() razdvaja u listu tipa array
  #na primjer, upisivanjem 'idi istok' dobit ćemo listu:
  #['idi','istok']
  pomakni = ''
  while pomakni == '':
    pomakni = input('>')

  pomakni = pomakni.lower().split()

  #ako se prvo upiše 'idi'
  if pomakni[0] == 'idi':
    zdravlje = zdravlje - 1
    #provjeri da smije ići gdje želi
    if pomakni[1] in prostorije[currentRoom]:
      #postavi trenutnu prostoriju na novu prostoriju
      trenutnaProstorija = prostorije[currentRoom][pomakni[1]]
    #ne postoje vrata (link) koja vode u novu prostoriju
    else:
      print('Ne možeš ići tuda!')

  #ako se prvo upiše 'uzmi'
  if pomakni[0] == 'uzmi' :
    #ako se u prostoriji nalazi predmet i igrač ga želi uzeti
    if "predmet" in prostorije[currentRoom] and pomakni[1] in prostorije[currentRoom]['predmet']:
      #dodaj predmet u inventar
      inventar += [pomakni[1]]
      #prikaži poruku za pomoć igraču
      print(pomakni[1] + ' dohvaćen!')
      #obriši predmet iz prostorije
      del prostorije[currentRoom]['predmet']
    #inače, ako ne postoji predmet koji igrač želi uzeti
    else:
      #reci igraču da ne može uzeti predmet
      print('Ne možeš uzeti ' + pomakni[1] + '!')

  #igrač gubi igru ako uđe u prostoriju sa čudovištem
  if 'predmet' in prostorije[currentRoom] and 'čudovište' in prostorije[currentRoom]['predmet']:
    print('Čudovište te uhvatilo... IGRA JE GOTOVA!')
    break

  if zdravlje == 0:
    print('Srušili ste se od umora... GAME OVER!')

  #igrač pobjeđuje ako dođe do vrta s ključem i čarobnim napitkom
  if trenutnaProstorija == 'Vrt' and 'ključ' in inventar and 'napitak' in inventar:
    print('Pobjegao/la si iz kuće... POBIJEDIO/LA SI!')
    break

  #-# VAŠ KOD DOLAZI OVDJE #-#
  # Spremite podatke u datoteku