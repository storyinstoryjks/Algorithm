# https://www.acmicpc.net/problem/3187
# 양치기 꿍
# 그래프 탐색, DFS, BFS

input=__import__('sys').stdin.readline
deque=__import__('collections').deque

def bfs(sx,sy):
    q=deque([(sx,sy)])
    visited[sx][sy]=1
    cnt_ship,cnt_wolf=0,0
    
    while q:
        x,y=q.popleft()
        if board[x][y]=='v':cnt_wolf+=1
        if board[x][y]=='k':cnt_ship+=1
        for dx,dy in [(-1,0),(1,0),(0,-1),(0,1)]:
            nx,ny=x+dx,y+dy
            if 0<=nx<r and 0<=ny<c:
                if board[nx][ny]!='#' and visited[nx][ny]==0:
                    visited[nx][ny]=1
                    q.append((nx,ny))

    return cnt_ship,cnt_wolf

total_ship,total_wolf=0,0
r,c=map(int,input().split())
board=[]

for _ in range(r):
    l=[*input()][:-1]
    for i in l:
        if i=='v':total_wolf+=1
        if i=='k':total_ship+=1
    board.append(l)
    
visited=[[0]*c for _ in range(r)]
for i in range(r):
    for j in range(c):
        if board[i][j]!='#' and visited[i][j]==0:
            k,v=bfs(i,j)
            if k==0 or v==0:
                continue
            if k>v:
                total_wolf-=v
            else:
                total_ship-=k

print(total_ship,total_wolf)