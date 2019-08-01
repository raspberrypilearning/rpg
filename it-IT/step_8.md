## Vincere il gioco

Diamo al tuo giocatore una missione che deve essere completata per vincere la partita.

\--- task \--- In questo gioco il giocatore vince arrivando in giardino e fuggendo dalla casa. Deve anche avere con sè la chiave e la pozione magica. Ecco la mappa del gioco.

![screenshot](images/rpg-final-map.png) \--- /task \---

\--- task \--- Per cominciare aggiungi un giardino a sud della sala da pranzo. Ricorda di aggiungere porte per collegarti ad altre stanze della casa.

## \--- code \---

language: python

## line_highlights: 16-17,18-22

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
                'south' : 'Giardino'
            },
    
            'Giardino' : {
                'north' : 'Sala da Pranzo'
            }
    
        }
    

\--- /code \--- \--- /task \---

\--- task \--- Aggiungi una pozione in sala da pranzo (o in un'altra stanza della tua casa).

## \--- code \---

language: python

## line_highlights: 3-4

            'Sala da Pranzo' : {
                'west' : 'Ingresso',
                'south' : 'Giardino',
                'item' : 'pozione'
            },
    

\--- /code \--- \--- /task \---

\--- task \--- Aggiungi questo codice per consentire al giocatore di vincere la partita quando arriva in giardino con la chiave e la pozione:

## \--- code \---

language: python

## line_highlights: 6-9

# il giocatore perde se nella stanza c'è un mostro

if 'item' in rooms\[currentRoom] and 'monster' in rooms[currentRoom\]\['item'\]: print('Un mostro ti ha catturato... HAI PERSO!') break

# il giocatore vince se raggiunge il giardino con una chiave e un pozione

if currentRoom == 'Giardino' and 'chiave' in inventory and 'pozione' in inventory: print('Sei fuggito dalla casa... HAI VINTO!') break \--- /code \---

Assicurati che il codice sia indentato, allineato col codice che lo precede. Questo codice significa che il messaggio `Sei fuggito dalla casa... HAI VINTO!` VERRÀ visualizzato se il giocatore si trova nella stanza 4 (il giardino) e se la chiave e la pozione sono nell'inventario.

Se hai più di 4 camere, potresti dover utilizzare un numero di stanza diverso per il tuo giardino nel codice qui sopra. \--- /task \---

\--- task \--- Prova il tuo gioco per assicurarti che il giocatore possa vincere!

![screenshot](images/rpg-win-test.png) \--- /task \---

\--- task \--- Infine aggiungi alcune istruzioni al gioco, in modo che il giocatore sappia cosa deve fare. Modifica la funzione `showInstructions()` per includere più informazioni.

## \--- code \---

language: python

## line_highlights: 7-8

def showInstructions(): #mostra un meni e i comandi print('''

# Gioco RPG

Raggiungi il giardino con una chiave e una pozione Evita i mostri!

Comandi: go [direction] get [item] ''') \--- /code \---

Dovrai aggiungere istruzioni per dire all'utente quali oggetti devono raccogliere e cosa devono evitare! \--- /task \---

\--- task \--- Prova il tuo gioco e dovresti vedere le tue nuove istruzioni.

![screenshot](images/rpg-instructions-test.png) \--- /task \---