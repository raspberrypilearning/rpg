## Adicionar novas divisões

\--- task \---

Open the Python starter project.

**Online:** abre o projeto Python inicial em [rpf.io/rpgon](http://rpf.io/rpgon){:target="_blank"}.

**Offline**: Abre o [projecto inicial](http://rpf.io/p/en/rpg-go){:target="_blank"} no editor offline.

\--- /task \---

\--- task \---

This is a very basic RPG game that only has 2 rooms. Aqui está um mapa do jogo:

![captura de ecrã](images/rpg-map1.png)

Podes digitar `vai sul` para ir da entrada para a cozinha, e depois `vai norte` para voltar para a entrada!

![captura de ecrã](images/rpg-controls.png)

\--- /task \---

\--- task \---

What happens when you type in a direction that you cannot go? Digita `vai oeste` na entrada e vais receber uma simpática mensagem de erro.

![captura de ecrã](images/rpg-error.png)

\--- /task \---

\--- task \---

If you find the `rooms` variable, you can see that the map is coded as a dictionary of rooms:

## \--- code \---

## language: python

# um dicionário a ligar uma divisão a outras divisões

divisoes = {

            'Entrada' : {
                'sul' : 'Cozinha'
            },
    
            'Cozinha' : {
                'norte : 'Entrada'
            }
    
        }
    

\--- /code \---

Each room is a dictionary, and rooms are linked together using directions.

\--- /task \---

\--- task \---

Let’s add a dining room to your map, to the east of the hall.

![captura de ecrã](images/rpg-dining.png)

Precisas de adicionar uma terceira divisão, chamada de `sala de jantar`, e ligá-la à entrada (para oeste). Também precisas de adicionar dados à entrada, para que possas ir para a sala de jantar a este.

**Não te esqueças de que também vais precisar de adicionar vírgulas nas linhas acima do teu novo código.**

## \--- code \---

language: python

## line_highlights: 5-6,11-15

# um dicionário a ligar uma divisão a outras divisões

rooms = {

            'Entrada' : {
                'sul' : 'Cozinha',
                'este' : 'Sala Jantar'
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

\--- task \---

Try out the game with your new dining room:

![captura de ecrã](images/rpg-dining-test.png)

Se não consegues entrar ou sair da sala de jantar, verifica se adicionaste todo o código acima (incluindo as vírgulas extras nas linhas acima).

\--- /task \---