#!/bin/python3

def showInstructions():
    # اطبع القائمة الرئيسية والأوامر
    print('''
لعبة RPG (لعبة تقمُّص الأدوار Role-Play Game)
========

إذهب إلى الحديقة مع مفتاح و جرعة
تجنب الوحوش!

You are getting tired, each time you move you loose 1 health point. 

الأوامر:
  اذهب [الاتجاهات]
  احصل على [جرعة]
''')

def showStatus():
  # اطبع حالة اللاعب الحالية
  print('---------------------------')
  print(name + ' is in the ' + currentRoom)
  print("Health : " + str(health))
  # اطبع المخزون الحالي
  print("المخزون : " + str(inventory))
  # اطبع عنصر إذا كان هناك واحد
  if "عنصر" in rooms[currentRoom]:
    print('أنت ترى ' + rooms[currentRoom]['عنصر'])
  print("---------------------------")

# setup the game
name = None
health = 5
currentRoom = 'Hall'
inventory = []

#-# YOUR CODE GOES HERE #-#
# Load data from the file

# قاموس يربط بين غرفة وأماكن الغرف الأخرى
rooms = {

            'الصالة' : { 'جنوب' : 'المطبخ',
                  'شرق'  : 'غرفة الطعام',
                  'عنصر'  : 'مفتاح'
                },

            'المطبخ' : { 'شمال' : 'الصالة',
                  'عنصر'  : 'وحش'
                },

            'غرفة الطعام' : { 'غرب'  : 'الصالة',
                  'جنوب' : 'الحديقة',
                  'عنصر'  : 'جرعة'

                },

            'الحديقة' : { 'شمال' : 'غرفة الطعام' }

         }

# ask the player their name
if name is None:
  name = input("What is your name Adventurer? ")
  showInstructions()

# حَلَقَة تتكرر للأبد
while True:

  showStatus()

  # احصل على 'حركة' اللاعب التالية
  #()split. تقسمها إلى قائمة مجموعة
  # مثلاً: كتابة 'اذهب شرق' ستعطي القائمة:
  # ['اذهب','شرق']
  move = ''
  while move == '':
    move = input('>')

  move = move.lower().split()

  # اذا كتبوا 'اذهب' أولاً
  if move[0] == 'اذهب':
    health = health - 1
    # تأكد أنه مسموحٌ لهم الذهاب أينما يريدون
    if move[1] in rooms[currentRoom]:
      # تعيين الغرفة الحالية للغرفة الجديدة
      currentRoom = rooms[currentRoom][move[1]]
    # لا يوجد باب (رابط) بالغرفة الجديدة
    else:
      print('لا يمكنك الذهاب من هذا الطريق!')

  # إذا كتبوا 'احصل على' أولاً
  if move[0] == 'احصل على' :
    # إذا كانت الغرفة تحتوي على عنصر ، وكان العنصر هو الذي يريدون الحصول عليه
    if 'عنصر' in rooms[currentRoom] and move[1] in rooms[currentRoom]['عنصر']:
      # أضف العنصر إلى مخزونهم
      inventory += [move[1]]
      # اعرض رسالة مساعدة
      print(move[1] + 'تم التحصيل!')
      # قم بإزالة العنصر من الغرفة
      del rooms[currentRoom]['عنصر']
    # وإلا ، إذا لم يكن العنصر هناك للحصول عليه
    else:
      # أخبرهم أنهم لا يستطيعون الحصول عليه
      print('لا يمكنك الحصول على ' + move[1] + '!')

  #اللاعب يخسر إذا دخل غرفةً بها وحش
  if 'عنصر' in rooms[currentRoom] and 'monster' in rooms[currentRoom]['عنصر']:
    print('الوحش قد أمسك بك... انتهت اللعبة!')
    break

  if health == 0:
    print('You collapse from exhaustion... GAME OVER!')

  #يربح اللاعب إذا وصل إلى الحديقة مع مفتاح وجرعة
  if currentRoom == 'الحديقة' and 'مفتاح' in inventory and 'جرعة' in inventory:
    print('لقد هربت من المنزل... لقد ربحت!')
    break

  #-# YOUR CODE GOES HERE #-#
  # Save game data to the file