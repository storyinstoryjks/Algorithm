"""
난이도: 보통
시간: 35분

[요구사항 파악]
핵심: "2차원 배열의 원소값 재조정을 어떻게 해야하는가?"

1. 어떤 유형의 알고리즘인가?
=> 상하좌우 방향으로 모든 경우의 수를 비교하여, 최대값 블록을 찾는 문제.
=> 상태 그래프를 통해, 모든 경우의 수를 노드로 표현이 가능하다.
    => root노드(초기보드상태), 자식노드(부모노드에서 상하좌우 경우의 수 4가지 상태)
=> 5번 이동했을 때의, 최대값 블록을 찾는 것 == 트리 깊이 5일때의 단말노드(상태) 비교.
=> 그러므로, DFS 또는 BFS로 상태 그래프를 탐색하는 문제이다.
=> 브루트포스(모든 경우의 수) + DFS/BFS로 정리.
=> 최적의 해를 찾는 것이 아니고, 모든 상태 노드를 점검해야하므로, 탐색기법 아무거나 사용 가능.(DFS 선택.)

2. 어떤 자료구조를 사용해야하는가?
=> 상태 그래프. 즉, 노드는 게임보드 자체를 나타낸다.(데이터필드)
=> 다시 말해, 상하좌우 각 moving연산을 진행한 후의 게임보드 자체를 저장하면 됨.
=> '자료구조의 재배열(재조정)이 키포인트임.'
=> 그러므로, 기본 자료구조인 list 사용.

3. 그렇다면, moving 연산 프로세스는?
=> 먼저, (좌/우), (상/하)로 그룹을 묶어 생각해보자.(좌우-배열의열이 바뀌는 공통점, 상하-배열의행이 바뀌는 공통점)
=> 즉, 반복문을 통한 탐색시 한 그룹의 요소들끼리 각각 반대로 탐색을 진행하면 됨.
=> (좌/우) 그룹에서, 좌 moving에 대한 경우를 생각해보자.
=> 4 by 4 게임보드 기준의 한 행만을 보자.(나머지 행들도 어처피 똑같은 연산이기 때문)

<경우>
2 2 0 0 / 2 0 2 0 / 2 0 0 2 - 1그룹
2 4 0 0 / 2 0 4 0 / 2 0 0 4 - 2그룹

[2 2 0 0] - 4 0 0 0
=> 앞 2자리씩 비교해서, 같으면 합쳐서 앞자리에 보내고, 합친 1번째 인덱스의 값은 0으로 바뀐다.
=> 그러나, 이 방식은 다음의 경우에서 문제 발생.

[2 0 2 0]
=> 앞 2자리씩 비교하면, 다음과 같은 과정을 거침. (괄호가 현재 탐색 대상을 나타냄)
    => (2) (0) 2 0 : 비교 : 2 0 2 0
    => 2 (0) (2) 0 : 비교 : 2 2 0 0
    => 2 2 (0) (0) : 비교 : 2 2 0 0
=> 만약, 초기 게임보드가 0 2 2 0 이었다면?
    => (0) (2) 2 0 : 비교 : 2 0 2 0
    => 2 (0) (2) 0 : 비교 : 2 2 0 0
    => 2 2 (0) (0) : 비교 : 2 2 0 0
    => 원래 답: 4 0 0 0
=> 즉, '앞에서부터 2개 원소씩 순차적으로 비교하는 탐색 방법'은 잘못된 설계임.
=> 그렇기에, 핵심은 다음과 같다.
    "빈칸에 맞춰 위치를 마킹하면서 비교해나가는 방식"

예시를 통해 핵심 설계를 알아보자.
    => 초기: 0 2 2 0, 마킹(cursor): 인덱스 0
    => 1번째 for문 타겟대상(괄호표시) : 0 (2) 2 0
        - board[마킹]은 board[0] -> 빈칸이므로 -> 2 0 2 0 -> 마킹=인덱스 0 유지
    => 2번째 : 2 0 (2) 0 (마킹=0)
        - 현재 타겟값은 2이고, board[마킹]=2이므로, 마킹 자리에 합친다.
        - 이후, 현재 타겟값은 0으로 바꾼다. 마킹=인덱스0+1=1
        - 4 0 (0) 0
    => 3번째 : 4 0 0 (0) (마킹=1)
        - 0과 0이므로, 옮겨지나, 출력 티는 안남.
    
    => 예시 2번째
    => 초기: 2 0 2 0, 마킹=0
    => 1번째: 2 (0) 2 0, 마킹=0
        - 현재 탐색값이 0이기에, 건너뜀
    => 2번째: 2 0 (2) 0, 마킹=0
        - 현재 타겟값 2이고, board[마킹]=2이므로, 마킹 자리에 찹친다.
        - 이후, 현재 타겟값 0으로 바꿈. 마킹+=1=1
        - 4 0 (0) 0, 마킹=1
    => 3번째 생략

그러므로, "빈칸에 맞춰 위치를 마킹하면서 비교해나가는 방식"은 다음과 같은 말로 재해석 가능.
    "첫번째 원소의 자리값을 기억해놓고, 두번째 원소를 만나면 비교하여 연산처리를 진행한다."

(우)는 for문을 반대로! (상/하)는 내부반목문이 row로! 인덱스 탐색만 바꾸기만 하면됨.
    => 프로세스는 같으므로!

[알고리즘 설계]
1. dfs 시작
2. 4가지 방향 순서대로 진행.
3. tree_depth==5일시, 이때의 게임보드 상태를 체크.
4. 답 출력.
"""

# 12100 : 2048(Easy)

from sys import stdin
import copy
input=stdin.readline


def move(flag,board):
    # Left
    if flag==0:
        for row in range(n):
            prev=0 # 마킹
            for col in range(1,n):
                if board[row][col]!=0:
                    tmp=board[row][col] # 현재 탐색값
                    board[row][col]=0 # 우선 미리 현재 탐색값 0 설정
                    
                    # 마킹 자리값이 0이라면
                    if board[row][prev]==0:
                        board[row][prev]=tmp # 현재 블록 마킹자리로 옮기기
                                             # 2번째 원소만날때까지 대기
                    # 마킹 자리값 == 현재 탐색값
                    elif board[row][prev]==tmp:
                        board[row][prev]*=2 # 마킹 자리값*2(현재 탐색값은 미리 0처리 했음)
                        prev+=1 # 현재 마킹자리는 완료했으므로, 그 다음 자리를 기억!
                    # 마킹 자리값이 0이 아니고, 현재 탐색값!=마킹 자리값이면,
                    # == 이전 블록값이 0이 아니고, 현재 블록값과 이전블록값도 다르면
                    else:
                        prev+=1 # 건너뛰기
                        board[row][prev]=tmp # 미리 0으로 바꾼 현재 탐색값 원상복귀
                        # 두줄과 상동 코드 : board[row][col]=tmp
    # Right
    elif flag==1:
        for row in range(n):
            prev=n-1
            for col in range(n-2,-1,-1):
                if board[row][col]!=0:
                    tmp=board[row][col]
                    board[row][col]=0
                    
                    if board[row][prev]==0:
                        board[row][prev]=tmp
                    elif board[row][prev]==tmp:
                        board[row][prev]*=2
                        prev-=1
                    else:
                        prev-=1
                        board[row][prev]=tmp
    # Up
    elif flag==2:
        for col in range(n):
            prev=0
            for row in range(1,n):
                if board[row][col]!=0:
                    tmp=board[row][col]
                    board[row][col]=0
                    
                    if board[prev][col]==0:
                        board[prev][col]=tmp
                    elif board[prev][col]==tmp:
                        board[prev][col]*=2
                        prev+=1
                    else:
                        prev+=1
                        board[prev][col]=tmp
    # Down
    else:
        for col in range(n):
            prev=n-1
            for row in range(n-2,-1,-1):
                if board[row][col]!=0:
                    tmp=board[row][col]
                    board[row][col]=0
                    
                    if board[prev][col]==0:
                        board[prev][col]=tmp
                    elif board[prev][col]==tmp:
                        board[prev][col]*=2
                        prev-=1
                    else:
                        prev-=1
                        board[prev][col]=tmp
    return board


def dfs(tree_depth, board):
    global ans
    # 5번 이동후, 최대값 블록 찾기
    if tree_depth==5:
        for i in range(n):
            ans=max(ans,max(board[i]))
        return
    
    # 상하좌우 무빙 연산 진행
    for flag in range(4):
        copy_board=copy.deepcopy(board) # 상태 노드
        dfs(tree_depth+1,move(flag,copy_board))
    
    
n,ans=int(input()),-1
init_board=[[*map(int,input().split())] for _ in range(n)]
dfs(0,init_board)
print(ans)