## Voorwerpen toevoegen om te verzamelen

We gaan voorwerpen in de kamers achterlaten die de speler kan verzamelen terwijl die door het doolhof zwerft.

\--- task \---

Adding an item into a room is easy, you can just add it to a room's dictionary. Let’s put a key in the hall.

Remember to put a comma after the line above the new item, or your program won’t run!

## \--- code \---

language: python

## line_highlights: 6-7

# een woordenboek die een kamer verbindt met andere kamers

rooms = {

            'Hall' : {
                'south' : 'Kitchen',
                'east' : 'Dining Room',
                'item' : 'key'
            },
    
            'Kitchen' : {
                'north' : 'Hall'
            },
    
            'Dining Room' : {
                'west' : 'Hall'
            }
    
        }
    

\--- /code \---

\--- /task \---

\--- task \---

If you run your game after adding the code above, you can now see a key in the hall, and you can even pick it up (by typing `get key`) which adds it to your inventory!

![screenshot](images/rpg-key-test.png)

\--- /task \---