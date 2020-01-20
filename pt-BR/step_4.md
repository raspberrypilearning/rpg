## Adicionando itens para coletar

Vamos deixar itens nos cômodos para o jogador coletar enquanto eles se movem pelo labirinto.

\--- task \---

Adding an item into a room is easy, you can just add it to a room's dictionary. Let’s put a key in the hall.

Remember to put a comma after the line above the new item, or your program won’t run!

## \--- code \---

language: python

## line_highlights: 6-7

# um dicionário ligando um cômodo aos demais cômodos

rooms = {

            'Saguao' : {
                'sul' : 'Cozinha',
                'leste' : 'Sala Jantar',
                'item' : 'chave'
            },
    
            'Cozinha' : {
                'norte' : 'Saguão'
            },
    
            'Sala Jantar' : {
                'oeste' : 'Saguão'
            }
    
        }
    

\--- /code \---

\--- /task \---

\--- task \---

If you run your game after adding the code above, you can now see a key in the hall, and you can even pick it up (by typing `get key`) which adds it to your inventory!

![screenshot](images/rpg-key-test.png)

\--- /task \---