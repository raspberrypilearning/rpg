## Ganhar o jogo

Vamos dar ao teu jogador uma missão, que precisa ser concluída para ganhar o jogo.

\--- task \---

Neste jogo, o jogador ganha ao chegar ao jardim e fugir da casa. Também precisa de ter a chave e a garrafa de poçāo com ele. Aqui está um mapa do jogo.

![captura de ecrã](images/rpg-final-map.png)

\--- /task \---

\--- task \---

Primeiro, precisas de adicionar um jardim a sul da sala de jantar. Lembra-te de adicionar portas, para ligar a outras divisões da casa.

## \--- code \---

language: python

## line_highlights: 16-17,18-22

# um dicionário a ligar uma divisāo a outras divisões

rooms = {

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
                'oeste' : 'Entrada',
                'sul' : 'Jardim"
            },
    
           'Jardim' : {
                'norte' : 'Sala Jantar'
           }
    
        }
    

\--- /code \---

\--- /task \---

\--- task \---

Adiciona uma garrafa de poçāo à sala de jantar (ou a outra divisāo da tua casa).

## \--- code \---

language: python

## line_highlights: 3-4

            'Sala Jantar' : {
                'oeste' : 'Entrada',
                'sul' : 'Jardim",
                'item' : 'garrafa'
            },
    

\--- /code \---

\--- /task \---

\--- task \---

Adiciona este código para o jogador ganhar o jogo quando chegar ao jardim com a chave e a garrafa de poçāo:

## \--- code \---

language: python

## line_highlights: 6-9

# o jogador perde se entrar numa divisāo com um monstro

if 'item' in divisoes\[divAtual] and 'monstro' in divisoes[divAtual\]\['item'\]: print('O monstro apanhou-te... PERDESTE!') break

# o jogador ganha se entrar no jardim com a chave e a garrafa de poçāo

if divAtual == 'Jardim' and 'chave' in inventario and 'garrafa' in inventario: print('Fugiste da casa... GANHASTE!') break

\--- /code \---

Assegura-te de que este código está indentado, em linha com o código acima dele. Este código significa que a mensagem ` Escapaste da casa... Ganhaste!` é mostrada se o jogador está na divisāo 4 (o jardim) e se a chave e a garrafa de poçāo estiverem no inventário.

No código acima, se tiveres mais de quatro divisões, podes ter de usar um número diferente para o teu jardim.

\--- /task \---

\--- task \---

Testa o teu jogo para ter a certeza de que o jogador pode ganhar!

![captura de ecrã](images/rpg-win-test.png)

\--- /task \---

\--- task \---

Finalmente, vamos adicionar algumas instruções ao teu jogo, para que o jogador saiba o que tem de fazer. Edita a funçāo `mostraInstrucoes()` para incluir mais informaçāo.

## \--- code \---

language: python

## line_highlights: 7-8

def mostraInstrucoes(): #imprime um menu principal e os comandos print('''

# Jogo RPG

Chega ao jardim com uma chave e uma garrafa de poçāo Evita os monstros!

Comandos: vai [direçāo] apanha [item] ''')

\--- /code \---

Vais precisar de instruções para dizer ao jogador quais os itens que precisa de apanhar, e quais precisa de evitar!

\--- /task \---

\--- task \---

Testa o teu jogo e deves ver as tuas novas instruções.

![captura de ecrã](images/rpg-instructions-test.png)

\--- /task \---