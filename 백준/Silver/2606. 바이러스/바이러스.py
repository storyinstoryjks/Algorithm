# 2606 : Virus

def dfs(v):
    global cnt
    visitedDFS[v]=1
    cnt+=1
    for i in range(1,n+1):
        if not visitedDFS[i] and graph[v][i]:
            dfs(i)

n=int(input())
m=int(input())
visitedDFS=[0]*(n+1)
graph=[[0]*(n+1)for _ in range(n+1)]
cnt=0

for _ in [0]*m:
    a,b=map(int,input().split())
    graph[a][b]=graph[b][a]=1

dfs(1)
print(cnt-1)