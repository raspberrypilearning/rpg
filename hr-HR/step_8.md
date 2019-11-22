## Pobjeda u igri

Dajmo tvom igraču nekakvu misiju koju mora izvršiti kako bi pobijedio u igri.

--- task --- U ovoj će igri igrač pobijediti ako dođe do vrta i pobjegne iz kuće. Također sa sobom mora imati ključ, i čarobni napitak. Ispod se nalazi nacrt igre.

![screenshot](images/rpg-final-map.png) --- /task ---

--- task --- Prvo moraš dodati vrt južno od blagovaonice. Ne zaboravi dodati i vrata kako bi vrt bio povezan s drugim prostorijama u kući.

--- code ---
---
language: python
line_highlights: 16-17,18-22
---

# rječnik koji povezuje prostorije jednu s drugom

prostorije = {

            'Hall' : {
                'south' : 'Kitchen',
                'east' : 'Dining Room',
                'item' : 'key'
            },
    
            'Kitchen' : {
                'north' : 'Hall',
                'item' : 'monster'
            },
    
            'Dining Room' : {
                'west' : 'Hall',
                'south' : 'Garden'
            },
    
            'Garden' : {
                'north' : 'Dining Room'
            }
    
        }
    

--- /code --- --- /task ---

--- task --- Dodaj čarobni napitak u blagovaonicu (ili bilo koju drugu prostoriju u kući).

--- code ---
---
language: python
line_highlights: 3-4
---

            'Dining Room' : {
                'west' : 'Hall',
                'south' : 'Garden',
                'item' : 'potion'
            },
    

--- /code --- --- /task ---

--- task --- Dodaj sljedeći kôd kojim ćeš omogućiti igraču da bude pobjednik ako dođe do vrta sa ključem i čarobnim napitkom:

--- code ---
---
language: python
line_highlights: 6-9
---

# igrač gubi igru ako uđe u prostoriju sa čudovištem

if 'predmet' in rooms\[currentRoom] and 'čudovište' in rooms[currentRoom\]\['predmet'\]: print('Čudovište te uhvatilo... IGRA JE GOTOVA!') break

# igrač pobjeđuje ako dođe do vrta s ključem i čarobnim napitkom

if currentRoom == 'Vrt' i 'ključ' u inventaru i 'napitak' u inventaru: print('Pobjegao si iz kuće... POBJEDIO/LA SI!') break --- /code ---

Pobrini se da je kôd uvučen, odnosno u razini sa kôdom iznad njega. Ovaj kôd ispisat će poruku `Pobjegao/la si iz kuće...POBIJEDIO/LA SI!` ako se igrač nalazi prostoriji 4 (vrt) i u svom inventaru ima ključ i čarobni napitak.

Ako tvoja kuća ima više od četiri prostorije, možda ćeš, u kôdu iznad, morati upisati drugi naziv prostorije. --- /task ---

--- task --- Testiraj igru i provjeri može li tvoj igrač pobijediti!

![screenshot](images/rpg-win-test.png) --- /task ---

--- task --- Konačno, dodajmo upute za igru kako bi igrač znao što treba raditi. Izmijeni funkciju `prikaziUpute()` tako da sadrži više informacija.

--- code ---
---
language: python
line_highlights: 7-8
---

def prikaziUpute(): #ispiši glavni izbornik i naredbe print('''

# RPG Igra

Doši do Vrta sa ključem i čudotvornim napitkom Izbjegavajte čudovišta!

Commands: go [direction] get [item] ''') --- /code ---

Dodaj upute koje govore igraču koje predmete treba sakupiti i što treba izbjegavati! --- /task ---

--- task --- Testiraj igru i tvoje nove upute bi se trebale prikazati.

![screenshot](images/rpg-instructions-test.png) --- /task ---