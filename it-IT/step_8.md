## Vincere il gioco

Diamo al tuo giocatore una missione che deve essere completata per vincere il gioco.

+ In questo gioco, il giocatore vince raggiungendo il giardino e scappando dalla casa. Avrà bisogno di avere anche la chiave e la pozione magica. Ecco una mappa del gioco.

  ![screenshot](images/rpg-final-map.png)

+ Per prima cosa, dovrai aggiungere un giardino al sud della stanza da pranzo. Ricordati di aggiungere porte che colleghino alle altre stanze della casa.

  ![screenshot](images/rpg-garden.png)

+ Aggiungi una pozione alla stanza da pranzo (o in un'altra stanza della casa).

  ![screenshot](images/rpg-potion.png)

+ Aggiungi questo codice per fare in modo che il giocatore possa vincere il gioco quando arriva al giardino con la chiave e la pozione:

  ![screenshot](images/rpg-win-code.png)

  Assicurati che questo codice sia indentato, in linea con il codice di sopra. Questo codice significa che il messaggio 'Sei scappato dalla casa...HAI VINTO!' sia visualizzato se il giocatore si trova nella stanza 4 (il giardino) e se la chiave e la pozione sono nell'inventario.

  Se hai più di 4 stanze, potresti aver bisogno di usare un numero di stanza diverso per il tuo giardino nel codice sopra.

+ Prova il tuo gioco per assicurarti che il giocatore possa vincere!

  ![screenshot](images/rpg-win-test.png)

+ Per finire, aggiungiamo delle istruzioni al gioco, così che il giocatore sappia quello che deve fare. Modifica la funzione `showInstructions()` per includere altre informazioni.

  ![screenshot](images/rpg-instructions-code.png)

  Dovrai aggiungere istruzioni per indicare all'utente quali oggetti deve raccogliere, e cosa deve evitare!

+ Prova il tuo gioco e vedrai le tue nuove istruzioni!

  ![screenshot](images/rpg-instructions-test.png)
