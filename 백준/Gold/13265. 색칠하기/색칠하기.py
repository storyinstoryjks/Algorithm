# https://www.acmicpc.net/problem/13265
# 색칠하기
# 그래프 탐색

deque=__import__('collections').deque
input=__import__('sys').stdin.readline

def bfs(sv):
    q=deque([sv])
    visited[sv]=1
    colors[sv]='c1'
    
    while q:
        v=q.popleft()
        for nv in graph[v]:
            # 미방문 동그라미 처리
            if not visited[nv]:
                visited[nv]=1
                colors[nv]='c2' if colors[v]=='c1' else 'c1' # 부모와 다르게 색 배정
                q.append(nv)
            # 방문 동그러미 접근시
            elif colors[v]==colors[nv]: # 배정된 부모색과 자식색 비교
                return False
            
    return True
    

for _ in range(int(input())):
    n,m=map(int,input().split())
    graph=[[] for _ in range(n+1)]
    visited=[0 for _ in range(n+1)]
    colors=['' for _ in range(n+1)]
    
    for _ in range(m):
        start,end=map(int,input().split())
        graph[start].append(end)
        graph[end].append(start)
    
    result=True
    for v in range(1,n+1):
        if not visited[v]:
            result=bfs(v)
            if result==False:
                break
    
    print("impossible" if not result else "possible")