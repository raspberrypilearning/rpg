## Adicionar inimigos

Este jogo está demasiado fácil! Vamos adicionar inimigos que o jogador deve evitar a algumas das divisões.

\--- task \--- Adicionar um inimigo a uma divisāo é tāo fácil como adicionar outro item. Vamos adicionar um monstro esfomeado à cozinha:

## \--- code \---

language: python

## line_highlights: 11-12

# um dicionário a ligar uma divisāo a outras divisões

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
    

\--- /code \--- \--- /task \---

\--- task \--- Também vais querer ter a certeza de que o jogo acaba se o jogador entrar numa divisāo com um monstro. Podes fazer isso com o código seguinte, que deves adicionar ao fim do jogo:

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

Este código verifica se há um item na divisāo, e se houver, se o item é um monstro. Toma nota de que o código está indentado, em linha com o código acima. Isso significa que o jogo vai verificar se há um monstro de cada vez que o jogador entrar numa nova divisāo. \--- /task \---

\--- task \--- Testa o teu código indo para a cozinha, que agora tem um monstro.

![captura de ecrã](images/rpg-monster-test.png) \--- /task \---