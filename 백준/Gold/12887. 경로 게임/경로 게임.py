# https://www.acmicpc.net/problem/12887
# 경로 게임
# 그래프 탐색

deque=__import__('collections').deque
input=__import__('sys').stdin.readline

def bfs(sx,sy):
    if (sx,sy) in [(0,m-1),(1,m-1)]: # m=1인 경우
        return 0
    
    q=deque([(sx,sy,0)]) # idx,distance
    visited=[[0]*m for _ in range(n)]
    visited[sx][sy]=1
    
    while q:
        x,y,cnt=q.popleft()
        for dx,dy in [(0,1),(-1,0),(1,0),(0,-1)]: #우상하좌
            nx,ny=x+dx,y+dy
            if 0<=nx<n and 0<=ny<m:
                if board[nx][ny]=='.' and (nx,ny) in [(0,m-1),(1,m-1)]:
                    return cnt+1
                if board[nx][ny]=='.' and visited[nx][ny]==0:
                    visited[nx][ny]=1
                    q.append((nx,ny,cnt+1))
                    
    
n,m=2,int(input())
board,total_white=[],0
answer=0

for i in range(n):
    tmp=input().strip()
    total_white+=tmp.count('.')
    board.append([*tmp])

for start_row in range(n):
    if board[start_row][0]=='.':
        cur_invisited_white=total_white-bfs(start_row,0)-1
        answer=max(answer,cur_invisited_white)

print(answer)