# Mothers Milk
# https://www.acmicpc.net/problem/2251

"""
수학계산을 필요로 하는 문제.
그렇게 어렵지는 않으나, 수식을 생각하는 요령이 필요하다.

1. 물을 옮기는 방법의 수는?
=> a->b / a->c / b->a / b->c / c->a / c->b : 총 6가지.
=> 하나의 상황에서 6가지씩 생기는 형식.
=> 즉, 부모-자식 관계를 지니므로, 그래프(트리) 표현 가능.
=> dfs bfs 모두 가능. 최적의 해를 보장하는 bfs 선택.

2. 옮기는 과정에서의 물 용량은?
=> 얼만큼 옮길 수 있는가를 생각해보자.
=> a->b로 예를 들자.
=> a물통에 차있는 모든 물을 옮길 수 있다.(1) vs b물통에 현재 들어있는 양 + a물통의 일부분(2)
=>  (1),(2) 중 더 작은 수를 선택하면 된다.
=> (1)의 경우: (a,b)=(8,0) : a물통에 들어있는 8L를 b에 다 옮길 수 있다.
=> (2)의 경우: (a,b)=(8,2) : a물통에 들어있는 7L를 통해 B물통 최대용량 9L를 채울 수 있다.

3. bfs이므로, 큐 원소 설정은?
=> a,b만 알면, c에 들어있는 용량을 알 수 있다.
=> '초기상태는 항상 0,0,n 이기 때문'
=> 현재 들어있는 c물통의 용량 z = c물통의 최대용량(n) - a물통에 들어있는 현재양(x) - b물통에 들어있는 현재양(y)
=> 즉, 큐 원소의 형식은 (a물통에 들어있는 양, b물통에 들어있는 양) 으로 설정할 수 있다.
=> 물론, (a,b,c) 형식으로 할 수 있으나, 그만큼 메모리 부담이 된다.
=> 이를 바탕으로, 중복노드 제거를 위한 방문배열 visited의 형식도 visited[a물통 현재용량][b물통 현재용량]으로 설정하면 된다.
"""
import sys
from collections import deque
input=sys.stdin.readline

def move(e1,e2):
    if visited[e1][e2]==0:
        visited[e1][e2]=1
        q.append((e1,e2))
        
def bfs(a,b,c,L):
    visited[0][0]=1
    
    while q:
        x,y=q.popleft() # a물통, b물통 각 현재 물 용량
        z=c-x-y # c물통 현재 물 용량
        if x==0:
            L.append(z)
        # a->b
        water=min(x,b-y)
        move(x-water,y+water)
        # a->c
        water=min(x,c-z)
        move(x-water,y) # 큐 원소는 a,b만 따지므로, c는 따질필요 없음. (a->c이므로, y변화없음.)
        # b->a
        water=min(y,a-x)
        move(x+water,y-water)
        # b->c
        water=min(y,c-z)
        move(x,y-water) # //
        # c->a
        water=min(z,a-x)
        move(x+water,y) # //
        # c->b
        water=min(z,b-y)
        move(x,y+water) # //
    
    return L

a,b,c=map(int,input().split())
visited=[[0]*(b+1) for _ in range(a+1)]
q=deque([(0,0)])

ans=bfs(a,b,c,[])
ans.sort()
print(*ans)