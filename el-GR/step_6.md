## Προσθήκη εχθρών

Αυτό το παιχνίδι παρά είναι εύκολο! Ας προσθέσουμε εχθρούς σε κάποια δωμάτια που ο παίκτης πρέπει να αποφύγει.

\--- task \--- Adding an enemy to a room is as easy as adding any other item. Ας προσθέσουμε ένα πεινασμένο τέρας στην κουζίνα:

## \--- code \---

language: python

## line_highlights: 11-12

# ένα λεξικό που συνδέει ένα δωμάτιο με τα άλλα

rooms = {

            'Hall' : {
                'south' : 'Kitchen',
                'east' : 'Dining Room',
                'item' : 'key'
            },
    
            'Kitchen' : {
                'north' : 'Hall',
                'item' : 'monster'
            },
    
            'Dining Room' : {
                'west' : 'Hall'
            }
    
        }
    

\--- /code \--- \--- /task \---

\--- task \--- You also want to make sure that the game ends if the player enters a room with a monster in. Μπορείς να το κάνεις με τον παρακάτω κώδικα, τον οποίο πρέπει να προσθέσεις στο τέλος του παιχνιδιού:

## \--- code \---

language: python

## line_highlights: 6-9

        #otherwise, if the item isn't there to get
        else:
            #tell them they can't get it
            print('Can\'t get' + move[1] + '!')
    
    #player loses if they enter a room with a monster
    if 'item' in rooms[currentRoom] and 'monster' in rooms[currentRoom]['item']:
        print('A monster has got you... GAME OVER!')
        break
    

\--- /code \---

Αυτός ο κώδικας ελέγχει εάν υπάρχει ένα αντικείμενο στο δωμάτιο και αν ναι, αν το αντικείμενο είναι ένα τέρας. Παρατήρησε ότι ο κώδικας αυτός είναι σε εσοχή, ευθυγραμμισμένος με τον κώδικα από πάνω του. Αυτό σημαίνει ότι το παιχνίδι θα ελέγξει αν υπάρχει τέρας κάθε φορά που ο παίκτης μετακινείται σε ένα νέο δωμάτιο. \--- /task \---

\--- task \--- Test out your code by going into the kitchen, which now contains a monster.

![screenshot](images/rpg-monster-test.png) \--- /task \---