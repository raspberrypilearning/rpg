## Προσθήκη εχθρών

Αυτό το παιχνίδι παρά είναι εύκολο! Ας προσθέσουμε εχθρούς σε κάποια δωμάτια που ο παίκτης πρέπει να αποφύγει.

\--- task \---

Adding an enemy to a room is as easy as adding any other item. Let’s add a hungry monster to the kitchen:

## \--- code \---

language: python

## line_highlights: 11-12

# ένα λεξικό που συνδέει ένα δωμάτιο με τα άλλα

rooms = {

            'Χωλ' : {
                'νότια' : 'Κουζίνα',
                'ανατολικά' : 'Τραπεζαρία',
                'αντικείμενο' : 'κλειδί'
            },
    
            'Κουζίνα' : {
                'βόρεια' : 'Χωλ',
                'αντικείμενο' : 'τέρας'
            },
    
            'Τραπεζαρία' : {
                'δυτικά' : 'Χωλ'
            }
    
        }
    

\--- /code \---

\--- /task \---

\--- task \---

You also want to make sure that the game ends if the player enters a room with a monster in. You can do this with the following code, which you should add to the end of the game:

## \--- code \---

language: python

## line_highlights: 6-9

        #αλλιώς, αν το αντικείμενο δεν υπάρχει εκεί
        else:
            #πες ότι δεν μπορεί να το πάρει
            print('Δεν μπορώ να πάρω το' + move[1] + '!')
    
    #ο παίκτης χάνει, αν μπει σε δωμάτιο με τέρας 
    if 'αντικείμενο' in rooms[currentRoom] and 'τέρας' in rooms[currentRoom]['αντικείμενο']:
        print('Ένα τέρας σε έπιασε... ΤΕΛΟΣ ΠΑΙΧΝΙΔΙΟΥ!')
    break
    

\--- /code \---

This code checks whether there is an item in the room, and if so, whether that item is a monster. Notice that this code is indented, putting it in line with the code above it. This means that the game will check for a monster every time the player moves into a new room.

\--- /task \---

\--- task \---

Test out your code by going into the kitchen, which now contains a monster.

![screenshot](images/rpg-monster-test.png)

\--- /task \---