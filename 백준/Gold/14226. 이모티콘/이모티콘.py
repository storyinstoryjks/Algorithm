# imoticon
# https://www.acmicpc.net/problem/14226

"""
그렇게 어렵지 않게 풀었던 문제이다.

[알고리즘 선택 과정]
"3가지 연산을 통한 경우의 수들이 트리와 같이 그려진다."
=> 그래프를 그릴 수 있다.
=> 부모노드-자식노드(3개)가 존재한다.
=> 그러므로, 그래프 탐색 적용!

"답 유형이 최소를 물어본다."
=> 그래프에서 최적의 해를 보장해야 한다.
=> 자식 노드 탐색을 레벨 순회 형식으로 진행해야 한다.
=> 그러므로, bfs 탐색 적용!

[키포인트]
1. memozation 기법 필요.
=> 같은 수가 반복적으로 나올 수 있기 때문. (동일한 데이터 필드의 노드들 반복 존재 가능성)
=> DP로도 가능하지 않을까..?

2. 방문 배열 설정
=> 동일한 노드의 데이터 필드는 어떤 형식일까?
=> 화면의 개수만 같다고 판단하면 되는 것일까?
=> No!
=> 화면의 개수도 같고, 클립보드 개수도 같아야 반복된 노드라고 할 수 있다.
=> 그러므로, visited[화면][클립보드]로 설정해야 한다.
"""
import sys
from collections import deque
input=sys.stdin.readline

def bfs(S):
    q=deque([(1,0,0)]) # screen,clipboard,time
    visited=[[0]*1001 for _ in range(1001)]
    visited[1][0]=1
    
    while q:
        scr,clip,time=q.popleft()
        if scr==S:
            return time
        # 1번연산, 2번연산, 3번연산 자식노드 차례로 순회
        for nScr,nClip in [(scr,scr),(scr+clip,clip),(scr-1,clip)]:
            # 화면수 및 클립보드 수가 범위 내이고, 미방문이면
            if 0<=nScr<1001 and 0<=nClip<1001 and visited[nScr][nClip]==0:
                visited[nScr][nClip]=1
                q.append((nScr,nClip,time+1))

S=int(input())
print(bfs(S))