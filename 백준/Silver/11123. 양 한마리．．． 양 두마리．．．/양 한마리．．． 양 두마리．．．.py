# https://www.acmicpc.net/problem/11123
# 양 한마리
# 그래프 탐색, dfs, bfs

import sys
input=sys.stdin.readline
sys.setrecursionlimit(10**6)

def dfs(sx,sy):
    for dx,dy in [(-1,0),(1,0),(0,1),(0,-1)]:
        nx,ny=sx+dx,sy+dy
        if 0<=nx<n and 0<=ny<m:
            if board[nx][ny]=='#' and not visited[nx][ny]:
                visited[nx][ny]=1
                dfs(nx,ny)

for _ in range(int(input())):
    n,m=map(int,input().split())
    board=[[*input()][:-1] for _ in range(n)]
    visited=[[0]*m for _ in range(n)]
    answer=0
    
    for i in range(n):
        for j in range(m):
            if board[i][j]=='#' and not visited[i][j]:
                answer+=1
                visited[i][j]=1
                dfs(i,j)
    
    print(answer)