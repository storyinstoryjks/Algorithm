# https://www.acmicpc.net/problem/23352
# 방탈출
# 그래프 탐색, 브루트포스 

deque=__import__('collections').deque
input=__import__('sys').stdin.readline

def bfs(sx,sy):
    global distance,answer
    q=deque([(sx,sy)])
    visited=[[0]*m for _ in range(n)] # 방문여부 및 임의 지점 간 거리
    visited[sx][sy]=1
    
    while q:
        x,y=q.popleft()
        # 이전 거리보다 긴 경우
        if visited[x][y]-1>distance:
            distance=visited[x][y]-1
            answer=board[x][y]+board[sx][sy]
        # 가장 긴 루트가 여러 개인 경우
        if visited[x][y]-1==distance:
            answer=max(answer,board[x][y]+board[sx][sy])
        for dx,dy in [(-1,0),(1,0),(0,-1),(0,1)]:
            nx,ny=x+dx,y+dy
            if 0<=nx<n and 0<=ny<m:
                if board[nx][ny]>0 and visited[nx][ny]==0:
                    visited[nx][ny]=visited[x][y]+1
                    q.append((nx,ny))
     

n,m=map(int,input().split())
board=[[*map(int,input().split())] for _ in range(n)]

distance,answer=0,0

for i in range(n):
    for j in range(m):
        if board[i][j]>0:
            bfs(i,j)

print(answer or 0)