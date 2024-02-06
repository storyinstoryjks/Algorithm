# Easy Shortest-distance
# https://www.acmicpc.net/problem/14940

import sys
from collections import deque
input=sys.stdin.readline

def bfs(n,m,sx,sy):
    q=deque([(sx,sy)])
    
    while q:
        x,y=q.popleft()
        for dx,dy in [(-1,0),(1,0),(0,-1),(0,1)]:
            nx=x+dx; ny=y+dy;
            if 0<=nx<n and 0<=ny<m:
                if graph[nx][ny]==1 and visited[nx][ny]==0:
                    visited[nx][ny]=visited[x][y]+1
                    q.append((nx,ny))
    
    for i in range(n):
        for j in range(m):
            if graph[i][j]==1 and visited[i][j]==0:
                visited[i][j]=-1
        print(*visited[i])

n,m=map(int,input().split())
graph,visited=[],[[0]*m for _ in range(n)]
sx,sy=0,0

for i in range(n):
    l=[*map(int,input().split())]
    for j in range(m):
        if l[j]==2:
            sx=i; sy=j
    graph.append(l)
    
bfs(n,m,sx,sy)