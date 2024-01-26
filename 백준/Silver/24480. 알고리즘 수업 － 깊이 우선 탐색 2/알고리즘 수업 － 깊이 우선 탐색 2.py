# 24480 : DFS2

import sys
input=sys.stdin.readline
sys.setrecursionlimit(150000)

def dfs(v):
    global orderCnt
    visited[v]=orderCnt
    graph[v].sort()
    for nv in graph[v][::-1]: # 내림차순
        if visited[nv]==0:
            orderCnt+=1
            dfs(nv)
    
n,m,r=map(int,input().split())
graph=[[] for _ in range(n+1)]
for _ in range(m):
    start,end=map(int,input().split())
    graph[start].append(end)
    graph[end].append(start)
visited=[0]*(n+1)
orderCnt=1

dfs(r)

print('\n'.join(map(str,visited[1:])))