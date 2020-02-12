#!/bin/python3

# Reemplaza el proyecto inicial RPG con este codigo cuando aparezcan nuevas instrucciones

def mostrarInstrucciones():
  #imprime un menu principal y los comandos
  print('''
Juego RPG
=========
Comandos:
  ir [direction]
  coger [item]
''')

def mostrarEstado():
  #Imprime el estado actual del jugador
  print('---------------------------')
  print("Estás en el / la " + habitacionActual)
  #Imprime el inventario actual
  print("Inventario: " + str(inventario))
  #imprime un objeto si hay uno
  if "objeto" in habitaciones[habitacionActual]:
    print('Puedes ver una ' + habitaciones[habitacionActual]['objeto'])
  print("---------------------------")

#un inventario, que está vacío al principio
inventario = []

#un diccionario que une una habitación a las posiciones de las otras habitaciones
habitaciones = {

            'Sala' : { 
                  'sur' : 'Cocina'
                },

            'Cocina' : {
                  'norte' : 'Sala'
                }

         }

#comienza con el jugador en la Sala
habitacionActual = 'Sala'

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
    #verifica que esta permitido ir a donde quieren ir
    if movimiento[1] in habitaciones[habitacionActual]:
      #haz que la habitacion en la que esta el jugador sea la nueva habitacion
      habitacionActual = habitaciones[habitacionActual][movimiento[1]]
    #si no hay una puerta (conectando) hacia donde quieren ir
    else:
        print('¡No puedes ir en esa dirección!')

  #si escriben 'coger' primero
  if movimiento[0] == 'coger' :
    #si la habitacion contiene un objeto y ese objeto es el que el jugador quiere coger
    if 'objeto' in habitaciones[habitacionActual] and movimiento[1] in habitaciones[habitacionActual]['objeto']:
      #añade el objeto al inventario
      inventario += [movimiento[1]]
      #muestra un mensaje de ayuda
      print('¡Ahora tienes un/una ' + movimiento[1] + '!')
      #borra el objeto de la habitación
      del habitaciones[habitacionActual]['objeto']
    #si el objeto que se quiere no esta en la habitación
    else:
      #diles que no pueden cogerlo
      print('¡No puedes coger el/la ' + movimiento[1] + '!')

