## Adăugarea de obiecte de colectat

Hai să lăsăm în camere obiecte de colectat pentru jucător pe măsură ce se mișcă prin labirint.

\--- task \--- Adăugarea unui obiect într-o cameră este simplă, trebuie doar adăugat în dicționarul unei camere. Hai să lăsăm o cheie în hol.

Amintește-ți să pui o virgulă după linia de deasupra noului obiect, altfel programul tău nu va merge!

## \--- code \---

language: python

## line_highlights: 6-7

# un dicționar asociind o cameră cu alte camere

camere = {

            'Hol' : {
                'sud' : 'Bucatarie',
                'est' : 'Sufragerie',
                'item' : 'cheie'
            },
    
            'Bucatarie' : {
                'nord' : 'Hol'
            },
    
            'Sufragerie' : {
                'vest' : 'Hol'
            }
    
        }
    

\--- /code \---

\--- /task \---

\--- task \--- Dacă pornești jocul după ce ai adăugat codul de mai sus, poți vedea acuma o cheie în hol si o poți chiar lua (tastând `ia cheie`), ceea ce o va adăuga în inventarul tău!

![captură de ecran](images/rpg-key-test.png) \--- /task \---