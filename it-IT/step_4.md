## Aggiungere oggetti da raccogliere

Lascia degli oggetti nelle stanze in modo che il giocatore possa raccoglierli mentre si sposta attraverso il labirinto.

\--- task \--- Adding an item into a room is easy, you can just add it to a room's dictionary. Mettiamo una chiave nell'ingresso.

Ricorda di mettere una virgola dopo la riga sopra il nuovo oggetto, altrimenti il tuo programma non funzionerà!

## \--- code \---

language: python

## line_highlights: 6-7

# un dizionario collega una stanza alle altre

stanze = {

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

\--- task \--- If you run your game after adding the code above, you can now see a key in the hall, and you can even pick it up (by typing `get key`) which adds it to your inventory!

![schermata](images/rpg-key-test.png) \--- /task \---