## Dodavanje neprijatelja

Ova igra je prejednostavna! Dodajmo u neke od prostorija neprijatelje koje će igrač izbjegavati.

\--- task \--- Dodavanje neprijatelja u prostoriju je jednostavno kao i dodavanje bilo kojeg drugog predmeta. Dodajmo gladno čudovište u kuhinju:

## \--- code \---

jezik: python

## line_highlights: 11-12

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
                'west' : 'Hall'
            }
    
        }
    

\--- /code \--- \--- /task \---

\--- task \--- Također se želiš pobrinuti da se igra završi ako igrač uđe u prostoriju u kojoj se nalazi čudovište. To možeš napraviti dodavanjem sljedećeg kôda na kraju igre:

## \--- code \---

jezik: python

## line_highlights: 6-9

        #u suprotnom, ako predmet nije tu za nabaviti
        else:
            #tell them they can't get it
            print('Can\'t get' + move[1] + '!')
    
    #igrač gubi ako uđe u sobu s čudovištem
    if 'item' in rooms[currentRoom] and 'monster' in rooms[currentRoom]['item']:
        print('Čudovište te uhvatilo... IGRA JE GOTOVA!')
        break
    

\--- /code \---

Ovaj kôd provjerava postoji li neki predmet u prostoirji i ako postoji je li taj predmet čudovište. Primijeti da je kôd uvučen pa je na istoj razini kao i kôd iznad njega. To znači da će igra provjeravati postoji li čudovište u prostoriji svaki put kada igrač uđe u novu prostoriju. \--- /task \---

\--- task \--- Testiraj svoj kôd tako da uđeš u kuhinju u kojoj se sada nalazi čudovište.

![screenshot](images/rpg-monster-test.png) \--- /task \---