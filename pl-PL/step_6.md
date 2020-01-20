## Dodawanie wrogów

Ta gra jest zbyt łatwa! Dodajmy wrogów do niektórych pomieszczeń, których gracz musi unikać.

\--- task \---

Adding an enemy to a room is as easy as adding any other item. Let’s add a hungry monster to the kitchen:

## \--- code \---

language: python

## line_highlights: 11-12

# słownik łączący pokój z innymi pokojami

rooms = {

            'Korytarz' : {
                'południe' : 'Kuchnia',
                'wschód' : 'Jadalnia',
                'item' : 'klucz'
            },
    
            'Kuchnia' : {
                'północ' : 'Korytarz',
                'item' : 'potwór'        },
    
            'Jadalnia' : {
                'zachód' : 'Korytarz'
            }
    
        }
    

\--- /code \---

\--- /task \---

\--- task \---

You also want to make sure that the game ends if the player enters a room with a monster in. You can do this with the following code, which you should add to the end of the game:

## \--- code \---

language: python

## line_highlights: 6-9

        #w przeciwnym wypadku, jeśli przedmiotu nie można wziąć bo go nie ma
        else:
            #powiedz, że nie da się tego wziąć
            print('Tego nie możesz wziąć: ' + move[1] + '!')
    
    #gracz przegrywa jeśli wejdzie do pokoju z potworem
    if 'item' in rooms[currentRoom] and 'potwór' in rooms[currentRoom]['item']:
        print('Dorwał cię potwór... PRZEGRYWASZ!')
        break
    

\--- /code \---

This code checks whether there is an item in the room, and if so, whether that item is a monster. Notice that this code is indented, putting it in line with the code above it. This means that the game will check for a monster every time the player moves into a new room.

\--- /task \---

\--- task \---

Test out your code by going into the kitchen, which now contains a monster.

![screenshot](images/rpg-monster-test.png)

\--- /task \---