## Προσθήκη αντικειμένων για συλλογή

Ας αφήσουμε μερικά αντικείμενα στα δωμάτια για να τα μαζέψει ο παίκτης καθώς κινείται μέσα στον λαβύρινθο.

\--- task \--- Adding an item into a room is easy, you can just add it to a room's dictionary. Ας βάλουμε ένα κλειδί στο χωλ.

Θυμήσου να βάλεις ένα κόμμα μετά τη γραμμή πάνω από το νέο αντικείμενο αλλιώς το πρόγραμμά σου δεν θα τρέξει!

## \--- code \---

language: python

## line_highlights: 6-7

# ένα λεξικό που συνδέει ένα δωμάτιο με τα άλλα

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

![screenshot](images/rpg-key-test.png) \--- /task \---