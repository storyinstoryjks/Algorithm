# Snakes and Ladders
# https://www.acmicpc.net/problem/16928
"""
초기 제출 코드는 출력을 잘못해서 틀렸다(젠장..)

1. 100번에 가까워지는 주사위 수를 기준으로 append 진행.
2. 사다리 또는 뱀을 만나는 경우는 횟수 카운팅 제외.
3. BFS 탐색 순서는 '최소값을 저장'해나간다.
4. 사다리를 만나면, 이동될 수를 appendleft해서 먼저 탐색하게끔 한다. (노드 탐색 줄이기)
"""
import sys
from collections import deque
input=sys.stdin.readline

def bfs(start):
    q=deque([start])
    visited[start]=0
    
    while q:
        x=q.popleft()
        if x==100:
            print(visited[100])
            return
        for dice in (6,5,4,3,2,1):
            nx=x+dice
            if 1<=nx<=100 and visited[nx]==-1:
                # ladder
                try:
                    nx=ladders[nx]
                except:
                    pass
                # snake
                try:
                    nx=snakes[nx]
                except:
                    pass
                if visited[nx]==-1:
                    visited[nx]=visited[x]+1
                    q.append(nx)
                    

n,m=map(int,input().split())
ladders={k:v for k,v in [[*map(int,input().split())] for _ in range(n)]}
snakes={k:v for k,v in [[*map(int,input().split())] for _ in range(m)]}
visited=[-1]*101

bfs(1)