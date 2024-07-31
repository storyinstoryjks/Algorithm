# https://www.acmicpc.net/problem/20058
# 마법사 상어와 파이어스톰
# 시뮬, 그래프 탐색
"""
난이도 : 보통~어려움
시간 : 1시간

90도 회전하는 것만 잘 생각하면 나머지는 구현 그자체여서 쉬움.
그러나, 90도 회전할 시의 '행과 열의 전치를 일반화하는 규칙 찾기가 어려웠다.'
"""
from sys import stdin
from collections import deque
scan=lambda:map(int,stdin.readline().split())

def rotate(step):
    step=2**step
    new_board=[[0]*(2**n) for _ in range(2**n)]
    
    for i in range(0,2**n,step):
        for j in range(0,2**n,step):
            # L by L
            for di in range(step):
                for dj in range(step):
                    # 전치
                    new_board[i+dj][j+(step-1)-di]=board[i+di][j+dj]
    
    return new_board

def melt_bfs(sx,sy):
    melt=0
    melting_list=[]
    q=deque([(sx,sy)])
    visited=[[0]*(2**n) for _ in range(2**n)]
    visited[sx][sy]=1
      
    while q:
        x,y=q.popleft()
        child=0
        for i in range(4):
            nx=x+dx[i]
            ny=y+dy[i]
            if 0<=nx<2**n and 0<=ny<2**n:
                if board[nx][ny]>0:
                    child+=1
                if visited[nx][ny]==0:
                    visited[nx][ny]=1
                    q.append((nx,ny))
        if child<3 and board[x][y]>0:
            melting_list.append((x,y))
            melt+=1
    
    for r,c in melting_list:
        board[r][c]-=1
    
    return melt

def area_bfs(sx,sy):
    cnt=0
    q=deque([(sx,sy)])
    history[sx][sy]=1
    
    while q:
        x,y=q.popleft()
        cnt+=1
        for i in range(4):
            nx=x+dx[i]
            ny=y+dy[i]
            if 0<=nx<2**n and 0<=ny<2**n:
                if board[nx][ny]!=0 and history[nx][ny]==0:
                    history[nx][ny]=1
                    q.append((nx,ny))
    
    return cnt

n,q=scan()
board=[]
total,melt,area=0,0,0
dx=[-1,1,0,0]
dy=[0,0,-1,1]

for _ in range(2**n):
    tmp=[*scan()]
    total+=sum(tmp)
    board.append(tmp)

for step in scan():
    board=rotate(step)
    melt+=melt_bfs(0,0)

history=[[0]*(2**n) for _ in range(2**n)]
for i in range(2**n):
    for j in range(2**n):
        if board[i][j]!=0 and history[i][j]==0:
            area=max(area,area_bfs(i,j))
            
print(total-melt)
print(area)