# Puyo Puyo
# https://www.acmicpc.net/problem/11559
"""
이번 문제에서 터트릴 칸들을 찾는 것은 어렵지 않았다.
상하좌우로 탐색을 진행하기에, bfs를 통해 진행하면 된다.
그러나, '제거 후, 남은 칸들 이동하는 부분'에서 생각보다 시간이 꽤 걸렸다.

<1: 벽돌 탐색 및 제거 방법>
=> 그래프를 전체 순회한다.
=> 컬러칸이고, 미방문칸이면 bfs 시작정점으로 탐색 시작.
=> 트리를 그리며, 방문한 컬러의 좌표들을 list에 저장.
=> list의 길이가 4이상인가 확인 후, 제거할 좌표 리스트 반환.(조건불충족 시, [] 리턴)
=> bfs 종료후, 반환된 리스트가 []이 아니면, 제거 작업.('.'으로 값 변경)

<2: 남은 칸들 이동>
문제에서 중력이 작용하기에, 칸들은 아래로 떨어진다라고 되있다.
다시 말해, 행을 기준으로 순회하는 것이 아닌, '열을 기준으로 순회해야 한다.'
ex) 0열 : 0행 ~ 12행 / 1열 : 0행 ~ 12행 / ...

이를 파악했으면, 제거된 후의 다음의 경우들을 생각해보자.
.Y  BB
.Y  YYYY YY 
RR  GG   GG
RR  RR   GG
    RR   BB
[1] [2]  [3]

[1]
=> R로 이루어진 사각형이 제거되면 1열의 1행과 0행의 Y들이 내려와야한다.
=> R칸들은 현재 '.'으로 변경되있다.
=> '열을 역으로 순회하면서 .의 개수를 탐색하면 된다.'
=> 1행 도달했을 시, 점의 개수는 2이므로, graph[1+2][1]=Y로 진행하면된다.
=> 0행도 마찬가지로, 점의 개수는 2이므로, graph[0+2][1]=Y를 진행하면된다.

[2]도 [1]처럼 진행.

[3]
만약, 이처럼 '마지막 행에 color가 있는 경우는?'
=> '.'의 개수가 0이기에 건너띄고 다음행부터 점의 개수 카운팅을 진행하면 된다.
즉, 개수>0일때 칸 내리기 작업을 진행하면 된다.
"""

import sys
from collections import deque
input=sys.stdin.readline

def bfs(sx,sy,color):
    global n,m
    q=deque([(sx,sy)])
    visited[sx][sy]=1
    idx_list=[(sx,sy)]
    
    while q:
        x,y=q.popleft()
        for dx,dy in [(-1,0),(1,0),(0,-1),(0,1)]:
            nx=x+dx; ny=y+dy
            if 0<=nx<n and 0<=ny<m:
                if graph[nx][ny]==color and visited[nx][ny]==0:
                    visited[nx][ny]=1
                    q.append((nx,ny))
                    idx_list.append((nx,ny))
    
    return [] if len(idx_list)<4 else idx_list
    
def remove_color(l):
    for i,j in l:
        graph[i][j]='.'

def move_color():
    global n,m
    # 열 기준 순회
    for col in range(m):
        gap=0 # 점의 개수
        # 해당 열의 모든 행들 조사 시작. (역으로 진행)
        for row in range(n-1,-1,-1):
            # 점인 경우
            if graph[row][col]=='.':
                gap+=1
            # 컬러칸이고, 점의개수>0인 경우
            # (==해당 열의 n-1행이 컬러칸이 아니다 and 방금전 이동칸의 인접칸이다.)
            elif gap>0:
                graph[row+gap][col]=graph[row][col]
                graph[row][col]='.'
    
n,m=12,6
graph=[[*input()[:-1]] for _ in range(n)]
ans=0

while True:
    visited=[[0]*m for _ in range(n)]
    flag=False
    for i in range(n):
        for j in range(m):
            # 컬러 발견시
            if graph[i][j]!='.' and visited[i][j]==0:
                # 해당 컬러 시작으로 연결된 칸들 찾기.
                remove_idx_list=bfs(i,j,graph[i][j]) # 좌표 반환
                if remove_idx_list: # 4개 이상인 칸들의 묶음이면
                    flag=True
                    remove_color(remove_idx_list) # 제거 작업
    # 제거 작업을 한번도 못한 경우
    if not flag:
        break
    # 나머지 칸들 이동하기
    move_color()
    ans+=1 # 답 카운팅(연쇄 작용 카운팅)

print(ans)