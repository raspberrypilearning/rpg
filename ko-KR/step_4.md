## 획득할 아이템 추가

플레이어가 미로를 탈출하면서 획득할 수 있는 아이템을 추가해 봅시다.

\--- task \--- Adding an item into a room is easy, you can just add it to a room's dictionary. key를 hall에 한번 추가해 봅시다.

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

\--- task \--- If you run your game after adding the code above, you can now see a key in the hall, and you can even pick it up (by typing `get key`) which adds it to your inventory!

![스크린샷](images/rpg-key-test.png) \--- /task \---