## Dodavanje novih prostorija

+ Dio kôda za ovu igru smo ti već pripremili. Otvori ovaj trinket: <a href="http://jumpto.cc/rpg-go" target="_blank">jumpto.cc/rpg-go</a>.

+ Ovo je vrlo jednostavna RPG igra koja se sastoji od samo dvije prostorije. Ispod se nalazi nacrt igre:
    
    ![screenshot](images/rpg-map1.png)
    
    Upiši `idi jug` za pomicanje iz hodnika u kuhinju, a zatim `idi sjever` za povratak u hodnik!
    
    ![screenshot](images/rpg-controls.png)

+ Što se dogodi kada upišeš smjer u kojem ne možeš ići? Upiši `idi zapad` dok si u hodniku i dobit ćeš simpatičnu poruku o grešci.
    
    ![screenshot](images/rpg-error.png)

+ Pronađi varijablu `prostorije` i vidjet ćeš da je nacrt kodiran u obliku rječnika prostorija:
    
    ![screenshot](images/rpg-rooms.png)
    
    Svaka prostorija je jedan rječnik, a prostorije su međusobno povezane smjerovima.

+ Dodajmo istočno od hodnika blagovaonicu.
    
    ![screenshot](images/rpg-dining.png)
    
    Moraš dodati treću prostoriju koju ćeš nazvati `blagovaonica`. Također ju moraš povezati sa hodnikom na zapadu. Moraš dodati i podatke prostoriji hodnik u rječniku kako bi bilo moguće pomicati se u blagovaonicu na istoku.
    
    ![screenshot](images/rpg-dining-code.png)

+ Isprobaj igru sad kad si dodao blagovaonicu:
    
    ![screenshot](images/rpg-dining-test.png)
    
    Ako se ne možeš pomicati u blagovaonicu i iz nje, provjeri jesi li dodao sav kôd koji se nalazi iznad (uključujući i dodatne zareze u linijama).