## Aggiungere nemici

Il gioco è troppo semplice! In alcune stanze, aggiungiamo nemici che il giocatore deve evitare.

+ Aggiungere un nemico a una stanza è facile come aggiungere qualsiasi altro oggetto. Aggiungi un mostro affamato in cucina:
    
    ![screenshot](images/rpg-monster-dict.png)

+ Devi anche assicurarti che il gioco finisca se il giocatore entra in una stanza abitata da un mostro. Puoi farlo con il seguente codice, che dovresti aggiungere alla fine del gioco:
    
    ![screenshot](images/rpg-monster-code.png)
    
    Questo codice controlla se c'è un oggetto nella stanza, e in tal caso, se quell'oggetto è un mostro. Fai attenzione che questo codice rientra (indentazione), cioé é allineato con il codice sopra di esso. Ciò significa che il gioco controllerà la presenza di un mostro ogni volta che il giocatore si trasferisce in una nuova stanza.

+ Prova il tuo codice andando in cucina, che ora contiene un mostro.
    
    ![screenshot](images/rpg-monster-test.png)