# https://www.acmicpc.net/problem/17086
# 아기 상어2

from collections import deque
input=__import__('sys').stdin.readline

def bfs(sx,sy,visited):
    global ans
    q=deque([(sx,sy,0)])
    visited[sx][sy]=1
    
    while q:
        x,y,cnt=q.popleft()
        if board[x][y]:
            ans=max(ans,cnt)
            return
        for i in range(8):
            nx,ny=x+dx[i],y+dy[i]
            if 0<=nx<n and 0<=ny<m:
                if not visited[nx][ny]:
                    visited[nx][ny]=1
                    q.append((nx,ny,cnt+1))
    
n,m=map(int,input().split())
board=[[*map(int,input().split())] for _ in range(n)]
dx,dy=[-1,1,0,0,-1,1,-1,1],[0,0,-1,1,-1,-1,1,1]
ans=-1

for i in range(n):
    for j in range(m):
        bfs(i,j,[[0]*m for _ in range(n)])

print(ans)