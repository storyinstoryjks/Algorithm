# https://www.acmicpc.net/problem/22352
# 항체 인식
# 그래프 탐색

deque=__import__('collections').deque
input=__import__('sys').stdin.readline

def bfs(sx,sy):
    q=deque([(sx,sy)])
    visited[sx][sy]=1
    
    target_num_by_org=org_board[sx][sy]
    target_num_by_tar=tar_board[sx][sy]
    
    while q:
        x,y=q.popleft()
        org_board[x][y]=target_num_by_tar
        for dx,dy in [(0,-1),(0,1),(-1,0),(1,0)]:
            nx,ny=x+dx,y+dy
            if 0<=nx<n and 0<=ny<m:
                if org_board[nx][ny]==target_num_by_org and visited[nx][ny]==0:
                    visited[nx][ny]=1
                    q.append((nx,ny))

n,m=map(int,input().split())
org_board=[[*map(int,input().split())] for _ in range(n)]
tar_board=[[*map(int,input().split())] for _ in range(n)]
visited=[[0]*m for _ in range(n)]

for i in range(n):
    flag=True
    for j in range(m):
        if org_board[i][j]!=tar_board[i][j] and visited[i][j]==0:
            bfs(i,j) # bfs를 한번만 해야함.
            flag=False
            break
    if not flag:
        break
            
for i in range(n):
    for j in range(m):
        if org_board[i][j]!=tar_board[i][j]:
            print("YNEOS"[1::2])
            exit(0)
print("YNEOS"[::2])