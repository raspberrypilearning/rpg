## 적 만들기

이 게임은 너무 쉽습니다. 이제 플레이어가 피해야만 하는 몬스터를 추가해서 조금 더 게임을 어렵게 만들어 봅시다.

\--- task \---

Adding an enemy to a room is as easy as adding any other item. Let’s add a hungry monster to the kitchen:

## \--- code \---

language: python

## line_highlights: 11-12

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
                'west' : 'Hall'
            }
    
        }
    

\--- /code \---

\--- /task \---

\--- task \---

You also want to make sure that the game ends if the player enters a room with a monster in. You can do this with the following code, which you should add to the end of the game:

## \--- code \---

language: python

## line_highlights: 6-9

        # 만약에 아이템이 없다면
        else:
            # 아이템이 없다라고 메시지 출력 
            print(move[1] + '아이템을 획득할 수 없습니다!')
    
    # 플레이어가 몬스터가 있는 방에 진입하면 게임 종료 
    if 'item' in rooms[currentRoom] and 'monster' in rooms[currentRoom]['item']:
        print('괴물에게 잡혔습니다... GAME OVER!')
        break
    

\--- /code \---

This code checks whether there is an item in the room, and if so, whether that item is a monster. Notice that this code is indented, putting it in line with the code above it. This means that the game will check for a monster every time the player moves into a new room.

\--- /task \---

\--- task \---

Test out your code by going into the kitchen, which now contains a monster.

![screenshot](images/rpg-monster-test.png)

\--- /task \---