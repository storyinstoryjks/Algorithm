# https://www.acmicpc.net/problem/1240
# 노드 사이의 거리

from sys import stdin 
input=stdin.readline

def dfs(s,e,w):
    global flag,ans
    visited[s]=1
    if s==e:
        ans=w
        return
    for next_node,weight in graph[s]:
        if not visited[next_node]:
            if not flag:
                dfs(next_node,e,w+weight)
            else:
                return
                
    
n,m=map(int,input().split())
graph=[[] for _ in range(n+1)]
visited=[0]*(n+1)
flag,ans=False,0

for _ in range(n-1):
    start,end,weight=map(int,input().split())
    graph[start].append((end,weight))
    graph[end].append((start,weight))

for _ in range(m):
    start,end=map(int,input().split())
    dfs(start,end,0)
    print(ans)
    visited=[0]*(n+1)