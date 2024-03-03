# Problems
# https://www.acmicpc.net/problem/1766

# 1번 코드
"""
import sys
input=sys.stdin.readline

n,m=map(int,input().split())
graph=[[0]*(n+1) for _ in range(n+1)]

for _ in range(m):
    a,b=map(int,input().split())
    graph[a][b]=1

ans=[]

while len(ans)<n:
    degreeCnt,node=200000,0
    for i in range(1,n+1):
        tmp=0
        if i not in ans:
            for j in range(1,n+1):
                tmp+=graph[j][i]
            if tmp<degreeCnt:
                degreeCnt=tmp
                node=i
            elif tmp==degreeCnt and i<node:
                node=i
    ans.append(node)
    for i in range(1,n+1):
        graph[i][node]=0
        graph[node][i]=0

print(*ans)
"""
"""
1번 코드 메모리 초과.
아래 코드 성공 코드.
이번 제출 Python3도전 및 설명 추가.

난이도 : 보통~어려움
시간 : 40분

[설계]
1. 어떤 자료구조를 사용해야 하는가?
=> N개의 문제와 문제를 푸는 순서가 조건으로 나와있음.
=> N개의 문제를 정점으로, 문제 푸는 순서를 간선을 통한 이동으로 해석.
=> 그러므로, 그래프 자료구조 사용.
=> '순서'가 존재하는 가중치 없는 방향 그래프이다.

2. 어떤 알고리즘을 사용해야 하는가?
=> 순서가 존재하기에, 서순관계가 명확하다.
=> 이는 위상을 나타내며, 탐색 순서를 결정하기 위해, 위상 정렬을 이용해야 한다.
=> 다음과 같이 예제 입력1번을 나타낼 수 있다.
    |-------|
    v       |
    1   2   3   4
        ^        |
        |--------|        

    위상 정렬은 다음의 순서로 진행된다.
    (1) 진입차수가 0인 정점을 q에 삽입.
    (2) q에서 꺼낸 원소의 모든 간선을 제거.
    (3) (1),(2) 반복.
    (최종) q에서 꺼낸 순서가 정답.
    
3. 구현은 어떻게 해야하는가?
=> 필자의 1번코드 같은 경우 '큐를 사용하지 않고, 직접 ans 리스트에 삽입하는 식'으로 구현하였다.
=> 이 자체로는 문제를 푸는데 전혀 지장이 없으나, 핵심은 '그래프의 구현방식'이다.
=> 인접행렬로 구현하였기에, 이 문제처럼 희소 그래프에서는 메모리 낭비가 평균보다 심하다.
=> 그렇기에, 2번 코드처럼 인접리스트로 구현하였다.
=> 단, 인접리스트로 구현시, 진입 차수를 세기 위한 별도의 1차원 리스트가 필요하다.
=> 또한, ans에 문제번호를 삽입 시, 이용되는 조건들을 줄이기 위해 '이 문제의 2,3번을 만족시키는' Min Heap를 사용하였다.    
"""
import sys,heapq
input=sys.stdin.readline

n,m=map(int,input().split())
graph=[[] for _ in range(n+1)]
degree=[0 for _ in range(n+1)]

for _ in range(m):
    a,b=map(int,input().split())
    graph[a].append(b) # 단방향 그래프
    degree[b]+=1 # 진입 차수 카운트

heap,ans=[],[]

for i in range(1,n+1):
    # 진입 차수가 0이라면
    if degree[i]==0:
        heapq.heappush(heap,i);

while heap:
    sel=heapq.heappop(heap)
    ans.append(sel)
    # 선택된 문제번호를 가진 정점의 진출차수를 따라 연결된 정점들 탐색
    for i in graph[sel]:
        degree[i]-=1 # 도착지점 정점은 자신 기준에서 진입 차수이므로, -1 카운트.
        # 그렇게 진입차수 0이 되었다면
        if degree[i]==0:
            heapq.heappush(heap,i);
    # 그렇다면, 간선이 없는 정점들은?
    # while 위의 for문에서 이미 삽입되어 있음.
    # while문은 초기 진입차수>0인 애들을 추가로 넣어주기 위한 것이다.
            
print(*ans)