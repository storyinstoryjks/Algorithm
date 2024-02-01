# make bridge
# https://www.acmicpc.net/problem/2146
"""
핵심 질문 2가지.
1. 섬을 어떻게 구분할 것인가
2. 다리를 놓는 모든 경로 카운팅을 어떻게 할 것인가

graph의 섬에 해당되는 값을 구분하는 것으로 1번 질문 해결 가능.
=> bfs_land() 탐색을 통해 라벨링 진행.

섬을 둘러싸는 첫 바다칸들을 미리 q에 삽입해놓고,
한 좌표씩 빼서 섬까지 가는 다리를 놓으면서, 거리를 저장해나간다.
이를 통해 2번 질문 해결.
=> bfs()를 통해 다리 만들기 진행.
=> 시작 섬 != 현재 도달한 섬이면, 해당 다리 길이 ans에 min비교하여 갱신.

"""
import sys
from collections import deque
input=sys.stdin.readline

def bfs_land(sx,sy):
    global n,land_label
    q=deque([(sx,sy)])
    land_visited[sx][sy]=1
    graph[sx][sy]=land_label
    
    while q:
        x,y=q.popleft()
        for i in range(4):
            nx=x+dx[i]
            ny=y+dy[i]
            if 0<=nx<n and 0<=ny<n:
                if graph[nx][ny]==1 and land_visited[nx][ny]==0:
                    land_visited[nx][ny]=1
                    graph[nx][ny]=land_label
                    q.append((nx,ny))
                # 해당 섬의 가장 가까운 바다칸이며, seaQ에 없는경우
                if graph[nx][ny]==0 and (nx,ny) not in seaQ:
                    seaQ.append((nx,ny,land_label))
    
    land_label-=1 # 다른 섬 라벨링을 위해 섬라벨+1


def bfs(sx,sy,start_label):
    global n
    q=deque([(sx,sy)])
    path=[[-1 for _ in range(n)] for _ in range(n)] # 시작 바다 칸 기준 길이 저장 배열.
    path[sx][sy]=1
    
    while q:
        x,y=q.popleft()
        for i in range(4):
            nx=x+dx[i]
            ny=y+dy[i]
            if 0<=nx<n and 0<=ny<n:
                # 바다칸이고, 방문하지 않은 칸이면
                if graph[nx][ny]==0 and path[nx][ny]==-1:
                    path[nx][ny]=path[x][y]+1
                    q.append((nx,ny))
                # 섬을 만났고, 시작섬이 아닌 다른 섬을 만났으면
                if graph[nx][ny]<0 and graph[nx][ny]!=start_label:
                    return path[x][y] # 시작섬~현재만난섬의 다리길이 반환.
    # 바다칸이 상하좌우가 모든 섬칸으로 막힌 경우라면
    # 이 칸은 버려야 하기에, 답이 될수없는 수를 리턴하여 넘겨버린다.
    # (이것땜에 TypeError 찾느라 시간이 좀 걸렸다 ㅠ)
    return 300 
    
n=int(input())
graph=[[*map(int,input().split())] for _ in range(n)]
dx=[-1,1,0,0]
dy=[0,0,-1,1]

## Land Labeling
land_label=-1 # 섬번호
land_visited=[[0 for _ in range(n)] for _ in range(n)] # 섬 해당칸 방문배열
seaQ=deque([]) # 섬을 둘러싸는 바다 좌표 담는 큐
for i in range(n):
    for j in range(n):
        if graph[i][j]==1 and land_visited[i][j]==0:
            bfs_land(i,j) # 섬 라벨링
            
## Search Start
ans=300
while seaQ:
    # 시작 바다칸 좌표 i,j 그리고 시작 섬 번호(라벨)
    i,j,label=seaQ.popleft()
    # 시작 바다칸 기준으로 다리 놓기 시작.
    ans=min(ans,bfs(i,j,label)) # 다리 길이 비교 및 갱신

print(ans)