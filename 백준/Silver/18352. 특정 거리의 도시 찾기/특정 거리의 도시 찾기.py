# Find to City of Specific Distance : https://www.acmicpc.net/problem/18352
"""
bfs 탐색 진행하면서, 현재 노드의 다음 자식노드가 이미 방문되었으면
'이미 다음 자식노드는 자신의 최단거리를 계산을 끝낸상태로 방문처리가 된것.'
=> 다익스트라 알고리즘 (시작노드~각노드까지의 거리를 저장)
즉, BFS + 다익스트라 = 각 노드까지의 최단거리를 저장 및 방문처리하는것.

[알고리즘 과정]
1. BFS 탐색
2. 현재 탐색 노드 기준, 다음 자식노드들(인접정점들) 탐색.
3. if 방문(==이미 다음 자식노드의 최단경로 구한 상황), then continue
4. if 미방문, then 현재 노드까지의 거리+1를 visited에 저장.(거리갱신+방문처리)
4-1. 거리 갱신시, 저장 거리==k이면 cnt++
5. BFS 탐색 종료
6-1. k거리를 가진 정점이 없다면, -1 출력
6-2. 반대면, visited 탐색하여 답 출력.
"""
import sys
from collections import deque
input=sys.stdin.readline

def bfs(start):
    global k
    q=deque([start])
    cnt=0
    visited[start]=0
    
    while q:
        v=q.popleft()
        for nv in graph[v]:
            if visited[nv]==-1:
                q.append(nv)
                visited[nv]=visited[v]+1
                if visited[nv]==k:
                    cnt+=1
    
    return cnt
    
n,m,k,x=map(int,input().split())
graph=[[] for _ in range(n+1)]
visited=[-1]*(n+1)

for _ in range(m):
    start,end=map(int,input().split())
    graph[start].append(end)

total=bfs(x)
if total>0:
    for i in range(1,n+1):
        if visited[i]==k:
            print(i)
else:
    print(-1)
