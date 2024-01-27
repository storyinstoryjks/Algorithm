# 1707

import sys
from collections import deque
input=sys.stdin.readline

def bfs(v,g):
    q=deque([v])
    visited[v]=g
    while q:
        v=q.popleft()
        for i in graph[v]:
            if visited[i]==0:
                q.append(i)
                visited[i]=visited[v]*(-1)
            elif visited[v]==visited[i]:
                return False
    return True
    
for _ in range(int(input())):
    V,E=map(int,input().split())
    graph=[[] for _ in range(V+1)]
    visited=[0 for _ in range(V+1)]
    flag=True
    
    for _ in range(E):
        start,end=map(int,input().split())
        graph[start].append(end)
        graph[end].append(start)
    
    for i in range(1,V+1):
        if not visited[i]:
            flag=bfs(i,1)
            if not flag:
                break
    
    print("YES" if flag else "NO")