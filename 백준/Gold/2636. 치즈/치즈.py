# Cheese : https://www.acmicpc.net/problem/2636
# BFS

"""
[설계]
핵심이 되는 질문: "구멍을 어떻게 판별하는가?"
=> 구멍 좌표들을 배열에 저장 후, BFS를 돌면서 구멍 좌표들은 피해주는 방법 초안.
=> 구멍 찾기에 for문 한번, BFS돌면서 for문 적용되기에 시간 제한 걸릴 수 있음.
(그렇기에, 다른 방법 고안해야함.)
=> 치즈 덩어리의 '가' 부분만 녹이는 문제임.
=> 즉, 외부 공기에 접촉되는 '가'의 치즈칸만 탐색하면 된다.
=> BFS 탐색 대상은 결국 공기인 0이 된다.
=> 2차원 배열인 문제 상황 graph 기준 시작정점(0,0)부터 왼쪽에서 오른쪽으로 대각선 방향에 존재하는
    라인들을 한번의 탐색때 조사하게됨. (마치, 파스칼 삼각형 처럼 보면됨. 꼭대기는 시작정점)
=> 구멍을 감싸는 치즈를 녹이고, 방문처리를 하게 되면, 구멍의 공기는 탐색 대상에서 제외하게됨.
결국, 알고리즘은 'BFS 탐색 대상은 공기이며, 각 공기 또는 치즈 녹이기 작업은 탐색마다 바로 방문처리를 진행'이다.

[알고리즘 과정]
0. 초기 치즈 개수 total에 저장.
1. 0,0 시작 정점 기준 BFS 탐색 시작.
2. 외부 공기인 경우: 방문처리 및 큐에 삽입
3. 치즈인 경우: 방문처리/0으로 변경/카운팅(cnt++)
4. BFS 탐색 종료 후 : total==녹인치즈개수 then, 정답 출력
5. BFS 탐색 종료 후 : total!=녹인치즈개수 then, total 갱신 및 BFS 재탐색.(time+1)
"""
import sys
from collections import deque
input=sys.stdin.readline

def bfs(visited):
    global n,m
    q=deque([(0,0)])
    visited[0][0]=1
    cnt=0 # 녹인 치즈 개수
    
    while q:
        x,y=q.popleft()
        for i in range(4):
            nx=x+dx[i]
            ny=y+dy[i]
            if 0<=nx<n and 0<=ny<m:
                # 방문하지 않은 칸(노드)이면
                if visited[nx][ny]==0:
                    # 외부 공기이면
                    if graph[nx][ny]==0:
                        q.append((nx,ny)) # 큐에 삽입
                    # 치즈이면
                    else:
                        graph[nx][ny]=0 # 치즈 녹이기
                        cnt+=1 # 녹인 치즈 카운팅
                    visited[nx][ny]=1 # 외부공기이든 치즈이든 방문처리
                    
    return cnt


n,m=map(int,input().split())
graph=[]
time,total=0,0
dx=[-1,1,0,0]
dy=[0,0,-1,1]

for i in range(n):
    row=[*map(int,input().split())]
    total+=row.count(1) # 초기 총 치즈 개수
    graph.append(row)
    
while True:
    visited=[[0 for _ in range(m)] for _ in range(n)]
    melt_cnt=bfs(visited) # 현재 탐색 후 녹인 치즈 개수
    time+=1
    # 다 녹였으면, 정답 출력
    if total==melt_cnt:
        print(time)
        print(melt_cnt)
        break
    # 다 못녹였으면, 총 치즈 개수 갱신 후, 재탐색 진행
    total-=melt_cnt
