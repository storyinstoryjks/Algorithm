# Fire
# https://www.acmicpc.net/problem/4179

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
        if (graph[x][y]=="." or graph[x][y]=="J") and visited[x][y]!=-1 and (x==0 or x==n-1 or y==0 or y==m-1):
            print(visited[x][y])
            return
        for dx,dy in [(-1,0),(1,0),(0,-1),(0,1)]:
            nx=x+dx
            ny=y+dy
            if 0<=nx<n and 0<=ny<m:
                # J
                if graph[nx][ny]=="." and visited[x][y]>=1 and visited[nx][ny]==-2:
                    visited[nx][ny]=visited[x][y]+1
                    q.append((nx,ny))
                # Fire
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
        