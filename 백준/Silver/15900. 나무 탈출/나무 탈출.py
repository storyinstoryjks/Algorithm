# https://www.acmicpc.net/problem/15900
# 나무 탈출
# 트리, 그래프탐색, dfs

import sys
sys.setrecursionlimit(10**5*6)
input=sys.stdin.readline

def dfs(root):
    visited[root]=1
    for next_node in graph[root]:
        if not visited[next_node]:
            paths[next_node]=paths[root]+1
            dfs(next_node)


n=int(input())
graph=[[] for _ in range(n+1)]
visited=[0]*(n+1)

for _ in range(n-1):
    s,e=map(int,input().split())
    graph[s].append(e)
    graph[e].append(s)

paths=[0]*(n+1)
dfs(1)
print('YNeos'[sum(paths[i] for i in range(2,n+1) if len(graph[i])==1)%2==0::2])