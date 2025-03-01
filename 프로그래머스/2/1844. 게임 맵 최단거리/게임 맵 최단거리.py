from collections import deque

def solution(maps):
    n,m=len(maps),len(maps[0])
    
    q=deque([(0,0)])
    visited=[[0]*m for _ in range(n)]
    visited[0][0]=1
    
    while q:
        x,y=q.popleft()
        if (x,y)==(n-1,m-1):
            return visited[x][y]
        for dx,dy in [(0,-1),(0,1),(-1,0),(1,0)]:
            nx,ny=x+dx,y+dy
            if 0<=nx<n and 0<=ny<m:
                if maps[nx][ny]==1 and not visited[nx][ny]:
                    visited[nx][ny]=visited[x][y]+1
                    q.append((nx,ny))
    
    return -1