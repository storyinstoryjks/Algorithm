# prime path
# https://www.acmicpc.net/problem/1963

"""
어렵지 않은 문제.
핵심은 소수 판별을 어떻게 할 것인가이다.

에라토스테네스의 체를 이용하여, 9999까지의 소수를 미리 구해놓는다.
bfs 탐색으로 자식노드를 탐색시 이를 활용.
"""
import sys
from collections import deque
input=sys.stdin.readline

def Eratosthenes():
    # 10000의 제곱근까지만 순회.
    for i in range(2,101):
        if prime_list[i]:
            # i의 배수들 제거
            for j in range(i*i,10001,i):
                prime_list[j]=False

def bfs(sv,ev):
    q=deque([(sv,0)])
    visited=[0]*10001
    visited[sv]=1
    
    while q:
        target,cnt=q.popleft()
        if target==ev:
            print(cnt)
            return
        # 1000
        f,r=target//1000,target%1000
        for i in range(1,10):
            if i==f: continue
            nv=(i*1000)+r
            if prime_list[nv] and visited[nv]==0:
                visited[nv]=1
                q.append((nv,cnt+1))
        # 100
        f,r=(target%1000)//100,target-(((target%1000)//100)*100)
        for i in range(10):
            if i==f: continue
            nv=(i*100)+r
            if prime_list[nv] and visited[nv]==0:
                visited[nv]=1
                q.append((nv,cnt+1))
        # 10
        f,r=((target%1000)%100)//10,target-((((target%1000)%100)//10)*10)
        for i in range(10):
            if i==f: continue
            nv=(i*10)+r
            if prime_list[nv] and visited[nv]==0:
                visited[nv]=1
                q.append((nv,cnt+1))
        # 1
        f,r=((target%1000)%100)%10,target-(((target%1000)%100)%10)
        for i in range(10):
            if i==f: continue
            nv=i+r
            if prime_list[nv] and visited[nv]==0:
                visited[nv]=1
                q.append((nv,cnt+1))
    
    print("Impossible")

prime_list=[True]*10001
Eratosthenes()

for _ in range(int(input())):
    start,end=map(int,input().split())
    bfs(start,end)