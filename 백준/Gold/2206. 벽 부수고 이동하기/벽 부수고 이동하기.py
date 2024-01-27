"""
[시간 초과 알고리즘]
=> 벽 위치를 미리 파악.
=> 벽 위치 모든 경우에 대한, bfs탐색

벽 위치 파악을 위한 반복문 + 벽 위치 개수만큼 bfs탐색 반복 => 시간초과. O((n*m)**2)

[해결 알고리즘]
"한 번의 bfs탐색에서 벽을 뚫고 오는 경우 + 벽을 뚫고 오지 않는 경우를 모두 탐색"
=> 그래프의 모양을 유지하며 2가지 경우를 파악하는 그릇 필요.
=> 3차원 리스트.
=> bfs탐색을 통해 2경우를 카운팅하며 목표좌표까지 진행.
"""
# Break Wall and Move

import sys
from collections import deque
input=sys.stdin.readline

def bfs(x,y,wallFlag):
    q=deque([(x,y,wallFlag)]) # Time: list > tuple
    # wallFlag경우의 현재좌표 방문 처리.
    visited[x][y][wallFlag]=1 
    while q:
        x,y,wallFlag=q.popleft()
        if x==n-1 and y==m-1:
            return visited[x][y][wallFlag]
        for i in range(4):
            nx=x+dx[i]
            ny=y+dy[i]
            if 0<=nx<n and 0<=ny<m:
                # 벽이 아니고, wallFlag경우의 다음 좌표를 아직 방문하지 않았다면
                if graph[nx][ny]==0 and visited[nx][ny][wallFlag]==0:
                    q.append((nx,ny,wallFlag))
                    # wallFlag경우의 다음 좌표에 '최근까지의 경로를 카운팅한 값' 저장.
                    visited[nx][ny][wallFlag]=visited[x][y][wallFlag]+1
                # 벽이고, 아직 벽을 뚫지 않았다면
                if graph[nx][ny]==1 and wallFlag==1:
                    # 다음 좌표는 벽을 뚫고
                    q.append((nx,ny,0))
                    # 벽을 뚫지 않았던 바로 전까지의 경로를 카운팅.
                    visited[nx][ny][0]=visited[x][y][wallFlag]+1
    # wallFlag가 어떤 경우가 되든, while에서 리턴이 안되면 목표까지 도달 못한것.
    return -1 

n,m=map(int,input().split())
graph=[[*map(int,input()[:m])] for _ in range(n)]
visited=[[[0,0] for _  in range(m)] for _ in range(n)] # idx: (0,1) = (벽을 뚫고 오는 경우, 그렇지 않은 경우)
dx=[-1,1,0,0]
dy=[0,0,-1,1]

print(bfs(0,0,1)) # 시작 좌표는 벽이 아님.