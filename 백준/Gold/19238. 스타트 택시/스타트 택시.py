# 19238 : start taxi
# https://www.acmicpc.net/problem/19238

"""
난이도 : 보통
시간 : 50분
첫시도(pypy3) : 성공
현재 재시도 : 동일 코드.

1. 택시~승객 사이의 거리?
=> 각 '정점'~'정점'까지의 거리이므로, 그래프 탐색 필요.
=> DFS VS BFS
=> 목표정점까지 최적의 해를 보장해야하고, 각 레벨에서 최단인지 비교해야함.(최소값을 찾는다 == 최소의 레벨)
=> 그러므로, BFS 적절.
    주의점 : "최적의 해를 보장하지만, 최단거리를 보장하는 것은 아님."
    
    BFS는 동서남북방향을 모두 탐색하므로, 다음과 같은 경우의 거리 비교가 필요. (예)
    시작 -> 동 -> ... -> 목적지
    시작 -> 북 -> ... -> 목적지
    1번째 레벨에서 동/북으로 선택된 경우의 서브트리 비교가 필요하다는 것.
    
    즉, 2가지 경우로 나뉜다.
    IF 다음 노드(==다음칸)의 좌표가 미방문.
        THEN, 부모 노드(==현재칸)까지의 거리 + 1
    ELSE (== 방문처리가 된 다음 노드이면)
        THEN, min(이전 처리된 거리, 현재 부모 노드까지 거리 + 1)

2. 택시~각 승객의 최종 선택?
=> 결국, 각 택시~승객 거리의 최소 비교가 필요.
=> 현재 문제에서, m<=n*n이므로, 최대 400명의 승객이 존재할 수 있음.
=> 우선, '최소값 찾기' 시간복잡도를 비교해보자.
    - 리스트 삽입(m번) 및 정렬(m개요소) -> O(1)*(m) + O(m*log m) = O(m) + O(m*log m)
    - 최소힙 삽입(m번) 및 삭제(루트노드 삭제) -> O(log m)*(m) + O(log m) = O(log m) + O(m*log m)
=> 위의 과정이 택시의 위치가 바뀔때마다 반복!
=> 그러므로, 최소힙 선정.

3. BFS를 어떻게 적용해야할까?
=> 현재 두가지 '거리' 정보가 필요하다는 것을 알 수 있다.
    - 택시 ~ 승객 : 택시의 위치가 바뀌므로, 동적 변수
    - 승객 ~ 목적지 : 승객 및 목적지의 위치는 '변하지 않으므로, 고정 변수'
=> 즉, BFS를 먼저 쓰면 좋은 정보는 '승객~목적지'이다.
    승객의 위치에서 목적지까지 도달하지 못한다? 무조건 -1
    이런 경우는 택시 ~ 승객의 정보를 알 필요없이, 바로 답 처리.
    
이를 바탕으로, 자세한 로직 프로세스는 주석으로 처리.

TMI) 한 정점에서 한 정점까지의 거리를 모든 정점에서 알 수 있다면?
==> 데익스트라 알고리즘(모든정점~모든정점의 거리)
==> 과연 시간차이는 얼마나 날까? 나중에 해보자.
"""

from sys import stdin 
from collections import deque
import heapq
input=stdin.readline

# BFS 1 : 승객위치 ~ 목적지 위치 탐색
def find_client_goal(cX,cY,gX,gY):
    q=deque([(cX,cY)])
    visited=[[0]*n for _ in range(n)]
    visited[cX][cY]=1
    
    while q:
        x,y=q.popleft()
        if x==gX and y==gY:
            return True, visited[x][y]-1
        for i in range(4):
            nx=x+dx[i]; ny=y+dy[i]
            # 범위 내이고, 벽이 아니면
            if 0<=nx<n and 0<=ny<n and graph[nx][ny]!=1:
                # 처음 방문하는 칸이면
                if visited[nx][ny]==0:
                    visited[nx][ny]=visited[x][y]+1 # 이전 칸까지의 거리+1
                    q.append((nx,ny)) # 다른 경로의 위치와 비교하는것이 필요하므로, 다시 넣어주기
                # 처음 방문했던 칸과 다른 경로로 도착한 경우.
                else:
                    # 처음 방문했을 때의 거리 vs 현재 부모 좌표의 거리+1(==다른경로로 도착한 현재 경우)
                    visited[nx][ny]=min(visited[nx][ny],visited[x][y]+1)

    return False, -1

# BFS 2 : 택시 위치~승객 위치 탐색
def find_client_taxi(sx,sy):
    q=deque([(sx,sy)])
    heap,visited=[],[[0]*n for _ in range(n)]
    visited[sx][sy]=1
    heap_size=0
    
    while q:
        x,y=q.popleft()
        # 현재 탐색칸이 승객 위치이고(== 택시가 해당 승객위치까지 갈 수 있다면)
        # 현재 탐색 대상의 승객을 태워준적이 없다면
        if (x,y) in clientDis and clientDis[(x,y)][3]==False: # 
            heap_size+=1
            heapq.heappush(heap,(visited[x][y]-1,x,y)) # 택시~해당승객 거리, 승객좌표
        # 다음 칸 탐색은 위의 BFS 1 함수와 동일.
        for i in range(4):
            nx=x+dx[i]; ny=y+dy[i]
            if 0<=nx<n and 0<=ny<n and graph[nx][ny]!=1:
                if visited[nx][ny]==0:
                    visited[nx][ny]=visited[x][y]+1
                    q.append((nx,ny))
                else:
                    visited[nx][ny]=min(visited[nx][ny],visited[x][y]+1)
                
    return heap_size,heap
    
dx=[-1,1,0,0]
dy=[0,0,-1,1]
n,m,fuel=map(int,input().split())
graph=[[*map(int,input().split())] for _ in range(n)]
curX,curY=map(int,input().split()) # 택시 현재 좌표

curX-=1; curY-=1
clientDis={} # (key,value)=((승객좌표) : (목적지X, 목적지Y, 승객~목적지 거리, 택시 손님 후보 여부))
moveFlag=True # 루프 탈출 조건(==택시가 승객에게 갈수있는가? 또는 택시가 목적지까지 갈수있는가?)

for _ in range(m):
    clientX,clientY,goalX,goalY=map(int,input().split())
    # 각 승객~목적지까지의 길탐색
    flag,distance=find_client_goal(clientX-1,clientY-1,goalX-1,goalY-1)
    # 한 승객의 위치에서 목적지까지 갈 수 없는 경우가 있다면
    if flag==False:
        moveFlag=False # 바로 답 처리
    # 해당 승객의 목적지 좌표, 거리, 택시 손님 대상 여부(false: 태워야할 손님!, true: 이미 태워준 손님!)
    clientDis[(clientX-1,clientY-1)]=(goalX-1,goalY-1,distance,False)

if moveFlag: # 어떤 승객 한명을 목적지까지 태워다 줄 수 없다.(상황: 목적지가 모두 벽으로 둘러싸임.)
    # 총 손님 수만큼 반복
    for i in range(m):
        heap_size,heap=find_client_taxi(curX,curY) # 최소힙 원소 개수, 최소힙
        # 초기 상태이고, 택시가 손님 한명이라도 갈 수 없는 상황이면. (모두 벽으로 둘러싸인 경우.)
        if i==0 and heap_size!=m: 
            moveFlag=False
            break
        
        # 택시~승객 거리(연료소비1), 승객좌표
        taxi_client_distance,clientX,clientY=heapq.heappop(heap)
        # 해당 승객 목적지 좌표, 승객~목적지 거리(연료소비2), 택시손님후보여부(_)
        goalX,goalY,client_goal_distance,_=clientDis[(clientX,clientY)]
        
        # 택시의 총 이동거리=연료소비1+연료소비2
        total_move_distance=taxi_client_distance+client_goal_distance
        # 택시 총 예상 이동거리 > 현재 구비 연료
        # 손님에게 이동한 후, 목적지까지 가는 과정을 따로 구현하는 것이 아닌 한번에 구현 가능하기 때문.
        # 즉 연료가 부족해서, '손님에게 갈 수 없거나, 목적지까지 갈 수 없는 경우'
        if total_move_distance>fuel:
            moveFlag=False
            break
            
        curX,curY=goalX,goalY # 택시 현재 좌표 승객 목적지 좌표로 갱신
        fuel=(fuel-total_move_distance)+(2*client_goal_distance) # 현재 구비 연료 갱신
        clientDis[(clientX,clientY)]=(0,0,0,True) # 태워'줬기에' 손님후보에서 제외.(False->True)
    
print(fuel if moveFlag else -1)