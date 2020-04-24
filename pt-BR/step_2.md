## Adicionar novos cômodos

\--- task \---

Abre o projeto inicial em Python.

**Online**: Abra o projeto inicial em [rpf.io/rpgon](http://rpf.io/rpgon){:target="_blank"}.

**Off-line**: Abra o [projeto inicial](http://rpf.io/p/en/rpg-go){:target="_ blank"} no editor offline.

\--- /task \---

\--- task \---

Este é um jogo de RPG muito básico que só tem 2 cômodos. Aqui está o mapa do jogo:

![screenshot](images/rpg-map1.png)

Você pode digitar `para baixo` para ir do saguão até a cozinha e, em seguida, `para cima` para voltar ao saguão novamente!

![screenshot](images/rpg-controls.png)

\--- /task \---

\--- task \---

O que acontece quando você digita uma direção que você não pode ir? Digite `para esquerda` no saguãoe você receberá uma mensagem de erro amigável.

![screenshot](images/rpg-error.png)

\--- /task \---

\--- task \---

Se você encontrar a variável `cômodos` , poderá ver que o mapa está estruturado como um dicionário de salas:

## \--- code \---

## language: python

# um dicionário ligando um cômodo aos outros cômodos

comodos= {

            'Saguão' : {
                'baixo' : 'Cozinha'
            },
    
            'Cozinha' : {
                'cima' : 'Saguão'
            }
    
        }
    

\--- /code \---

Cada cômodo é um dicionário, e os cômodos sāo ligados uns aos outros usando as direções.

\--- /task \---

\--- task \---

Vamos adicionar uma sala de jantar ao seu mapa, a direita do saguão.

![screenshot](images/rpg-dining.png)

Você precisa adicionar um terceiro cômodo, chamado de `Sala de Jantar`, e ligá-lo ao saguão (esquerda). Você também precisa adicionar dados ao saguão, para que você possa ir para a sala de jantar a direta.

**Não esqueça que você também vai precisar adicionar vírgulas nas linhas anteriores ao novo código.**

## \--- code \---

language: python

## line_highlights: 5-6,11-15

# um dicionário ligando um cômodo aos demais cômodos

comodos= {

            'Saguão' : {
                'baixo' : 'Cozinha',
                'direita' : 'Sala de Jantar'
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

Teste o jogo com sua nova sala de jantar:

![screenshot](images/rpg-dining-test.png)

Se você não pode entrar e sair da sala de jantar, basta verificar se você adicionou todo o código acima (incluindo as vírgulas extras para as linhas acima).

\--- /task \---