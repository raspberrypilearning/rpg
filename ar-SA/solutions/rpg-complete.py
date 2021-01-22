#!/bin/python3

def showInstructions():
    # اطبع القائمة الرئيسية والأوامر
    print('''
لعبة RPG (لعبة تقمُّص الأدوار Role-Play Game)
========

إذهب إلى الحديقة ومعك مفتاح و جرعة
تجنب الوحوش!

بدأت تصاب بالتعب، في كل مرة تتحرك ستفقد نقطة واحدة من الصحة. 

Commands:
  go [direction]
  get [item]
''')

showStatus():
  # اطبع حالة اللاعب الحالية
  print('---------------------------')
  print(name + ' موجود في ' + currentRoom)
  print("الصحة: " + str(health))
  # اطبع المخزون الحالي
  print("المخزن : " + str(inventory))
  # اطبع عنصر إذا كان هناك واحد
  if "عنصر" in rooms[currentRoom]:
    print('أنت ترى ' + rooms[currentRoom]['عنصر'])
  print("---------------------------")

# إعدادات اللعبة
name = None
health = 5
currentRoom = 'الصالة'
inventory = []

#-# ضع أوامرك البرمجية هنا #-#
# تحميل البيانات من الملف

# قاموس يربط بين غرفة وأماكن الغرف الأخرى
rooms = {

            'الصالة' : { 'حنوب' : 'المطبخ',
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

# اسأل اللاعب عن إسمة
if name is None:
  name = input("ماهو اسمك أيها المغامر؟ ")
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
  if move[0] == 'go':
    health = health - 1
    # تأكد أنه مسموحٌ لهم الذهاب أينما يريدون
    if move[1] in rooms[currentRoom]:
      # تعيين الغرفة الحالية للغرفة الجديدة
      currentRoom = rooms[currentRoom][move[1]]
    # لا يوجد باب (رابط) للغرفة الجديدة
    else:
      print('لا يمكنك الذهاب من هذا الطريق!')

  # إذا كتبوا 'احصل' أولاً
  if move[0] == 'get' :
    # إذا كانت الغرفة تحتوي على عنصر ، وكان هذا هو العنصر الذي يريدون الحصول عليه
    if 'عنصر' in rooms[currentRoom] and move[1] in rooms[currentRoom]['عنصر']:
      # أضف العنصر إلى مخزونهم
      inventory += [move[1]]
      # اعرض رسالة مساعدة
      print(move[1] + ' got!')
      # قم بإزالة العنصر من الغرفة
      del rooms[currentRoom]['عنصر']
    # وإلا ، إذا لم يكن العنصر موجود للحصول عليه
    else:
      # أخبرهم أنهم لا يستطيعون الحصول عليه
      print('لا يمكنك الحصول على ' + move[1] + '!')

  #اللاعب يخسر إذا دخل غرفةً بها وحش
  if 'عنصر' in rooms[currentRoom] and 'وحش' in rooms[currentRoom]['عنصر']:
    print('لقد أمسك بك الوحش... انتهت اللعبة!')
    break

  if health == 0:
    print('لقد انهرت من الانهاك... انتهت اللعبة!')

  #يربح اللاعب إذا وصل إلى الحديقة مع مفتاح وجرعة
  if currentRoom == 'الحديقة' and 'مفتاح' in inventory and 'جرعة' in inventory:
    print('لقد هربت من المنزل... لقد ربحت!')
    break

  #-# ضع أوامرك البرمجية هنا #-#
  # الآن قم بإضافة بيانات اللعبة إلى الملف