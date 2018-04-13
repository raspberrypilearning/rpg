## Dodawanie wrogów

Ta gra jest zbyt łatwa! Dodajmy wrogów do niektórych pomieszczeń, których gracz musi unikać.

+ Dodanie wroga do pokoju jest tak proste, jak dodanie dowolnego innego przedmiotu. Dodajmy głodnego potwora do kuchni:
    
    ![zrzut ekranu](images/rpg-monster-dict.png)

+ Musisz również upewnić się, że gra się kończy, jeśli gracz wejdzie do pokoju z potworem. Możesz to zrobić za pomocą następującego kodu, który powinieneś dodać na końcu gry:
    
    ![zrzut ekranu](images/rpg-monster-code.png)
    
    Ten kod sprawdza, czy w pokoju jest przedmiot, a jeśli tak, to czy jest to potwór. Zauważ, że ten kod jest wcięty, co jest zgodne z kodem znajdującym się nad nim. Oznacza to, że gra sprawdzi potwora za każdym razem, gdy gracz wejdzie do nowego pokoju.

+ Przetestuj swój kod wchodząc do kuchni, w której teraz znajduje się potwór.
    
    ![zrzut ekranu](images/rpg-monster-test.png)