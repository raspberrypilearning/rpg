## Het spel winnen

We gaan de speler een doel geven wat gehaald moet worden om het spel te kunnen winnen.

\--- task \--- In dit spel wint de speler als die in de tuin komt en zo uit het huis ontsnapt. De sleutel en de toverdrank moet ook zijn gepakt. Hier is een kaart van het spel.

![screenshot](images/rpg-final-map.png) \--- /task \---

\--- task \--- Ten eerste moet er een tuin worden gemaakt, ten zuiden van de eetkamer. Vergeet niet om deuren toe te voegen voor de verbinding met andere kamers in het huis.

## \--- code \---

language: python

## line_highlights: 16-17,18-22

# een woordenboek die een kamer verbindt met andere kamers

kamers = {

            'Hal' : {
                'zuid' : 'Keuken',
                'oost' : 'Eetkamer',
                'voorwerp' : 'sleutel'
            },
    
            'Keuken' : {
                'noord' : 'Hal',
                'voorwerp' : 'monster'
            },
    
            'Eetkamer' : {
                'west' : 'Hal',
                'zuid' : 'Tuin'
            },
    
            'Tuin' : {
                'noord' : 'Eetkamer'
            }
    
        }
    

\--- /code \--- \--- /task \---

\--- task \--- Plaats een toverdrank in de eetkamer (of een andere kamer in je huis).

## \--- code \---

language: python

## line_highlights: 3-4

            'Eetkamer' : {
                'west' : 'Hal',
                'zuid' : 'Tuin',
                'voorwerp' : 'toverdrank'
            },
    

\--- /code \--- \--- /task \---

\--- task \--- Voeg deze code toe om ervoor te zorgen dat de speler wint als die in de tuin aankomt met sleutel en toverdrank:

## \--- code \---

language: python

## line_highlights: 6-9

# de speler verliest als er een monster in de kamer is

if 'voorwerp' in kamers\[dezeKamer] and 'monster' in kamers[dezeKamer\]\['voorwerp'\]: print('Een monster heeft je te pakken... GAME OVER!') break

# speler wint als ze in the tuin komen met de sleutel en de toverdrank

if currentRoom == 'Tuin' and 'sleutel' in inventaris and 'toverdrank' in inventaris: print('Je bent uit het huis ontsnapt... JE WINT!') break \--- /code \---

Zorg ervoor dat de code inspringt zodat het gelijk staat met de code erboven. Deze code zorgt ervoor dat het bericht `Je bent ontsnapt...JIJ WINT!` wordt getoond als de speler in kamer 4 is (de tuin) en de sleutel en de toverdrank in de inventaris zit.

Als je meer dan 4 kamers hebt kan het zijn dat je in de code hierboven een ander kamernummer moet gebruiken voor de tuin. \--- /task \---

\--- task \--- Test het spel en zorg ervoor dat de speler kan winnen!

![screenshot](images/rpg-win-test.png) \--- /task \---

\--- task \--- Tot slot voegen we wat instructies toe aan het spel zodat de speler weet wat die moet doen. Bewerk de functie `toonInstructies()` om meer informatie te geven.

## \--- code \---

language: python

## line_highlights: 7-8

def toonInstracties(): #print een hoofdmenu en de commando's print('''

# RPG Spel

Ga naar de Tuin met een speutel en een toverdrank Vermijd de monsters!

Commando's: ga [richting] pak [item] ''') \--- /code \---

Je moet instructies toevoegen om de speler te vertellen welke voorwerpen ze moeten verzamelen en wat ze moeten zien te vermijden! \--- /task \---

\--- task \--- Test het spel en kijk of de instructies zichtbaar zijn.

![screenshot](images/rpg-instructions-test.png) \--- /task \---