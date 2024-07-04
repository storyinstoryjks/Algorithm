"""
난이도 : 보통
시간 : 40분

<문제 유형 파악>
메인 로직 프로세스가 문제에서 설명되있기에, 구현 유형!

<요구사항 파악>
핵심 : "나무 정보들을 어떻게 저장할 것인가"

1. 연산 작업의 핵심 사항은 무엇인가?
    => 해당 문제에서의 핵심 연산은 '봄'과 '가을'이다.
    => 봄의 프로세스 설명의 핵심 내용은 다음과 같다.
        (1) 한 칸에 여러 나무 존재 가능.
        (2) 나이가 적은 나무부터 양분을 먹인다.
    => (1)은 자료구조의 원소 길이를 나타내기에, 나무들은 리스트에 저장.
    => (2)는 연산 작업이 이루어지는 설명이다.
        즉, '리스트의 최소 원소부터 순차적으로 작업'이 이루어진다는 의미.
    그러므로, 리스트 정렬 후 양분 먹이는 작업을 진행해야 한다.

2. 어떤 방식의 정렬을 사용할 것인가? 어떤 자료구조를 사용해야 하는가?
    => 우선 최소 나이를 가지는 나무만 뽑아서 작업을 진행하면 된다.
    => 즉, '최소 나이 기준, 느슨한 정렬'이 효과적이다.
    => 그러므로, 우선순위 큐(최소힙)을 떠올렸다.
    => 그러나, 힙의 삽입/삭제연산이 이루어지고 n*O(logn) 시간의 재정렬이 진행된다.
        이는 시간초과의 가능성이 존재한다.(0.3초)
    => 그렇기에, 정말로 정렬이 필요한지 검토해봐야 한다.

* 정렬 검토
문제설명 1) 초기 입력 나무 정보들은 모두 다른 위치로 주어진다.(좌표가 다르다.)
문제설명 2) 새로운 묘목 추가시, 모두 나이가 1이다.

우선 문제설명 2번에 집중해봐야 한다.
예를 들어보자. list[r][c]=[1,1,2,4] (각 원소는 나무의 나이)
양분 상태 A[r][c]=10라고 가정해보고, 양분 작업을 진행하면, 다음과 같이 될것이다.
list[r][c][0] -> 양분 작업 -> A[r][c]=9
list[r][c][1] -> 양분 작업 -> A[r][c]=8
list[r][c][2] -> 양분 작업 -> A[r][c]=6
list[r][c][3] -> 양분 작업 -> A[r][c]=4

이후, list 상황은 다음과 같다.
list[r][c]=[2,2,3,5]

여기서, '가을'이 되면, list[r][c][3]=5이므로, 8방향에 나무가 추가된다.
그랬을 때, 왼쪽 좌표(r,c-1)의 list가 다음과 같다고 가정하자.
list[r][c-1]=[2,3,5]

"여기서, list의 앞에 새로운 나무가 추가되면, 봄 때의 연산 진행시 정렬이 필요없게 된다."

이에 대한 이유는 이 문제의 특수성에 있다.
문제설명 2번과 같이, '새로운 나무의 나이는 모두 1로 고정되기에, 중간 나이가 존재하지 않는다.'
또한, 문제설명 1번을 통해 '초기 나무들의 좌표는 모두 고유하다'
다시 말해, '초기, 한 칸에 여러 나무가 존재할 수 없다.' + '중간 나이가 존재하지 않다'라는 특수성이 존재한다.
만약, 새로운 나무의 나이가 4, 즉 중간나이가 들어올 수 있다면, 이 경우에는 무조건 우선순위 큐이지만,
현재 문제에서는 최소의 나이가 고정적으로 들어오기에 정렬을 할 필요가 없다.

즉, 리스트의 앞에 추가하면 되는 것이고, 이는 자료구조 deque를 활용할 수 있다는 의미이다.

이 정렬 검토를 바탕으로 <요구사항 파악 2번>은 다음과 같이 정리할 수 있다.
    - 정렬 방식 : 필요없음
    - 자료구조 : deque

3. 나무들을 한 deque에 저장? 좌표별 deque에 저장?
    정렬 검토에서도 살펴봤듯이, 이 문제의 특수성으로 인해 둘다 상관없다.
    어처피, 양분을 먹은 애들은 '무조건 현재나이+1'이 되기 때문이다.
    한 데큐에 저장할때의 원소를 (r,c,age) 타입으로 하면 된다.
    좌표별 데큐는 age만 저장하면 된다.

* 더 나아가기
문제설명 1번과 2번이 없어, 중간 나이가 들어올 수 있다면, 우선순위 큐가 효율적이다.
(문제 시간 기준도 1초 이상이었을 것)

<구현 알고리즘 핵심>
초기 deque의 길이만큼 popleft를 진행.
    - 양분 가능? : 작업 후 append
    - 제거 대상? : 제거 대상 리스트에 append 
"""

# 16235 : tree retech

from sys import stdin 
from collections import deque
scan=lambda:map(int,stdin.readline().split())

def spring():
    remove_trees=[]
    for i in range(n):
        for j in range(n):
            # 현재 deque의 길이만큼 조회하면서, pop연산을 진행.
            #popCnt=len(Trees[i][j])
            for _ in range(len(Trees[i][j])):
                curAge=Trees[i][j].popleft() # 최소 나이 나무
                # 제거 조건
                if curAge>A[i][j]:
                    remove_trees.append((i,j,curAge))
                # 양분 먹이기 가능
                else:
                    Trees[i][j].append(curAge+1) # 나이+1됬기에, 뒤로 이동
                    A[i][j]-=curAge # 밭 양분정보 갱신
    return remove_trees

def summer(targets):
    for r,c,age in targets:
        A[r][c]+=age//2

def fall_winter():
    # 가을
    for i in range(n):
        for j in range(n):
            for curAge in Trees[i][j]:
                if curAge%5==0:
                    for idx in range(8):
                        nr,nc=i+dx[idx],j+dy[idx]
                        if 0<=nr<n and 0<=nc<n:
                            Trees[nr][nc].appendleft(1) # 새로운 나무 추가.
            # 겨울
            A[i][j]+=Extra_A[i][j]


n,m,k=scan()
dx=[-1,-1,-1,0,0,1,1,1]
dy=[-1,0,1,-1,1,-1,0,1]
A=[[5]*n for _ in [0]*n] # 밭 배열
Extra_A=[[*scan()] for _ in [0]*n] # 추가되는 양분 배열
Trees=[[deque([]) for _ in [0]*n] for _ in [0]*n] # 나무 정보들 배열

for _ in [0]*m:
    r,c,age=scan()
    Trees[r-1][c-1].append(age)

for _ in [0]*k:
    Removes=spring() # 봄 : 제거나무 리턴
    summer(Removes) # 여름
    fall_winter() # 가을+겨울

alive_cnt=0
for i in range(n):
    for j in range(n):
        alive_cnt+=len(Trees[i][j])
print(alive_cnt)