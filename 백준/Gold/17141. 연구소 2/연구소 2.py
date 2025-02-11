# https://www.acmicpc.net/problem/17141
# 연구소2
# 그래프탐색, bfs, 브루트포스

from sys import stdin 
from collections import deque
from itertools import combinations
input=stdin.readline

def bfs(init_virus):
    q=deque([(x,y,0) for x,y in init_virus]) # virus_idx_x, virus_idx_y, time(==depth)
    visited=[[0]*n for _ in range(n)]
    for x,y in init_virus:
        visited[x][y]=1
    
    state_blank,state_time=0,0
    while q:
        x,y,depth=q.popleft()
        state_time=max(state_time,depth)
        for dx,dy in [(-1,0),(1,0),(0,-1),(0,1)]:
            nx,ny=x+dx,y+dy
            if 0<=nx<n and 0<=ny<n:
                if board[nx][ny]!=1 and visited[nx][ny]==0:
                    visited[nx][ny]=1
                    q.append((nx,ny,depth+1))
                    state_blank+=1
    
    return state_time, [False,True][state_blank==total_blank-m]

n,m=map(int,input().split())
candidates,board=[],[]
total_blank=0
answer=-1

for i in range(n):
    tmp=[*map(int,input().split())]
    for j in range(n):
        if tmp[j]==2:
            candidates.append((i,j))
        if tmp[j]!=1:
            total_blank+=1
    board.append(tmp)
    
for cur_candidate in combinations(candidates,m):
    time,flag=bfs(cur_candidate)
    if flag:
        if answer==-1:
            answer=time
        else:
            answer=min(answer,time)

print(answer)