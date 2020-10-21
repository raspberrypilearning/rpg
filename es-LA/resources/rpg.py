#!/bin/python3

# Reemplaza el proyecto de inicio RPG con este código cuando aparezcan nuevas instrucciones

def mostrarInstrucciones():
  # imprime un menu principal y los comandos
  print('''
Juego RPG
========
Comandos:
  ir [dirección]
  tomar [objeto]
''')

def mostrarEstado():
  #Imprime el estado actual del jugador
  print('---------------------------')
  print("Estás en:  " + habitacionActual)
  #Imprime el inventario actual
  print("Inventario: " + str(inventario))
  #imprime un objeto si hay uno
  if "objeto" in habitaciones[habitacionActual]:
    print('Puedes ver:  ' + habitaciones[habitacionActual]['objeto'])
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

  #obtener el próximo 'movimiento' del jugador
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
      # establecer la habitación actual en la nueva habitación
      habitacionActual = habitaciones[habitacionActual][movimiento[1]]
    #no hay puerta (enlace) a la nueva habitación
    else:
        print('¡No puedes ir en esa dirección!')

  #si se escribe 'tomar' primero
  if movimiento[0]=='tomar' :
    #Si la habitación contiene un objeto, y el objeto es el que se quiere tomar
    if 'objeto' in habitaciones[habitacionActual] and movimiento[1] in habitaciones[habitacionActual]['objeto']:
      #añade el objeto al inventario
      inventario += [movimiento[1]]
      #mostrar un mensaje útil
      print('¡Ahora tienes en tus manos ' + movimiento[1] +'!')
      #elimina el objeto de la habitación
      del habitaciones[habitacionActual]['objeto']
    #Por el contrario, si el objeto que se quiere no esta en la habitación
    else:
      #diles que no pueden tomarlo
      print('¡No puedes tomarlo ' + movimiento[1])

