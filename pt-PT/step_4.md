## Adicionar itens para apanhar

Vamos deixar itens nas divisões para o jogador apanhar enquanto se move pelo labirinto.

\--- task \--- Adicionar um item a uma divisāo é fácil, basta adicioná-lo ao dicionário da divisāo. Vamos colocar uma chave na entrada.

Lembra-te de colocar uma vírgula depois da linha acima do novo item, ou o teu programa nāo vai funcionar!

## \--- code \---

language: python

## line_highlights: 6-7

# um dicionário a ligar uma divisāo a outras divisões

divisoes = {

            'Entrada' : {
                'sul' : 'Cozinha',
                'este' : 'Sala Jantar',
                'item' : 'chave'
            },
    
            'Cozinha' : {
                'norte' : 'Entrada'
            },
    
            'Sala Jantar' : {
                'oeste' : 'Entrada'
            }
    
        }
    

\--- /code \---

\--- /task \---

\--- task \--- Se correres o teu jogo depois de adicionar o código acima, podes ver agora uma chave na entrada, e podes até apanhá-la (escrevendo `apanha chave`) o que a adiciona ao teu inventário!

![captura de ecrã](images/rpg-key-test.png) \--- /task \---