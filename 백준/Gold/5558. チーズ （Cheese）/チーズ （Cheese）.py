# https://www.acmicpc.net/problem/5558
# Cheese
# 그래프 탐색

deque=__import__('collections').deque
input=__import__('sys').stdin.readline

def bfs(starts,targets):
    q=deque([starts])
    visited=[[0]*w for _ in range(h)] # 방문여부 및 거리(시간)저장
    #visited[starts[0]][starts[1]]=1
    
    while q:
        x,y=q.popleft()
        for i in range(4):
            nx=x+dx[i]
            ny=y+dy[i]
            if 0<=nx<h and 0<=ny<w:
                # 목표점 도달
                if (nx,ny)==targets:
                    return visited[x][y]+1
                # 빈칸이거나 치즈인 경우에서 미방문한 칸이면.(치즈의 경우 목표 치즈가 아닌 경우)
                if (board[nx][ny] in ['.','S'] or board[nx][ny].isdigit()) and visited[nx][ny]==0:
                    visited[nx][ny]=visited[x][y]+1
                    q.append((nx,ny))
    
    return 0

h,w,n=map(int,input().split())
visited=[[0]*w for _ in range(h)]
board,start_idx,cheese_idxs=[],(),[() for _ in range(n+1)]
total_distance=0

start_idx_flag=True
for i in range(h):
    tmp=[*input()][:-1]
    for j in range(w):
        if start_idx_flag and tmp[j]=='S':
            start_idx=(i,j)
            start_idx_flag=False
        if tmp[j].isdigit():
            cheese_idxs[int(tmp[j])]=(i,j)
    board.append(tmp)

dx=[-1,1,0,0]
dy=[0,0,-1,1]

# 치즈 1~N까지 순차적으로 BFS 탐색.
for idx in range(1,n+1):
    total_distance+=bfs(start_idx,cheese_idxs[idx]) # 현재 시작점~현재 치즈까지의 거리(시간) 갱신
    start_idx=cheese_idxs[idx] # 다음 탐색 시작점 갱신

print(total_distance)