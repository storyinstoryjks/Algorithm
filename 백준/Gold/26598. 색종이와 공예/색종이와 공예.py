# https://www.acmicpc.net/problem/26598
# 색종이와공예
# 그래프 탐색, 에드 훅, bfs

deque=__import__('collections').deque
input=__import__('sys').stdin.readline
    
def bfs(sx,sy):
    q=deque([(sx,sy)])
    paper_idxs=[(sx,sy)]
    min_row,max_row,min_col,max_col=sx,sx,sy,sy
    
    while q:
        x,y=q.popleft()
        for dx,dy in [(0,-1),(-1,0),(0,1),(1,0)]:
            nx,ny=x+dx,y+dy
            if 0<=nx<n and 0<=ny<m:
                if board[nx][ny]==board[sx][sy] and visited[nx][ny]==0:
                    visited[nx][ny]=1
                    q.append((nx,ny))
                    paper_idxs.append((nx,ny))
                    min_row=min(min_row,nx); max_row=max(max_row,nx)
                    min_col=min(min_col,ny); max_col=max(max_col,ny)
                    
    return len(paper_idxs)==(max_col-min_col+1)*(max_row-min_row+1)
        

n,m=map(int,input().split())
board=[[*input()][:-1] for _ in range(n)]
visited=[[0]*m for _ in range(n)]

for i in range(n):
    for j in range(m):
        if visited[i][j]==0:
            visited[i][j]=1
            if not bfs(i,j):
                print('BaboBabo')
                exit(0)
print('dd')