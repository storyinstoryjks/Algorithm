# https://www.acmicpc.net/problem/1245
# 농장 관리
# 그래프 탐색

input=__import__('sys').stdin.readline
deque=__import__('collections').deque

def bfs(sx,sy):
    global all_check_idxs
    q=deque([(sx,sy)])
    visited=[[0]*m for _ in range(n)]
    cur_check_idxs=[(sx,sy)]
    
    visited[sx][sy]=1
    
    while q:
        x,y=q.popleft()
        for k in range(8):
            nx,ny=x+dx[k],y+dy[k]
            if 0<=nx<n and 0<=ny<m:
                # 현재 탐색 지역보다 인접 지역이 더 높은 경우 산봉우리 x
                if board[nx][ny]>board[x][y]:
                    return 0
                # 같은 고도인 경우, 산봉우리 같은 지역 탐색을 위한 큐 삽입
                if board[nx][ny]==board[x][y] and visited[nx][ny]==0:
                    visited[nx][ny]=1
                    q.append((nx,ny))
                    cur_check_idxs.append((nx,ny))
                    
    all_check_idxs+=cur_check_idxs # 탐색했던 지역 전역 방문 처리
    return 1 # 산봉우리 확정
    
n,m=map(int,input().split())
board=[[*map(int,input().split())] for _ in range(n)]
all_check_idxs=[]
answer=0

dx=[-1,1,0,0,-1,1,-1,1]
dy=[0,0,-1,1,-1,-1,1,1]

for i in range(n):
    for j in range(m):
        if (i,j) not in all_check_idxs:
            answer+=bfs(i,j)

print(answer)