## إضافة غرف جديدة

\--- task \--- Open the Python starter project.

**بالاتصال بالانترنت**: افتح المشروع المبدئي من هنا [rpf.io/rpgon](http://rpf.io/rpgon){:target="_blank"}.

**دون اتصال بالانترنت**: افتح [المشروع المبدئي](http://rpf.io/p/en/rpg-go){:target="_blank"} عبر المحرر الموجود على جهازك. \--- /task \---

\--- task \--- This is a very basic RPG game that only has 2 rooms. ها ذي خريطة للعبة:

![لقطة الشاشة](images/rpg-map1.png)

يمكنك كتابة `اذهب جنوب` للتحرك من الصالة إلى المطبخ، ومن ثم `اذهب شمال` للعودة إلى الصالة مجدداً!

![لقطة الشاشة](images/rpg-controls.png) \--- /task \---

\--- task \--- What happens when you type in a direction that you cannot go? اكتب `اذهب غرب` من الصالة وستحصل على رسالة خطأ ودودة.

![لقطة الشاشة](images/rpg-error.png) \--- /task \---

\--- task \--- If you find the `rooms` variable, you can see that the map is coded as a dictionary of rooms:

## \--- code \---

## language: python

# a dictionary linking a room to other rooms

rooms = {

            'Hall' : {
                'south' : 'Kitchen'
            },
    
            'Kitchen' : {
                'north' : 'Hall'
            }
    
        }
    

\--- /code \---

Each room is a dictionary, and rooms are linked together using directions.  
\--- /task \---

\--- task \--- Let’s add a dining room to your map, to the east of the hall.

![لقطة الشاشة](images/rpg-dining.png)

You need to add a 3rd room, called the `dining room`, and link it to the hall (to the west). ستحتاج أيضاً لإضافة بعض البيانات للصالة، حتى تستطيع التحرك إلى غرفة الطعام من الشرق.

**Don't forget that you'll also need to add commas to lines before your new code.**

## \--- code \---

language: python

## line_highlights: 5-6,11-15

# a dictionary linking a room to other rooms

rooms = {

            'Hall' : {
                'south' : 'Kitchen',
                'east' : 'Dining Room'
            },
    
            'Kitchen' : {
                'north' : 'Hall'
            },
    
            'Dining Room' : {
                'west' : 'Hall'
            }
    
        }
    

\--- /code \--- \--- /task \---

\--- task \--- Try out the game with your new dining room:

![لقطة الشاشة](images/rpg-dining-test.png)

إذا لم تتمكن من الدخول و الخروج من غرفة الطعام ، فقط تحقق من أنك أضفت جميع الأكواد الواردة أعلاه (بما في ذلك الفواصل الإضافية إلى الأسطر أعلاه). \--- /task \---