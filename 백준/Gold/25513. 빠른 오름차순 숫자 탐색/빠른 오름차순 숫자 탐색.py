# https://www.acmicpc.net/problem/25513
# 빠른 오름차순 숫자 탐색
# 그래프 탐색, bfs

input=__import__('sys').stdin.readline
deque=__import__('collections').deque

def bfs(sx,sy,goal):
    q=deque([(sx,sy)]) # row_idx,col_idx
    visited[sx][sy]=1
    
    while q:
        x,y=q.popleft()
        for dx,dy in [(-1,0),(1,0),(0,-1),(0,1)]:
            nx,ny=x+dx,y+dy
            if 0<=nx<5 and 0<=ny<5:
                if board[nx][ny]==goal:
                    return visited[x][y],nx,ny
                if board[nx][ny]!=-1 and visited[nx][ny]==0:
                    q.append((nx,ny))
                    visited[nx][ny]=visited[x][y]+1
    
    return -1,0,0

board=[[*map(int,input().split())] for _ in range(5)]
start_x,start_y=map(int,input().split())
answer=0

for target in range(1,7):
    visited=[[0]*5 for _ in range(5)]
    cur_cnt,next_x,next_y=bfs(start_x,start_y,target)
    start_x,start_y=next_x,next_y
    if cur_cnt>-1:
        answer+=cur_cnt
    else:
        print(-1)
        exit(0)

print(answer)