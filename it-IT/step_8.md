## Vincere il gioco

Diamo al tuo giocatore una missione che deve essere completata per vincere la partita.

+ In questo gioco il giocatore vince arrivando in giardino e fuggendo dalla casa. Deve anche avere con sè la chiave e la pozione magica. Ecco la mappa del gioco.
    
    ![screenshot](images/rpg-final-map.png)

+ Per cominciare aggiungi un giardino a sud della sala da pranzo. Ricorda di aggiungere porte per collegarti ad altre stanze della casa.
    
    ![screenshot](images/rpg-garden.png)

+ Aggiungi una pozione in sala da pranzo (o in un'altra stanza della tua casa).
    
    ![screenshot](images/rpg-potion.png)

+ Aggiungi questo codice per consentire al giocatore di vincere la partita quando arriva in giardino con la chiave e la pozione:
    
    ![screenshot](images/rpg-win-code.png)
    
    Assicurati che il codice sia indentato, allineato col codice che lo precede. Questo codice significa che il messaggio `Sei fuggito dalla casa... HAI VINTO!` VERRÀ visualizzato se il giocatore si trova nella stanza 4 (il giardino) e se la chiave e la pozione sono nell'inventario.
    
    Se hai più di 4 camere, potresti dover utilizzare un numero di stanza diverso per il tuo giardino nel codice qui sopra.

+ Prova il tuo gioco per assicurarti che il giocatore possa vincere!
    
    ![screenshot](images/rpg-win-test.png)

+ Infine aggiungi alcune istruzioni al gioco, in modo che il giocatore sappia cosa deve fare. Modifica la funzione `mostraIstruzioni()` per includere più informazioni.
    
    ![screenshot](images/rpg-instructions-code.png)
    
    Dovrai aggiungere istruzioni per dire all'utente quali oggetti devono raccogliere e cosa devono evitare!

+ Prova il tuo gioco e dovresti vedere le tue nuove istruzioni.
    
    ![screenshot](images/rpg-instructions-test.png)