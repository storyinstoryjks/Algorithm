# Jump Jump
# https://www.acmicpc.net/problem/11060

"""
1. 0번 인덱스 기준으로 bfs 탐색 시작
2. 배열값이 0이면 '자식 노드 없음'
3. 배열값 0 초과이면, '배열값만큼 자식노드 존재'
4. 배열 범위 내이고, 미방문 자식노드면 => 부모가 거쳐온 점프횟수+1로 갱신 및 que에 자식노드 삽입.
5. bfs 종료 후 ans[n-1] 바로 출력.
    => n-1번째 미방문은 '탈출구에 도달하지 못하였다'라는 의미와 일맥상통.
    => bfs에서 n-1번째 갱신안했으면 -1로 존재하기 때문에, 바로 출력해도 상관없다.
"""
import sys
from collections import deque
input=sys.stdin.readline

def bfs(sv):
    global n
    q=deque([sv])
    visited[sv]=0
    
    while q:
        v=q.popleft()
        if graph[v]==0:
            continue
        # 최소에 가까워지기 위해서는 가장 멀리 점프하는 노드를 먼저 삽입.
        for dv in range(graph[v],0,-1):
            nv=v+dv
            if nv<n and visited[nv]==-1:
                visited[nv]=visited[v]+1
                q.append(nv)
                   
                    
n=int(input())
graph=[*map(int,input().split())]
visited=[-1]*n
bfs(0)
print(visited[n-1])