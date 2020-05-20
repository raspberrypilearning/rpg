## गेम जीतना

आइए अपने खिलाड़ी को एक मिशन दें, जिसे गेम जीतने के लिए पूरा करना जरुरी है।

\--- task \---

इस गेम में, खिलाड़ी घर से भागकर, बगीचे में पहुंचने पर जीतता है। उनके पास key और जादुई औषधि(potion) भी होनी चाहिए। यह खेल का एक नक्शा है:

![स्क्रीनशॉट](images/rpg-final-map.png)

\--- /task \---

\--- task \---

सबसे पहले, आपको dining room के south में एक garden को जोड़ना है। याद रहे की कमरे में दूसरे कमरे में आने जाने के लिए दरवाज़ा हो|

## \--- code \---

language: python

## line_highlights: 16-17,18-22

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
                'west' : 'Hall',
                'south' : 'Garden'
            },
    
            'Garden' : {
                'north' : 'Dining Room'
            }
    
        }
    

\--- /code \---

\--- /task \---

\--- task \---

dining room (या अपने घर के किसी और कमरे में) में एक potion जोड़ें।

## \--- code \---

language: python

## line_highlights: 3-4

            'Dining Room' : {
                'west' : 'Hall',
                'south' : 'Garden',
                'item' : 'potion'
            },
    

\--- /code \---

\--- /task \---

\--- task \---

इस कोड को जोड़ने पर खिलाड़ी को गेम जीत सकता है जब वो key और potion के साथ garden में आता है:

## \--- code \---

language: python

## line_highlights: 6-9

# खिलाड़ी हार जाता है अगर वो एक कमरे में प्रवेश करता हैं जिसमे एक राक्षस हो

if 'item' in rooms\[currentRoom] and 'monster' in rooms[currentRoom\]\['item'\]: print('A monster has got you... GAME OVER!') break

# खिलाड़ी जीतता है जब वो कुंजी और औषधि के साथ बगीचे में आता हैं

if currentRoom == 'Garden' and 'key' in inventory and 'potion' in inventory: print('You escaped the house... YOU WIN!') break

\--- /code \---

सुनिश्चित करें कि यह कोड इंडेंटेड है, इसके ऊपर के कोड की तरह। इस कोड का अर्थ है कि संदेश `You escaped the house...YOU WIN!` दिखाया जाता है जब खिलाड़ी कमरे 4 (garden) में है और यदि सूची में key और potion हैं।

यदि आपके पास 4 से अधिक कमरे हैं, तो आपको ऊपर दिए गए कोड में अपने garden के लिए एक अलग कमरे की संख्या का उपयोग करना पड़ सकता है।

\--- /task \---

\--- task \---

खिलाड़ी जीत सकते हैं यह सुनिश्चित करने के लिए अपने गेम का परीक्षण करें!

![स्क्रीनशॉट](images/rpg-win-test.png)

\--- /task \---

\--- task \---

अंत में, अपने गेम में कुछ निर्देश जोड़ें, ताकि खिलाड़ी को पता हो कि उन्हें क्या करना है। संपादित करके `showInstructions()` में और जानकारी जोड़े।

## \--- code \---

language: python

## line_highlights: 7-8

def showInstructions(): #print a main menu and the commands print('''

# RPG Game

एक कुंजी और एक औषधि के साथ गार्डन में जाओ राक्षसों से बचें!

Commands: go [direction] get [item] ''')

\--- /code \---

आपको खिलाड़ी को यह बताने के लिए निर्देश जोड़ना आवश्यक है कि उन्हें किन वस्तुओं को इकट्ठा करना जरुरी है, और उन्हें किन चीज़ों से बचना है!

\--- /task \---

\--- task \---

अपने गेम का परीक्षण करने पर, आपको अपने नए निर्देश दिखने चाहिए।

![स्क्रीनशॉट](images/rpg-instructions-test.png)

\--- /task \---