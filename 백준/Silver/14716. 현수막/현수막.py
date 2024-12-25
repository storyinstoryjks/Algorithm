# https://www.acmicpc.net/problem/14716
# 현수막
# 그래프 탐색, DFS, BFS

import sys
input=sys.stdin.readline
sys.setrecursionlimit(10**8)

def dfs(sx,sy):
    for dx,dy in [(0,-1),(0,1),(-1,0),(1,0),(-1,-1),(-1,1),(1,-1),(1,1)]:
        nx=sx+dx
        ny=sy+dy
        if 0<=nx<n and 0<=ny<m:
            if board[nx][ny]==1 and visited[nx][ny]==0:
                visited[nx][ny]=1
                dfs(nx,ny)
    
n,m=map(int,input().split())
board=[[*map(int,input().split())] for _ in range(n)]
visited=[[0]*m for _ in range(n)]

cnt=0
for i in range(n):
    for j in range(m):
        if board[i][j]==1 and visited[i][j]==0:
            cnt+=1
            visited[i][j]=1
            dfs(i,j)

print(cnt)