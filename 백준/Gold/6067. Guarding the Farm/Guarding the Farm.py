# https://www.acmicpc.net/problem/6067
# Guarding the Farm
# 그래프탐색, bfs

input=__import__('sys').stdin.readline
deque=__import__('collections').deque

def bfs(sx,sy):
    q=deque([(sx,sy)])
    visited[sx][sy]=1
    flag=True
    
    while q:
        x,y=q.popleft()
        for k in range(8):
            nx,ny=x+dx[k],y+dy[k]
            if 0<=nx<n and 0<=ny<m:
                if board[nx][ny]>board[x][y]:
                    flag=False
                if board[nx][ny]==board[x][y] and not visited[nx][ny]:
                    visited[nx][ny]=1
                    q.append((nx,ny))

    return flag
                    

n,m=map(int,input().split())
board=[[*map(int,input().split())] for _ in range(n)]
visited=[[0]*m for _ in range(n)]
dx=[0,0,-1,1,1,1,-1,-1]
dy=[-1,1,0,0,-1,1,-1,1]
answer=0

for i in range(n):
    for j in range(m):
        if board[i][j]>0 and not visited[i][j]:
            answer+=bfs(i,j)

print(answer)