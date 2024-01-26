# 24444 : BFS1

import sys
from collections import deque
input=sys.stdin.readline

def bfs(v):
    global orderCnt
    visited[v]=orderCnt
    q.append(v)
    
    while q:
        x=q.popleft()
        graph[x].sort()
        for nv in graph[x]:
            if visited[nv]==0:
                orderCnt+=1
                visited[nv]=orderCnt
                q.append(nv)
                
    
n,m,r=map(int,input().split())
graph=[[] for _ in range(n+1)]
visited=[0]*(n+1)
q=deque() # bfs 탐색을 위한 인접 정점 리스트
orderCnt=1 # 방문 순서를 visited 값으로 저장하기 위한 변수
for _ in range(m):
    start,end=map(int,input().split())
    graph[start].append(end)
    graph[end].append(start)

bfs(r)

print('\n'.join(map(str,visited[1:])))