# Find me! : https://www.acmicpc.net/problem/13913

"""
경로 찾는 부분이 은근 헷갈린다.
=> path 배열에 경로를 찾아갈 수 있도록 값을 설정해야함.
=> path 배열을 q에 넣어버리면, 각 노드마다 path 배열을 가지므로 메모리 낭비.
=> 10만개의 원소를 지니는 path 배열 생성.
=> path의 인덱스는 자식노드 정점이 되며, 값은 부모노드 정점이 된다.
ex) path의 16번 인덱스의 값은 8이다. == 16의 부모는 8이다.
=> 즉 정답 출력시, '거꾸로'해야한다.
"""

from collections import deque

def path(x):
    arr = []
    temp = x
    for _ in range(dist[x]+1):
        arr.append(temp)
        temp = move[temp]
    print(' '.join(map(str, arr[::-1])))

def bfs():
    q = deque()
    q.append(N)
    while q:
        x = q.popleft()
        if x == K:
            print(dist[x])
            path(x)
            return x
        for i in (x+1, x-1, 2*x):
            if 0<=i<=100000 and dist[i]==0:
                q.append(i)
                dist[i] = dist[x] + 1
                move[i] = x

N, K = map(int, input().split())
dist = [0]*100001
move = [0]*100001
bfs()