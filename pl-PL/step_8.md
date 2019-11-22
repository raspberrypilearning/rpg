## Wygranie gry

Dajmy graczowi misję, która musi zostać ukończona, aby wygrać grę.

\--- task \--- W tej grze gracz wygrywa, wchodząc do ogrodu i wydostając się z domu. Musi też mieć ze sobą klucz i magiczną miksturę. Oto mapa gry.

![zrzut ekranu](images/rpg-final-map.png) \--- /task \---

\--- task \--- Najpierw musisz dodać ogród na południe od jadalni. Pamiętaj, aby dodać drzwi, żeby połączyć go z innymi pokojami w domu.

## \--- code \---

language: python

## line_highlights: 16-17,18-22

# słownik łączący pokój z innymi pokojami

rooms = {

            'Korytarz' : {
                'południe' : 'Kuchnia',
                'wschód' : 'Jadalnia',
                'item' : 'klucz'
            },
    
            'Kuchnia' : {
                'północ' : 'Korytarz',
                'item' : 'potwór'        },
    
            'Jadalnia' : {
                'zachód' : 'Korytarz',
                'południe' : 'Ogród'
            },
    
            'Ogród' : {
                'północ' : 'Jadalnia'
            }
    
        }
    

\--- /code \--- \--- /task \---

\--- task \--- Dodaj miksturę do jadalni (lub innego pokoju w Twoim domu).

## \--- code \---

language: python

## line_highlights: 3-4

            'Jadalnia' : {
                'zachód' : 'Korytarz',
                'południe' : 'Ogród',
                'item' : 'mikstura'
            },
    

\--- /code \--- \--- /task \---

\--- task \--- Dodaj ten kod aby gracz mógł wygrać jeśli dojdzie do ogrodu z kluczem i miksturą:

## \--- code \---

language: python

## line_highlights: 6-9

# gracz przegrywa jeśli wejdzie do pokoju z potworem

if 'item' in rooms\[currentRoom] and 'potwór' in rooms[currentRoom\]\['item'\]: print('Dorwał cię potwór... PRZEGRYWASZ!') break

# gracz wygrywa jeśli dostanie się do ogrodu z kluczem i miksturą

if currentRoom == 'Ogród' and 'klucz' in inventory and 'mikstura' in inventory: print('Wydostałeś się z domu... WYGRYWASZ!') break \--- /code \---

Upewnij się, że ten kod ma wcięcie takie samo jak kod nad nim. Ten kod oznacza, że wiadomość `Wydostałeś się z domu... WYGRYWASZ!` jest wyświetlana, jeśli gracz jest pokoju nr 4 (ogród) i jeśli klucz i mikstura są w ekwipunku.

Jeśli masz więcej niż 4 pomieszczenia, możesz potrzebować użyć innego numeru pomieszczenia dla ogrodu w powyższym kodzie. \--- /task \---

\--- task \--- Przetestuj swoja grę aby się upewnić, że gracz jest w stanie wygrać!

![zrzut ekranu](images/rpg-win-test.png) \--- /task \---

\--- task \--- Na koniec dodajmy instrukcję do gry, tak aby gracz wiedział co ma zrobić. Uzupełnij funkcję `showInstructions()` o dodatkowe informacje.

## \--- code \---

language: python

## line_highlights: 7-8

def showInstructions(): #drukuj manu główne i komendy print('''

# Gra RPG

Dostań się do ogrodu z kluczem i miksturą Unikaj potworów!

Polecenia: rusz.na [kierunek] bierz [przedmiot] ''') \--- /code \---

Musisz też dodać instrukcje aby powiedzieć graczowi jakie przedmioty musi zebrać i czego ma unikać! \--- /task \---

\--- task \--- Przetestuj grę, powinieneś widzieć swoje nowe instrukcje.

![zrzut ekranu](images/rpg-instructions-test.png) \--- /task \---