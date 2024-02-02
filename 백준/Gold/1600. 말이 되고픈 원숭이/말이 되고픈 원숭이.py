# Monkey
# https://www.acmicpc.net/problem/1600
"""
어떠한 문제였는지 기억이 안나지만, 이런 부류 문제를 풀어본 적이 있다.

'특정한 행동방식에 횟수가 제한되어있다.'
=> 방문처리 배열을 3차원으로 설정해야 한다.

핵심 Q) 원숭이처럼 갈때와 말처럼 갈때의 횟수 구분을 어떻게 할것인가?
예를 들어보자. (방문 배열 2차원 - 해당 좌표 방문여부 값)
- 원숭이처럼 가다가 x,y 좌표 만남.
- 원숭이->말처럼 가다가 x,y 좌표 만남.
- 원숭이->말->원숭이로 가다가 x,y 좌표 만남.
=> 2차원 배열로는 이 모든 경우를 기록할 수가 없다.

그러므로, 3차원 배열을 통해 '하나의 (x,y)좌표에서 이전까지의 경로들을 k횟수로 구분'해야 한다.
ex) visited[x][y][1] : x,y좌표 칸을 '말 행동 1번만 적용하여' 방문하였다.
ex) 말행동 1번으로 도착한 x,y좌표 칸에서 다음 원숭이 방식으로 nx,ny에 간다면?
    => visited[nx][ny]['0']=visited[x][y][1]+1
    => (해설) 다음 칸인 nx,ny는 결국 말 행동 2번을 한 것이며, 1번 움직였던 경로의 길이+1을 진행.
"""
import sys
from collections import deque
input=sys.stdin.readline

def bfs(sx,sy,k):
    global n,m
    q=deque([(sx,sy,k)])
    dxy1=[(2,1),(1,2),(-1,2),(-2,1),(-2,-1),(-1,-2),(1,-2),(2,-1)] # 말 움직임
    dxy2=[(1,0),(0,1),(-1,0),(0,-1)] # 원숭이 움직임(상하좌우)
    
    while q:
        x,y,k=q.popleft() # 좌표, 말 남은 횟수
        if x==n-1 and y==m-1:
            print(visited[x][y][k])
            return
        
        # 말 움직임 가능하면
        if k>0:
            # 말 방향 다음 칸 탐색
            for dx,dy in dxy1:
                nx=x+dx
                ny=y+dy
                if 0<=nx<n and 0<=ny<m:
                    # k-1번 말 횟수 적용한 경로의 nx,ny를 방문하지 않았으면
                    if graph[nx][ny]==0 and visited[nx][ny][k-1]==0:
                        # k-1번의 nx.ny 방문 처리
                        visited[nx][ny][k-1]=visited[x][y][k]+1
                        q.append((nx,ny,k-1))
                            
        for dx,dy in dxy2:
            nx=x+dx
            ny=y+dy
            if 0<=nx<n and 0<=ny<m:
                if graph[nx][ny]==0 and visited[nx][ny][k]==0:
                    visited[nx][ny][k]=visited[x][y][k]+1
                    q.append((nx,ny,k))

    print(-1)
                            

k=int(input())
m,n=map(int,input().split())
graph=[[*map(int,input().split())] for _ in range(n)]
# [x][y][0,1,2] : (x,y)칸까지 말[0번,1번,...,k번]
visited=[[[0]*(k+1) for _ in range(m)] for _ in range(n)] 

bfs(0,0,k)