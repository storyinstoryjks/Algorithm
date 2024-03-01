# Competition-Viros
# https://www.acmicpc.net/problem/18405

"""
난이도: 쉬움~보통
시간: 20분

[알고리즘]
핵심: 그래프(트리)의 깊이별 체크. (트리 깊이==시간)
=> 시작점을 기준으로 자식노드들을 모두 방문한다. (한 레벨별)
=> 즉, 트리의 깊이가 시간의 흐름과 같다.
=> 이때, 바이러스가 놓아져 있는 현 상황의 '모든 바이러스들을 부모노드로 bfs 탐색을 진행한 후, 깊이 체크를 한다.'

1. q에 바이러스 번호 순대로, 모든 바이러스 좌표 삽입. (정렬 이용)
2. bfs 탐색 시작
3. 자식노드값이 0이라면, 큐에 삽입 + 해당 자식노드 좌표값 해당 바이러스로 설정
4. 마지막 부모노드 k번 bfs까지 다 진행한 경우,
    4.1 현재 깊이(=현재 시간) < s 이면, 다음 깊이 탐색 시작(time+1)
    4.2 현재 시간 == s 이면, bfs 탐색 종료(return)
5. 정답 출력.

[4번이 가능한 이유]
=> 초기 q에 바이러스 번호 순서대로 좌표를 삽입했기 때문.
=> 예시 (예제입력 1번)

[초기: 편의상 원소는 바이러스 번호로] q=[1,2,3]
[bfs 탐색 시작]
q=[2,3,'1-1','1-2'] (1-1: 1번바이러스 0,0위치의 자식노드 1번)
q=[3, 1-1, 1-2, '2-1', '2-2']
q=[1-1, 1-2, 2-1, 2-2, '3-1']
--- 트리 한 깊이 종료. (위는 시간 0초대에서의 큐 진행과정을 나타낸 것이다.)

=> 즉, 바이러스 번호순서대로 삽입했기에 큐 특성상 계속해서 자식노드들도 바이러스 번호대로 탐색하게됨.

"""
import sys
from collections import deque
input=sys.stdin.readline

def bfs():
    global n,s,k
    time=0
    while q:
        # 4-2
        if time==s:
            break
        for _ in range(len(q)):
            p,x,y=q.popleft()
            for dx,dy in [(-1,0),(1,0),(0,-1),(0,1)]:
                nx=x+dx; ny=y+dy
                if 0<=nx<n and 0<=ny<n:
                    # 3
                    if graph[nx][ny]==0:
                        graph[nx][ny]=graph[x][y] # 3-2
                        q.append((graph[nx][ny],nx,ny)) # 3-1
        # 4-1
        time+=1
        
    
    
n,k=map(int,input().split())
graph=[[*map(int,input().split())] for _ in range(n)]
s,gx,gy=map(int,input().split())

# 1
virus=[]
for i in range(n):
    for j in range(n):
        if graph[i][j]>0:
            virus.append((graph[i][j],i,j))
q=deque(sorted(virus))
# 2
bfs()
print(graph[gx-1][gy-1])