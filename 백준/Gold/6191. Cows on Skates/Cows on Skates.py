# https://www.acmicpc.net/problem/6191
# Cows on Skates
# 그래프 탐색, BFS, DFS

input=__import__('sys').stdin.readline
deque=__import__('collections').deque

def bfs(sx,sy):
    q=deque([(sx,sy,[(sx,sy)])]) # x,y,path
    visited[sx][sy]=1
    
    while q:
        x,y,path=q.popleft()
        for dx,dy in [(1,0),(0,1),(-1,0),(0,-1)]: #하우상좌
            nx=x+dx
            ny=y+dy
            if 0<=nx<r and 0<=ny<c:
                if (nx,ny)==(r-1,c-1):
                    path.append((nx,ny))
                    return path
                if board[nx][ny]!='*' and not visited[nx][ny]:
                    visited[nx][ny]=1
                    tmp=[i for i in path]+[(nx,ny)]
                    q.append((nx,ny,tmp))


r,c=map(int,input().split())
board=[[*input()][:-1] for _ in range(r)]
visited=[[0]*c for _ in range(r)]

history=bfs(0,0)
for i,j in history:
    print(i+1,j+1)