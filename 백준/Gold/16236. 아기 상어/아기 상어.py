# 16236 : Baby Shark
"""
시간이 많이 걸린 문제.
핵심 조건인 '먹을 수 있는 물고기 1마리 이상...'을 어떻게 구현할 것인가가 중요.

[정답 카운팅 방법]
1초에 한칸 이동 = 타겟 물고기까지 1초씩 이동한다. = 타겟 물고기까지의 거리

그러므로, 엄마상어를 호출할때까지 잡아먹는 각 물고기까지의 거리를 더하면 된다.

[제약조건]
1. 물고기 크기와 동일하거나, 이상일때 이동 가능.
2. 가장 가까운 거리의 물고기를 먹는다. (중요)
3. 후보 물고기가 여러 마리라면, 위 > 왼쪽 순서로 이동한다. (중요중요)

[제약분석]
<1. 물고기 크기와 동일하거나, 이상일때 이동가능.>
=> 먹은 개수를 카운팅하며, 아기상어의 크기를 갱신한다.
=> 후보 물고기를 찾을 때, 이 크기를 조건문으로 이용한다.

<2. 가장 가까운 거리의 물고기를 먹는다.>
=> 후보 노드까지의 이동 경로는 최단 경로여야 한다.
=> 그래프 탐색에서 항상 최단 경로를 보장하는 것은 레벨 순회의 성격을 지닌 BFS이다.
=> '현재 아기 상어 위치'를 기준으로 'BFS'를 통해 '각 물고기까지의 거리를 파악'해야한다.

<3. 후보 물고기가 여러 마리라면, 위>왼쭉 우선순위>
=> 현재 아기상어 위치에서 각 물고기까지의 거리를 저장하는 리스트를 visited라 가칭한다.
=> 리스트는 행과 열을 가진다. 리스트의 탐색 순서를 생각해보자.
=> n행을 기준으로 m열을 '오름차순으로 탐색'한다.
=> 즉, 위=행, 왼쪽=열이므로, 'visited를 0행0열부터 탐색하면서 조건에 맞는 물고기를 발견하면, 바로 먹으러 가면 된다.'
=> 이중 for문을 통해 visited를 탐색하는 것은 이 조건을 자연스럽게 내포한다.

[알고리즘]
1. 현재 아기 상어 위치를 기준으로 각 물고기까지의 거리를 계산하여 visited에 저장 및 반환. 방법은 BFS. (ADT(func) : checkDistance)
2. visited를 활용하여, 후보 물고기를 찾는다. 이중for문을 통해 visited를 탐색. (ADT : findCandidate)
2-1. 후보 물고기를 못찾는다는 것은 '먹을 수 있는 물고기가 없다는 것'. false 반환.
2-2. 후보 물고기를 찾았다면, 해당 후보 물고기의 x,y,거리를 반환.
3-1. false라면, 정답 출력.
3-2. 해당 후보 물고기 먹음 처리 + 거리 정답 누적 진행. 아기 상어 위치 갱신
3-3. 아기 상어 크기 체크.
4. 1~3 반복. (더 이상 못먹을때까지 진행되는 것이기 때문)
"""

import sys
from collections import deque
input=sys.stdin.readline

# 물고기 거리 계산 함수
def checkDistance():
    q=deque([(cur_x,cur_y)])
    visited=[[0]*n for _ in range(n)]
    
    while q:
        x,y=q.popleft()
        for i in range(4):
            nx=x+dx[i]
            ny=y+dy[i]
            if 0<=nx<n and 0<=ny<n:
                # 아기상어크기>=물고기크기 and 방문하지 않은 공간이라면
                if sharkSize>=graph[nx][ny] and visited[nx][ny]==0:
                    q.append((nx,ny))
                    # 방문할 곳까지 가는 루트 수를 저장. (이전 루트+1)
                    visited[nx][ny]=visited[x][y]+1 
    return visited

# 먹을 후보 물고기 찾는 함수
def findCandidate(visited):
    cand_x,cand_y=0,0 # 후보 물고기 좌표
    min_dist=INF # 후보 물고기까지의 거리
    
    # 각 물고기까지의 거리 탐색 시작(반복 순서 자체가 위>아래 성격 가짐.)
    for i in range(n):
        for j in range(n):
            # 거리가 0이라는 것은 해당 좌표를 거치지 않았다는 것 + 물고기 크기 체크(0빈칸체크<=타겟물고기<아기상어크기)
            if visited[i][j]!=0 and 1<=graph[i][j]<sharkSize:
                # 최단 경로 갱신, 후보 물고기 좌표 갱신
                if visited[i][j]<min_dist:
                    cand_x,cand_y=i,j
                    min_dist=visited[i][j]

    # 갱신 안되면 후보 물고기 못찾은 것.
    if min_dist==INF:
        return False
    else:
        return cand_x,cand_y,min_dist

n=int(input())
dx,dy=[-1,1,0,0],[0,0,-1,1]
cur_x,cur_y=0,0 # 아기 상어 현재 위치.
graph=[] # 공간
ans,sharkSize,foodCnt=0,2,0 # 정답,아기상어크기,물고기먹은개수
INF=1e9

# 공간 입력 받기 및 아기 상어 초기 위치 찾기.
for i in range(n):
    l=[*map(int,input().split())]
    for j in range(n):
        if l[j]==9:
            cur_x,cur_y=i,j
            l[j]=0 # 상어 크기가 9보다 커질 수 있기때문에.
    graph.append(l)


# 4번 (Main Logic)
while True:
    # 1번 진행 후, 2번 진행.
    result=findCandidate(checkDistance())
    
    # 2-1번에 해당된다면, 3-1 진행.
    if result==False:
        print(ans); break
    # 2-2번에 해당된다면, 3-2진행
    else:
        cur_x,cur_y=result[0],result[1] # 아기 상어 후보 물고기 좌표로 갱신.
        ans+=result[2] # 정답 카운팅(누적)
        graph[cur_x][cur_y]=0 # 후보 물고기 먹음 처리.
        foodCnt+=1 # 먹은 물고기 개수 누적.
    
    # 3-3 진행
    if foodCnt>=sharkSize:
        sharkSize+=1
        foodCnt=0