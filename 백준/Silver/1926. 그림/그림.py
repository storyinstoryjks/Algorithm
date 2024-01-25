# 1926 : Picture

# Fail : DFS
# Time over (recursion)
"""
import sys
input=sys.stdin.readline

def dfs(x,y):
    global ans
    visited[x][y]=1
    for i in range(4):
        nx=x+dx[i]
        ny=y+dy[i]
        if 0<=nx<n and 0<=ny<m:
            if graph[nx][ny]==1 and visited[nx][ny]==0:
                graph[nx][ny]=graph[x][y]+1
                ans=max(ans,graph[nx][ny])
                dfs(nx,ny)

n,m=map(int,input().split())
graph=[[*map(int,input().split())] for _ in range(n)]
visited=[[0 for _ in range(m)] for _ in range(n)]
dy=[-1,1,0,0]
dx=[0,0,-1,1]
cnt,ans=0,0

for i in range(n):
    for j in range(m):
        if graph[i][j]==1 and visited[i][j]==0:
            dfs(i,j)
            cnt+=1

print(cnt)
print(ans)
"""

# BFS
import sys
from collections import deque
input=sys.stdin.readline

# 그림의 넓이를 bfs 방식으로 파악
def bfs(x,y):
    each_picture=1 # 대상 그림의 넓이 저장 그릇
    q=deque()
    q.append((x,y))
    visited[x][y]=1 # (x,y)좌표 노드 방문 처리
    
    while q:
        x,y=q.popleft()
        # 상하좌우 탐색.
        for i in range(4):
            nx=x+dx[i]
            ny=y+dy[i]
            if 0<=nx<n and 0<=ny<m:
                if graph[nx][ny]==1 and visited[nx][ny]==0:
                    visited[nx][ny]=1 # 방문처리
                    q.append((nx,ny)) # 다음 탐색할 자식노드 저장.
                    each_picture+=1 # 대상 그림 넓이 +1
    
    return each_picture
    
n,m=map(int,input().split())
graph=[[*map(int,input().split())] for _ in range(n)]
visited=[[0 for _ in range(m)] for _ in range(n)]
dy=[-1,1,0,0]
dx=[0,0,-1,1]
cnt,ans=0,0

for i in range(n):
    for j in range(m):
        # 그림이고, 방문하지 않은 노드이면
        if graph[i][j]==1 and visited[i][j]==0:
            cnt+=1 # 그림 카운팅
            ans=max(ans,bfs(i,j)) # 넓이 갱신

print(cnt)
print(ans)