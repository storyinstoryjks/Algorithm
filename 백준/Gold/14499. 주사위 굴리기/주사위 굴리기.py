"""
난이도: 보통
시간: 40분

[요구사항 파악]
핵심: "주사위를 어떻게 저장해나갈 것인가?"

우선, 동서북남 방향에 따라, 주사위 전개도가 어떻게 달라지는지 살펴보았다.
문제설명에 나와있는 주사위 전개도를 이용하였다.
<동쪽 한칸 이동>
  2       2
4 1 3   6 4 1
  5       5
  6       3
(초기)   (이동후)
=> 여기서, 2와5는 '위치가 바뀌지 않는다.'

<서쪽 한칸 이동>
  2       2
4 1 3   1 3 6
  5       5
  6       4
(초기)   (이동후)
=> 여기서, 동쪽 이동했을 때와 같이, 2와 5는 위치가 바뀌지 않는다.
=> 즉, 초기 상태에서 (4,1,3)과 (6) 사이에서만 위치가 변한다는 사실을 알 수 있다.

(발견)
여기서, 나는 다음과 같은 특징을 찾아내었다.
   '(4,1,3)그룹에서 동/서 방향에 따라, 마지막/첫 원소가 pop되고, 그 반대 위치에 (6)그룹의 6이 들어온다.
    
구체적으로 보자.
동쪽 이동시에는 (4,1,3)에서 3이 빠져 (4,1,빠짐)이 남는다.
이후, 4는 (6)그룹의 6과 교환되고, 6은 4가 빠진 '마지막 자리의 반대위치인 첫 위치에 6이 들어오기에' (6,4,1)이 된다.

서쪽 이동시에는 동쪽과 반대로 진행하면 된다.

그러므로, 여기서 필자는 가로그룹 (4,1,3) + 세로그룹(2,1,5,6)으로 나누자는 생각을 하게 되었고,
첫위치 / 마지막위치에서 'pop / 삽입 연산이 이루어지므로', deque 자료구조를 사용하자는 결론을 내렸다.

그렇다면, 북쪽과 남쪽은 어떨까?
<북쪽>
  2       1
4 1 3   4 5 3
  5       6
  6       2
(초기)   (이동후)

<남쪽>
  2       6
4 1 3   4 2 3
  5       1
  6       5
(초기)   (이동후)

=> 여기서는 4와 3은 고정되고, '세로그룹만 위로 또는 아래로 1칸씩 밀어지거나, 땡겨진다'
=> Deque에 더 적합!

그러므로, 다음과 같은 자료구조를 결정하게 되었다.
=> 주사위 전개도 : 주사위_가로_그룹 / 주사위_세로_그룹 / 모두 deque 자료구조 사용.
=> 전개도 위치 연산 : 동서남북 방향에 따른 pop/popleft/append/appendleft 연산 사용.

[알고리즘 설계]
1. 현재 x,y 위치 검사 및 갱신.
2. 주사위 전개도 변경하기.
3. 바닥과 주사위의 숫자 연산 처리. (여기서, 주사위가 바닥과 붙는 면은 주사위_세로_그룹의 마지막 원소로 고정.)
4. 답 출력.
"""

# Dice Mage

from sys import stdin
from collections import deque
scan=lambda:map(int,stdin.readline().split())

def check_floor():
    board_target=board[x][y]
    dice_target=dice_h[-1]
    if board_target==0:
        board[x][y]=dice_target
    else:
        dice_h[-1]=board_target
        board[x][y]=0
    
def change_dice(flag):
    # 동쪽 또는 서쪽
    if flag==1 or flag==2:
        # 동쪽인 경우는 가로그룹의 마지막원소, 서쪽인 경우는 가로그룹의 첫번째원소
        dice_w_target=dice_w.pop() if flag==1 else dice_w.popleft()
        # 동쪽 서쪽 모두 세로그룹은 마지막 원소(주사위 바닥면)
        dice_h_target=dice_h.pop()
        dice_h.append(dice_w_target)
        # 요구사항 파악과 같이 삽입 처리 진행.
        dice_w.appendleft(dice_h_target) if flag==1 else dice_w.append(dice_h_target)
        # 세로그룹과 가로그룹 모두 윗면을 중복으로 가지고 있음.
        # 그러나, 세로그룹은 윗면 갱신처리가 안되있음.(이유: 위 요구사항 파악시, 2와5가 안바뀐다? 윗면도 안바뀜)
        # 그러므로, 가로그룹의 갱신된 윗면을 그대로 복사하기.
        dice_h[1]=dice_w[1]
    elif flag==3: # N
        dice_h.append(dice_h.popleft())
        dice_w[1]=dice_h[1]
    else:
        dice_h.appendleft(dice_h.pop())
        dice_w[1]=dice_h[1]

n,m,x,y,k=scan()
board=[[*scan()] for _ in range(n)]
k_cmd=[*scan()]
dice_w=deque([0,0,0]) # 주사위_가로_그룹
dice_h=deque([0,0,0,0]) # 주사위_세로_그룹
drt=[(),(0,1),(0,-1),(-1,0),(1,0)] # E,W,N,S

for cmd in k_cmd:
    # x,y 검사
    dx,dy=x+drt[cmd][0],y+drt[cmd][1]
    if 0<=dx<n and 0<=dy<m:
        x,y=dx,dy # x,y 갱신
        change_dice(cmd) # 주사위 전개도 체크
        check_floor() # 바닥면 숫자 체크
        print(dice_h[1]) # 답 출력