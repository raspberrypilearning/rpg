## إضافة أعداء

هذه اللعبة سهلة للغاية! لنقم بإضافة بعض الأعداء لبعض الغرف التي يجب على اللاعب تجنبها.

\--- task \--- Adding an enemy to a room is as easy as adding any other item. لنقم بإضافة وحش جائع إلى المطبخ:

## \--- code \---

language: python

## line_highlights: 11-12

# a dictionary linking a room to other rooms

rooms = {

            'Hall' : {
                'south' : 'Kitchen',
                'east' : 'Dining Room',
                'item' : 'key'
            },
    
            'Kitchen' : {
                'north' : 'Hall',
                'item' : 'monster'
            },
    
            'Dining Room' : {
                'west' : 'Hall'
            }
    
        }
    

\--- /code \--- \--- /task \---

\--- task \--- You also want to make sure that the game ends if the player enters a room with a monster in. يمكنك فعل هذا بالكود التالي، الذي يجب عليك إضافته في آخر اللعبة:

## \--- code \---

language: python

## line_highlights: 6-9

        #otherwise, if the item isn't there to get
        else:
            #tell them they can't get it
            print('Can\'t get' + move[1] + '!')
    
    #player loses if they enter a room with a monster
    if 'item' in rooms[currentRoom] and 'monster' in rooms[currentRoom]['item']:
        print('A monster has got you... GAME OVER!')
        break
    

\--- /code \---

هذا الكود يتحقق ما إذا كان هنالك عنصر في الغرفة، وإذا كان كذلك، يتحقق ما إذا كان وحشاً. لاحظ أن هذا الكود مسبق بمسافة بادئة، بإضافتها في السطر مع الكود أعلاه. هذا يعني أن اللعبة ستتحقق من وجود وحش في كل مرة يقوم اللاعب بالتحرك إلى غرفة جديدة. \--- /task \---

\--- task \--- Test out your code by going into the kitchen, which now contains a monster.

![لقطة الشاشة](images/rpg-monster-test.png) \--- /task \---