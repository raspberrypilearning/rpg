#!/bin/python3

# Reemplaza el proyecto inicial RPG con este codigo cuando aparezcan nuevas instrucciones

def showInstructions():
  #imprime un menu principal y los comandos
  print('''
Juego RPG
========
Comandos:
  ir [direction]
  coger [item]
''')

def showStatus():
  #Imprime el estado actual del jugador
  print('---------------------------')
  print("Estás en el / la " + currentRoom)
  #Imprime el inventario actual
  print("Inventario: " + str(inventory))
  #imprime un objeto si hay uno
  if "item" in rooms[currentRoom]:
    print('Puedes ver ' + rooms[currentRoom]['item'])
  print("---------------------------")

#un inventario, que esta vacio al principio
inventory = []

#un diccionario que une una habitacion a las posiciones de las otras habitaciones
rooms = {

            'Sala' : { 
                  'sur' : "Cocina'
                },

            'Cocina' : {
                  'norte' : 'Sala'
                }

         }

#comienza con el jugador en la Sala
currentRoom = 'Sala'

showInstructions()

#Repetir indefinidamente
while True:

  showStatus()

  #obtiene el siguiente movimiento del jugador
  #.split() lo separa en una lista
  #por ejemplo escribir 'ir este' va a dar la lista:
  #['ir','este']
  move = ''
  while move == '':  
    move = input('>')
    
  move = move.lower().split()

  #si escriben 'ir' primero
  if move[0] == 'ir':
    #verifica que esta permitido ir a donde quieren ir
    if move[1] in rooms[currentRoom]:
      #haz que la habitacion en la que esta el jugador sea la nueva habitacion
      currentRoom = rooms[currentRoom][move[1]]
    #si no hay una puerta (conectando) hacia donde quieren ir
    else:
        print('¡No puedes ir en esa direccion!')

  #si escriben 'coger' primero
  if move[0] == 'coger' :
    #si la habitacion contiene un objeto y ese objeto es el que el jugador quiere coger
    if 'item' in rooms[currentRoom] and move[1] in rooms[currentRoom]['item']:
      #añade el objeto al inventario
      inventory += [move[1]]
      #muestra un mensaje de ayuda
      print('¡Ahora tienes un/una ' + move[1] + '!')
      #borra el objeto de la habitación
      del rooms[currentRoom]['item']
    #si el objeto que se quiere no esta en la habitación
    else:
      #diles que no pueden cogerlo
      print('¡No puedes coger el/la ' + move[1] + '!')

