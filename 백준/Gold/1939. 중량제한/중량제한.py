# Restrict to weight
# https://www.acmicpc.net/problem/1939
"""
난이도 : 보통~어려움
설계시간 : 1시간

[핵심]
1. 어떤 자료구조를 사용할 것인가?
=> 섬들, 다리, 다리중량 input값 존재.
=> 각각 정점,간선,가중치로 해석 가능.
=> 그래프 중 가중치 그래프(네트워크) 자료구조로 파악가능.
=> 인접행렬(2차원배열) vs 인접리스트(연결리스트)
==> [인접행렬]
==> 정점과 간선 정보 파악 가능
==> 가중치도 함께 입력하기 위해서는 3차원 배열로 구성되어야함.
==> 모든 다리 파악하므로, O(n*n*n) 걸림.
==> [인접리스트]
==> 각 정점을 나타내는 헤더노드의 노드들(원소)의 형식을 튜플로 설정하면,
==> 간선+가중치 표현 쉽게 가능.
==> 모든 다리 파악하므로, O(v+e) 걸림.
그러므로, 인접리스트 형식의 그래프 자료구조 선택.

2. 목적지까지의 경로 파악?
=> 그래프 탐색 기법 필요.
=> DFS vs BFS
=> 아무거나 해도 상관없음. 핵심은 가중치이기 때문.
=> 필자는 BFS 선택.

3. 다리 중량 파악?
=> 이 부분이 핵심인 문제.
=> 다리 중량의 최대값을 물어보는 문제이므로, 가능한 중량을 조사해야한다.
=> 제한범위가 0~10억까지이므로, 완전탐색진행시 시간초과 가능성 있음.(O(n), n=10억)

=> '필요없는 범위를 제거해나가는 방식으로 제한범위를 탐색 과정마다 줄이는 방식 고안.'

=> 이는 '이분 탐색'으로 해결 가능.
=> (start+end)//2로 중간값을 구한 뒤, 이동시키고자하는 물품 중량을 이 값으로 bfs 경로 탐색 진행.
=> 가능하다? then, start=mid+1로 설정해서 '이 값보다 더 높은 중량으로 경로 가능한지 확인'
=> 불가능하다? then, end=mid-1로 설정해서 '이 값보다 작은 중량에서 경로 가능한지 확인'
"""
import sys
from collections import deque
input=sys.stdin.readline

def bfs(sn,en,targetWeight):
    global n
    q=deque([sn])
    visited=[0]*(n+1)
    visited[sn]=1
    
    while q:
        x=q.popleft()
        for nx,maxWeight in graph[x]: # 자식노드들(해당간선들) 탐색
            # 간선 타고 이동한 섬 미방문이고
            # 해당 간선 최대 중량 >= 물품 중량이면
            if visited[nx]==0 and maxWeight>=targetWeight:
                visited[nx]=1 # 방문 표시
                q.append(nx) # 이동처리.
    
    # 해당 물품 중량으로 공장 B까지 갈 수 있다면, 가능 메시지 리턴.
    # 불가능하다면, 불가능 메시지 리턴.
    return visited[en] or 0


n,m=map(int,input().split())
graph=[[] for _ in range(n+1)] # 다리 그래프
ans,startWeight,endWeight=0,0,1000000000 # 답, 이분탐색시작점,이분탐색종료점

for _ in range(m):
    start,end,weight=map(int,input().split()) # 간선시작,간선종료,해당간선가중치
    # 양방향(무방향) 그래프
    graph[start].append((end,weight))
    graph[end].append((start,weight))

startNode,endNode=map(int,input().split()) # 공장 A, 공장 B

# 이분 탐색 시작.
while(startWeight<=endWeight):
    mid=(startWeight+endWeight)//2 # 중간값 설정.
    # 해당 중간값을 물품중량으로 설정하여, 공장A->B 경로가 가능한지 조사.
    if bfs(startNode,endNode,mid): # 가능하면
        ans=mid # 답 갱신
        startWeight=mid+1 # 이보다 높은 범위에서의 중량 구하기 위해 시작점 갱신
    else: # 불가능하면
        endWeight=mid-1 # 이보다 낮은 범위 중량 구하기 위해 종료점 갱신

print(ans)
