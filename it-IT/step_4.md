## Aggiungere oggetti da raccogliere

Lascia degli oggetti nelle stanze in modo che il giocatore possa raccoglierli mentre si sposta attraverso il labirinto.

--- task ---

Aggiungere un oggetto in una stanza è facile, basta aggiungerlo al dizionario di una stanza. Mettiamo una chiave nell'ingresso.

Ricorda di mettere una virgola dopo la riga sopra il nuovo oggetto, altrimenti il tuo programma non funzionerà!

--- code ---
---
language: python
line_highlights: 6-7
---

# un dizionario collega una stanza alle altre

stanze = {

            'Ingresso' : {
                'sud' : 'Cucina',
                'est' : 'Sala da Pranzo'
            },
    
            'Cucina' : {
                'nord' : 'Ingresso'
            },
    
            'Sala da Pranzo' : {
                'ovest' : 'Ingresso'
            }
    
        }
    

--- /code ---

--- /task ---

--- task ---

Se esegui il gioco dopo aver aggiunto il codice sopra, ora puoi vedere una chiave nell'ingresso e puoi persino raccoglierla (digitando `prendi chiave`), aggiungendola al tuo inventario!

![schermata](images/rpg-key-test.png)

--- /task ---