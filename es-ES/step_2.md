## Añadir nuevas habitaciones

--- task ---

Abre el proyecto inicial de Python.

**En línea**: abre el proyecto de inicio en [trinket.io/python/e4186c55a3](https://trinket.io/python/e4186c55a3){:target="_blank"}.

**Offline**: abre el [proyecto de inicio](http://rpf.io/p/es-ES/rpg-go){:target=_blank"} en el editor offline.

--- /task ---

--- task ---

Este es un juego RPG muy básico que sólo tiene 2 habitaciones. Aquí hay un mapa del juego:

![captura de pantalla](images/rpg-map1.png)

¡Puedes escribir `ir sur` para moverte de la sala a la cocina, y luego `ir norte` para regresar a la sala!

![captura de pantalla](images/rpg-controls.png)

--- /task ---

--- task ---

¿Qué pasa cuando escribes una dirección en la cual no puedes ir? Escribe `ir oeste` en la sala y obtendrás un mensaje de error.

![captura de pantalla](images/rpg-error.png)

--- /task ---

--- task ---

Si te fijas en la variable `habitaciones`, verás que el mapa está codificado como un diccionario de habitaciones:

--- code ---

## language: python

# un diccionario que une una habitacion a las posiciones de las otras habitaciones

habitaciones = {

            'Sala' : {
                'sur' : 'Cocina'
            },
    
            'Cocina' : {
                'norte' : 'Sala'
            }
    
        }
    

--- /code ---

Cada habitación es un diccionario y las habitaciones están ligadas entre ellas usando direcciones.

--- /task ---

--- task ---

Agreguemos un comedor a tu mapa, al este de la sala.

![captura de pantalla](images/rpg-dining.png)

Necesitas añadir una 3ra habitación, llamada `Comedor` y vincularlo a la sala (al oeste). También necesitas agregar datos a la sala, así puedes moverte hacia el comedor al este.

**No olvides que también necesitas añadir comas a las líneas antes de tu nuevo código.**

--- code ---

language: python

## line_highlights: 5-6,11-15

# un diccionario que une una habitacion a las posiciones de las otras habitaciones

habitaciones = {

            'Sala' : {
                'sur' : 'Cocina',
                'este' : 'Comedor'
            },
    
            'Cocina' : {
                'norte' : 'Sala'
            },
    
            'Comedor' : {
                'oeste' : 'Sala'
            }
    
        }
    

--- /code ---

--- /task ---

--- task ---

Prueba el juego con tu nuevo comedor:

![captura de pantalla](images/rpg-dining-test.png)

Si no puedes entrar y salir del comedor, verifica que agregaste todo el código de arriba (incluyendo las comas extra).

--- /task ---