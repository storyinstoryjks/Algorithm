# https://www.acmicpc.net/problem/27211
# 도넛 행성
# 그래프 탐색

deque=__import__('collections').deque
input=__import__('sys').stdin.readline

def bfs(sx,sy):
    q=deque([(sx,sy)])
    visited[sx][sy]=1
    
    while q:
        x,y=q.popleft()
        for i in range(4):
            nx=(n+x+dx[i])%n
            ny=(m+y+dy[i])%m
            if board[nx][ny]==0 and visited[nx][ny]==0:
                visited[nx][ny]=1
                q.append((nx,ny))
            
            
n,m=map(int,input().split())
board=[[*map(int,input().split())] for _ in range(n)]
visited=[[0]*m for _ in range(n)]
dx,dy=[-1,1,0,0],[0,0,-1,1]
total_space=0

for i in range(n):
    for j in range(m):
        if board[i][j]==0 and visited[i][j]==0:
            bfs(i,j)
            total_space+=1

print(total_space)