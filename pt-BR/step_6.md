## Adicionando inimigos

Este jogo é muito fácil! Vamos adicionar inimigos em alguns cômodos que o jogador deve evitar.

\--- task \---

Adding an enemy to a room is as easy as adding any other item. Let’s add a hungry monster to the kitchen:

## \--- code \---

language: python

## line_highlights: 11-12

# um dicionário ligando um cômodo aos demais cômodos

rooms = {

            'Saguao' : {
                'sul' : 'Cozinha',
                'leste' : 'Sala Jantar',
                'item' : 'chave'
            },
    
            'Cozinha' : {
                'norte' : 'Saguão',
                'item' : 'monstro'
            },
    
            'Sala Jantar' : {
                'oeste' : 'Saguão'
            }
    
        }
    

\--- /code \---

\--- /task \---

\--- task \---

You also want to make sure that the game ends if the player enters a room with a monster in. You can do this with the following code, which you should add to the end of the game:

## \--- code \---

language: python

## line_highlights: 6-9

        #senāo, se nāo houver item para coletar
        else:
            #diz ao jogador que nāo pode pegar item
            print('Nāo pode apanhar uma ' + move[1] + '!')
    
    #o jogador perde se entrar numa divisāo com um monstro
    if "item" in comodos[divAtual] and 'monstro' in comodos[divAtual]['item']:
        print('O monstro te pegou... Fim de jogo!')
        break
    

\--- /code \---

This code checks whether there is an item in the room, and if so, whether that item is a monster. Notice that this code is indented, putting it in line with the code above it. This means that the game will check for a monster every time the player moves into a new room.

\--- /task \---

\--- task \---

Test out your code by going into the kitchen, which now contains a monster.

![screenshot](images/rpg-monster-test.png)

\--- /task \---