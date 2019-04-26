## Dodawanie nowych pokoi

+ Dostarczono kod do tej gry. Otwórz ten szablon: <a href="http://jumpto.cc/rpg-go" target="_blank">jumpto.cc/rpg-go</a>.

+ Jest to bardzo prosta gra RPG, która ma tylko 2 pokoje. Oto mapa gry:
    
    ![zrzut ekranu](images/rpg-map1.png)
    
    Możesz wpisać `i udać się na południe` , aby przejść z hali do kuchni, a następnie `na północ` , aby wrócić do hali!
    
    ![zrzut ekranu](images/rpg-controls.png)

+ Co się stanie, gdy wpiszesz kierunek, w którym nie możesz iść? Wpisz `przejdź na zachód` w hali, a otrzymasz przyjazny komunikat o błędzie.
    
    ![zrzut ekranu](images/rpg-error.png)

+ Jeśli znajdziesz zmienną `pokoje` , możesz zobaczyć, że mapa jest zakodowana jako słownik pokoi:
    
    ![screenshot](images/rpg-rooms.png)
    
    Każdy pokój jest słownikiem, a pokoje są ze sobą połączone za pomocą wskazówek.

+ Dodajmy jadalnię do mapy, na wschód od hali.
    
    ![screenshot](images/rpg-dining.png)
    
    Musisz dodać trzeci pokój o nazwie `jadalnia`. Musisz również połączyć go z halą na zachodzie. Musisz również dodać dane do hali, abyś mógł przenieść się do jadalni na wschód.
    
    ![zrzut ekranu](images/rpg-dining-code.png)

+ Wypróbuj grę z nową jadalnią:
    
    ![zrzut ekranu](images/rpg-dining-test.png)
    
    Jeśli nie możesz wejść i wyjść z jadalni, po prostu sprawdź, czy dodano cały powyższy kod (w tym dodatkowe przecinki do powyższych linii).