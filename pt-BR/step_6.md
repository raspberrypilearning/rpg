## Adicionando inimigos

Este jogo é muito fácil! Vamos adicionar inimigos em alguns cômodos que o jogador deve evitar.

\--- task \--- Adicionar um inimigo em um cômodo é tão fácil como adicionar outro item. Vamos adicionar um monstro faminto à cozinha:

## \--- code \---

language: python

## line_highlights: 11-12

# um dicionário ligando um cômodo aos demais cômodos

comodos= {

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
    

\--- /code \--- \--- /task \---

\--- task \--- Você também quer ter a certeza de que o jogo acaba se o jogador entrar numa divisão com um monstro. Você pode fazer isso com o seguinte código, que você deve adicionar ao final do jogo:

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

Este código verifica se há um item no cômodo e, se houver, se o item é um monstro. Observe que esse código é recuado, colocando-o de acordo com o código acima dele. Isso significa que o jogo vai verificar se há um monstro de cada vez que o jogador entrar em um novo cômodo. \--- /task \---

\--- task \--- Testa seu código indo até a cozinha, que agora contém um monstro.

![screenshot](images/rpg-monster-test.png) \--- /task \---