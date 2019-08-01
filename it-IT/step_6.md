## Aggiungere nemici

Il gioco è troppo semplice! Aggiungiamo in alcune stanze nemici da evitare.

\--- task \--- Aggiungere un nemico a una stanza è facile come aggiungere qualsiasi altro oggetto. Aggiungi un mostro affamato in cucina:

## \--- code \---

language: python

## line_highlights: 11-12

# un dizionario collega una stanza alle altre

stanze = {

            'Ingresso' : {
                'south' : 'Cucina',
                'east' : 'Sala da Pranzo'
            },
    
            'Cucina' : {
                'north' : 'Ingresso'
            },
    
            'Sala da Pranzo' : {
                'west' : 'Ingresso'
            }
    
        }
    

\--- /code \--- \--- /task \---

\--- task \--- Devi anche assicurarti che il gioco finisca se il giocatore entra in una stanza con un mostro. Puoi farlo con il seguente codice, che dovresti aggiungere alla fine del gioco:

## \--- code \---

language: python

## line_highlights: 6-9

        #altrimenti, se l'oggetto non c'è
        else:
            #informa che non possono prenderlo
            print('Can\'t get' + move[1] + '!')
    
    #il giocatore perde se entra in una stanza con un mostro
    if 'item' in rooms[currentRoom] and 'monster' in rooms[currentRoom]['item']:
        print('Un mostro ti ha catturato... HAI PERSO!')
        break
    

\--- /code \---

Questo codice controlla se c'è un oggetto nella stanza, e in tal caso, se quell'oggetto è un mostro. Nota che questo codice è indentato in modo da allinearlo con la linea di codice precedente. Di conseguenza il gioco controllerà la presenza di un mostro ogni volta che il giocatore si trasferisce in una nuova stanza. \--- /task \---

\--- task \--- Test out your code by going into the kitchen, which now contains a monster.

![schermata](images/rpg-monster-test.png) \--- /task \---