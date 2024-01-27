# 1260 DFS and BFS

from collections import deque

def dfs(s):
    visitedDFS[s]=1
    print(s, end=" ")
    for i in range(1,n+1):
        if not visitedDFS[i] and graph[s][i]:
            dfs(i)

def bfs(s):
    q = deque()
    q.append(s)

    while q:
        x=q.popleft()
        visitedBFS[x]=1
        print(x,end=" ")
        for i in range(1,n+1):
            if not visitedBFS[i] and graph[x][i]:
                if i not in q:
                    q.append(i)

n,m,v = map(int, input().split())
visitedDFS = [0]*(n+1)
visitedBFS = [0]*(n+1)
graph = [[0]*(n+1) for _ in range(n+1)]

for _ in range(m):
    start, end = map(int, input().split())
    graph[start][end]=graph[end][start]=1

dfs(v)
print()
bfs(v)

