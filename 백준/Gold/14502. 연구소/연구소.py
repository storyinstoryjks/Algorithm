# 14502 : Lab
"""
문제의 핵심 : "3개의 벽을 세우는 모든 방법에서 각 경우의 바이러스 개수."

[제약조건]
1. 3개의 벽을 세우는 모든 경우의 수는?
2. 바이러스를 탐색하는 방법은?
3. 안전 영역(0의 개수)를 카운팅하는 방법은?

[제약조건에 따른 해결방법]
1-1. 이중중첩을 통한 재귀.
1-2. 벽 세우는 모든 경우의 수를 미리 구함. : 조합 사용.
2. '안전 영역의 최대 개수' = '바이러스 퍼지는 정도를 알아야 안전 영역 카운팅 가능' = '바이러스 전파 최소화' = BFS
3-1. 바이러스 전파 전, 초기 연구소 안전 영역을 미리 카운팅 후, 바이러스 전파마다 안전 영역 개수 갱신.
3-2. 바이러스 전파 후, 연구소 안전 영역 카운팅.

[제약조건 해결방법 선택]
<1-1 vs 1-2>
=> 1-1은 이중중첩으로 0 위치를 알아낸 후, 벽을 세우고, 재귀를 통해 다음 0위치를 발견해야함.
=> 3개의 벽을 세우고 바이러스 전파 파악후 "백트래킹을 통해 3개의 벽을 다시 0으로 바꿔야한다."
=> 1-2는 모든 경우의 수를 구하는 combination 라이브러리를 통해 한 리스트에 저장.
=> for문 반복 한번 마다 3개의 벽 대입연산으로 설정 가능
그러므로, 1-2 선택.

<3-1 vs 3-2>
=> 3-1은 for문을 한번 더 써서 파악.
=> 3-2는 탐색하면서 파악.
그러므로, 3-2 선택.

[알고리즘]
1. 벽세우기 모든 경우 구하기.
2. 초기 연구소 바이러스 위치 파악.
3. BFS 탐색으로 바이러스 위치 갱신.
4. 카운팅된 0 개수 최대 비교.
"""

import sys
from collections import deque
from itertools import combinations as cb
input=sys.stdin.readline

def bfs(V,cntZero):
    q=deque([])
    for i in V:
        q.append(i) # 초기 연구소 모든 바이러스 위치들 큐에 삽입.
    while q: # bfs 탐색 시작. (바이러스 위치 갱신 및 실시간 0개수 카운팅)
        x,y=q.popleft()
        for i in range(4):
            nx=x+dx[i]
            ny=y+dy[i]
            if 0<=nx<n and 0<=ny<m:
                if tmp[nx][ny]==0:
                    tmp[nx][ny]=2
                    q.append([nx,ny])
                    cntZero-=1 # 0->2로 갱신되므로, 초기0개수-1
    return cntZero
    
n,m=map(int,input().split())
graph,virus,idx=[],[],[] # 연구소,바이러스위치,0위치
ans,cnt=-1,0 # 정답,0개수
dx=[-1,1,0,0]
dy=[0,0,-1,1]

for i in range(n):
    l=[*map(int,input().split())]
    for j in range(m):
        if l[j]==0:
            idx.append([i,j])
            cnt+=1
        if l[j]==2:
            virus.append([i,j])
    graph.append(l)

for ele in cb(idx,3): # 3개 벽 모든 경우
    tmp=[[graph[i][j] for j in range(m)] for i in range(n)] # 각 경우에서 사용될 연구소.(깊은복사)
    countZero=cnt
    for i in ele:
        tmp[i[0]][i[1]]=1
        countZero-=1
    ans=max(ans,bfs(virus,countZero))
        
print(ans)