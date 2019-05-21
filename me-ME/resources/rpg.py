#!/bin/python3

# Replace RPG starter project with this code when new instructions are live

def prikaziUputstva():
  #ispiši glavni meni i naredbe
  print('''
RPG igra
========
Naredbe:
  idi [smjer]
  uzmi [predmet]
''')

def prikaziStatus():
  #ispiši igračev trenutni status
  print('---------------------------')
  print('Prostorija u kojoj se nalaziš je ' + trenutnaProstorija)
  #ispiši trenutno stanje inventara
  print('Inventar : ' + str(inventar))
  #ispiši predmet ako postoji
  if "predmet" in prostorije[trenutnaProstorija]:
    print('Vidiš ' + prostorije[trenutnaProstorija]['predmet'])
  print("---------------------------")

#inventar koji je na početku prazan
inventar = []

#rječnik koji povezuje prostorije jednu sa drugom
prostorije = {

            'Hodnik' : { 
                  'jug' : 'Kuhinja'
                },

            'Kuhinja' : {
                  'sjever' : 'Hodnik'
                }

         }

#igrač započinje igru u Hodniku
trenutnaProstorija = 'Hodnik'

prikaziUputstva()

#ponavljaj neprestano
while True:

  prikaziStatus()

  #igračev sljedeći 'potez'
  #.split() ga razdvaja u listu
  #na primjer, upisivanjem 'idi istok' dobićemo listu:
  #['idi','istok']
  potez = ''
  while potez == '':  
    potez = input('>')
    
  potez = potez.lower().split()

  #ako se prvo upiše 'idi'
  if potez[0] == 'idi':
    #provjeri da li može da ide gdje želi
    if potez[1] in prostorije[trenutnaProstorija]:
      #postavi trenutnu prostoriju na novu prostoriju
      trenutnaProstorija = prostorije[trenutnaProstorija][potez[1]]
    #ne postoje vrata (veza) za novu prostoriju
    else:
        print('Ne možeš ići tuda!')

  #ako se prvo upiše 'uzmi'
  if potez[0] == 'uzmi' :
    #ako se u prostoriji nalazi predmet i igrač ga želi uzeti
    if 'predmet' in prostorije[trenutnaProstorija] and potez[1] in prostorije[trenutnaProstorija]['predmet']:
      #dodaj predmet u inventar
      inventar += [potez[1]]
      #prikaži potvrdnu poruku
      print(potez[1] + ' uzet!')
      #obriši predmet iz prostorije
      del prostorije[trenutnaProstorija]['predmet']
    #inače, ako ne postoji predmet koji igrač želi uzeti
    else:
      #reci igraču da ne može uzeti predmet
      print('Ne možeš uzeti ' + potez[1] + '!')

