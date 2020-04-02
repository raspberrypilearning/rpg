## Adicionando inimigos

Este jogo está muito fácil! Vamos adicionar inimigos em alguns cômodos que o jogador deve evitar.

\--- task \---

Adicionar um inimigo a um cômodo é tão fácil quanto adicionar qualquer outro item. Vamos adicionar um monstro faminto à cozinha:

## \--- code \---

language: python

## line_highlights: 11-12

# um dicionário ligando um cômodo aos demais cômodos

comodos= {

            'Saguao' : {
                'baixo' : 'Cozinha',
                'direita' : 'Sala de Jantar',
                'item' : 'chave'
            },
    
            'Cozinha' : {
                'Cima' : 'Saguão',
                'item' : 'monstro'
            },
    
            'Sala de Jantar' : {
                'esquerda' : 'Saguão'
            }
    
        }
    

\--- /code \---

\--- /task \---

\--- task \---

Você também quer ter certeza de que o jogo vai acabar se o jogador entrar em uma sala com um monstro. Você pode fazer isso com o seguinte código, que você deve adicionar ao final do jogo:

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