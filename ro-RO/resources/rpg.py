#!/bin/python3

# Inlocuieste proiectul initial RPG cu acest cod cand noile instructiuni apar online

def afiseazaInstructiuni():
  #afiseaza meniul principal si comenzile
  print('''
Jocul RPG
========
Comenzile:
  misca [directie]
  ia [item]
''')

def afiseazaStatus():
  #afiseaza statusul actual al jucatorului
  print('---------------------------')
  print('Te afli in ' + cameraCurenta)
  #afiseaza inventarul curent
  print('Inventar : ' + str(inventar))
  #afiseaza un item daca exista
  if "item" in camere[cameraCurenta]:
    print('Vezi un ' + camere[cameraCurenta]['item'])
  print("---------------------------")

#un inventar initial vid
inventar = []

#un dictionar asociind o camera cu alte camere
camere = {

            'Hol' 
                  'sud' : 'Bucatarie'
                },

            'Bucatarie'
                  'nord' : 'Hol'
                }

         }

#incepe cu jucatorul in Hol
cameraCurenta = 'Hol'

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
      print(miscare[1] + 'luat!')
      #sterge acest item din camera
      del camere[cameraCurenta]['item']
    #altfel, daca itemul nu este acolo si nu poate fi luat
    else:
      #spune-i ca nu il poate lua
      print('Nu poti lua ' + miscare[1] + '!')

