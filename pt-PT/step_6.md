## Adicionar inimigos

Este jogo está demasiado fácil! Vamos adicionar a algumas das divisões inimigos que o jogador deve evitar.

\--- task \---

Adding an enemy to a room is as easy as adding any other item. Vamos adicionar um monstro esfomeado à cozinha:

## \--- code \---

language: python

## line_highlights: 11-12

# um dicionário a ligar uma divisão a outras divisões

divisoes = {

            'Entrada' : {
                'sul' : 'Cozinha',
                'este' : 'Sala Jantar',
                'item' : 'chave'
            },
    
            'Cozinha' : {
                'norte' : 'Entrada',
               'item' : 'monstro'
            },
    
            'Sala Jantar' : {
                'oeste' : 'Entrada'
            }
    
        }
    

\--- /code \---

\--- /task \---

\--- task \---

You also want to make sure that the game ends if the player enters a room with a monster in. Podes fazer isso com o código seguinte, que deves adicionar ao fim do jogo:

## \--- code \---

language: python

## line_highlights: 6-9

        #senāo, se nāo houver item para apanhar
        else:
            #diz ao jogador que nāo pode apanhar o item
            print('Nāo podes apanhar uma ' + jogada[1] + '!')
    
    #o jogador perde se entrar numa divisāo com um monstro
    if "item" in divisoes[divAtual] and 'monstro' in divisoes[divAtual]['item']:
        print('O monstro apanhou-te... PERDESTE!')
        break
    

\--- /code \---

Este código verifica se há um item na divisão, e se houver, se o item é um monstro. Toma nota de que o código está indentado, em linha com o código acima. Isso significa que o jogo vai verificar se há um monstro de cada vez que o jogador entrar numa nova divisāo.

\--- /task \---

\--- task \---

Test out your code by going into the kitchen, which now contains a monster.

![captura de ecrã](images/rpg-monster-test.png)

\--- /task \---