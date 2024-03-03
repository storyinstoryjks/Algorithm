# Sheep
# https://www.acmicpc.net/problem/3184

"""
난이도 : 쉬움
시간: 15분

전형적인 그래프 탐색 문제.
=> DFS든 BFS든 한번의 DFS()가 호출되고 종료된다면, 1개의 우리 탐색이 종료된 것.
=> DFS라면, DFS()의 재귀가 모두 끝마치는 무렵 양과 늑대의 개수 비교를 하면되고,
=> BFS라면, queue가 비게 되었을때, 양과 늑대 개수 체크를 하면 된다.

[알고리즘 과정]
1. (0,0)부터 양인지 늑대인지 탐색 시작.
2. 양, 늑대 둘중하나라면, 우리 탐색을 위한 BFS 시작.
3. 다음 자식노드가(다음 좌표) '.','v','o' 3개 중 하나라면, queue에 삽입.
4. 현재 탐색 좌표가 양 또는 늑대라면, 현재 우리의 양 또는 늑대 변수+1
5. queue가 비게 되면(=현재 우리 탐색 끝), 현재 우리의 양 개수 및 늑대 개수 비교하여 정답 카운팅.
6. 1번으로 돌아가 반복.(다음 1번갈 시, (0,0)기준, (0,1)부터 진행.)
"""
import sys
from collections import deque
input=sys.stdin.readline

def bfs(sx,sy):
    global sheep,wolf,r,c
    q=deque([(sx,sy)])
    visited[sx][sy]=1
    curSheep,curWolf=0,0
    
    while q:
        x,y=q.popleft()
        if graph[x][y]=='v':
            curWolf+=1
        elif graph[x][y]=='o':
            curSheep+=1
        for dx,dy in [(-1,0),(1,0),(0,-1),(0,1)]:
            nx=x+dx; ny=y+dy
            if 0<=nx<r and 0<=ny<c:
                if graph[nx][ny]!='#' and visited[nx][ny]==0:
                    visited[nx][ny]=1
                    q.append((nx,ny))
    
    if curSheep>curWolf:
        sheep+=curSheep
    else:
        wolf+=curWolf
    
r,c=map(int,input().split())
graph=[[*input()][:-1] for _ in range(r)]
visited=[[0]*c for _ in range(r)]

sheep,wolf=0,0

for i in range(r):
    for j in range(c):
        if graph[i][j] in 'ov' and visited[i][j]==0:
            bfs(i,j)

print(sheep,wolf)