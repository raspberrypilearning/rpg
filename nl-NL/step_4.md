## Voorwerpen toevoegen om te verzamelen

We gaan voorwerpen in de kamers achterlaten die de speler kan verzamelen terwijl die door het doolhof zwerft.

\--- task \--- Het is makkelijk om een voorwerp in een kamer toe te voegen, je kunt het in het woordenboek van de kamer zetten. Laten we een sleutel in de hal leggen.

Vergeet niet om een komma achter de regel erboven te zetten, anders werkt je programma niet!

## \--- code \---

language: python

## line_highlights: 6-7

# een woordenboek die een kamer verbindt met andere kamers

kamers = {

            'Hal' : {
                'zuid' : 'Keuken',
                'oost' : 'Eetkamer',
                'voorwerp' : 'sleutel'
            },
    
            'Keuken' : {
                'noord' : 'Hal'
            },
    
            'Eetkamer' : {
                'west' : 'Hal'
            }
    
        }
    

\--- /code \---

\--- /task \---

\--- task \--- Als je het spel uitvoert na het toevoegen van bovenstaande code zie je een sleutel in de hal die je kunt oppakken (met `pak sleutel`) en aan de inventaris laten toevoegen!

![screenshot](images/rpg-key-test.png) \--- /task \---