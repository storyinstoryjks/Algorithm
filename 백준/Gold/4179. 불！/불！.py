# Fire
# https://www.acmicpc.net/problem/4179

"""
이번 문제는 어렵지 않게 구현하였다.

불은 여러 개 들어올 수 있고, 가장자리 벽이 없을 수도 있다.

0. 가장 빠른 시간이므로, 최소 문제이다. BFS 탐색 진행.
1. 불은 J를 덮칠 수 있으므로, J 탐색 후 Fire 탐색 진행.
2. visited에 들어갈 원소를 3개 설정.
   => (-2,미방문) (-1, 불 방문) (>0, J 방문 및 시간 저장값)
"""
import sys
from collections import deque
input=sys.stdin.readline

def bfs(j_x,j_y):
    global n,m
    q=deque([(j_x,j_y)])
    visited[j_x][j_y]=1
    for i,j in fire:
        q.append((i,j))
        visited[i][j]=-1
    
    while q:
        x,y=q.popleft()
        # J 자체가 가장자리인 경우 또는 J가 가장자리에 도달했을 경우.
        if (graph[x][y]=="." or graph[x][y]=="J") and visited[x][y]!=-1 and (x==0 or x==n-1 or y==0 or y==m-1):
            print(visited[x][y])
            return
        for dx,dy in [(-1,0),(1,0),(0,-1),(0,1)]:
            nx=x+dx
            ny=y+dy
            if 0<=nx<n and 0<=ny<m:
                # J
                # 이동 가능 칸이며, 부모노드가 J이고, 미방문 칸이면
                if graph[nx][ny]=="." and visited[x][y]>=1 and visited[nx][ny]==-2:
                    visited[nx][ny]=visited[x][y]+1
                    q.append((nx,ny))
                # Fire
                # (이동가능칸 또는 초기 J위치)이며, 부모노드가 불이고, (미방문 또는 J가 지나간 자리이면)
                if (graph[nx][ny]=="." or graph[nx][ny]=="J") and visited[x][y]==-1 and visited[nx][ny]!=-1:
                    visited[nx][ny]=-1
                    q.append((nx,ny))
    
    print("IMPOSSIBLE")

n,m=map(int,input().split())
graph=[]
j_x,j_y,fire=0,0,[]
visited=[[-2]*m for _ in range(n)] # -2: invisit, -1: fire, >1: J

for i in range(n):
    l=[*input()][:-1]
    for j in range(m):
        if l[j]=="J":
            j_x=i; j_y=j
        elif l[j]=="F":
            fire.append((i,j))
    graph.append(l)

bfs(j_x,j_y)
        