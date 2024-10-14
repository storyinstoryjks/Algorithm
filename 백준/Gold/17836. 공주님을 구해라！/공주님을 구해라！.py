# https://www.acmicpc.net/problem/17836
# 공주님을 구해라

"""
검을 찾는 경우와 그렇지 않은 경우 2가지에 한해 경로를 탐색해야하기에,
방문 배열을 3차원으로 구성.
""" 
    
from sys import stdin 
from collections import deque
input=stdin.readline

def bfs(sx,sy):
    q=deque([(sx,sy,0)]) # x,y,sword
    visited[sx][sy][0]=1
    visited[sx][sy][1]=1
    
    while q:
        x,y,sword=q.popleft()
        for i in range(4):
            nx=x+dx[i]
            ny=y+dy[i]
            if 0<=nx<n and 0<=ny<m:
                if sword:
                    if board[nx][ny] in [0,1] and visited[nx][ny][1]==0:
                        visited[nx][ny][1]=visited[x][y][1]+1
                        q.append((nx,ny,sword))
                elif board[nx][ny]==0 and visited[nx][ny][0]==0:
                    visited[nx][ny][0]=visited[x][y][0]+1
                    q.append((nx,ny,sword))
                elif board[nx][ny]==2 and visited[nx][ny][0]==0:
                    visited[nx][ny][1]=visited[x][y][0]+1
                    q.append((nx,ny,1))
    


n,m,t=map(int,input().split())
board=[[*map(int,input().split())] for _ in range(n)]
visited=[[[0,0] for _ in range(m)] for _ in range(n)]
dx,dy=[-1,1,0,0],[0,0,-1,1]

bfs(0,0)

cnt=visited[n-1][m-1].count(0)
if cnt==2:
    print('Fail')
elif cnt==1:
    tmp=(visited[n-1][m-1][0] or visited[n-1][m-1][1])-1
    print('Fail' if tmp>t else tmp)
else:
    tmp=min(visited[n-1][m-1][0],visited[n-1][m-1][1])-1
    print('Fail' if tmp>t else tmp)