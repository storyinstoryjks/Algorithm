# Castle Defence
# https://www.acmicpc.net/problem/17135
"""
문제에 주어진 조건을 순서대로 처리하면 되는 문제이다.(구현 문제)
탐색 시, 주어진 조건을 자연스럽게 녹여내는것이 핵심인 것 같다.

1. 조합을 통해 궁수의 위치를 순회한다.
    => 궁수의 위치마다 새로 게임이 시작됨.
    => 초기 graph를 게임에 쓰기 위해 for문 안에 가져와야됨.
    => 깊은 복사 필요.
2. 각 궁수의 위치에서 적을 탐색한다.
    => 이중 for문을 통해도 가능하지만, 가장 가까운 적의 탐색은 BFS가 효율적.
    => 그런 적이 여러명일 경우 왼쪽이므로, BFS 탐색 순서를 '좌->상->우'로 설정.
        (왼쪽부터 탐색을 시작하여, 해당 적일시 바로 해당 적 좌표를 리턴하면 된다.)
        (그럼, 상 및 우 방향의 적들은 탐색을 안하기 때문이다.)
    => 중복 좌표가 들어올 수 있으므로, set에 저장.
3. 탐색된 적 위치들을 순회하여, 적 제거 실시.
4. 적 제거 수 갱신
5. 현재 남은 적 수 갱신
    => 다음 시간에 성에 도착하는 적들 수를 제거해야 한다.
    => 한 게임의 시뮬레이션을 위해 while이 사용되고, cur_enemy를 통해 시뮬레이션 동안 적 파악 진행.
    => 즉, 초기 enemy 파악 시, n-1행의 적들도 파악한 것.
    => 그러므로, cur_enemy 갱신시, n-1행의 남은 적들도 빼줘야함.
        (graph값 갱신은 상관없음. n-2행을 n-1행에 덮어쓰기 하기 때문.)
6. 게임 종료시(한 궁수 좌표 시뮬레이션 종료시), 최대 적수(ans) 갱신.

"""
import sys,copy
from collections import deque
from itertools import combinations
input=sys.stdin.readline

# 타겟 적 찾기 함수
def bfs(col):
    global n,m,d
    q=deque([(n-1,col)])
    
    while q:
        x,y=q.popleft()
        # 맨허튼 거리 계산: 궁수위치-적위치
        if abs(n-x)+abs(col-y)>d:
            return 0
        # 사정거리 안 적인 경우
        if graph[x][y]==1:
            return (x,y)
        # 좌->상->우 방향으로 다음 적 탐색
        for dx,dy in [(0,-1),(-1,0),(0,1)]:
            nx=x+dx; ny=y+dy
            if 0<=nx<n and 0<=ny<m:
                q.append((nx,ny))

# 다음에 성에 도착하는 적 개수 카운팅 함수
def del_enemy():
    global n,m
    cnt=0
    for i in range(m):
        if graph[n-1][i]==1:
            cnt+=1
    return cnt

# 남아있는 적들 아래로 1칸 이동하는 함수
def move_enemy():
    global n,m
    for j in range(m):
        for i in range(n-2,-1,-1):
            graph[i+1][j]=graph[i][j]
    for j in range(m):
        graph[0][j]=0
    
n,m,d=map(int,input().split())
arr=[]
ans,enemy=0,0 # 답, 초기 적 개수

for i in range(n):
    l=[*map(int,input().split())]
    for j in range(m):
        if l[j]==1:
            enemy+=1
    arr.append(l)

# 가능한 궁수 위치 후보들 순회 
# 좌표(1,2,4) ==> n행의 1열, 2열, 4열
for archer in combinations([i for i in range(m)],3):
    graph=copy.deepcopy(arr) # 깊은 복사
    kill_cnt=0 # 해당 게임에서 죽인 적 개수
    cur_enemy=enemy # 현재(남은) 적 개수
    # 남은 적 개수가 0이 될때까지 반복.
    while cur_enemy>0:
        kill_list=set() # 타겟 적들의 좌표 리스트(중복제거)
        # 각 궁수 위치 시작 정점으로 탐색.
        for i in archer:
            enemy_idx=bfs(i) # 궁수가 발견한 적의 좌표.
            if enemy_idx:
                kill_list.add(enemy_idx)
        
        # 타겟 적들 제거 작업
        for i,j in kill_list:
            graph[i][j]=0
        
        # 갱신 작업
        kill_cnt+=len(kill_list) # 제거한 적들 개수만큼 죽인 적 개수 더하기
        cur_enemy-=len(kill_list) # 남아있는 적 개수 갱신(죽인 적 개수 빼기)
        cur_enemy-=del_enemy() # 남아있는 적 개수 갱신(다음에 성 도착할 적 개수)
        move_enemy() # 남아있는 모든 적들 아래로 한칸 이동.
        
    ans=max(ans,kill_cnt)
    
print(ans)