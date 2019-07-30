## Aggiungere nuove stanze

\--- task \--- Open the Python starter project.

**Online**: open the starter project at [rpf.io/rpgon](http://rpf.io/rpgon){:target="_blank"}.

**Offline**: open the [starter project](http://rpf.io/p/en/rpg-go){:target="_blank"} in the offline editor. \--- /task \---

\--- task \--- This is a very basic RPG game that only has 2 rooms. Ecco la mappa del gioco:

![schermata](images/rpg-map1.png)

Puoi digitare `vai sud`per spostarti dalla sala alla cucina, e poi `vai nord` per tornare di nuovo all'ingresso!

![schermata](images/rpg-controls.png) \--- /task \---

\--- task \--- What happens when you type in a direction that you cannot go? Digita `vai ovest`nell'ingresso e riceverai un messaggio di errore.

![schermata](images/rpg-error.png) \--- /task \---

\--- task \--- If you find the `rooms` variable, you can see that the map is coded as a dictionary of rooms:

## \--- code \---

## language: python

# un dizionario collega una stanza alle altre

stanze = {

            'Hall' : {
                'south' : 'Kitchen'
            },
    
            'Kitchen' : {
                'north' : 'Hall'
            }
    
        }
    

\--- /code \---

Each room is a dictionary, and rooms are linked together using directions.  
\--- /task \---

\--- task \--- Let’s add a dining room to your map, to the east of the hall.

![schermata](images/rpg-dining.png)

You need to add a 3rd room, called the `dining room`, and link it to the hall (to the west). Devi anche aggiungere dati all'ingresso, in modo da poterti spostare nella sala da pranzo ad est.

**Don't forget that you'll also need to add commas to lines before your new code.**

## \--- code \---

language: python

## line_highlights: 5-6,11-15

# un dizionario collega una stanza alle altre

stanze = {

            'Hall' : {
                'south' : 'Kitchen',
                'east' : 'Dining Room'
            },
    
            'Kitchen' : {
                'north' : 'Hall'
            },
    
            'Dining Room' : {
                'west' : 'Hall'
            }
    
        }
    

\--- /code \--- \--- /task \---

\--- task \--- Try out the game with your new dining room:

![schermata](images/rpg-dining-test.png)

Se non riesci ad entrare e uscire dalla sala da pranzo, controlla di aver aggiunto tutto il codice sopra riportato (comprese le virgole extra alle righe sopra). \--- /task \---