# Puyo Puyo
# https://www.acmicpc.net/problem/11559

import sys
from collections import deque
input=sys.stdin.readline

def bfs(sx,sy,color):
    global n,m
    q=deque([(sx,sy)])
    visited[sx][sy]=1
    idx_list=[(sx,sy)]
    
    while q:
        x,y=q.popleft()
        for dx,dy in [(-1,0),(1,0),(0,-1),(0,1)]:
            nx=x+dx; ny=y+dy
            if 0<=nx<n and 0<=ny<m:
                if graph[nx][ny]==color and visited[nx][ny]==0:
                    visited[nx][ny]=1
                    q.append((nx,ny))
                    idx_list.append((nx,ny))
    
    return [] if len(idx_list)<4 else idx_list
    
def remove_color(l):
    for i,j in l:
        graph[i][j]='.'

def move_color():
    global n,m
    for col in range(m):
        gap=0
        for row in range(n-1,-1,-1):
            if graph[row][col]=='.':
                gap+=1
            elif gap>0:
                graph[row+gap][col]=graph[row][col]
                graph[row][col]='.'
    
n,m=12,6
graph=[[*input()[:-1]] for _ in range(n)]
ans=0

while True:
    visited=[[0]*m for _ in range(n)]
    flag=False
    for i in range(n):
        for j in range(m):
            if graph[i][j]!='.' and visited[i][j]==0:
                remove_idx_list=bfs(i,j,graph[i][j])
                if remove_idx_list:
                    flag=True
                    remove_color(remove_idx_list)
    if not flag:
        break
    move_color()
    ans+=1

print(ans)