from sys import stdin
from collections import deque
input=stdin.readline

def bfs(sx,sy):
    cnt=0
    q=deque([(sx,sy)])
    visited[sx][sy]=1
    
    while q:
        x,y=q.popleft()
        if campus[x][y]=='P':
            cnt+=1
        for i in range(4):
            nx,ny=x+dx[i],y+dy[i]
            if 0<=nx<n and 0<=ny<m:
                if campus[nx][ny]!='X' and visited[nx][ny]==0:
                    visited[nx][ny]=1
                    q.append((nx,ny))
    
    return cnt
            
dx=[-1,1,0,0]
dy=[0,0,-1,1]
n,m=map(int,input().split())
visited=[[0]*m for _ in range(n)]
campus=[]
posX,posY=0,0
for i in range(n):
    l=[*input()[:-1]]
    for j in range(m):
        if l[j]=='I':
            posX,posY=i,j
    campus.append(l)

print(bfs(posX,posY) or 'TT')