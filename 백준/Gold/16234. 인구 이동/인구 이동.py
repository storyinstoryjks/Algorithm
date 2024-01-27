# 16234 : Migrate
"""
[분석]
<1. 그래프 탐색 DFS vs BFS>
=> 인접한 칸을 계속 이어나가는 형태로써 '자식 노드들을 모두 찾으면서 가야한다'
=> 다시 말해, 인접한 가까운 후보 연합국들을 전부 파악하면서 진행해야한다.
=> 가장 중요한 것은 '최대 또는 최소를 신경쓰지 않고, 자식 노드들을 탐색'하는 것이기에,
=> 어떤 방법을 써도 상관없다.
=> 그렇기에, 데이터의 흐름 파악이 조금 더 편한 BFS 선택.

<2. 인구 이동 분석>
다음의 경우를 보자(탐색 순서 0행 0열부터 오름차순)
10 100 20 90
80 100 60 70
70 20 30 40
50 20 100 10

연합 바탕 갱신 후
10 100 53 53
53 53 53 53
53 53 53 53
53 20 100 53

다음 탐색할 idx=(i,j)가 현재 (1,0)이라고 하자.
자신의 자식인 (0,0)과 국경선을 다시 열어 갱신가능하다는 것을 알 수 있다.
이 부분을 통해 '이중 반복문을 통해 그래프 탐색 시, 이중 반복문은 한번으로 충분한가'에 대한 생각을 가지게 된다.
만약, (1,0) 전에 이런 상황이 발생한다면?
이중반복문을 한번만 써서는 파악되지 않는다. 그렇기에 반례를 찾아보려 했으나 쉽지 않았다.

그렇기에 관점을 바꿔 문제읽기에 집중해보았다.
"인구 이동은 하루동안 진행. 나라는 국경선을 오늘 하루 동안 연다."
이를 풀어서 다음과 같이 생각하였더니 이중반복문 횟수 문제도 해결되었다.
"연합은 하루에 한번이루어진다."

즉, 인구수 갱신 이후, 다음 연합을 찾는 것은 다음 이중반복문때 진행하면 된다는 것이기에,
이중반복문을 while 안으로 집어넣고 국경선을 열수없으면(연합 가능 나라들이 없다면) break를 하면 된다.
결국, while문 한번은 하루를 의미한다.

[알고리즘]
1. 방문하지 않은 나라(노드)라면, bfs탐색 시작.
2. 연합 국가가 없다면, 1번으로 스킵.
3. 연합 국가가 존재한다면, 갱신
4. 모든 국가가 국경선을 닫거나, 연합 불가능하다면 정답 출력.
"""

import sys
from collections import deque
input=sys.stdin.readline

def bfs(x,y):
    q=deque([(x,y)])
    tmp=[(x,y)]
    
    while q:
        x,y=q.popleft()
        for i in range(4):
            nx=x+dx[i]
            ny=y+dy[i]
            if 0<=nx<n and 0<=ny<n:
                if visited[nx][ny]==0 and l<=abs(graph[nx][ny]-graph[x][y])<=r:
                    visited[nx][ny]=1
                    q.append((nx,ny))
                    tmp.append((nx,ny))
    return tmp
        
n,l,r=map(int,input().split())
graph=[[*map(int,input().split())] for _ in range(n)]
ans=0
dx=[-1,1,0,0]
dy=[0,0,-1,1]

while True:
    visited=[[0]*n for _ in range(n)] # 하루동안, 연합을 이루는지 확인할 방문 리스트.
    flag=0 # 하루동안, 연합국가 있는지 확인을 위한 플래그.
    for i in range(n):
        for j in range(n):
            # 해당 국가 인구수 확인 전이라면
            if not visited[i][j]:
                visited[i][j]=1 # 확인 처리
                country=bfs(i,j) # 해당 국가를 기준으로 연합 후보들 확인하기.
                lenTry=len(country) # 연합 국가수 저장.
                # 연합 국가가 최소 2군데 이상이라면
                if lenTry>1:
                    flag=1 # 인구이동 가능.
                    newCnt=sum([graph[x][y] for x,y in country])//lenTry
                    for x,y in country:
                        graph[x][y]=newCnt
    
    # 인구 이동이 가능한 연합 국가가 없다면, 더이상 없는 거임.
    if flag==0:
        break
    # 오늘 하루, 인구이동 진행했으므로, +1 및 다음 날로 이동.
    ans+=1
    
print(ans)