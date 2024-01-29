# DSLR - https://www.acmicpc.net/problem/9019
"""
문제 풀기 전, '맞힌 사람' 칸에서 python3 정답자가 많이 없다.
그래서 pypy3로 도전.

이 문제의 핵심은 '자리수 분리'이다.
=> str은 간편하지만, O(n)이 걸릴 때도 있음.
=> 안전하게 '수식'을 통해 O(1)을 선택.
=> 주의점 : L,R 시 0의 위치.
=> 예) 123 (L: 1230=0+123*10) (R: 3012=12+3*1000)
=> 알고리즘 순서는 DSLR 순대로 Q에 삽입 진행.

(추후 python3 도전시 참고)
=> BFS + DP (+BitMask)로 하면 python3로 풀릴 것 같음.
=> 나중에 도전해보자.
"""
# DSLR - https://www.acmicpc.net/problem/9019

import sys
from collections import deque
input=sys.stdin.readline

def bfs(a,b,visited):
    q=deque([(a,"")])
    visited[a]=1
    
    while q:
        n,command=q.popleft()
        if n==b:
            return command
        # D
        t=(n*2)%10000
        if visited[t]==0:
            q.append((t,command+"D"))
            visited[t]=1
        # S
        t=(n-1)%10000
        if visited[t]==0:
            q.append((t,command+"S"))
            visited[t]=1
        # L
        t=(n//1000)+(n%1000)*10
        if visited[t]==0:
            q.append((t,command+"L"))
            visited[t]=1
        # R
        t=(n//10)+(n%10)*1000
        if visited[t]==0:
            q.append((t,command+"R"))
            visited[t]=1
    
for _ in range(int(input())):
    a,b=map(int,input().split())
    visited=[0 for _ in range(10001)]
    print(bfs(a,b,visited))