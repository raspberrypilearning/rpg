## Vijanden toevoegen

Dit spel is te makkelijk! We gaan vijanden in een paar kamers toevoegen die de speler moet zien te vermijden.

\--- task \--- Het toevoegen van een vijand in een kamer is net zo makkelijk als het toevoegen van een voorwerp. We voegen een hongerig monster toe aan de keuken:

## \--- code \---

language: python

## line_highlights: 11-12

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
                'west' : 'Hal'
            }
    
        }
    

\--- /code \--- \--- /task \---

\--- task \--- Je wilt ook zeker weten dat het spel eindigt als de speler een kamer met een monster binnenkomt. Dit kun je doen door de volgende code aan het einde van je spel te zetten:

## \--- code \---

language: python

## line_highlights: 6-9

        #anders, als het voorwerp er niet is om te pakken
        else:
            #vertel ze dat ze het niet kunnen pakken
            print('Kan ' + move[1] + ' niet pakken!')
    
    #speler verliest als ze een kamer met een monster ingaan
    if 'voorwerp' in kamers[dezeKamer] and 'monster' in kamers[dezeKamer]['voorwerp']:
        print('Een monster heeft je te pakken... GAME OVER!')
        break
    

\--- /code \---

Deze code bekijkt of er een voorwerp in de kamer is en zo ja, of het een monster is. Let er op dat de code inspringt zodat het gelijk staat met de code erboven. Elke keer dat de speler naar een andere kamer gaat, controleert het spel of er een monster is. \--- /task \---

\--- task \--- Probeer het uit door naar de keuken te gaan, waar nu een monster zit.

![screenshot](images/rpg-monster-test.png) \--- /task \---