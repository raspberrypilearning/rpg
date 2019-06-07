## Añadir nuevas habitaciones

\--- task \--- Open the Python starter project.

**Online**: open the starter project at [rpf.io/rpgon](http://rpf.io/rpgon){:target="_blank"}.

**Offline**: abre el [proyecto de inicio](http://rpf.io/p/en/rpg-go){:target=_blank"} en el editor offline. \--- /task \---

\--- task \--- This is a very basic RPG game that only has 2 rooms. Aquí hay un mapa del juego:

![screenshot](images/rpg-map1.png)

¡Puedes escribir `ir sur` para moverte de la sala a la cocina, y luego `ir norte` para regresar a la sala!

![captura de pantalla](images/rpg-controls.png) \--- /task \---

\--- task \--- What happens when you type in a direction that you cannot go? Escribe `ir oeste` en la sala y obtendrás un mensaje de error.

![captura de pantalla](images/rpg-error.png) \--- /task \---

\--- task \--- If you find the `rooms` variable, you can see that the map is coded as a dictionary of rooms:

## \--- code \---

## language: python

# un diccionario que une una habitacion a las posiciones de las otras habitaciones

rooms = {

            'Hall' : {
                'south' : 'Kitchen'
            },
    
            'Kitchen' : {
                'north' : 'Hall'
            }
    
        }
    

\--- /code \---

Each room is a dictionary, and rooms are linked together using directions.  
\--- /task \---

\--- task \--- Let’s add a dining room to your map, to the east of the hall.

![captura de pantalla](images/rpg-dining.png)

You need to add a 3rd room, called the `dining room`, and link it to the hall (to the west). También necesitas agregar datos a la sala, así puedes moverte hacia el comedor al este.

**Don't forget that you'll also need to add commas to lines before your new code.**

## \--- code \---

language: python

## line_highlights: 5-6,11-15

# un diccionario que une una habitacion a las posiciones de las otras habitaciones

rooms = {

            'Hall' : {
                'south' : 'Kitchen',
                'east' : 'Dining Room'
            },
    
            'Kitchen' : {
                'north' : 'Hall'
            },
    
            'Dining Room' : {
                'west' : 'Hall'
            }
    
        }
    

\--- /code \--- \--- /task \---

\--- task \--- Try out the game with your new dining room:

![captura de pantalla](images/rpg-dining-test.png)

Si no puedes entrar y salir del comedor, verifica que agregaste todo el código de arriba (incluyendo las comas extra). \--- /task \---