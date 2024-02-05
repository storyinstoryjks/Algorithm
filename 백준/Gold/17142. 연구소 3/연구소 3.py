# lab 3
# https://www.acmicpc.net/problem/17142

import sys,copy
from collections import deque
from itertools import combinations
input=sys.stdin.readline

def bfs(active_birus):
    global n,m,wall_cnt
    q=deque([])
    visited=[[0]*n for _ in range(n)]
    time,change_cnt=0,0
    
    for i,j in active_birus:
        q.append((i,j))
        graph[i][j]=3
        
    while q:
        x,y=q.popleft()
        for dx,dy in [(-1,0),(1,0),(0,-1),(0,1)]:
            nx=x+dx; ny=y+dy
            if 0<=nx<n and 0<=ny<n:
                if graph[nx][ny]==0 and visited[nx][ny]==0:
                    visited[nx][ny]=visited[x][y]+1
                    change_cnt+=1
                    time=max(time,visited[nx][ny])
                    q.append((nx,ny))
                if graph[nx][ny]==2 and visited[nx][ny]==0:
                    visited[nx][ny]=visited[x][y]+1
                    q.append((nx,ny))
                    graph[nx][ny]=3

    return time,n*n-wall_cnt-len(birus)-change_cnt
        
    
n,m=map(int,input().split())
birus,arr=[],[]
ans,wall_cnt=3000,0

for i in range(n):
    l=[*map(int,input().split())]
    for j in range(n):
        if l[j]==2:
            birus.append((i,j))
        if l[j]==1:
            wall_cnt+=1
    arr.append(l)


for active_birus in combinations(birus,m):
    graph=copy.deepcopy(arr)
    time,empty_cnt=bfs(active_birus)
    if empty_cnt==0:
        ans=min(ans,time)
    
print(ans if ans!=3000 else -1)