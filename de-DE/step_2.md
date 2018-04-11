## Neue Zimmer hinzufügen

+ Ein Teil des Codes für dieses Spiel wurde dir hier schon bereit gestellt. Schreibe dieses Trinket: <a href="http://jumpto.cc/rpg-go" target="_blank">jumpto.cc/rpg-go</a>. 

+ Dies ist ein sehr vereinfachtes Rollenspiel-Spiel, das nur 2 Zimmer hat. Hier ist eine Übersichtskarte des Spiels:

  ![screenshot](images/rpg-map1.png)

  Du kannst `go south` (nach Süden gehen) tippen, um von der Eingangshalle zur Küche zu gehen und dann `go north` (nach Norden gehen) tippen, um wieder zurück zur Eingangshalle zu gelangen!

  ![screenshot](images/rpg-controls.png)

+ Was passiert, wenn du eine Richtung eingibst, in die du gar nicht gehen kannst? Tippe `go west` (nach Westen gehen) in die Eingangshalle, du wirst dann eine freundliche Fehlermeldung erhalten.

  ![screenshot](images/rpg-error.png)

 + Wenn du die `rooms` (Zimmer) Variable findest, kannst du sehen, dass die Karte als ein Wörterbuch der Zimmer kodiert worden ist:

  ![screenshot](images/rpg-rooms.png)

  Jedes Zimmer ist ein Wörterbuch und die Zimmer sind mit Hilfe der Richtungsanweisungen miteinander verknüpft.  
  

+ Lass uns deiner Karte ein Eßzimmer hinzufügen, das östlich von der Eingangshalle liegt.

  ![screenshot](images/rpg-dining.png)

  Du musst ein 3. Zimmer mit dem Namen `dining room` (Eßzimmer) hinzufügen. Du musst es auch mit der Eingangshalle, westlich gelegen, verknüpfen. Du musst der Eingangshalle auch Daten hinzufügen, damit du dich zum Eßzimmer im Osten bewegen kannst.
  
  ![screenshot](images/rpg-dining-code.png)

+ Probiere das Spiel mit deinem neuen Eßzimmer aus:

  ![screenshot](images/rpg-dining-test.png)

  Wenn du nicht in das Eßzimmer ein- und ausgehen kannst, prüfe bitte, dass du den kompletten o.g. Code eingefügt hast (inklusive der zusätzlichen Kommata in den o.g. Zeilen).
