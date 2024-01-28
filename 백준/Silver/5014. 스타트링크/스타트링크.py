# 5014 : StartLink
"""
층 : 정점번호
간선 : Up Down
= 이진트리

최소를 구하는 문제 => 트리를 그리는 중 발견시, 정답 출력.
즉, 레벨 순회 형식으로 트리 그려야함.
= BFS (queue 사용)

Tip) 같은 트리의 높이에서 중복 노드 제거!
예) 10 1 10 2 1
<트리 모양> - 0층은 존재하지 않지만, 설명을 위해 삽입
    1
   3   0   
  5 2  2
=> root노드 깊이를 0으로 가정
=> level 2(5 2 2) 부분에서 마지막 2 노드는 할 필요 없음.
=> 즉, 방문여부 배열 cnt의 값이 0보다 크면 탐색 대상에서 제외.
=> ex) 3 : 자식노드 5,2에 해당되는 cnt[5]=cnt[3]+1, cnt[2]=cnt[3]+1을 진행하게 됨.
=> 이후, 0 : 자식노드 2 확인시, cnt[2]>0이므로, 탐색 대상에서 제외.
"""
import sys
from collections import deque
input=sys.stdin.readline

def bfs():
    global f,g
    
    while q:
        v=q.popleft()
        if v==g:
            return cnt[v]
        # 자식 노드 탐색
        for e in direction:
            # 간선 존재하지 않으면, 스킵
            if e==0: continue
            nv=v+e # 자식노드
            # 자식노드가 유효층이고, 방문하지 않은 노드라면
            if 1<=nv<=f and cnt[nv]==0:
                cnt[nv]=cnt[v]+1 # 정답 카운팅 : 이전층 높이 + 1(=현재까지 버튼수 + 1)
                q.append(nv)
                
    return -1

f,s,g,u,d=map(int,input().split())
q=deque([s])
direction=[u,-d]
cnt=[0]*(f+1) # 버튼 카운팅(트리 높이) + 각 정점 방문여부

# 현재 층 == 목표 층
if s==g:
    print(0)
# (현재층이 목표층보다 높은데, 내려갈수가 없음) 또는 (현재층이 목표층보다 낮은데, 올라갈수가없음)
elif (s>g and d==0) or (s<g and u==0):
    print("use the stairs")
else:
    ans=bfs() # 탐색
    print(ans if ans!=-1 else "use the stairs")