## Adicionando itens para coletar

Vamos deixar itens nos cômodos para o jogador coletar enquanto eles se movem pelo labirinto.

\--- task \---

Adicionar um item no cômodo é fácil, basta adicioná-lo ao dicionário da sala. Vamos colocar uma chave no saguão.

Lembre-se de colocar uma vírgula após a linha acima do novo ite ou seu programa não será executado!

## \--- code \---

language: python

## line_highlights: 6-7

# um dicionário ligando um cômodo aos demais cômodos

comodos= {

            'Saguão' : {
                'baixo' : 'Cozinha',
                'direita' : 'Sala de Jantar',
                'item' : 'chave'
            },
    
            'Cozinha' : {
                'cima' : 'Saguão'
            },
    
            'Sala de Jantar' : {
                'esquerda' : 'Saguão'
            }
    
        }
    

\--- /code \---

\--- /task \---

\--- task \---

Se você executar o seu jogo depois de adicionar o código acima, você pode encontrará uma chave no saguão, e você pode até mesmo pegá-la (digitando `pegar chave`), a adicionando ao seu inventário!

![screenshot](images/rpg-key-test.png)

\--- /task \---