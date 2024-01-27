# 13549

""" 메모리 초과
import sys
from collections import deque
input=sys.stdin.readline

def bfs():
    q=deque([n])
    while q:
        v=q.popleft()
        if v==k:
            return path[v]
        for i in (v-1,v+1,2*v):
            if 0<=i<100001:
                if i==2*v and path[i]==0:
                    path[i]=path[v]
                if path[i]==0:
                    path[i]=path[v]+1
                q.append(i)
                
n,k=map(int,input().split())
path=[0 for _ in range(100001)]
print(bfs())"""

""" 시간초과
import sys
from collections import deque
input=sys.stdin.readline

def bfs():
    q=deque([(n,0)])
    c=[]
    while q:
        v,cnt=q.popleft()
        if v==k:
            return cnt
        for i in (v-1,v+1,2*v):
            if 0<=i<100001 and i not in c:
                if i==2*v:
                    q.append((i,cnt))
                else:
                    q.append((i,cnt+1))
                c.append(v)
                
n,k=map(int,input().split())
print(bfs())"""

"""
위의 2개의 코드에서 각각 메모리초과와 시간초과 발생.
=> 3개의 자식 노드를 순차적으로 탐색 시, 큐 메모리 증가
=> 반대로, closed 리스트를 활용하여 가중치를 저장해나가는 방법은 for문 하나가 더 들어가므로 시간초과.

<해결>
=> 순간이동을 이용하여 탐색을 하면 탐색범위가 좁아짐.
=> 큐의 메모리를 감소시키고, for문을 안쓰는 방법은 '순간이동 노드를 먼저 탐색 진행'하면 된다.
"""

import sys
from collections import deque
input=sys.stdin.readline

def bfs():
    q=deque([n])
    while q:
        v=q.popleft()
        if v==k:
            return path[v]
        for i in (v-1,v+1,2*v):
            if 0<=i<100001 and path[i]==-1:
                if i==2*v:
                    path[i]=path[v]
                    q.appendleft(i)
                else:
                    path[i]=path[v]+1
                    q.append(i)
                
n,k=map(int,input().split())
path=[-1 for _ in range(100001)]
path[n]=0
print(bfs())