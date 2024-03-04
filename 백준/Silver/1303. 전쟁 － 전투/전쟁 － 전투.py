# War
# https://www.acmicpc.net/problem/1303
"""
난이도 : 쉬움
시간 : 10분

[알고리즘 과정]
=> 가중치 없는 그래프
=> 자식노드들을 찾는 단순한 탐색 문제
=> DFS / BFS 중 BFS 선택

1. 방문하지 않은 좌표 기준 BFS 탐색 시작
2. 자식노드들 탐색 및 카운팅
3. 아군 / 적 판단 후, 정답 카운팅

(추가)
항상 입력 변수를 잘 보자..
row,col=m,n이다..
"""
import sys
from collections import deque
input=sys.stdin.readline

def bfs(sx,sy):
    global n,m,team,enemy
    q=deque([(sx,sy)])
    visited[sx][sy]=1
    manId,cnt=graph[sx][sy],1
    
    # 2
    while q:
        x,y=q.popleft()
        for dx,dy in [(-1,0),(1,0),(0,-1),(0,1)]:
            nx=x+dx; ny=y+dy
            if 0<=nx<n and 0<=ny<m:
                if graph[nx][ny]==manId and visited[nx][ny]==0:
                    visited[nx][ny]=1
                    q.append((nx,ny))
                    cnt+=1
    
    # 3
    if manId=='W':
        team+=(cnt*cnt)
    else:
        enemy+=(cnt*cnt)
        
m,n=map(int,input().split())
graph=[[*input()[:-1]] for  _ in range(n)]
visited=[[0]*m for _ in range(n)]
team,enemy=0,0

# 1
for i in range(n):
    for j in range(m):
        if visited[i][j]==0:
            bfs(i,j)

print(team,enemy)