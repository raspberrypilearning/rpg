## Adicionar novos cômodos

\--- task \---

Abre o projeto inicial em Python.

**Online**: Abra o projeto inicial em [rpf.io/rpgon](http://rpf.io/rpgon){:target="_blank"}.

**Off-line**: Abra o [projeto inicial](http://rpf.io/p/en/rpg-go){:target="_ blank"} no editor offline.

\--- /task \---

\--- task \---

Este é um jogo de RPG muito básico que só tem 2 cômodos. Aqui está o mapa do jogo:

![screenshot](images/rpg-map1.png)

You can type `go south` to move from the hall to the kitchen, and then `go north` to go back to the hall again!

![screenshot](images/rpg-controls.png)

\--- /task \---

\--- task \---

What happens when you type in a direction that you cannot go? Type `go west` in the hall and you’ll get a friendly error message.

![screenshot](images/rpg-error.png)

\--- /task \---

\--- task \---

If you find the `rooms` variable, you can see that the map is coded as a dictionary of rooms:

## \--- code \---

## language: python

# um dicionário ligando um cômodo aos outros cômodos

rooms = {

            'Saguão' : {
                'sul' : 'Cozinha'
            },
    
            'Cozinha' : {
                'norte' : 'Saguão'
            }
    
        }
    

\--- /code \---

Each room is a dictionary, and rooms are linked together using directions.

\--- /task \---

\--- task \---

Let’s add a dining room to your map, to the east of the hall.

![screenshot](images/rpg-dining.png)

You need to add a 3rd room, called the `dining room`, and link it to the hall (to the west). You also need to add data to the hall, so that you can move to the dining room to the east.

**Don't forget that you'll also need to add commas to lines before your new code.**

## \--- code \---

language: python

## line_highlights: 5-6,11-15

# um dicionário ligando um cômodo aos demais cômodos

rooms = {

            'Saguão' : {
                'sul' : 'Cozinha',
                'leste' : 'Sala de Jantar'
            },
    
            'Cozinha' : {
                'norte' : 'Saguão'
            },
    
            'Sala de Jantar' : {
                'oeste' : 'Saguão'
            }
    
        }
    

\--- /code \---

\--- /task \---

\--- task \---

Try out the game with your new dining room:

![screenshot](images/rpg-dining-test.png)

If you can’t move in and out of the dining room, just check that you added all of the code above (including the extra commas to the lines above).

\--- /task \---