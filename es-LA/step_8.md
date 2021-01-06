## Ganar el juego

Demos a tu jugador una misión que necesite completar para ganar el juego.

--- task ---

En este juego, el jugador gana al llegar al jardín y escapar de la casa. También van a necesitar tener una llave y una poción mágica con ellos. Aquí hay un mapa del juego.

![captura de pantalla](images/rpg-final-map.png)

--- /task ---

--- task ---

Primero, necesitas agregar un jardín al sur del comedor. Recuerda añadir puertas, para conectarlo a otras habitaciones de la casa.

--- code ---
---
language: python
line_highlights: 16-17,18-22
---
# un diccionario que conecte una habitación con las otras habitaciones
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
            'sur': 'Jardín'
        },
    
        'Jardín':{
            'norte': 'Comedor'
        }
    
    }
    

--- /code ---

--- /task ---

--- task ---

Agrega una poción al comedor (u otra habitación de tu casa).

--- code ---
---
language: python
line_highlights: 3-4
---
            'Comedor' : {
                'oeste' : 'Sala',
                'sur' : 'Jardín',
                'objeto' : 'poción'
            },
    

--- /code ---

--- /task ---

--- task ---

Agrega este código para dejar que el jugador gane cuando llegue al jardín con la llave y la poción:

--- code ---
---
language: python
line_highlights: 6-9
---
# el jugador pierde si entra a una habitación con un monstruo
if 'objeto' in habitaciones[habitacionActual] and 'monstruo' in habitaciones[habitacionActual]['objeto']: 
    print('Un monstruo te atrapó... ¡PERDISTE!) 
    break

# el jugador gana si llega al jardín con una llave y una poción
if habitacionActual == 'Jardín' and 'llave' in inventario and 'poción' in inventario: 
    print('Te escapaste de la casa... ¡GANASTE!') 
    break

--- /code ---

Asegúrate de que el código tiene sangría, al estar en línea con el código anterior. Este código quiere decir que el mensaje `Te escapaste de la casa... ¡GANASTE!` es mostrado si el jugador está en la habitación 4 (el jardín) y si la llave y la poción están en su inventario.

Si tienes más de 4 habitaciones, puedes utilizar un número diferente para tu jardín en el código anterior.

--- /task ---

--- task ---

¡Prueba tu juego para asegurarte de que el jugador puede ganar!

![captura de pantalla](images/rpg-win-test.png)

--- /task ---

--- task ---

Finalmente, agreguemos instrucciones al juego, de ese modo el jugador sabe qué tiene que hacer. Edita la función `mostrarInstrucciones()` para incluir más información.

--- code ---
---
language: python
line_highlights: 7-8
---
def mostrarInstrucciones(): 
    #imprime un menu principal y los comandos 
        print('''
Juego RPG
========

Llega al jardín con una llave y una poción. 
¡Evita a los monstruos!

Comandos: ir [dirección] 
tomar [objeto] 
''')

--- /code ---

¡Vas a necesitar añadir instrucciones para decirle al usuario qué objetos necesitan recoger y qué necesitan evitar!

--- /task ---

--- task ---

Prueba tu juego y ve tus nuevas instrucciones.

![captura de pantalla](images/rpg-instructions-test.png)

--- /task ---
