# 11724 : Connected Component
# Search count : Part of graph
import sys
sys.setrecursionlimit(10**6)
input=sys.stdin.readline

def dfs(v):
    visited[v]=1
    
    for i in range(1,n+1):
        if not visited[i] and graph[v][i]:
            dfs(i)

cnt=0
n,m=map(int,input().split())
graph=[[0]*(n+1) for _ in range(n+1)]
visited=[0]*(n+1)
for _ in range(m):
    u,v=map(int,input().split())
    graph[u][v]=1
    graph[v][u]=1

for i in range(1,n+1):
    if not visited[i]:
        dfs(i)
        cnt+=1
            
print(cnt)