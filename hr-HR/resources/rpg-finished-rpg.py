#!/bin/python3

def prikaziUpute():
    #ispis glavnog izbornika i naredbi
    print('''
RPG igra labirinta
========

Otiđi do vrta s ključem i čarobnim napitkom
Izbjegni čudovišta!

Naredbe:
  idi [smjer]
  uzmi [predmet]
''')

def prikaziStatus():
  #ispis igračevog trenutnog statusa
  print('---------------------------')
  print('Prostorija u kojoj se nalaziš je ' + trenutnaProstorija)
  #ispis trenutnog stanja inventara
  print('Stanje inventara: ' + str(inventar))
  #ispis predmeta (ako postoji)
  if "predmet" in prostorije[trenutnaProstorija]:
    print('Vidiš ' + prostorije[trenutnaProstorija]['predmet'])
  print("---------------------------")

#inventar koji je na početku prazan
inventar = []

#rječnik koji povezuje prostorije jednu s drugom
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
                
            'Vrt' : { 'sjever' : 'Blagovaonica' }

         }

#igrač započinje igru u Hodniku
trenutnaProstorija = 'Hodnik'

prikaziUpute()

#petlja se neprestano ponavlja
while True:

  prikaziStatus()

  #igračev sljedeći 'potez'
  #naredba .split() razdvaja u listu tipa array
  #na primjer, upisivanjem 'idi istok' dobit ćemo listu:
  #['idi','istok']
  pomakni = ''
  while pomakni == '':  
    pomakni = input('>')
    
  pomakni = pomakni.lower().split()

  #ako se prvo upiše 'idi'
  if pomakni[0] == 'idi':
    #provjeri da smije ići gdje želi
    if pomakni[1] in prostorije[trenutnaProstorija]:
      #postavi trenutnu prostoriju na novu prostoriju
      trenutnaProstorija = prostorije[trenutnaProstorija][pomakni[1]]
    #ne postoje vrata koja vode u novu prostoriju
    else:
      print('Ne možeš ići tuda!')

  #ako se prvo upiše 'uzmi'
  if pomakni[0] == 'uzmi' :
    #ako se u prostoriji nalazi predmet i igrač ga želi uzeti
    if "predmet" in prostorije[trenutnaProstorija] and pomakni[1] in prostorije[trenutnaProstorija]['predmet']:
      #dodaj predmet u inventar
      inventar += [pomakni[1]]
      #prikaži poruku za pomoć igraču
      print(pomakni[1] + ' dohvaćen!')
      #obriši predmet iz prostorije
      del prostorije[trenutnaProstorija]['predmet']
    #inače, ako ne postoji predmet koji igrač želi uzeti
    else:
      #reci igraču da ne može uzeti predmet
      print('Ne možeš uzeti ' + pomakni[1] + '!')

  #igrač gubi igru ako uđe u prostoriju sa čudovištem
  if 'predmet' in prostorije[trenutnaProstorija] and 'čudovište' in prostorije[trenutnaProstorija]['predmet']:
    print('Čudovište te uhvatilo... IGRA JE GOTOVA!')
    break

  #igrač pobjeđuje ako dođe do vrta s ključem i čarobnim napitkom
  if trenutnaProstorija == 'Vrt' and 'ključ' in inventar and 'napitak' in inventar:
    print('Pobjegao/la si iz kuće... POBIJEDIO/LA SI!')
    break
  
