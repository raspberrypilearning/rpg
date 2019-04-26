## परिचय:

In this project, you’ll design and code your own RPG maze game. The aim of the game will be to collect objects and escape from a house, making sure to avoid all the monsters!

<div class="trinket">
  <iframe src="https://trinket.io/embed/python/d06adeb527?outputOnly=true&start=result" width="600" height="500" frameborder="0" marginwidth="0" marginheight="0" allowfullscreen>
  </iframe>
  <img src="images/rpg-finished.png">
</div>

### क्लब लीडरों के लिए अतिरिक्त जानकारी

यदि आप इस प्रोजेक्ट को प्रिंट करना चाहते हैं, तो कृपया [प्रिंटर अनुकूल संस्करण](https://projects.raspberrypi.org/en/projects/rpg/print) का उपयोग करें।

## \--- collapse \---

## title: क्लब नेता नोट्स

## परिचय:

This project teaches game design through the development of an RPG maze game. In this game, the player has to pick up objects within a house and get to a specific room, while avoiding monsters lurking in some of the rooms. This game will be achieved by manipulating dictionaries and lists.

## ऑनलाइन संसाधन

**This project uses Python 3.** We recommend using [trinket](https://trinket.io/) to write Python online. इस प्रोजेक्ट में निम्नलिखित Trinket हैं:

+ ['RPG' starting point -- jumpto.cc/rpg-go](http://jumpto.cc/rpg-go)

There is also a trinket containing the finished project:

+ [‘RPG’ Finished -- trinket.io/python/d06adeb527](https://trinket.io/python/d06adeb527)

## ऑफ़लाइन संसाधन

This project can be [completed offline](https://www.codeclubprojects.org/en-GB/resources/python-working-offline/) if preferred. आप इस प्रोजेक्ट के लिए 'प्रोजेक्ट सामग्री' लिंक पर क्लिक करके प्रोजेक्ट के संसाधनों पर पहुँच प्राप्त कर सकते हैं। इस लिंक में 'प्रोजेक्ट संसाधन' खंड है, जिसमें ऐसे संसाधन सम्मिलित हैं जिसकी बच्चों को इस प्रोजेक्ट को ऑफ़लाइन पूरा करने की ज़रूरत होगी। सुनिश्चित करें कि प्रत्येक बच्चे को इन संसाधनों की प्रतिलिपि तक पहुँच प्राप्त होती है। इस खंड में निम्नलिखित फाइलें शामिल हैं:

+ rpg/rpg.py

You can also find the completed project project in the 'Volunteer Resources' section, which contains:

+ rpg-finished/rpg.py

(उपर्युक्त सभी संसाधन प्रोजेक्ट और स्वयंसेवक `.zip` फ़ाइलों के रूप में भी डाउनलोड किए जा सकते हैं।)

## सीखने के उद्देश्य

+ Game design;
+ Editing: 
    + Lists;
    + Dictionaries.
+ Boolean expressions.

इस प्रोजेक्ट में [Raspberry Pi डिजिटल निर्माण पाठ्यक्रम](http://rpf.io/curriculum) के निम्नलिखित पहलुओं के तत्व सम्मिलित हैं:

+ [किसी समस्या को हल करने के लिए प्रोग्रामिंग संरचनाओं को जोड़ें।](https://www.raspberrypi.org/curriculum/programming/builder)

## चुनौतियाँ

+ Adding new rooms;
+ Adding items to collect;
+ Adding enemies to avoid;
+ Develop your own game.

## अक्सर पूछे जाने वाले प्रश्न

+ Children may need reminding that elements of a dictionary/list are separated by a comma. For example, when adding a new room to the 'rooms' dictionary, a comma needs to be added between the new room being added and the previous room.
+ When adding a new room, children may forget to add a link to an existing room to the newly created room. This will mean that children can leave a room, but not enter it!
+ The code for checking whether the player has won or lost the game needs to be indented, to ensure that this check is performed upon entering each new room. If the code isn't indented, then it sits outside of the main game loop and is never run.

\--- /collapse \---

## \--- collapse \---

## title: प्रोजेक्ट सामग्री

## प्रोजेक्ट संसाधन

+ [सभी प्रोजेक्ट संसाधनों वाली .zip फ़ाइल](resources/rpg-project-resources.zip)
+ [Online Trinket containing all 'RPG' project resources](http://jumpto.cc/rpg-go)
+ [rpg/rpg.py](resources/rpg-rpg.py)

## क्लब नेता संसाधन

+ [सभी प्रोजेक्ट संसाधनों वाली .zip फ़ाइल](resources/rpg-volunteer-resources.zip)
+ [ऑनलाइन पूर्ण Trinket प्रोजेक्ट](https://trinket.io/python/d06adeb527)
+ [rpg-finished/rpg.py](resources/rpg-finished-rpg.py)

\--- /collapse \---