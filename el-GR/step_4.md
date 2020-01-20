## Προσθήκη αντικειμένων για συλλογή

Ας αφήσουμε μερικά αντικείμενα στα δωμάτια για να τα μαζέψει ο παίκτης καθώς κινείται μέσα στον λαβύρινθο.

\--- task \---

Adding an item into a room is easy, you can just add it to a room's dictionary. Let’s put a key in the hall.

Remember to put a comma after the line above the new item, or your program won’t run!

## \--- code \---

language: python

## line_highlights: 6-7

# ένα λεξικό που συνδέει ένα δωμάτιο με τα άλλα

rooms = {

            'Χωλ' : {
                'νότια' : 'Κουζίνα',
                'ανατολικά' : 'Τραπεζαρία',
                'αντικείμενο' : 'κλειδί'
            },
    
            'Κουζίνα' : {
                'βόρεια' : 'Χωλ'
            },
    
            'Τραπεζαρία' : {
                'δυτικά' : 'Χωλ'
            }
    
        }
    

\--- /code \---

\--- /task \---

\--- task \---

If you run your game after adding the code above, you can now see a key in the hall, and you can even pick it up (by typing `get key`) which adds it to your inventory!

![screenshot](images/rpg-key-test.png)

\--- /task \---