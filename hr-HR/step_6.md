## Dodavanje neprijatelja

Ova igra je prejednostavna! Dodajmo u neke od prostorija neprijatelje koje će igrač izbjegavati.

+ Dodavanje neprijatelja u prostoriju je jednostavno kao i dodavanje bilo kojeg drugog predmeta. Dodajmo gladno čudovište u kuhinju:
    
    ![screenshot](images/rpg-monster-dict.png)

+ Također se želiš pobrinuti da se igra završi ako igrač uđe u prostoriju u kojoj se nalazi čudovište. To možeš napraviti dodavanjem sljedećeg kôda na kraju igre:
    
    ![screenshot](images/rpg-monster-code.png)
    
    Ovaj kôd provjerava postoji li neki predmet u prostoirji i ako postoji je li taj predmet čudovište. Primijeti da je kôd uvučen pa je na istoj razini kao i kôd iznad njega. To znači da će igra provjeravati postoji li čudovište u prostoriji svaki put kada igrač uđe u novu prostoriju.

+ Testiraj svoj kôd tako da uđeš u kuhinju u kojoj se sada nalazi čudovište.
    
    ![screenshot](images/rpg-monster-test.png)