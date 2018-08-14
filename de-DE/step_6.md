## Feinde (Monster) hinzufügen

Dieses Spiel ist zu einfach! Lass uns Monster in einige Zimmer setzen, denen der Spieler ausweichen muss.

+ Ein Monster in ein Zimmer zu setzen ist genauso einfach wie einen neuen Gegenstand hineinzulegen. Setzen wir ein hungriges Monster in die Küche:
    
    ![screenshot](images/rpg-monster-dict.png)

+ Du willst auch, dass das Spiel zu Ende ist, wenn der Spieler ein Zimmer betritt, in dem sich ein Monster aufhält. Du kannst das mit folgendem Code bewerkstelligen, der am Ende des Spiels hinzugefügt wird:
    
    ![screenshot](images/rpg-monster-code.png)
    
    Dieser Code prüft, ob sich ein Gegenstand im Zimmer befindet; und wenn ja, ob dieser Gegenstand ein Monster ist. Denke daran, dass dieser Code eingerückt ist und er in der gleichen Spalte sein muss wie der Code darüber. Das heißt, jedes Mal wenn der Spieler einen neues Zimmer betritt, prüft das Spiel ob sich dort ein Monster befindet.

+ Teste dein Spiel indem du in die Küche gehst, wo sich jetzt ein Monster befindet.
    
    ![screenshot](images/rpg-monster-test.png)