## Pour gagner le jeu

Donnons au joueur une mission, qu'il a besoin d'accomplir pour gagner le jeu.

\--- task \---

Dans ce jeu, le joueur gagne en atteignant le jardin et en s'échappant de la maison. Il a besoin également d'avoir une clé avec lui, et la potion magique. Voici un plan du jeu.

![capture d'écran](images/rpg-final-map.png)

\--- /task \---

\--- task \---

En premier, tu dois ajouter un jardin au sud de la salle à manger. N'oublie pas d'ajouter des portes, à lier aux autres pièces dans la maison.

## \--- code \---

language: python

## line_highlights: 16-17,18-22

# un dictionnaire liant une pièce à d'autres pièces

rooms = {

            'Hall' : {
                'sud' : 'Cuisine',
                'est' : 'Salle a manger',
                'objet' : 'clé'
            },
    
            'Cuisine' : {
                'nord' : 'Hall',
                'objet' : 'monstre'
            },
    
            'Salle a manger' : {
                'ouest' : 'Hall',
                'sud' : 'Jardin'
            },
    
            'Jardin' : {
                'nord' : 'Salle a manger'
            }
    
        }
    

\--- /code \---

\--- /task \---

\--- task \---

Ajoute une potion magique à la salle à manger (ou une autre pièce dans ta maison).

## \--- code \---

language: python

## line_highlights: 3-4

            'Salle a manger' : {
                'ouest' : 'Hall',
                'sud' : 'Jardin',
                'objet' : 'potion'
            },
    

\--- /code \---

\--- /task \---

\--- task \---

Ajoute ce code pour permettre au joueur de gagner le jeu lorsqu'il atteint le jardin avec la clé et la potion :

## \--- code \---

language: python

## line_highlights: 6-9

# le joueur perd s'il entre dans une pièce avec un monstre

if 'objet' in rooms\[currentRoom] and 'monstre' in rooms[currentRoom\]\['objet'\]: print('Un monstre t a attrapé... FIN DU JEU !') break

# le joueur gagne s'il atteint le jardin avec la clé et la potion

if currentRoom == 'Jardin' and 'clé' in inventaire and 'potion' in inventaire: print('Tu t es échappé de la maison... TU GAGNES !') break

\--- /code \---

Note que ce code est indenté, mets le dans une ligne avec le code ci-dessus. Ce code signifie que le message `Tu t es échappé de la maison...TU GAGNES!` est affiché si le joueur est dans la pièce 4 (le jardin) et si la clé et la potion sont dans l'inventaire.

Si tu as plus de 4 pièces, tu devras utiliser un numéro de pièce différent pour ton jardin dans le code ci-dessus.

\--- /task \---

\--- task \---

Teste ton jeu pour t'assurer que le joueur peut gagner !

![capture d'écran](images/rpg-win-test.png)

\--- /task \---

\--- task \---

Pour finir, ajoutons quelques consignes à ton jeu, de sorte que le joueur sache ce qu'il doit faire. Édite la fonction `showInstructions()` pour inclure plus d'information.

## \--- code \---

language: python

## line_highlights: 7-8

def showInstructions(): #affiche un menu principal et les commandes print('''

# Jeu RPG

Atteins le jardin avec une clé et une potion Évite les monstres !

Commands: Aller [direction] prendre [objet] ''')

\--- /code \---

Tu devras ajouter des consignes pour indiquer à l'utilisateur quels objets il a besoin de collecter, et ce qu'il doit éviter !

\--- /task \---

\--- task \---

Teste ton jeu et tu devrais voir tes nouvelles consignes.

![capture d'écran](images/rpg-instructions-test.png)

\--- /task \---