# 24479 : DFS1

import sys
input=sys.stdin.readline
sys.setrecursionlimit(150000)

def dfs(v):
    global orderCnt
    visited[v]=orderCnt # 현재 노드에 방문 순서 저장.(방문처리가 함꼐됨)
    graph[v].sort() # 자식 노드 리스트 정렬
    # 자식 노드 리스트 탐색(인접 정점 리스트)
    for nv in graph[v]:
        # 방문하지 않은 자식 노드라면
        if visited[nv]==0:
            orderCnt+=1 # 다음 방문순서이므로 순서변수+1
            dfs(nv) # 다음 노드 방문
    
n,m,r=map(int,input().split())
graph=[[] for _ in range(n+1)]
for _ in range(m):
    start,end=map(int,input().split())
    # 무방향 그래프
    graph[start].append(end)
    graph[end].append(start)
visited=[0]*(n+1) # 방문 처리(인덱스: 정점번호, 값: 방문순서)
orderCnt=1 # visited 인덱스 자리에 방문순서 저장을 위한 변수

dfs(r)

print('\n'.join(map(str,visited[1:])))