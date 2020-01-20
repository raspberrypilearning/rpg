## إضافة أعداء

هذه اللعبة سهلة للغاية! لنقم بإضافة بعض الأعداء لبعض الغرف التي يجب على اللاعب تجنبها.

\--- task \---

Adding an enemy to a room is as easy as adding any other item. Let’s add a hungry monster to the kitchen:

## \--- code \---

language: python

## line_highlights: 11-12

# قاموس يربط بين غرفة والغرف الأخرى

rooms = {

            'الصالة' : {
                'جنوب' : 'المطبخ',
                'شرق' : 'غرفة الطعام',
                'عنصر' : 'مفتاح'
            },
    
            'المطبخ' : {
                'شمال' : 'الصالة',
                'عنصر' : 'وحش'
            },
    
            'غرفة طعام' : {
                'غرب' : 'الصالة'
            }
    
        }
    

\--- /code \---

\--- /task \---

\--- task \---

You also want to make sure that the game ends if the player enters a room with a monster in. You can do this with the following code, which you should add to the end of the game:

## \--- code \---

language: python

## line_highlights: 6-9

        #غير ذلك، لو الغرض لم يكن هناك للحصول عليه
        else:
            #اخبرهم انهم لا يستطيعون الحصول عليه
            print('لايمكن الحصول على' + move[1] + '!')
    
    #يخسر اللاعب اذا دخل غرفة بها وحش
    if 'item' in rooms[currentRoom] and 'monster' in rooms[currentRoom]['item']:
        print('قضى عليك الوحش... إنتهت اللعبة!')
        break
    

\--- /code \---

This code checks whether there is an item in the room, and if so, whether that item is a monster. Notice that this code is indented, putting it in line with the code above it. This means that the game will check for a monster every time the player moves into a new room.

\--- /task \---

\--- task \---

Test out your code by going into the kitchen, which now contains a monster.

![screenshot](images/rpg-monster-test.png)

\--- /task \---