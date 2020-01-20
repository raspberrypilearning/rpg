## Feinde (Monster) hinzufügen

Dieses Spiel ist zu einfach! Lass uns Monster in einige Zimmer setzen, denen der Spieler ausweichen muss.

\--- task \---

Adding an enemy to a room is as easy as adding any other item. Let’s add a hungry monster to the kitchen:

## \--- code \---

language: python

## line_highlights: 11-12

# Ein Dictionary (Wörterbuch) verbindet ein Zimmer mit anderen Zimmern

rooms = {

            'Diele' : {
                'süden' : 'Küche',
                'osten' : 'Esszimmer',
                'Gegenstand' : 'Schlüssel'
            },
    
            'Küche' : {
                'norden' : 'Diele',
                'Gegenstand' : 'Monster'
            },
    
            'Esszimmer' : {
                'westen' : 'Diele'
            }
    
        }
    

\--- /code \---

\--- /task \---

\--- task \---

You also want to make sure that the game ends if the player enters a room with a monster in. You can do this with the following code, which you should add to the end of the game:

## \--- code \---

language: python

## line_highlights: 6-9

        #Andernfalls ist der Gegenstand nicht vorhanden und kann auch nicht genommen werden
        else:
            #Sage dem Spieler, dass er diesen Gegenstand nicht nehmen kann
            print('Du kannst ' + spielzug[1] + ' nicht nehmen!')
    
    #Der Spieler verliert, wenn er ein Zimmer mit einem Monster betritt
    if 'Gegenstand' in zimmer[aktuellesZimmer] and 'Monster' in zimmer[aktuellesZimmer]['Gegenstand']:
        print('Du wurdest von einem hungrigen Monster gefressen... DAS SPIEL IST AUS!')
        break
    

\--- /code \---

This code checks whether there is an item in the room, and if so, whether that item is a monster. Notice that this code is indented, putting it in line with the code above it. This means that the game will check for a monster every time the player moves into a new room.

\--- /task \---

\--- task \---

Test out your code by going into the kitchen, which now contains a monster.

![screenshot](images/rpg-monster-test.png)

\--- /task \---