## إضافة عناصر لجمعها

لنترك بعض العناصر في الغرف للاعب حتى يقوم بجمعها أثناء تحركه خلال المتاهة.

\--- task \--- Adding an item into a room is easy, you can just add it to a room's dictionary. لنضع مفتاحاً في الصالة.

تذكر وضع فاصلة بعد السطر أعلى العنصر الجديد ، وإلا فلن يعمل برنامجك!

## \--- code \---

language: python

## line_highlights: 6-7

# a dictionary linking a room to other rooms

rooms = {

            'Hall' : {
                'south' : 'Kitchen',
                'east' : 'Dining Room',
                'item' : 'key'
            },
    
            'Kitchen' : {
                'north' : 'Hall'
            },
    
            'Dining Room' : {
                'west' : 'Hall'
            }
    
        }
    

\--- /code \---

\--- /task \---

\--- task \--- If you run your game after adding the code above, you can now see a key in the hall, and you can even pick it up (by typing `get key`) which adds it to your inventory!

![لقطة الشاشة](images/rpg-key-test.png) \--- /task \---