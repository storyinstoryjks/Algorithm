# lab 3
# https://www.acmicpc.net/problem/17142
"""
시간 제한 걱정이 되어, pypy3로 제출했더니 정답처리 되었다.
똑같은 코드+설명+python3 제출 시도를 해본다.

처음 데모 코드 작성 후, 테스트 케이스가 몇개 맞지 않아서 문제에 대한 
세부 조건을 면밀히 생각해보게 되었다.

세부조건 1) 초기 활성화 바이러스가 비활성화 바이러스를 만날 시, 활성화 과정에서의 '시간은 노카운트'.
    => 문제에서 '빈 칸에 바이러스가 복제될 시에만 카운팅'하라고 되어있다.
    => 활성화 진행 후, '활성화된 칸을 bfs 또는 dfs로 진행하면 안된다'는 의미.
세부조건 2) 초기부터 빈칸이 없다면, '바이러스가 모두 복제된 걸로 인식'한다.
    => 즉 초기부터 빈칸이 없고, 바이러스(2)와 벽(1)으로만 구성되있다면, 답은 0.
세부조건 3) M은 초기 활성화 바이러스 개수이며, 이후에 활성화 바이러스가 비활성화 바이러스를 만나
            '현재 활성화 개수가 M+1이 되어도 상관없다.'

모든 바이러스의 경우의 수 + 가장 빠른 시간(최소) = 브루트포스 + BFS

[알고리즘]
1. M개의 활성화 바이러스 모든 경우의수를 조합을 통해 구한다.
2. 각 경우의 수를 시작정점으로 하여, 모두 BFS 탐색을 진행한다.
3. 초기 활성화 바이러스 및 비활성화->활성화 바이러스는 graph에서 3으로 표시한다.
4. 빈칸들을 탐색한다.
"""

import sys,copy
from collections import deque
from itertools import combinations
input=sys.stdin.readline

def bfs(active_birus):
    global n,m,wall_cnt
    q=deque([])
    visited=[[0]*n for _ in range(n)] # 방문 배열 + 복제 시간 카운팅 그릇
    time,change_cnt=0,0 # 복제 시간, '빈칸->바이러스로 변한 칸들 개수'
    
    for i,j in active_birus:
        q.append((i,j))
        graph[i][j]=3
        
    while q:
        x,y=q.popleft()
        # 다음 자식노드들 탐색.(상하좌우)
        for dx,dy in [(-1,0),(1,0),(0,-1),(0,1)]:
            nx=x+dx; ny=y+dy
            if 0<=nx<n and 0<=ny<n:
                # 빈칸이고, 미방문이면
                if graph[nx][ny]==0 and visited[nx][ny]==0:
                    visited[nx][ny]=visited[x][y]+1 # 방문처리 및 복제시간+1
                    change_cnt+=1 # 값 변했으므로, +1
                    time=max(time,visited[nx][ny]) # 마지막에는 모든 빈칸 복제 경우의 시간이 저장.
                    q.append((nx,ny))
                # 중요
                # 비활성화 바이러스이고, 미방문칸이면
                if graph[nx][ny]==2 and visited[nx][ny]==0:
                    # 0 2 2 0 예를 들자.
                    # 0 3 0 0 -> 1 3 '1' 0 -> 1 3 3 2
                    # 비활성화 칸을 지나가고, 초기 3 왼쪽 1을 그대로 써야되기에,
                    # 'visited은 +1을 하지만, 답 카운팅을 위한 time은 갱신하지 않는다.'
                    # 이유) 세부조건 1
                    visited[nx][ny]=visited[x][y]+1
                    q.append((nx,ny))
                    graph[nx][ny]=3
    
    # 모두 복제된 최소 시간, 남아있는 빈칸의 개수
    # 남아있는 빈칸 개수 = 전체 칸 수 - 벽 개수 - 바이러스 개수 - 빈칸이 바이러스로 변한 개수
    return time,n*n-wall_cnt-len(birus)-change_cnt
        
    
n,m=map(int,input().split())
birus,arr=[],[] # 바이러스의 모든 좌표 그릇, 그래프
ans,wall_cnt=3000,0 # 답, 초기 벽 개수.

for i in range(n):
    l=[*map(int,input().split())]
    for j in range(n):
        if l[j]==2:
            birus.append((i,j))
        if l[j]==1:
            wall_cnt+=1
    arr.append(l)

# 각 경우의 수 탐색.
for active_birus in combinations(birus,m):
    graph=copy.deepcopy(arr) # 깊은 복사
    time,empty_cnt=bfs(active_birus) # 복제하는데 걸린 시간, 빈칸의 개수
    # 빈칸 개수가 0일때
    # == 바이러스가 모두 복제되었을 경우
    if empty_cnt==0:
        ans=min(ans,time)
    
print(ans if ans!=3000 else -1)