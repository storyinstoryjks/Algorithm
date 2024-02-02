# cheese 2
# https://www.acmicpc.net/problem/2638
# (cheese 1 : https://www.acmicpc.net/problem/2636)
"""
2636 치즈 문제를 풀어봤기에, 금방 풀 수 있었다.
차이점은 '2변 이상 닿은 치즈칸만 녹는다.'가 추가.

1. 외부 공기를 시작정점으로 bfs 탐색
    => 치즈로 둘러싼 내부 공기칸은 탐색에서 제외.
2. visited 값에 '치즈칸을 몇번 방문했는지 카운팅'
    => 탐색 시 해당 외부 공기칸의 상하좌우 자식노드 찾기.
    => 상하좌우가 치즈칸이면, '해당 치즈칸은 해당 공기칸 만났으므로 +1' 진행.
    => 다른 공기칸에서 같은 치즈칸 발생시 누적해서 +1로 처리됨.
    => 즉, 해당 치즈칸이 외부공기칸 몇개 맞닿았는지 파악 가능.
3. bfs탐색 종료후, visited값>=2인 좌표들을 실제 graph값 0으로 변경.

Tip) 'bfs탐색시, 치즈칸을 바로 녹이기 처리하면 안될까?'
=> 내부 구멍에 해당되는 치즈칸인 경우, 바로 녹인다면?
=> 내부 공기칸이 bfs 탐색 대상으로 들어가버리게 됨.
=> 그러므로, bfs 탐색 종료후, 대상 치즈칸들을 지워야 함.
"""
import sys
from collections import deque
input=sys.stdin.readline

def bfs(sx,sy):
    global n,m
    q=deque([(sx,sy)])
    visited[sx][sy]=1
    
    while q:
        x,y=q.popleft()
        for dx,dy in [(-1,0),(1,0),(0,-1),(0,1)]:
            nx=x+dx
            ny=y+dy
            if 0<=nx<n and 0<=ny<m:
                # 해당 노드가(좌표가) 외부 공기칸이고, 방문하지 않았다면
                if graph[nx][ny]==0 and visited[nx][ny]==0:
                    q.append((nx,ny))
                    visited[nx][ny]=1 # 방문처리 및 치즈칸에 맞닿은 공기수 체킹을 위해 1표시.
                # 해당 노드가 치즈칸이면,
                elif graph[nx][ny]==1:
                    visited[nx][ny]+=1 # 해당 공기칸 맞닿은 표시를 위한 +1
    
total_che_cnt,time=0,0 # 초기 주어진 총 치즈칸 개수, 다 녹이기까지 걸리는 시간
n,m=map(int,input().split())
graph=[]
for i in range(n):
    l=[*map(int,input().split())]
    for j in range(m):
        if l[j]==1:
            total_che_cnt+=1
    graph.append(l)

while True:
    visited=[[0]*m for _ in range(n)] 
    bfs(0,0) # 외부 공기 탐색 시작.
    time+=1
    
    melt_cnt=0 # 이번 bfs 탐색에서 파악된 녹일 대상 치즈칸 개수.
    for i in range(n):
        for j in range(m):
            if visited[i][j]>=2:
                graph[i][j]=0 # 치즈칸 녹이기
                melt_cnt+=1
    
    # 남아있는 치즈칸 개수 == 녹인 총 치즈칸 개수
    # graph에 남아있는 치즈가 없는것.
    if total_che_cnt==melt_cnt:
        print(time)
        break
    
    # 치즈칸이 graph에 남아있으면, 녹인 치즈 수만큼 total 갱신.
    # 다음 bfs 탐색 진행.
    total_che_cnt-=melt_cnt