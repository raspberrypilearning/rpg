## Neue Zimmer hinzufügen

\--- task \--- Öffne das Python Start-Projekt.

**Online**: Öffne das Basisprojekt: [rpf.io/rpgon](http://rpf.io/rpgon){:target="_blank"}.

**Offline**: Öffne das [Basisprojekt](http://rpf.io/p/en/rpg-go){:target="_blank"} im Offline-Editor. \--- /task \---

\--- task \--- Dies ist ein sehr einfaches RPG-Spiel mit nur zwei Zimmern. Hier ist eine Karte des Spiels:

![Bildschirmfoto](images/rpg-map1.png)

Du kannst `gehenach süden` eintippen, um von der Diele in die Küche zu gehen, und dann mit `gehenach norden` wieder zurück in die Diele gehen!

![Bildschirmfoto](images/rpg-controls.png) \--- /task \---

\--- task \--- Was passiert, wenn du eine Richtung eintippst, in die du nicht gehen kannst? Tippe `gehenach westen` wenn du in der Diele bist, und du erhältst eine freundliche Fehlermeldung.

![Bildschirmfoto](images/rpg-error.png) \--- /task \---

\--- task \--- Wenn du die Variable `zimmer` findest, kannst du sehen, dass die Karte als ein Wörterbuch (dictionary) von Zimmern programmiert ist:

## \--- code \---

## language: python

# Ein Dictionary (Wörterbuch) verbindet ein Zimmer mit anderen Zimmern

zimmer = {

            'Diele' : {
                'süden' : 'Küche'
            },
    
            'Küche' : {
                'norden' : 'Diele'
            }
    
        }
    

\--- /code \---

Jedes Zimmer ist ein Wörterbuch und die Zimmer sind über Richtungen miteinander verbunden  
\--- task \---

\--- task \--- Fügen wir ein Esszimmer zu deiner Karte hinzu, das sich östlich von der Diele befindet.

![Bildschirmfoto](images/rpg-dining.png)

Du musst einen dritten Raum hinzufügen, der `Esszimmer` heißt, und ihn mit der Diele (nach westen) verbinden. Du musst auch Daten zur Diele hinzufügen, damit du in das Esszimmer im Osten gehen kannst.

**Vergiss nicht, dass du auch Kommas in den Zeilen vor deinem neuen Code hinzufügen musst.**

## \--- code \---

language: python

## line_highlights: 5-6,11-15

# Ein Dictionary (Wörterbuch) verbindet ein Zimmer mit anderen Zimmern

zimmer = {

            'Diele' : {
                'süden' : 'Küche',
                'osten' : 'Esszimmer'
            },
    
            'Küche' : {
                'norden' : 'Diele'
            },
    
            'Esszimmer' : {
                'westen' : 'Diele'
            }
    
        }
    

\--- /code \--- \--- /task \---

\--- task \--- Probiere das Spiel mit deinem neuen Esszimmer aus:

![Bildschirmfoto](images/rpg-dining-test.png)

Wenn du nicht in das Esszimmer hinein- oder herausgehen kannst, dann prüfe, ob du den ganzen oben aufgeführten Code eingegeben hast (inklusive der zusätzlichen Kommas im Programm). \--- /task \---