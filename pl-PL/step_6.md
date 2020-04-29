## Dodawanie wrogów

Ta gra jest zbyt łatwa! Dodajmy wrogów do niektórych pomieszczeń, których gracz musi unikać.

--- task ---

Dodanie wroga do pokoju jest tak proste, jak dodanie dowolnego innego przedmiotu. Dodajmy głodnego potwora do kuchni:

--- code ---
---
language: python
line_highlights: 11-12
---

# słownik łączący pokój z innymi pokojami

pokoje = {

            'Korytarz' : {
                'południe' : 'Kuchnia',
                'wschód' : 'Jadalnia',
                'przedmiot' : 'klucz'
            },
    
            'Kuchnia' : {
                'północ' : 'Korytarz',
                'przedmiot' : 'potwór'        },
    
            'Jadalnia' : {
                'zachód' : 'Korytarz'
            }
    
        }
    

--- /code ---

--- /task ---

--- task ---

Powinieneś również upewnić się, że gra zakończy się gdy gracz wejdzie do pokoju z potworem. Aby to osiągnąć, dodaj taki kod na końcu swojej gry:

--- code ---
---
language: python
line_highlights: 6-9
---
        #w przeciwnym wypadku, jeśli przedmiotu nie można wziąć bo go nie ma
        else:
            #powiedz, że nie da się tego wziąć
            print('Tego nie możesz wziąć: ' + ruch[1] + '!')
    
    #gracz przegrywa jeśli wejdzie do pokoju z potworem
    if 'przedmiot' in pokoje[aktualnyPokoj] and 'potwór' in pokoje[aktualnyPokoj]['przedmiot']:
        print('Dorwał cię potwór... PRZEGRYWASZ!')
        break
    

--- /code ---

Ten kod sprawdza, czy w pokoju jest jakaś rzecz, a jeśli tak, to czy jest to potwór. Upewnij się, że kod ten został poprzedzony wcięciem. Oznacza to, że gra będzie sprawdzać obecność potwora za każdym razem, gdy gracz przejdzie do nowego pokoju.

--- /task ---

--- task ---

Przetestuj swój kod, wchodząc do kuchni, która zawiera teraz potwora.

![zrzut ekranu](images/rpg-monster-test.png)

--- /task ---