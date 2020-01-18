## 새로운 방 추가하기

\--- task \--- 파이썬 스타터 프로젝트를 엽니다.

**온라인** : [ rpf.io/rpgon ](http://rpf.io/rpgon) {: target = "_ blank"}에서 스타터 프로젝트 열기.

**오프라인** : [스타터 프로젝트](http://rpf.io/p/en/rpg-go){:target="_blank"} 를 오프라인 에디터에서 여세요. \--- /task \---

\--- task \--- 아주 간단한 RPG 게임으로 방이 2개밖에 없습니다. 아래 게임 맵을 참고해주세요:

![screenshot](images/rpg-map1.png)

`go south` 명령어를 입력하여 hall에서 kitchen으로 이동할 수 있고, `go north` 명령어를 입력하여 다시 hall로 이동할 수 있습니다.

![스크린샷](images/rpg-controls.png) \--- /task \---

\--- task \--- 만약 없는 방으로 가고자 한다면 어떻게 될까요? `go west`를 입력하면 친절한 에러 메시지를 출력하는 것을 볼 수 있습니다.

![스크린샷](images/rpg-error.png) \--- /task \---

\--- task \--- `rooms` 변수를 보면, 여러 개의 방 정보가 딕셔너리 형태로 입력되어 있음을 알 수 있습니다:

## \--- code \---

## language: python

# room 딕셔너리

rooms = {

            'Hall' : {
                'south' : 'Kitchen'
            },
    
            'Kitchen' : {
                'north' : 'Hall'
            }
    
        }
    

\--- /code \---

각 방은 딕셔너리 형태로 되어 있으며 방향에 따라 서로 연결되어 있습니다.   
\--- /task \---

\--- task \--- 지도 상에서 dining room을 hall의 동쪽에 추가해 봅시다.

![스크린샷](images/rpg-dining.png)

여러분은 3번째 방인 `dining room`을 추가해야 합니다. 그리고 이 dining room을 hall(서쪽으로) 과 연결해야 합니다. hall에도 dining room을 동쪽에 링크하여 플레이어가 hall에서 동쪽으로 이동 시 dining room으로 갈 수 있도록 한다.

**새로운 코드를 작성하기 전에 콤마를 추가하는 것을 절대 잊지 마세요.**

## \--- code \---

language: python

## line_highlights: 5-6,11-15

# room 딕셔너리

rooms = {

            'Hall' : {
                'south' : 'Kitchen',
                'east' : 'Dining Room'
            },
    
            'Kitchen' : {
                'north' : 'Hall'
            },
    
            'Dining Room' : {
                'west' : 'Hall'
            }
    
        }
    

\--- /code \--- \--- /task \---

\--- task \--- dining room을 추가한 게임을 플레이 해보세요:

![스크린샷](images/rpg-dining-test.png)

만약 dining room으로 들어가거나 나갈 수 없다면, 추가한 코드를 다시 한번 살펴보세요(','와 같은 요소들도 잘 확인해보세요). \--- /task \---