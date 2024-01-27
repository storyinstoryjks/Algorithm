# 2583
import sys
sys.setrecursionlimit(10**6)
input=sys.stdin.readline

def dfs(x,y,count):
    visited[x][y]=1
    for idx in range(4):
        nx=x+dx[idx]
        ny=y+dy[idx]
        if 0<=nx<m and 0<=ny<n:
            if not visited[nx][ny] and not graph[nx][ny]:
                count=dfs(nx,ny,count+1)
    return count

m,n,k=map(int,input().split())
graph=[[0]*n for _ in range(m)]
visited=[[0]*n for _ in range(m)]
dx=[-1,1,0,0]
dy=[0,0,-1,1]
cnt=[]

for _ in range(k):
    x1,y1,x2,y2=map(int,input().split())
    for i in range(y1,y2):
        for j in range(x1,x2):
            if not graph[i][j]:
                graph[i][j]=1

for i in range(m):
    for j in range(n):
        if not visited[i][j] and not graph[i][j]:
            cnt.append(dfs(i,j,1))
            
cnt.sort()
print(len(cnt))
print(' '.join(map(str,cnt)))