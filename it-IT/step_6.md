## Aggiungere nemici

Il gioco è troppo semplice! Aggiungiamo in alcune stanze nemici da evitare.

+ Aggiungere un nemico a una stanza è facile come aggiungere qualsiasi altro oggetto. Aggiungi un mostro affamato in cucina:
    
    ![screenshot](images/rpg-monster-dict.png)

+ Devi anche assicurarti che il gioco finisca se il giocatore entra in una stanza con un mostro. Puoi farlo con il seguente codice, che dovresti aggiungere alla fine del gioco:
    
    ![screenshot](images/rpg-monster-code.png)
    
    Questo codice controlla se c'è un oggetto nella stanza, e in tal caso, se quell'oggetto è un mostro. Nota che questo codice è indentato in modo da allinearlo con la linea di codice precedente. Di conseguenza il gioco controllerà la presenza di un mostro ogni volta che il giocatore si trasferisce in una nuova stanza.

+ Prova il tuo codice andando in cucina, che ora contiene un mostro.
    
    ![screenshot](images/rpg-monster-test.png)