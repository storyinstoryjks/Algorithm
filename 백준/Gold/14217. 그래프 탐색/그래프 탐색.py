# https://www.acmicpc.net/problem/14217
# 그래프 탐색
# 탐색 문제

input=__import__('sys').stdin.readline
deque=__import__('collections').deque

def bfs(sx):
    q=deque([(sx,0)]) # city,distance
    visited=[False for _ in range(n+1)]
    visited[sx]=True
    
    while q:
        x,cnt=q.popleft()
        for nx in graph[x]:
            if not visited[nx]:
                if nx==1:
                    return cnt+1
                visited[nx]=True
                q.append((nx,cnt+1))
    
    return -1

n,m=map(int,input().split())
graph=[[] for _ in range(n+1)]

for _ in range(m):
    start,end=map(int,input().split())
    graph[start].append(end)
    graph[end].append(start)

for _ in range(int(input())):
    a,i,j=map(int,input().split())
    if a==1:
        graph[i].append(j)
        graph[j].append(i)
    else:
        graph[i].remove(j)
        graph[j].remove(i)
    
    answer=[0]*(n+1)
    for k in range(2,n+1):
        answer[k]=bfs(k)
    
    print(*answer[1:])