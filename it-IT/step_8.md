## Vincere il gioco

Diamo al tuo giocatore una missione che deve essere completata per vincere la partita.

\--- task \--- In this game, the player wins by getting to the garden and escaping the house. Deve anche avere con sè la chiave e la pozione magica. Ecco la mappa del gioco.

![schermata](images/rpg-final-map.png) \--- /task \---

\--- task \--- First, you need to add a garden to the south of the dining room. Ricorda di aggiungere porte per collegarti ad altre stanze della casa.

## \--- code \---

language: python

## line_highlights: 16-17,18-22

# un dizionario collega una stanza alle altre

stanze = {

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
                'west' : 'Hall',
                'south' : 'Garden'
            },
    
            'Garden' : {
                'north' : 'Dining Room'
            }
    
        }
    

\--- /code \--- \--- /task \---

\--- task \--- Add a potion to the dining room (or another room in your house).

## \--- code \---

language: python

## line_highlights: 3-4

            'Dining Room' : {
                'west' : 'Hall',
                'south' : 'Garden',
                'item' : 'potion'
            },
    

\--- /code \--- \--- /task \---

\--- task \--- Add this code to allow the player to win the game when they get to the garden with the key and the potion:

## \--- code \---

language: python

## line_highlights: 6-9

# player loses if they enter a room with a monster

if 'item' in rooms\[currentRoom] and 'monster' in rooms[currentRoom\]\['item'\]: print('A monster has got you... GAME OVER!') break

# player wins is they get to the garden with the key and potion

if currentRoom == 'Garden' and 'key' in inventory and 'potion' in inventory: print('You escaped the house... YOU WIN!') break \--- /code \---

Assicurati che il codice sia indentato, allineato col codice che lo precede. Questo codice significa che il messaggio `Sei fuggito dalla casa... HAI VINTO!` VERRÀ visualizzato se il giocatore si trova nella stanza 4 (il giardino) e se la chiave e la pozione sono nell'inventario.

Se hai più di 4 camere, potresti dover utilizzare un numero di stanza diverso per il tuo giardino nel codice qui sopra. \--- /task \---

\--- task \--- Test your game to make sure the player can win!

![schermata](images/rpg-win-test.png) \--- /task \---

\--- task \--- Finally, let’s add some instructions to your game, so that the player knows what they have to do. Modifica la funzione `mostraIstruzioni()` per includere più informazioni.

## \--- code \---

language: python

## line_highlights: 7-8

def showInstructions(): #print a main menu and the commands print('''

# Gioco RPG

Get to the Garden with a key and a potion Avoid the monsters!

Commands: go [direction] get [item] ''') \--- /code \---

Dovrai aggiungere istruzioni per dire all'utente quali oggetti devono raccogliere e cosa devono evitare! \--- /task \---

\--- task \--- Test your game and you should see your new instructions.

![schermata](images/rpg-instructions-test.png) \--- /task \---