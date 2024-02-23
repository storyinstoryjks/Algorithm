# Dungeon Master
# https://www.acmicpc.net/problem/6593
"""
배열 구조가 3차원이라서 구현이 헷갈릴 뿐, 문제는 어렵지 않다.

1. 3차원 공간이므로, xyz좌표계 필요.
    => graph 및 visited을 3차원 배열로 설정.
    => graph[층수][해당 층의 x좌표][해당 층의 해당 x의 y좌표]
    => ex) graph[2][0][1] : 2층에서 0번째줄의 1번째 요소.
2. 최단 시간을 구하는 방법?
    => 그래프의 높이가 최대한 짧은 경우에서 최적의 해를 구하는 것이 필요.
    => 레벨순회가 필요하므로, bfs 그래프 탐색 진행.
3. 탐색 방법은?
    => 다음 이동할 자식노드들(동서남북상하)은 그래프 범위 내이고,
    => 미방문이라면,
    => 해당 자식노드의 부모노드에 저장된 시간+1 (where : visited)
    => 즉 visited 값이 0이면 미방문 상황이고, 1이상이면 방문됨과 동시에 '대상좌표까지의 최단시간을 나타냄'.
"""
import sys
from collections import deque
input=sys.stdin.readline

def bfs(sx,sy,sz,L,R,C):
    global goalX,goalY,goalZ
    q=deque([(sx,sy,sz)])
    visited[sz][sx][sy]=1
    
    while q:
        x,y,z=q.popleft()
        if x==goalX and y==goalY and z==goalZ:
            print(f"Escaped in {visited[z][x][y]-1} minute(s).")
            return
        # 순서대로, 동서남북상하
        for dx,dy,dz in [(0,1,0),(0,-1,0),(1,0,0),(-1,0,0),(0,0,1),(0,0,-1)]:
            nx=x+dx; ny=y+dy; nz=z+dz;
            # 그래프 범위 내이고
            if 0<=nx<R and 0<=ny<C and 0<=nz<L:
                # 금(벽)이 아니며, 방문하지 않은 자식노드이면
                if graph[nz][nx][ny]!='#' and visited[nz][nx][ny]==0:
                    visited[nz][nx][ny]=visited[z][x][y]+1 # 방문처리 및 최단 시간 갱신
                    q.append((nx,ny,nz))
                    
    print("Trapped!")
    
while True:
    L,R,C=map(int,input().split())
    if L==R==C==0:
        break
    graph=[]
    startX,startY,startZ=0,0,0 # start index
    goalX,goalY,goalZ=0,0,0 # goal index
    visited=[[[0]*C for _ in range(R)] for _ in range(L)]

    for k in range(L):
        t=[]
        for i in range(R):
            l=[*input()][:-1]
            for j in range(C):
                if l[j]=='S':
                    startX=i; startY=j; startZ=k
                if l[j]=='E':
                    goalX=i; goalY=j; goalZ=k
            t.append(l)
        graph.append(t)
        trash=input() # empty line : garbage
    
    bfs(startX,startY,startZ,L,R,C)
