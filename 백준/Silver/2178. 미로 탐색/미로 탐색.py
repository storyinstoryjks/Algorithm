# 2178 : Maze Searching
import sys
input=sys.stdin.readline

def bfs(x,y):
    q=[[x,y]]
    while q:
        e=q.pop(0)
        x,y=e
        visited[x][y]=1
        for i in range(4):
            nx=x+dx[i]
            ny=y+dy[i]
            if 0<=nx<n and 0<=ny<m:
                if not visited[nx][ny] and [nx,ny] not in q and graph[nx][ny]=='1':
                    q.append([nx,ny])
                    path[nx][ny]=path[x][y]+1
                        
        
n,m=map(int,input().split())
graph=[input() for _ in range(n)]
visited=[[0]*m for _ in range(n)]
path=[[-1]*m for _ in range(n)]
path[0][0]=1
dx=[-1,1,0,0]
dy=[0,0,-1,1]

bfs(0,0)

print(path[n-1][m-1])