# https://www.acmicpc.net/problem/23747
# 와드
# 시뮬,그래프탐색

"""
[알고리즘]
1. 시뮬레이션 상황대로 구현.
2. 와드 설치 시, BFS 탐색을 통해 같은 영역 시야 확보 처리.
"""

deque=__import__('collections').deque
input=__import__('sys').stdin.readline

dx={i:j for i,j in zip('UDLR',[-1,1,0,0])}
dy={i:j for i,j in zip('UDLR',[0,0,-1,1])}

def bfs(sx,sy):
    q=deque([(sx,sy)])
    wards[startX][startY]='.' # 와드 설치된 칸
    
    while q:
        x,y=q.popleft()
        for ddx,ddy in [(-1,0),(1,0),(0,-1),(0,1)]:
            nx=x+ddx
            ny=y+ddy
            if 0<=nx<r and 0<=ny<c:
                # 와드 설치칸과 같은 영역이고, 시야 체크하지 않은 첫 방문이라면
                if board[nx][ny]==board[sx][sy] and wards[nx][ny]=='#':
                    wards[nx][ny]='.'
                    q.append((nx,ny))
                    

r,c=map(int,input().split())
board=[[*input()][:-1] for _ in range(r)]
wards=[['#']*c for _ in range(r)]
startX,startY=map(int,input().split())
startX-=1; startY-=1

# 시뮬레이션
for dir in input()[:-1]:
    # 와드를 놓고
    if dir=='W':
        if wards[startX][startY]=='.': # 시야 확보 했던 칸이라면, 스킵
            continue
        bfs(startX,startY) # 설치된 와드의 해당 영역 탐색
        continue
    startX,startY=startX+dx[dir],startY+dy[dir]

# 최종 위치와 그 인접칸들은 무조건 시야 확보.
wards[startX][startY]='.'
for dir in 'UDLR':
    nx,ny=startX+dx[dir],startY+dy[dir]
    if 0<=nx<r and 0<=ny<c:
        wards[nx][ny]='.'

for row in wards:
    print(''.join(row))