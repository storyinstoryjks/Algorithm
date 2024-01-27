#2644 : Find Ancestor
"""
    [알고리즘]
    => 조상-부모-자손 관계이므로, 그래프 형식은 트리.
    => 2명의 촌수관계 파악을 위해서는 그래프 탐색 필요.
    => 항렬관계와 비항렬관계를 통해 촌수가 구분됨.
    => 같은 항렬(ex 형제)이면, 무조건 2촌 관계임. (1촌+1촌)
    => 즉, 항렬관계는 무조건 2촌, 비항렬관계는 타겟들이 트리에 존재하는 '해당 그래프의 깊이'를 더하면됨.(ex 3: 깊이1, 7: 깊이2)
    => 단, 같은 가문이 아니면 무조건 -1.
    
    이에 따른 알고리즘 제약조건은 다음과 같다.
    
    1. 같은 가문인가
    2. 같은 항렬인가
    3. 문제의 요구 시간은 1초. 즉 O(T) <= O(n)
    
    그러므로, 알고리즘 설계는 다음과 같다.
    
    => 제약조건 1번은 '같은 트리'인가를 확인. 이는 해당 노드까지의 '경로'를 바탕으로 파악.
        (같은 가문이라면, 트리의 루트가 같을 수 밖에 없기 때문.)
    => 제약조건 2번은 '촌수가 서로 같은가'를 확인. 촌수가 같다==그래프 깊이가 같다==한번의탐색 결과값은 1개이다.
    => 제약조건 3번은 맹목적 그래프 탐색 기법 DFS와 BFS 중 DFS를 선택.
    => 또한, O(n)의 시간을 위해서는 '최대한 한 반복문 내에서 1~2번 제약조건들을 파악해야함.'
    
    즉, 핵심은 "한 트리 내에 타켓 노드들이 모두 존재하며, 타켓노드~타켓노드2까지의 경로 길이"이다.
"""

import sys
sys.setrecursionlimit(10**6)
input=sys.stdin.readline

def dfs(x,cnt):
    visited[x]=1
    cnt+=1 # 부모 깊이 + 1 = 현재 깊이
    
    if x==target2:
        ans.append(cnt)
    
    for i in graph[x]:
        if not visited[i]:
            dfs(i,cnt)

n=int(input())
target1,target2=map(int,input().split())
graph=[[] for _ in range(n+1)]
visited=[0 for _ in range(n+1)]
ans=[]

for _ in range(int(input())):
    start,end=map(int,input().split())
    graph[start].append(end)
    graph[end].append(start)

dfs(target1,0)
        
print(-1 if len(ans)==0 else ans[0]-1)