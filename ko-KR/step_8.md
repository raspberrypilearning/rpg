## 게임 클리어하기

플레이어가 게임을 클리어하기 위한 미션을 부여해 봅시다.

\--- task \--- In this game, the player wins by getting to the garden and escaping the house. 물론, key와 magic potion을 소지하고 나가야 합니다. 아래 게임 맵을 참고하세요.

![스크린샷](images/rpg-final-map.png) \--- /task \---

\--- task \--- First, you need to add a garden to the south of the dining room. 꼭 두 방을 서로 링크하는 것 잊지 마세요.

## \--- code \---

language: python

## line_highlights: 16-17,18-22

# room 딕셔너리

rooms = {

            'Hall' : {
                'south' : 'Kitchen',
                'east' : 'Dining Room',
                'item' : 'key'
            },
    
            'Kitchen' : {
                'north' : 'Hall',
                'item' : 'monster'
            },
    
            'Dining Room' : {
                'west' : 'Hall',
                'south' : 'Garden'
            },
    
            'Garden' : {
                'north' : 'Dining Room'
            }
    
        }
    

\--- /code \--- \--- /task \---

\--- task \--- Add a potion to the dining room (or another room in your house).

## \--- code \---

language: python

## line_highlights: 3-4

            'Dining Room' : {
                'west' : 'Hall',
                'south' : 'Garden',
                'item' : 'potion'
            },
    

\--- /code \--- \--- /task \---

\--- task \--- Add this code to allow the player to win the game when they get to the garden with the key and the potion:

## \--- code \---

language: python

## line_highlights: 6-9

# player loses if they enter a room with a monster

if 'item' in rooms\[currentRoom] and 'monster' in rooms[currentRoom\]\['item'\]: print('A monster has got you... GAME OVER!') break

# player wins is they get to the garden with the key and potion

if currentRoom == 'Garden' and 'key' in inventory and 'potion' in inventory: print('You escaped the house... YOU WIN!') break \--- /code \---

이 코드는 들여 쓰기가 위 코드와 동일합니다. 이 코드는 플레이어가 인벤토리 내 key, potion을 소지하고 garden으로 탈출했을 때 `괴물의 집에서 탈출하셨습니다! YOU WIN!!!`을 출력하는 코드입니다.

4 개 이상의 방이 있는 경우 위의 코드에서 다른 방 번호를 사용해야 할 것입니다. \--- /task \---

\--- task \--- Test your game to make sure the player can win!

![스크린샷](images/rpg-win-test.png) \--- /task \---

\--- task \--- Finally, let’s add some instructions to your game, so that the player knows what they have to do. `showInstructions()` 함수를 수정해서 더 많은 정보를 출력하도록 합니다.

## \--- code \---

language: python

## line_highlights: 7-8

def showInstructions(): #print a main menu and the commands print('''

# RPG 게임

Get to the Garden with a key and a potion Avoid the monsters!

Commands: go [direction] get [item] ''') \--- /code \---

정보를 한국어로 어떤 아이템을 가지고 탈출해야 하는지, 무엇을 조심해야 하는지 자세히 명시해야 합니다. \--- /task \---

\--- task \--- Test your game and you should see your new instructions.

![스크린샷](images/rpg-instructions-test.png) \--- /task \---