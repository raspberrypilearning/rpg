## 적 만들기

이 게임은 너무 쉽습니다. 이제 플레이어가 피해야만 하는 몬스터를 추가해서 조금 더 게임을 어렵게 만들어 봅시다.

\--- task \--- Adding an enemy to a room is as easy as adding any other item. 배고픈 몬스터를 kitchen에 추가해 봅시다:

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
    

\--- /code \--- \--- /task \---

\--- task \--- You also want to make sure that the game ends if the player enters a room with a monster in. 아래와 같이 명령어를 추가해서 게임 오버가 되도록 설정할 수 있습니다:

## \--- code \---

language: python

## line_highlights: 6-9

        #otherwise, if the item isn't there to get
        else:
            #tell them they can't get it
            print('Can\'t get' + move[1] + '!')
    
    #player loses if they enter a room with a monster
    if 'item' in rooms[currentRoom] and 'monster' in rooms[currentRoom]['item']:
        print('A monster has got you... GAME OVER!')
        break
    

\--- /code \---

이 코드는 플레이어가 있는 방에 있는 아이템을 확인하며, 몬스터인 경우 게임을 종료하도록 합니다. 이 코드는 들여 쓰기가 위 코드와 동일합니다. 이 코드는 플레이어가 새로운 방에 들어갈 때마다 몬스터가 있는지 확인합니다. \--- /task \---

\--- task \--- Test out your code by going into the kitchen, which now contains a monster.

![스크린샷](images/rpg-monster-test.png) \--- /task \---