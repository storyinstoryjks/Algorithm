# https://www.acmicpc.net/problem/16174
# 점프왕 쩰리
# 그래프탐색, dp

input=__import__('sys').stdin.readline

def dfs(x,y):
    visited[x][y]=1
    
    for dx,dy in [(0,1),(1,0)]:
        nx=x+dx*board[x][y]
        ny=y+dy*board[x][y]
        if 0<=nx<n and 0<=ny<n:
            if not visited[nx][ny]:
                if board[nx][ny]==-1:
                    print('HaruHaru')
                    exit(0)
                dfs(nx,ny)
    
    return False

n=int(input())
board=[[*map(int,input().split())] for _ in range(n)]
visited=[[0]*n for _ in range(n)]

if not dfs(0,0):
    print('Hing')