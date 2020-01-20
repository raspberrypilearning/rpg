## Ajoute des objets à collecter

Laissons les objets dans les pièces pour que le joueur les collecte au fur et à mesure qu'il avance dans le labyrinthe.

\--- task \---

Adding an item into a room is easy, you can just add it to a room's dictionary. Let’s put a key in the hall.

Remember to put a comma after the line above the new item, or your program won’t run!

## \--- code \---

language: python

## line_highlights: 6-7

# un dictionnaire liant une pièce à d'autres pièces

rooms = {

            'Hall' : {
                'sud' : 'Cuisine',
                'est' : 'Salle a manger',
                'objet' : 'clé'
            },
    
            'Cuisine' : {
                'nord' : 'Hall'
            },
    
            'Salle a manger' : {
                'ouest' : 'Hall'
            }
    
        }
    

\--- /code \---

\--- /task \---

\--- task \---

If you run your game after adding the code above, you can now see a key in the hall, and you can even pick it up (by typing `get key`) which adds it to your inventory!

![screenshot](images/rpg-key-test.png)

\--- /task \---