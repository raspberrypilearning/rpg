#!/bin/python3

def afiseazaInstructiuni():
    #afiseaza meniul principal si comenzile
    print('''
Jocul RPG
========

Du-te in Gradina cu o cheie si o potiune
Evita monstrii!

Te simti tot mai obosit, de fiecare data cand te misti, pierzi 1 punct de sanatate. 

Comenzile:
  misca [directie]
  ia [item]
''')

def afiseazaStatus():
  #afiseaza statusul actual al jucatorului
  print('---------------------------')
  print(nume + 'se afla in  ' + cameraCurenta)
  print("Sanatate: " + str(sanatate))
  #afiseaza inventarul curent
  print('Inventar : ' + str(inventar))
  #afiseaza un item daca exista
  if "item" in camere[cameraCurenta]:
    print('Vezi un item  ' + camere[cameraCurenta]['item'])
  print("---------------------------")

# initializeaza jocul
nume = None
sanatate = 5
cameraCurenta = 'Hol'
inventar = []

#-# ADAUGA-TI AICI CODUL #-#
# Incarca datele din fisier

#un dictionar asociind o camera cu alte camere
camere = {

            'Hol' : { 'sud' : 'Bucatarie',
                  'est'  : 'Sufragerie',
                  'item'  : 'cheie'
                },

            'Bucatarie' : { 'nord' : 'Hol',
                  'item'  : 'monstru'
                },

            'Sufragerie' : { 'vest'  : 'Hol',
                  'sud' : 'Gradina',
                  'item'  : 'potiune'

                },

            'Gradina' : { 'nord' : 'Sufragerie' }

         }

# intreaba-l pe jucator cum se numeste
if nume is None:
  nume = input("Care este numele tau, aventurierule? ")
  afiseazaInstructiuni()

#repeta de un numar infinit de ori
while True:

  afiseazaStatus()

  #obtine urmatoare 'miscare' a jucatorului
  #.split() o imparte intr-un list array
  #de exemplu, daca tastezi 'misca est', vei obtine lista:
  #['misca','est']
  miscare = ''
  while miscare == '':
    miscare = input('>')

  miscare = miscare.lower().split()

  #daca utilizatorul tasteaza intai 'misca'
  if miscare[0] == 'misca':
    sanatate = sanatate - 1
    #verifica daca au voie sa mearga unde au cerut
    if miscare[1] in camere[cameraCurenta]:
      #seteaza camera curenta la noua camera
      cameraCurenta = camere[cameraCurenta][miscare[1]]
    #nu este nici o usa (legatura) catre noua camera
    else:
      print('Nu poti sa o iei pe acolo!')

  #daca utilizatorul tasteaza intai 'ia'
  if miscare[0] == 'ia' :
    #daca exista un item in camera si itemul este cel pe care utilizatorul il vrea
    if "item" in camere[cameraCurenta] and miscare[1] in camere[cameraCurenta]['item']:
      #adauga itemul la inventarul sau
      inventar += [miscare[1]]
      #afiseaza un mesaj util
      print(miscare[1] + ' luat!')
      #sterge acest item din camera
      del camere[cameraCurenta]['item']
    #altfel, daca itemul nu este acolo si nu poate fi luat
    else:
      #spune-i ca nu il poate lua
      print('Nu poti lua ' + miscare[1] + '!')

  #jucatorul pierde daca intra intr-o camera cu un monstru
  if "item" in camere[cameraCurenta] and 'monstru' in camere[cameraCurenta]['item']:
    print('Un monstru te-a prins... STOP JOC!')
    break

  if sanatate == 0:
    print('Te prabusesti de oboseala... STOP JOC!')

  #jucatorul castiga daca ajunge in gradina cu cheia si potiunea
  if cameraCurenta == 'Gradina' and 'cheie' in inventar and 'potiune' in inventar:
    print('Ai scapat din casa... AI CASTIGAT!')
    break

  #-# ADAUGA-TI AICI CODUL #-#
  # Salveaza informatiile despre joc in fisier