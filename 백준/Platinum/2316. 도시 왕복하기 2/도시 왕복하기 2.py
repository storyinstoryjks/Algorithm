from collections import *
from sys import stdin
input=stdin.readline
inf=float('inf')

# 최대 유량 계산 알고리즘
# O(VE**2)
def edmonds_karp(source,sink):
    flow_cnt=0
    parent={}
    
    # 2번막사까지 물길이 존재하는 경로들 찾기
    def bfs():
        visited=set()
        q=deque([source])
        parent.clear()
        while q:
            u=q.popleft()
            for v in graph[u]:
                if capacity[u][v]>0 and v not in visited:
                    visited.add(v)
                    parent[v]=u
                    if v==sink:
                        return 1
                    q.append(v)
        return 0
    
    # 모든 물길 경로들 왕복 가능여부 탐색
    while bfs():
        # 잔여 용량 구하기
        flow,s=inf,sink
        while s!=source:
            u=parent[s]
            flow=min(flow,capacity[u][s])
            s=u
        # 용량 갱신
        v=sink
        while v!=source:
            u=parent[v]
            capacity[u][v]-=flow
            capacity[v][u]+=flow
            v=u
        # 왕복 가능하면 누적 용량+1
        flow_cnt+=flow
    
    return flow_cnt

def find(x,t):
    return [f"{x}_{t}",str(x)][0<x<3]

n,p=map(int,input().split())
edges=[tuple(map(int,input().split())) for _ in range(p)]

graph=defaultdict(list)
capacity=defaultdict(lambda:defaultdict(int))

# 정점 분할(중간노드들)
for i in range(3,n+1):
    u_in,u_out=f"{i}_in",f"{i}_out"
    graph[u_in].append(u_out)
    graph[u_out].append(u_in)
    capacity[u_in][u_out]=1

# 간선 재구성
for s,e in edges:
    s_in,s_out=find(s,'in'),find(s,'out')
    e_in,e_out=find(e,'in'),find(e,'out')
    # 무방향 유량 그래프
    for a,b in [(s_out,e_in),(e_out,s_in)]:
        graph[a].append(b)
        graph[b].append(a)
        capacity[a][b]=inf # 돌아오는 경로때 통과 역할

print(edmonds_karp('1','2'))