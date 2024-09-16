from collections import deque

def bfs(n,m,maps,visited):
    dx=[-1,1,0,0]
    dy=[0,0,-1,1]
    q=deque([(0,0)])
    visited[0][0]=1
    
    while q:
        x,y=q.popleft()
        for i in range(4):
            nx=x+dx[i]
            ny=y+dy[i]
            if 0<=nx<n and 0<=ny<m:
                if maps[nx][ny]==1 and visited[nx][ny]==0:
                    visited[nx][ny]=visited[x][y]+1
                    q.append((nx,ny))
    
    return visited[n-1][m-1]

def solution(maps):
    n,m=len(maps),len(maps[0])
    visited=[[0]*m for _ in range(n)]
    return bfs(n,m,maps,visited) or -1