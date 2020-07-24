## ಶತ್ರುಗಳನ್ನು ಸೇರಿಸುವುದು

ಈ ಆಟವು ತುಂಬಾ ಸುಲಭ! ಆಟಗಾರನು ತಪ್ಪಿಸಬೇಕಾದ ಕೆಲವು ಕೊಠಡಿಗಳಿಗೆ ಶತ್ರುಗಳನ್ನು ಸೇರಿಸೋಣ.

--- task ---

ಕೊಠಡಿಗೆ ಶತ್ರುವನ್ನು ಸೇರಿಸುವುದು ಬೇರೆ ಯಾವುದೇ ವಸ್ತುವನ್ನು ಸೇರಿಸುವಷ್ಟು ಸುಲಭ. ಹಸಿದ monsterನನ್ನು kitchen ಇಗೆ ಸೇರಿಸೋಣ:

--- code ---
---
language: python
line_highlights: 11-12
---
# ಕೊಠಡಿಯನ್ನು ಇತರ ಕೊಠಡಿಗಳಿಗೆ ಜೋಡಿಸುವ ನಿಘಂಟು
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
--- /code ---

--- /task ---

--- task ---

ಆಟಗಾರನು monster ಇರುವ ಕೊಠಡಿಗೆ ಪ್ರವೇಶಿಸಿದರೆ ಆಟವು ಕೊನೆಗೊಳ್ಳುತ್ತದೆ ಎಂದು ಖಚಿತಪಡಿಸಿಕೊಳ್ಳಲು ನೀವು ಬಯಸುತ್ತೀರಿ. ಕೆಳಗಿನ ಕೋಡ್‌ನೊಂದಿಗೆ ನೀವು ಇದನ್ನು ಮಾಡಬಹುದು, ಅದನ್ನು ನೀವು ಆಟದ ಕೊನೆಯಲ್ಲಿ ಸೇರಿಸಬೇಕು:

--- code ---
---
language: python
line_highlights: 6-9
---
        #otherwise, if the item isn't there to get
        else:
            #tell them they can't get it
            print('Can\'t get' + move[1] + '!')

    #player loses if they enter a room with a monster
    if 'item' in rooms[currentRoom] and 'monster' in rooms[currentRoom]['item']:
        print('A monster has got you... GAME OVER!')
        break
--- /code ---

ಈ ಕೋಡ್ ಕೊಠಡಿಯಲ್ಲಿ ಐಟಂ ಇದೆಯೇ ಎಂದು ಪರಿಶೀಲಿಸುತ್ತದೆ, ಮತ್ತು ಹಾಗಿದ್ದಲ್ಲಿ, ಆ ಐಟಂ monsterದ್ದೇ ಎಂದು ಪರಿಶೀಲಿಸುತ್ತದೆ. ಈ ಕೋಡ್ ಅನ್ನು ಇಂಡೆಂಟ್ ಮಾಡಲಾಗಿದೆ ಎಂಬುದನ್ನು ಗಮನಿಸಿ, ಅದರ ಮೇಲಿನ ಕೋಡ್‌ಗೆ ಅನುಗುಣವಾಗಿ ಇರಿಸಿ. ಆಟಗಾರನು ಹೊಸ ಕೊಠಡಿಗೆ ಹೋದಾಗಲೆಲ್ಲಾ ಆಟವು monsterನನ್ನು ಪರಿಶೀಲಿಸುತ್ತದೆ ಎಂದರ್ಥ.

--- /task ---

--- task ---

ನಿಮ್ಮ ಕೋಡ್ ಅನ್ನು kitchenಗೆ ಹೋಗುವ ಮೂಲಕ ಪರೀಕ್ಷಿಸಿ, ಅದು ಈಗ monsterವನ್ನು ಒಳಗೊಂಡಿದೆ.

![screenshot](images/rpg-monster-test.png)

--- /task ---