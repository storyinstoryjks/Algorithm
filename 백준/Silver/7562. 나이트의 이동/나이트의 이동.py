# 7562 : Move to Night

import sys
from collections import deque
input=sys.stdin.readline

def bfs(i,j):
    q=deque([[i,j]])
    while q:
        x,y=q.popleft()
        if x==targetIdxX and y==targetIdxY:
            return graph[targetIdxX][targetIdxY]
        for idx in range(8):
            nx=x+dx[idx]
            ny=y+dy[idx]
            if 0<=nx<n and 0<=ny<n:
                if not graph[nx][ny]:
                    q.append([nx,ny])
                    graph[nx][ny]=graph[x][y]+1

dx=[-2,-1,1,2,-2,-1,1,2]
dy=[-1,-2,-2,-1,1,2,2,1]

for _ in range(int(input())):
    n=int(input())
    graph=[[0]*n for _ in range(n)]
    curIdxX,curIdxY=map(int,input().split())
    targetIdxX,targetIdxY=map(int,input().split())
    
    print(bfs(curIdxX,curIdxY))
    