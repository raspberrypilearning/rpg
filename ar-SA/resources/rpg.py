bin/python3/!#

# Replace RPG starter project with this code when new instructions are live

def showInstructions():
  # اطبع القائمة الرئيسية والأوامر
  print('''
لعبة RPG (لعبة تقمُّص الأدوار Role-Play Game)
========
الأوامر:
  اذهب [الاتجاه]
  خذ [عنصر]
''')

def showStatus():
  # اطبع حالة اللاعب الحالية
  print('---------------------------')
  print('أنت في ' + currentRoom)
  # اطبع المخزون الحالي
  print("المخزون : " + str(inventory))
  # اطبع عنصر إذا كان هناك واحد
  if "عنصر" in rooms[currentRoom]:
    print('أنت ترى ' + rooms[currentRoom]['عنصر'])
  print("---------------------------")

# المخزون ، والذي يكون فارغ في البداية
inventory = []

# قاموس يربط بين غرفة وأماكن الغرف الأخرى
rooms = {

            'الصالة' : { 
                  'جنوب' : 'المطبخ'
                },

            'المطبخ' : {
                  'شمال' : 'الصالة'
                }

         }

# يبدأ اللاعب في الصالة
currentRoom = 'الصالة'

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
    # تأكد أنه مسموحٌ لهم الذهاب أينما يريدون
    if move[1] in rooms[currentRoom]:
      # تعيين الغرفة الحالية للغرفة الجديدة
      currentRoom = rooms[currentRoom][move[1]]
    # لا يوجد باب (رابط) بالغرفة الجديدة
    else:
        print('لا يمكنك الذهاب من هذا الطريق!')

  # إذا كتبوا 'خذ' أولاً
  if move[0] == 'خذ' :
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

