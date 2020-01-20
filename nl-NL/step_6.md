## Vijanden toevoegen

Dit spel is te makkelijk! We gaan vijanden in een paar kamers toevoegen die de speler moet zien te vermijden.

\--- task \---

Adding an enemy to a room is as easy as adding any other item. Let’s add a hungry monster to the kitchen:

## \--- code \---

language: python

## line_highlights: 11-12

# een woordenboek die een kamer verbindt met andere kamers

rooms = {

            'Hal' : {
                'zuid' : 'Keuken',
                'oost' : 'Eetkamer',
                'voorwerp' : 'sleutel'
            },
    
            'Keuken' : {
                'noord' : 'Hal',
                'voorwerp' : 'monster'
            },
    
            'Eetkamer' : {
                'west' : 'Hal'
            }
    
        }
    

\--- /code \---

\--- /task \---

\--- task \---

You also want to make sure that the game ends if the player enters a room with a monster in. You can do this with the following code, which you should add to the end of the game:

## \--- code \---

language: python

## line_highlights: 6-9

        #anders, als het voorwerp er niet is om te pakken
        else:
            #vertel ze dat ze het niet kunnen pakken
            print('Kan ' + move[1] + ' niet pakken!')
    
    #speler verliest als ze een kamer met een monster ingaan
    if 'voorwerp' in kamers[dezeKamer] and 'monster' in kamers[dezeKamer]['voorwerp']:
        print('Een monster heeft je te pakken... GAME OVER!')
        break
    

\--- /code \---

This code checks whether there is an item in the room, and if so, whether that item is a monster. Notice that this code is indented, putting it in line with the code above it. This means that the game will check for a monster every time the player moves into a new room.

\--- /task \---

\--- task \---

Test out your code by going into the kitchen, which now contains a monster.

![screenshot](images/rpg-monster-test.png)

\--- /task \---