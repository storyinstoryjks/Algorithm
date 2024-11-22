# https://www.acmicpc.net/problem/15591
# MooTube
# 그래프 탐색

from collections import deque
scan=lambda:map(int,__import__('sys').stdin.readline().split())

def bfs(k,sv):
    q=deque([(sv,1e9)]) # 현재 방문 정점, 현 정점의 현 유사도
    visited=[0]*(N+1)
    visited[sv]=1
    
    cnt=0
    while q:
        v,cur_usado=q.popleft()
        if v!=sv and cur_usado>=k:
            cnt+=1
        for nv,e_usado in graph[v]:
            if not visited[nv]:
                q.append((nv,min(cur_usado,e_usado)))
                visited[nv]=1
    
    return cnt
    
N,Q=scan()
graph=[[] for _ in range(N+1)]

for _ in range(N-1):
    start,end,weight=scan()
    graph[start].append((end,weight))
    graph[end].append((start,weight))

for _ in range(Q):
    k,v=scan()
    print(bfs(k,v))