## दुश्मन जोड़ना

यह खेल बहुत आसान है! चलो कुछ कमरों में दुश्मनों को जोड़ते हैं जिनसे खिलाड़ी को बचना है।

\--- task \---

एक कमरे में किसी शत्रु को जोड़ना किसी भी अन्य आइटम को जोड़ने जितना आसान है। आइए रसोई में एक भूखा दैत्य(monster) जोड़ें:

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
    

\--- /code \---

\--- /task \---

\--- task \---

आपको यह भी निश्चित करना है कि अगर खिलाड़ी एक ऐसे कमरे में प्रवेश करता है जिसमें दैत्य है तो गेम समाप्त हो जाये| आप इसे निम्नलिखित कोड के साथ कर सकते हैं, जिसे आपको गेम के अंत में जोड़ना चाहिए:

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

यह कोड इस बात की जाँच करता है कि क्या कमरे में कोई आइटम है, और यदि हां, तो क्या वह वस्तु दैत्य है। ध्यान दें कि यह कोड इंडेंट है, इसे ऊपर दिए गए कोड के अनुरूप रखें। इसका मतलब यह है कि गेम हर बार एक दैत्य के लिए जाँच करेगा जब खिलाड़ी एक नए कमरे में जाता है।

\--- /task \---

\--- task \---

kitchen में जाकर अपने कोड का परीक्षण करें, जिसमें अब एक राक्षस है।

![स्क्रीनशॉट](images/rpg-monster-test.png)

\--- /task \---