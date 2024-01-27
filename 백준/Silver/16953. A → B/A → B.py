# 16953 : A->B

import sys
from collections import deque
input=sys.stdin.readline

def bfs(x):
    q=deque([(x,1)])
    while q:
        x,c=q.popleft()
        t=int(str(x)+"1")
        k=2*x
        if x==b:
            return c
        if t<=b:
            q.appendleft((t,c+1))
        if k<=b:
            q.append((k,c+1))
    return -1

a,b=map(int,input().split())
print(bfs(a))