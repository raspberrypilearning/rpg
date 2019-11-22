## Dodavanje predmeta za sakupljanje

U prostorije ćemo postaviti predmete koje će igrač sakupljati dok se bude kretao labirintom.

--- task --- Dodavanje predmeta u prostoriju je lako - jednostavno ga dodaj u rječnik prostorije u kojoj želiš da se pojavi. Pokušajmo staviti ključ u hodnik.

Ne zaboravi staviti zarez nakon linije iznad novogpredmeta, ili program neće raditi!

--- code ---
---
language: python
---
## line_highlights: 6-7

# rječnik koji povezuje prostorije jednu s drugom

prostorije = {

            'Hall' : {
                'south' : 'Kitchen',
                'east' : 'Dining Room',
                'item' : 'key'
            },
    
            'Kitchen' : {
                'north' : 'Hall'
            },
    
            'Dining Room' : {
                'west' : 'Hall'
            }
    
        }
    

--- /code ---

--- /task ---

--- task --- Pokreneš li sada igru, vidjet ćeš ključ u hodniku kojeg možeš čak i pokupiti (upisivanjem `uzmi ključ`). Tako ćeš ga dodati u svoj inventar!

![screenshot](images/rpg-key-test.png) --- /task ---