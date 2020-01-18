## 획득할 아이템 추가

플레이어가 미로를 탈출하면서 획득할 수 있는 아이템을 추가해 봅시다.

\--- task \--- 방에 아이템을 추가하는 것은 쉽습니다. 그냥 방의 딕셔너리에 추가하면 됩니다. key를 hall에 한번 추가해 봅시다.

새로운 아이템을 추가할 때, 사진과 같이 꼭 뒤에 콤마(',')를 삽입해 주세요. 삽입이 안되어 있으면 프로그램 실행이 되지 않습니다.

## \--- code \---

language: python

## line_highlights: 6-7

# room 딕셔너리

rooms = {

            'Hall' : {
                'south' : 'Kitchen',
                'east' : 'Dining Room',
                'item' : 'key'
            },
    
            'Kitchen' : {
                'north' : 'Hall'
            },
    
            'Dining Room' : {
                'west' : 'Hall'
            }
    
        }
    

\--- /code \---

\--- /task \---

\--- task \--- 프로그램을 실행하면 key가 hall에 있다고 뜰 것입니다. 그리고 key를 주워 인벤토리에 추가할 수도 있습니다. (`get key` 명령어 입력을 통해)

![스크린샷](images/rpg-key-test.png) \--- /task \---