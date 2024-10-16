# https://www.acmicpc.net/problem/2660
# 화장뽑기

from collections import deque
input=__import__('sys').stdin.readline

def bfs(start):
    global ans
    q=deque([(start,0)])
    visited=[0 for _ in range(n+1)]
    path=[0 for _ in range(n+1)]
    
    visited[start]=1
    while q:
        x,y=q.popleft()
        for next_node in graph[x]:
            if visited[next_node]==0:
                visited[next_node]=1
                q.append((next_node,y+1))
                path[next_node]=y+1
    
    tmp=max(path)
    if tmp<ans[0][1]:
        ans=[(start,tmp)]
    elif tmp==ans[0][1]:
        ans.append((start,tmp))
    
    
n=int(input())
graph=[[] for _ in range(n+1)]
ans=[(0,1000)]

while True:
    a,b=map(int,input().split())
    if a==-1:
        break
    graph[a].append(b)
    graph[b].append(a)

for node in range(1,n+1):
    bfs(node)

print(ans[0][1],len(ans))
print(*[i for i,_ in ans])