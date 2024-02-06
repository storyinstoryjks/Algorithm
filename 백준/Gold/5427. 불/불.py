# Fire
# https://www.acmicpc.net/problem/5427
"""
생각보다 쉽게 풀렸던 문제.
최소의 답을 구하는 문제이므로, 그래프 탐색 방식은 bfs를 이용한다.
bfs에서 다음 노드를 찾아나갈때, 문제의 조건을 잘 녹이는게 핵심이다.
조건은 다음 2가지이다.

1. 상근이는 벽,불이 있는 칸에는 갈 수 없고, '다음 시간에 불이 번지는 칸은 갈 수 없다.'
2. 불은 벽에는 번질 수 없고, '상근이의 위치에 번질 수 있다.'

2번째 조건을 이해하면, 1번과의 공통점을 찾을 수 있다.
예를 들어, [* . @] 배열을 보자
* . @ -> * @ @ -> * * @ (최종)
=> '@'를 먼저 움직인 후, '*'를 덮어씌우면, 1번 및 2번 조건을 모두 만족 시킬 수 있다.

[알고리즘]
1. 데이터 셋팅(graph, visited)
2. bfs탐색 시작
3. @가 가장자리에 도착하면 계산한 거리 반환.
    => visited의 값은 다음과 같이 설정
        0: 미방문 또는 벽, >0: 상근이 이동거리, -1: 불 위치
    => 가장자리는 벽 또는 빈칸일 수 있다.(문제에서 가장자리에는 벽만 준다고 하지 않았기에)
    => visited[가장자리좌표]의 값이 0이면 벽인 것이고, -1이라면 탈출자리를 불이 이미 차지한 것.
4. 다음 자식 탐색.(코드 주석)
5. bfs 함수 리턴 값에 따라 정답 출력.
"""

import sys
from collections import deque
input=sys.stdin.readline

def bfs(n,m,start,fire):
    q=deque([start])
    visited=[[0]*m for _ in range(n)]
    visited[start[0]][start[1]]=1 # 초기 상근이 위치에 값 1 설정.(탈출구에 도착한 후 빠져나가는것까지 계산하므로)
    for e in fire:
        q.append(e)
        visited[e[0]][e[1]]=-1 # 초기 불 방문처리
    
    while q:
        x,y=q.popleft()
        # 가장자리에 도착하였고, 탈출구에 상근이가 온 것이면,
        if (x==0 or x==n-1 or y==0 or y==m-1) and visited[x][y]>0:
            return visited[x][y]
        # 다음 자식 노드들 탐색(상하좌우)
        for dx,dy in [(-1,0),(1,0),(0,-1),(0,1)]:
            nx=x+dx; ny=y+dy
            if 0<=nx<n and 0<=ny<m:
                # 상근이 이동 차례이고, 다음 루트가 빈칸이며, 다음 루트가 미방문칸이면 
                if graph[x][y]=="@" and graph[nx][ny]=="." and visited[nx][ny]==0:
                    visited[nx][ny]=visited[x][y]+1
                    graph[nx][ny]="@" # 현재 루트의 대상 구별을 위해 갱신
                    q.append((nx,ny))
                # 불 이동 차례이고, '다음 루트가 벽이 아니고', (미방문이거나, 상근이가 지나간 자리라면)
                # 다음 루트가 상근이가 위치하고 있으면 '덮어 씌우면 된다.'
                # 선술한 문제조건 1,2번
                if graph[x][y]=="*" and graph[nx][ny]!="#" and visited[nx][ny]!=-1:
                    visited[nx][ny]=-1
                    graph[nx][ny]="*" # 현재 루트의 대상 구별을 위해 갱신
                    q.append((nx,ny))
    
    return False
    
    
for _ in range(int(input())):
    m,n=map(int,input().split())
    graph,start,fire=[],(),[] # 문제상황,상근이위치,초기 모든 불 위치
    for i in range(n):
        l=[*input()][:-1]
        for j in range(m):
            if l[j]=="@":
                start=(i,j)
            if l[j]=="*":
                fire.append((i,j))
        graph.append(l)
    cnt=bfs(n,m,start,fire)
    print(cnt if cnt else "IMPOSSIBLE")
    