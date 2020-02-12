## Ganar el juego

Demos a tu jugador una misión que necesita completar para ganar el juego.

--- task ---

En este juego, el jugador gana al llegar al jardín y escapar de la casa. También van a necesitar tener una llave y una poción mágica con ellos. Aquí hay un mapa del juego.

![captura de pantalla](images/rpg-final-map.png)

--- /task ---

--- task ---

Primero, necesitas agregar un jardín al sur del comedor. Recuerda añadir puertas, para unirlo a otras habitaciones de la casa.

--- code ---

language: python

## line_highlights: 16-17,18-22

# un diccionario que une una habitacion a las posiciones de las otras habitaciones

habitaciones = {

            'Sala': {
            'sur': 'Cocina',
            'este': 'Comedor',
            'objeto': 'llave'
        },
    
        'Cocina': {
            'norte': 'Sala',
            'objeto': 'monstruo'
        },
    
        'Comedor': {
            'oeste': 'Sala',
            'sur': 'Jardin'
        },
    
        'Jardin':{
            'norte': 'Comedor'
        }
    
    }
    

--- /code ---

--- /task ---

--- task ---

Agrega una poción al comedor (u otra habitación de tu casa).

--- code ---

language: python

## line_highlights: 3-4

            'Comedor' : {
                'oeste' : 'Sala',
                'sur' : 'Jardin',
                'objeto' : 'pocion'
            },
    

--- /code ---

--- /task ---

--- task ---

Agrega este código para permitir que el jugador gane cuando llegue al jardín con la llave y la poción:

--- code ---

language: python

## line_highlights: 6-9

# el jugador pierde si entra a una habitación con un monstruo

if 'objeto' in habitaciones\[habitacionActual] and 'monstruo' in habitaciones[habitacionActual\]\['objeto'\]: print('Te ha pillado el monstruo... JUEGO TERMINADO!') break

# el jugador gana si llega al jardín con una llave y una poción

if habitacionActual == 'Jardin' and 'llave' in inventario and 'pocion' in inventario: print('Has escapado de la casa... HAS GANADO!') break

--- /code ---

Asegúrate de que el código tiene sangría, estando en línea con el código de arriba. Este código quiere decir que el mensaje `Has escapado de la casa... HAS GANADO!` si el jugador está en la habitación 4 (el jardín) y si la llave y la poción están en su inventario.

Si tienes más de 4 habitaciones, puedes utilizar un número diferente para tu jardín en el código de arriba.

--- /task ---

--- task ---

¡Prueba tu juego para asegurarte de que el jugador puede ganar!

![captura de pantalla](images/rpg-win-test.png)

--- /task ---

--- task ---

Finalmente, agreguemos instrucciones al juego, así el jugador sabe qué tiene que hacer. Edita la función `mostrarInstrucciones()` para incluir más información.

--- code ---

language: python

## line_highlights: 7-8

def mostrarInstrucciones(): #imprime un menu principal y los comandos print('''

# Juego RPG

Llega la jardín con una llave y una poción. ¡Evita a los monstruos!

Comandos: ir [direccion] coger [objeto] ''')

--- /code ---

¡Vas a necesitar añadir instrucciones para decirle al usuario qué objetos necesitan recoger y qué necesitan evitar!

--- /task ---

--- task ---

Prueba tu juego y vas a ver tus nuevas instrucciones.

![captura de pantalla](images/rpg-instructions-test.png)

--- /task ---