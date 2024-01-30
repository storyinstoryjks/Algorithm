# 2589 : https://www.acmicpc.net/problem/2589
# BFS

"""
[설계]
<보물이 위치는 고정 좌표가 아니다.>
<최단경로 중, 가장 시간이 길다>

2가지 사실을 모두 갖는 바탕은?
=> "모든 좌표를 시작정점으로 BFS 탐색하여 거리 계산."
=> 이유) 시작 정점이 다르면, 해당 그래프에서의 종점까지의 거리가 다 다르기 때문.
=> 즉, 모든 좌표를 시작정점으로 BFS 탐색하면서 "최대 거리"를 갱신하면 됨.

"""
import sys
from collections import deque
input=sys.stdin.readline

def bfs(x,y):
    q=deque([(x,y)])
    visited=[[0 for _ in range(m)] for _ in range(n)] # 값: 거리(역할: 거리계산+방문처리)
    visited[x][y]=1
    max_cnt=0
    
    while q:
        x,y=q.popleft()
        for i in range(4):
            nx=x+dx[i]
            ny=y+dy[i]
            if 0<=nx<n and 0<=ny<m:
                if graph[nx][ny]=='L' and visited[nx][ny]==0:
                    q.append((nx,ny))
                    visited[nx][ny]=visited[x][y]+1
                    max_cnt=max(max_cnt,visited[nx][ny])
    
    return max_cnt-1

n,m=map(int,input().split())
graph=[[*input()[:-1]] for _ in range(n)]
dx=[-1,1,0,0]
dy=[0,0,-1,1]
cnt=0

for i in range(n):
    for j in range(m):
        if graph[i][j]=='L':
            cnt=max(cnt,bfs(i,j))

print(cnt)