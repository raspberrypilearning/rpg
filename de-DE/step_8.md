## Das Spiel gewinnen

Geben wir dem Spieler eine Mission die ausgeführt werden muss um das Spiel zu gewinnen.

+ In diesem Spiel gewinnt der Spieler, wenn er aus dem Haus fliehen kann und in den Garten gelangt. Dazu muss er/sie auch den Schlüssel und den Zaubertrank dabei haben. Hier ist ein Plan des Spiels.
    
    ![screenshot](images/rpg-final-map.png)

+ Dazu musst du erst einmal einen Garten im Süden des Esszimmers hinzufügen. Denke daran, Türen hinzuzufügen um ihn mit anderen Zimmern im Haus zu verbinden.
    
    ![Screenshot](images/rpg-garden.png)

+ Stelle einen Zaubertrank in das Esszimmer (oder in ein anderes Zimmer im Haus).
    
    ![screenshot](images/rpg-potion.png)

+ Füge diesen Code hinzu damit der Spieler das Spiel gewinnt wenn er den Garten mit dem Schlüssel und dem Zaubertrank erreicht:
    
    ![screenshot](images/rpg-win-code.png)
    
    Vergewissere dich, dass der Code genauso weit wie der darüberstehende Code eingerückt ist. Dieser Code bedeutet, dass die Nachricht `Du bist aus dem Haus entkommen... DU HAST GEWONNEN!` angezeigt wird, wenn der Spieler im 4. Zimmer (dem Garten) ist und sich der Schlüssel und der Zaubertrank in seinem Inventar befinden.
    
    Wenn du mehr als 4 Zimmer hast, musst du vielleicht eine andere Raumnummerierung für den Garten im obenstehenden Code verwenden.

+ Prüfe dein Spiel und vergewissere dich, dass der Spieler auch gewinnen kann!
    
    ![screenshot](images/rpg-win-test.png)

+ Lass uns zum Schluss ein paar Anweisungen hinzufügen, damit der Spieler auch weiß, was er tun muss. Bearbeite die Funktion `zeigeAnweisungen()` damit ausführlichere Information angezeigt wird.
    
    ![screenshot](images/rpg-instructions-code.png)
    
    Du musst Anleitungen hinzufügen um dem Spieler zu sagen, welche Gegenstände er nehmen muss und wem er ausweichen sollte!

+ Prüfe dein Spiel und du solltest die neuen Anweisungen sehen.
    
    ![screenshot](images/rpg-instructions-test.png)