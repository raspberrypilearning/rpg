## Wygranie gry

Dajmy graczowi misję, która musi zostać ukończona, aby wygrać grę.

--- task ---

W tej grze gracz wygrywa, wchodząc do ogrodu i uciekając z domu. Musi też mieć ze sobą klucz i magiczną miksturę. Oto mapa gry.

![zrzut ekranu](images/rpg-final-map.png)

--- /task ---

--- task ---

Najpierw musisz dodać ogród na południe od jadalni. Pamiętaj, aby dodać drzwi, żeby połączyć go z innymi pokojami w domu.

--- code ---
---
language: python
line_highlights: 16-17,18-22
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
                'przedmiot' : 'potwór'
            },
    
            'Jadalnia' : {
                'zachód' : 'Korytarz',
                'południe' : 'Ogród'
            },
    
            'Ogród' : {
                'północ' : 'Jadalnia'
            }
    
        }
    

--- /code ---

--- /task ---

--- task ---

Dodaj miksturę do jadalni (lub innego pokoju w domu).

--- code ---
---
language: python
line_highlights: 3-4
---
            'Jadalnia' : {
                'zachód' : 'Korytarz',
                'południe' : 'Ogród',
                'przedmiot' : 'mikstura'
            },
    

--- /code ---

--- /task ---

--- task ---

Dodaj ten kod, aby gracz mógł wygrać grę, gdy dotrze do ogrodu z kluczem i miksturą:

--- code ---
---
language: python
line_highlights: 6-9
---
# gracz przegrywa jeśli wejdzie do pokoju z potworem

if 'przedmiot' in pokoje\[aktualnyPokoj] and 'potwór' in pokoje[aktualnyPokoj\]\['przedmiot'\]: print('Dorwał cię potwór... PRZEGRYWASZ!') break

# gracz wygrywa jeśli dostanie się do ogrodu z kluczem i miksturą

if aktualnyPokoj == 'Ogród' and 'klucz' in ekwipunek and 'mikstura' in ekwipunek: print('Wydostałeś się z domu... WYGRYWASZ!') break

--- /code ---

Upewnij się, że ten kod został poprzedzony wcięciem. Ten kod oznacza, że wiadomość `Wydostałeś się z domu... WYGRYWASZ!` jest wyświetlana, jeśli gracz jest pokoju nr 4 (ogród) i jeśli klucz i mikstura są w ekwipunku.

Jeśli masz więcej niż 4 pomieszczenia, konieczne będzie użycie innego numeru pomieszczenia dla ogrodu w powyższym kodzie.

--- /task ---

--- task ---

Sprawdź swoją grę, aby upewnić się, że gracz może wygrać!

![zrzut ekranu](images/rpg-win-test.png)

--- /task ---

--- task ---

Na koniec dodajmy kilka instrukcji do gry, aby gracz wiedział, co musi zrobić. Uzupełnij funkcję `pokazInstrukcje()` o dodatkowe informacje.

--- code ---
---
language: python
line_highlights: 7-8
---

def pokazInstrukcje(): #wyświetl menu główne i komendy print('''

# Gra przygodowa (RPG)

Dostań się do ogrodu z kluczem i miksturą Unikaj potworów!

Polecenia: rusz-na [kierunek] bierz [przedmiot] ''')

--- /code ---

Musisz też dodać instrukcje aby powiedzieć graczowi jakie przedmioty musi zebrać i czego ma unikać!

--- /task ---

--- task ---

Przetestuj swoją grę, a powinieneś zobaczyć nowe instrukcje.

![zrzut ekranu](images/rpg-instructions-test.png)

--- /task ---