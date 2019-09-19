#!/bin/python3

def showInstructions():
    #εμφάνισε ένα κύριο μενού και τις εντολές
    print('''
Παιχνίδι RPG
========

Βγες στον κήπο με ένα κλειδί κι ένα μαγικό φίλτρο
Απέφυγε τα τέρατα!

You are getting tired, each time you move you loose 1 health point. 

Εντολές:
  πήγαινε [κατεύθυνση]
  πάρε [αντικείμενο]
''')

def showStatus():
  #εμφάνισε την κατάσταση του παίκτη
  print('---------------------------')
  print(name + ' is in the ' + currentRoom)
  print("Health : " + str(health))
  #εμφάνισε το απόθεμα
  print("Απόθεμα : " + str(inventory))
  #εμφάνισε ένα αντικείμενο, αν υπάρχει
  if "αντικείμενο" in rooms[currentRoom]:
    print('Βλέπεις ένα ' + rooms[currentRoom]['αντικείμενο'])
  print("---------------------------")

# setup the game
name = None
health = 5
currentRoom = 'Hall'
inventory = []

#-# YOUR CODE GOES HERE #-#
# Load data from the file

#ένα λεξικό που συνδέει ένα δωμάτιο με άλλα δωμάτια
rooms = {

            'Χωλ' : { 'νότια' : 'Κουζίνα',
                  'ανατολικά'  : 'Τραπεζαρία',
                  'αντικείμενο'  : 'κλειδί'
                },

            'Κουζίνα' : { 'βόρεια' : 'Χωλ',
                  'αντικείμενο'  : 'τέρας'
                },

            'Τραπεζαρία' : { 'δυτικά'  : 'Χωλ',
                  'νότια' : 'Κήπος',
                  'αντικείμενο'  : 'φίλτρο'

                },

            'Κήπος' : { 'βόρεια' : 'Τραπεζαρία' }

         }

# ask the player their name
if name is None:
  name = input("What is your name Adventurer? ")
  showInstructions()

#επανέλαβε για πάντα
while True:

  showStatus()

  #παίρνουμε την επόμενη κίνηση του παίκτη
  #το .split() χωρίζει την απάντηση σε μία λίστα
  #για παράδειγμα το "πήγαινε ανατολικά" δίνει τη λίστα
  #['πήγαινε','ανατολικά']
  move = ''
  while move == '':
    move = input('>')

  move = move.lower().split()

  #αν πληκτρολογήσει "πήγαινε" στην αρχή
  if move[0] == 'πήγαινε':
    health = health - 1
    #έλεγξε ότι επιτρέπεται να πάει εκεί που θέλει
    if move[1] in rooms[currentRoom]:
      #δώσε στη μεταβλητή του τρέχοντος δωματίου την τιμή του νέου δωματίου
      currentRoom = rooms[currentRoom][move[1]]
    #δεν υπάρχει πόρτα (σύνδεσμος) για το νέο δωμάτιο
    else:
      print('Δεν μπορείς να πας προς τα εκεί!')

  #αν πληκτρολογήσει "πάρε" στην αρχή
  if move[0] == 'πάρε' :
    #αν το δωμάτιο περιέχει ένα αντικείμενο και το αντικείμενο είναι αυτό που θέλει να πάρει
    if 'αντικείμενο' in rooms[currentRoom] and move[1] in rooms[currentRoom]['αντικείμενο']:
      #πρόσθεσε το αντικείμενο στο απόθεμά του
      inventory += [move[1]]
      #εμφάνισε ένα επεξηγηματικό μήνυμα
      print(move[1] + ' ελήφθη!')
      #σβήσε το αντικείμενο από το δωμάτιο
      del rooms[currentRoom]['αντικείμενο']
    #αλλιώς, αν δεν υπάρχει το αντικείμενο
    else:
      #πες του ότι δεν μπορεί να το πάρει
      print('Δεν μπορείς να πάρεις το ' + move[1] + '!')

  #ο παίκτης χάνει αν μπει σε ένα δωμάτιο με τέρας
  if 'αντικείμενο' in rooms[currentRoom] and 'τέρας' in rooms[currentRoom]['αντικείμενο']:
    print('Ένας τέρας σε έπιασε... ΤΕΛΟΣ ΠΑΙΧΝΙΔΙΟΥ!')
    break

  if health == 0:
    print('You collapse from exhaustion... GAME OVER!')

  #ο παίκτης κερδίζει αν βγει στον κήπο με ένα κλειδί και ένα φίλτρο
  if currentRoom == 'Κήπος' and 'κλειδί' in inventory and 'φίλτρο' in inventory:
    print('Βγήκες από το σπίτι... ΝΙΚΗΣΕΣ!')
    break

  #-# YOUR CODE GOES HERE #-#
  # Save game data to the file