# https://www.acmicpc.net/problem/13565
# 침투
# 그래프 탐색, dfs, bfs

input=__import__('sys').stdin.readline
import sys
sys.setrecursionlimit(10**7)

def dfs(x,y):
    global answer
    
    if x==n-1:
        answer="YES"
        return
    
    for dx,dy in [(1,0),(0,-1),(0,1),(1,0)]:
        nx,ny=x+dx,y+dy
        if 0<=nx<n and 0<=ny<m:
            if board[nx][ny]=='0' and not visited[nx][ny]:
                visited[nx][ny]=1
                dfs(nx,ny)

n,m=map(int,input().split())
board=[[*input()][:-1] for _ in range(n)]
answer="NO"

visited=[[0]*m for _ in range(n)]
for j in range(m):
    if not visited[0][j]:
        visited[0][j]=1
        dfs(0,j)
        if answer=='YES':
            break

print(answer)