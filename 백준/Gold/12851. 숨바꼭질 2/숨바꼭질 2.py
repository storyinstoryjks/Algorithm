# Find 2
# https://www.acmicpc.net/problem/12851
"""
-,+,*로 나오는 수가 같으면 제외시켜야하는줄 알았다..
이것때문에 시간이 오래 걸렸다 ㅜ

'나올 수 있는 모든 경로는 같은 수라도 -,+,* 구성이 다르면 탐색을 해줘야 한다.'
즉, 이전 지점에서 다른 연산 방식으로 같은 수가 나오더라도 카운팅 해야함.
ex)
1 10
    1
  0 2(+) 2(*)
  ...
이 경우, 2로 가는 경로가 2개인 것이다.
1개의 방문(거리) 배열로 어떻게 구분할까?
=> + 탐색 후, * 탐색 순서로 진행된다고 가정.
=> + 때, visited[2]=0+1 저장.
=> * 때, visited[2]=0+1로 똑같음.
즉, visited[한 자식노드] == visited[부모노드]+1인 경우도 q에 삽입하면 됨.
    (==한 자식노드의 길이가 존재하는데, 같은 레벨의 다른 자식노드에서 갱신된거면)
"""
import sys
from collections import deque
input=sys.stdin.readline

def bfs(start,target):
    q=deque([start])
    visited[start]=0
    cnt,total=0,0
    
    while q:
        #print(q)
        x=q.popleft()
        # 최단 길이의 최초 경로가 발견된 후, 최초 경로의 target 레벨보다 더 높으면
        # 더이상 탐색 필요없음.
        if cnt!=0 and cnt<visited[x]:
            break
        if x==target:
            cnt=visited[x]
            total+=1
            continue
        for nv in (x-1,x+1,x*2):
            # 생략 and 
            # (최초 방문이거나, 연산결과에 해당되는 거리는 갱신되었으나 '같은 레벨의 다른 연산 자식이라면')
            if 0<=nv<=100000 and (visited[nv]==-1 or visited[nv]==visited[x]+1):
                visited[nv]=visited[x]+1
                q.append(nv)
    
    return cnt,total


n,k=map(int,input().split())
visited=[-1]*100001

ans0,ans1=bfs(n,k)
print(ans0)
print(ans1)