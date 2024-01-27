# 1389 : Kevin Bacon

import sys
from collections import deque
input=sys.stdin.readline


def bfs(v,visited):
    q=deque([v])
    while q:
        v=q.popleft()
        for i in graph[v]:
            if visited[i]==0:
                q.append(i)
                visited[i]=visited[v]+1

n,m=map(int,input().split())
graph=[[]*(n+1) for _ in range(n+1)]
min_node,min_cnt=0,1e9

for _ in range(m):
    start,end=map(int,input().split())
    graph[start].append(end)
    graph[end].append(start)

for i in range(1,n+1):
    visited=[0 for _ in range(n+1)]
    bfs(i,visited)
    check=0
    for j in range(1,n+1):
        if j!=i:
            check+=visited[j]
    if check<min_cnt:
        min_node=i
        min_cnt=check
print(min_node)