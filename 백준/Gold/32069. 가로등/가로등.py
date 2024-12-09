# https://www.acmicpc.net/problem/32069
# 가로등
# 정렬, 그래프 탐색

"""
기존 코드는 가로등의 기준으로 전,중간,후 3가지 범위를 바탕으로, 각 범위를 for문을 돌려 거리를 비교 저장하는 방식.
그러나, 메모리 초과가 나옴.

가로등을 큐에 넣어, +1,-1 위치를 BFS로 탐색하여, 거리를 저장.
방문한 위치는 큐에 삽입하지 않도록 하여, '최단 경로를 보장.'
이 때, BFS 탐색은 k번까지만 진행.

* 왜 k번까지만 탐색을 진행할까?
가장 작은 거리를 출력해야하기 때문에, 이미 방문했던 애들이 가장 작은 거리들의 위치 후보이다.
그러므로, 방문한 위치의 총수==k번이라고 할 수 있다.
"""

deque=__import__('collections').deque
input=__import__('sys').stdin.readline

def bfs():
    cnt=0
    while q:
        x=q.popleft()
        cnt+=1
        t,a=x-1,x+1
        # 왼쪽
        if t>=0 and t not in visited:
            visited.add(t)
            light[t]=light[x]+1
            q.append(t)
        # 오른쪽
        if a<=l and a not in visited:
            visited.add(a)
            light[a]=light[x]+1
            q.append(a)
        if cnt==k:
            break
    
l,n,k=map(int,input().split())
lights=[*map(int,input().split())]

q=deque()
visited=set()
light={} # {위치:어두운정도}

for i in range(n):
    light[lights[i]]=0
    visited.add(lights[i])
    q.append(lights[i])

bfs()

print('\n'.join(map(str,[i for _,i in sorted(light.items(),key=lambda x:x[1])][:k])))