## Uvod:

U ovom projektu dizajnirat ćeš i napraviti vlastitu RPG igru labirinta. Cilj igre je skupiti sve objekte i pobjeći iz kuće, izbjegavajući pri tome sva čudovišta!

<div class="trinket">
  <iframe src="https://trinket.io/embed/python/d06adeb527?outputOnly=true&start=result" width="600" height="500" frameborder="0" marginwidth="0" marginheight="0" allowfullscreen>
  </iframe>
  <img src="images/rpg-finished.png">
</div>

### Dodatne informacije za voditelje kluba

Ako želite ispisati ovaj projekt, molimo Vas da koristite [verziju koja je prilagođena za ispis](https://projects.raspberrypi.org/en/projects/rpg/print).

## \--- collapse \---

## title: Bilješke za voditelja kluba

## Uvod:

U ovom projektu djeca uče o dizajnu igara kroz izradu RPG igre labirinta. U ovoj igri igrač mora sakupiti objekte unutar kuće i doći do određene prostorije, a pritom izbjegavati čudovišta koja vrebaju u nekim prostorijama. Igra će biti napravljena manipuliranjem rječnicima i listama.

## Online izvori

**U ovom projektu koristi se Python 3.** Predlažemo korištenje [trinketa](https://trinket.io/) za online pisanje u Pythonu. Ovaj projekt sadrži sljedeće Trinkete:

+ ['RPG' početni materijal -- jumpto.cc/rpg-go](http://jumpto.cc/rpg-go)

Također je uključen i trinket koji sadrži dovršeni projekt:

+ [‘RPG’ dovršeni projekt -- trinket.io/python/d06adeb527](https://trinket.io/python/d06adeb527)

## Offline izvori

Ako želite, ovaj projekt može bit [završen offline](https://www.codeclubprojects.org/en-GB/resources/python-working-offline/). Materijalima projekta možete pristupiti klikom na poveznicu 'Project Materials'. Poveznica sadrži odjeljak 'Project Resources' u kojem se nalaze materijali koji će djeci biti potrebni za izradu projekta offline. Pobrinite se da svako dijete ima pristup kopiji ovih materijala. U odjeljku se nalaze sljedeće datoteke:

+ rpg/rpg.py

Dovršenu verziju projekta možete pronaći i u odjeljku 'Resursi za volontere' koji sadrži:

+ rpg-finished/rpg.py

(Svi spomenuti materijali nalaze se u materijalima projekta i materijalima za volontere, moguće je preuzeti kao `.zip` datoteke.)

## Ishodi učenja

+ Dizajn igre;
+ Uređivanje: 
    + Liste;
    + Rječnika.
+ Booleovi izrazi.

Ovaj projekt pokriva elemente iz sljedećih dijelova plana i programa [Raspberry Pi Digital Making Curriculum](http://rpf.io/curriculum):

+ [Uporaba različitih programskih struktura za rješavanje problema.](https://www.raspberrypi.org/curriculum/programming/builder)

## Izazovi

+ Dodavanje novih prostorija;
+ Dodavanje predmeta za sakupljanje;
+ Dodavanje neprijatelja za izbjegavanje;
+ Osmisli vlastitu igru.

## Često postavljana pitanja

+ Djecu će možda biti potrebno podsjetiti da se elementi unutar rječnika/liste odvajaju zarezom. Primjerice, kada dodajemo novu prostoriju u rječnik 'prostorije', između nove prostorije i zadnje prostorije koja se nalazi u rječniku moramo dodati zarez.
+ Pri dodavanju nove prostorije, djeca će možda zaboraviti u novoj prostoriji dodati poveznicu na već postojeću prostoriju. Tada će moći izaći iz prostorije, ali ne i ući u nju!
+ Dio kôda koji provjerava je li igrač pobijedio ili izgubio u igri mora biti uvučen kako bi se osiguralo da se ta provjera obavlja prilikom svakog ulaska u novu prostoriju. Ukoliko kôd nije uvučen, onda će se nalaziti izvan glavne petlje igre i neće se nikada pokrenuti.

\--- /collapse \---

## \--- collapse \---

## title: Materijali projekta

## Resursi projekta

+ [.zip datoteka koja sadrži sve materijale projekta](resources/rpg-project-resources.zip)
+ [Online Trinket koji sadrži sve resurse projekta 'RPG'](http://jumpto.cc/rpg-go)
+ [rpg/rpg.py](resources/rpg-rpg.py)

## Materijali za voditelja Kluba

+ [.zip datoteka koja sadrži sve dovršene materijale projekta](resources/rpg-volunteer-resources.zip)
+ [Dovršeni Online Trinket projekt](https://trinket.io/python/d06adeb527)
+ [rpg-finished/rpg.py](resources/rpg-finished-rpg.py)

\--- /collapse \---