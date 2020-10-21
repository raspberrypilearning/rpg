#!/bin/python3

def mostrarInstrucciones():
    # imprime un menu principal y los comandos
    print('''
Juego RPG
========

Llega al Jardín con una llave y una poción
¡Evita a los monstruos!

Te irás cansando, con cada movimiento pierdes un punto de vida. 

Comandos:
  ir [dirección]
  tomar [objeto]
''')

def mostrarEstado():
  #Imprime el estado actual del jugador
  print('---------------------------')
  print(nombre + " estás en: " + habitacionActual)
  print("Salud : " + str(salud))
  #Imprime el inventario actual
  print("Inventario: " + str(inventario))
  #imprime un objeto si hay uno
  if "objeto" in habitaciones[habitacionActual]:
    print('Puedes ver ' + habitaciones[habitacionActual]['objeto'])
  print("---------------------------")

# configuración del juego
nombre = None
salud = 5
habitacionActual = 'Sala'
inventario = []

#-# TU CODIGO VA AQUI #-#
#Leer los datos desde un archivo

#un diccionario que une una habitación a las posiciones de las otras habitaciones
habitaciones = {

            'Sala': {'sur': 'Cocina',
                  'este': 'Comedor',
                  'objeto': 'llave'
                },

            'Cocina': {'norte': 'Sala',
                  'objeto': 'monstruo'
                },

            'Comedor': {'oeste': 'Sala',
                  'sur': 'Jardin',
                  'objeto': 'pocion'

                },

            'Jardín': {'norte': 'Comedor'}

         }

# pregunta el nombre del jugador
if nombre is None:
  nombre = input("¿Cual es tu nombre Aventurero? ")
  mostrarInstrucciones()

#Repetir indefinidamente
while True:

  mostrarEstado()

  #obtiene el siguiente movimiento del jugador
  #.split() lo separa en una lista
  #por ejemplo escribir 'ir este' va a dar la lista:
  #['ir','este']
  movimiento = ''
  while movimiento == '':
    movimiento = input('>')

  movimiento = movimiento.lower().split()

  #si escriben 'ir' primero
  if movimiento[0] == 'ir':
    salud = salud - 1
    #verifica que esta permitido ir a donde quieren ir
    if movimiento[1] in habitaciones[habitacionActual]:
      # haz que la habitacion en la que esta el jugador sea la nueva habitacion actual
      habitacionActual = habitaciones[habitacionActual][movimiento[1]]
    #si no hay una puerta (conectando) hacia donde quieren ir
    else:
      print('¡No puedes ir en esa dirección!')

  #si se escribe 'tomar' primero
  if movimiento[0]=='tomar' :
    #Si la habitación contiene un objeto, y el objeto es el que se quiere tomar
    if 'objeto' in habitaciones[habitacionActual] and movimiento[1] in habitaciones[habitacionActual]['objeto']:
      #añade el objeto al inventario
      inventario += [movimiento[1]]
      #mostrar un mensaje útil
      print('¡Ahora tienes en tus manos! ' + movimiento[1])
      #elimina el objeto de la habitación
      del habitaciones[habitacionActual]['objeto']
    #Por el contrario, si el objeto que se quiere no esta en la habitación
    else:
      #diles que no pueden tomarlo
      print('¡No puedes tomarlo! ' + movimiento[1])

  #el jugador pierde si entra a una habitacion con un monstruo
  if 'objeto' in habitaciones[habitacionActual] and 'monstruo' in habitaciones[habitacionActual]['objeto']:
    print ('Un monstruo te atrapó... PERDISTE!')
    break

  if salud == 0:
    print('Has colapsado por el agotamiento... PERDISTE!')

  #el jugador gana si llega al jardin con una llave y una pocion
  if habitacionActual == 'Jardin' and 'llave' in inventario and 'pocion' in inventario:
    print ('Te escapaste de la casa... GANASTE!')
    break

  #-# TU CODIGO VA AQUI #-#
  # Guarda los datos de la partida en un archivo