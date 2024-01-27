# 2468 : Adjusted-Space
import sys
input=sys.stdin.readline

def bfs(x,y,height,visited):
    q=[[x,y]]
    while q:
        #print(q)
        e=q.pop(0)
        x,y=e
        visited[x][y]=1
        # left
        if y-1>=0 and not visited[x][y-1] and [x,y-1] not in q and graph[x][y-1]>height:
            q.append([x,y-1])
        # right
        if y+1<n and not visited[x][y+1] and [x,y+1] not in q and graph[x][y+1]>height:
            q.append([x,y+1])
        # top
        if x-1>=0 and not visited[x-1][y] and [x-1,y] not in q and graph[x-1][y]>height:
            q.append([x-1,y])
        # bottum
        if x+1<n and not visited[x+1][y] and [x+1,y] not in q and graph[x+1][y]>height:
            q.append([x+1,y])


n=int(input())
m=0
graph=[[] for _ in range(n)]
ans=-1

for i in range(n):
    t=[*map(int,input().split())]
    graph[i]=t
    m=max(t)

for height in range(0,m+1):
    visited=[[0]*n for _ in range(n)]
    cnt=0
    for i in range(n):
        for j in range(n):
            if not visited[i][j] and graph[i][j]>height:
                #print(f"#BFS({i},{j},{height})")
                bfs(i,j,height,visited)
                cnt+=1
    #print(f"##height: {height}, cnt={cnt}")
    ans=max(ans,cnt)
print(ans)