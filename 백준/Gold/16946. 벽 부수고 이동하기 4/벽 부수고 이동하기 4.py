# https://www.acmicpc.net/problem/16946
# 벽 부수고 이동하기 4

"""
각 벽에서 bfs를 돌려, 이동거리를 구하는 풀이 방식
=> 시간 초과

from sys import stdin
from collections import deque
input=stdin.readline

def bfs(sx,sy):
    q=deque([(sx,sy)])
    visited=[[0]*m for _ in range(n)]
    visited[sx][sy]=1
    
    while q:
        x,y=q.popleft()
        for i in range(4):
            nx=x+dx[i]
            ny=y+dy[i]
            if 0<=nx<n and 0<=ny<m:
                if board[nx][ny]=='0' and visited[nx][ny]==0:
                    visited[nx][ny]=1
                    q.append((nx,ny))
                    ans[sx][sy]+=1
                    
    ans[sx][sy]+=1


n,m=map(int,input().split())
board,idxs=[],set()
ans=[[0]*m for _ in range(n)]
dx,dy=[-1,1,0,0],[0,0,-1,1]

for i in range(n):
    l=[*input()][:-1]
    for j in range(m):
        if l[j]=='1':
            idxs.add((i,j))
    board.append(l)

for i,j in idxs:
    bfs(i,j)
    
for i in range(n):
    for j in range(m):
        print(ans[i][j]%10,end="")
    print()
"""

"""
벽이 아닌 곳의 영역을 그룹화하고, 각 벽에 해당되는 영역들의 0개수를 모두 더해주는 방식
"""

from collections import deque
input=__import__('sys').stdin.readline

def bfs(sx,sy):
    q=deque([(sx,sy)])
    zero_cnt=1
    visited_zero[sx][sy]=1
    
    while q:
        x,y=q.popleft()
        zeros[x][y]=group_num
        for i in range(4):
            nx,ny=x+dx[i],y+dy[i]
            if 0<=nx<n and 0<=ny<m:
                if board[nx][ny]==0 and visited_zero[nx][ny]==0:
                    visited_zero[nx][ny]=1
                    q.append((nx,ny))
                    zero_cnt+=1
    
    return zero_cnt
    
n,m=map(int,input().split())
board=[[*map(int,input().strip())] for _ in range(n)]
visited_zero=[[0]*m for _ in range(n)]
zeros=[[0]*m for _ in range(n)]
group={}
group_num=1
group[0]=0
dx,dy=[-1,1,0,0],[0,0,-1,1]

# 0끼리 붙어있는 영역 구분 및 그 영역의 개수 찾기
for i in range(n):
    for j in range(m):
        if board[i][j]==0 and visited_zero[i][j]==0:
            c=bfs(i,j)
            group[group_num]=c
            group_num+=1

# 각 벽에 대해 어떤 0 영역들이 있는지 찾고, 각 영역의 0개수를 더하기
for i in range(n):
    for j in range(m):
        what_groups=set() # 상하가 같은 영역인 경우? 중복해서 더하면 안됨!
        if board[i][j]==1:
            for k in range(4):
                nx,ny=i+dx[k],j+dy[k]
                if 0<=nx<n and 0<=ny<m:
                    what_groups.add(zeros[nx][ny])
            for each_group_num in what_groups: # 각 벽의 상하좌우 각 영역에 해당되는 0의 개수 더하기
                board[i][j]+=group[each_group_num]
            board[i][j]%=10

for i in board:
    print("".join(map(str,i)))