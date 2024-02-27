# Make to maze
# https://www.acmicpc.net/problem/2665
""" 
난이도 : 쉬움~보통
시간 : 30분

[여러 알고리즘]
공통 그래프 탐색 기법 : bfs
1. 완전탐색
2. 다익스트라
3. 0-1 bfs

[1. 완전탐색]
=> 검은방을 뚫고 오는 경우, 안뚫고 오는 경우를 모두 카운팅해야함.
1. visited[x][y][0 | 1]로 설정. (0: 검은방 안뚫고 오는 경우, 1: 검은방 뚫고 오는 경우)
2-1. 다음 칸이 검은방이면 then, visited[nx][ny][1]=min(visited[x][y][0]+1,visited[x][y][1]+1) (visited[x][y][0] 방문했다면)
2-2. 다음 칸이 흰방이면 then, visited[nx][ny][0]=min(visited[x][y][0],visited[x][y][1]) (visited[x][y][1] 방문했다면)
3. min(visited[n-1][n-1][0], visited[n-1][n-1][1])
=> 시간초과 가능성 존재.

[2. 다익스트라]
아마 대부분 이 방식으로 풀지 않았을까.. 생략

[3. 0-1 bfs]
=> 최대한 흰방으로 가면서, 검은방을 만났을 경우 카운팅 진행.
==> 제한적 dfs가 되는 것.
==> 검은방을 만나 막히면, 최근 경로의 루트노드로 돌아가, 다른 자식노드의 경로를 탐색.
=> 이를 위해, visited의 값은 검은방->흰방 바꾼 횟수를 저장.
=> 다음 칸이 흰방이면, 부모의 visited값을 그대로 가져옴.
=> 다음 칸이 검은방이면, 부모 visited값+1 저장. (검은방 횟수+1 갱신해준것.)
=> 흰방을 먼저 탐색하기때문에, 끝방 도달했다 == '최소로 방문한것.'
"""
import sys
from collections import deque
input=sys.stdin.readline

def bfs(n):
    q=deque([(0,0)])
    visited=[[-1]*n for _ in range(n)]
    visited[0][0]=0
    
    while q:
        x,y=q.popleft()
        if(x==n-1 and y==n-1):
            return visited[x][y]
        for dx,dy in [(-1,0),(1,0),(0,-1),(0,1)]:
            nx=x+dx; ny=y+dy
            if 0<=nx<n and 0<=ny<n and visited[nx][ny]==-1:
                # 다음칸이 흰방이면
                if graph[nx][ny]=='1':
                    visited[nx][ny]=visited[x][y]
                    q.appendleft((nx,ny)) # 다음칸 먼저 탐색하게끔 삽입
                # 다음칸이 검은방이면
                if graph[nx][ny]=='0':
                    visited[nx][ny]=visited[x][y]+1 # 검은방 카운팅
                    q.append((nx,ny)) # 탐색 후보를 담는 q에 삽입
    
n=int(input())
graph=[[*input()][:-1] for _ in range(n)]

print(bfs(n))