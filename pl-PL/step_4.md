## Dodawanie przedmiotów do zebrania

Zostawmy przedmioty w pokojach, aby gracz mógł je zbierać, gdy przechodzi przez labirynt.

\--- task \---

Dodanie przedmiotu do pokoju jest łatwe, wystarczy dodać go do słownika pokoju. Pozostawmy klucz w korytarzu.

Pamiętaj, aby dodać przecinek za linią ponad nowym przedmiotem, bo inaczej Twój program się nie uruchomi!

## \--- code \---

language: python

## line_highlights: 6-7

# słownik łączący pokój z innymi pokojami

pokoje = {

            'Korytarz' : {
                'południe' : 'Kuchnia',
                'wschód' : 'Jadalnia',
                'przedmiot' : 'klucz'
            },
    
            'Kuchnia' : {
                'północ' : 'Korytarz'
            },
    
            'Jadalnia' : {
                'zachód' : 'Korytarz'
            }
    
        }
    

\--- /code \---

\--- /task \---

\--- task \---

Jeśli uruchomisz grę po dodaniu powyższego kodu, zobaczysz klucz w korytarzu, a nawet możesz go wziąć (wpisując `bierz klucz`), który dodaje go do Twojego ekwipunku!

![zrzut ekranu](images/rpg-key-test.png)

\--- /task \---