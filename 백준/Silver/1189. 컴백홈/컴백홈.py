# https://www.acmicpc.net/problem/1189
# 컴백홈
# 그래프 탐색, 백트래킹, 브루트포스, dfs

input=__import__('sys').stdin.readline

def dfs(sx,sy,cnt):
    global answer

    if (sx,sy)==(0,c-1) and cnt==k:
        answer+=1
        return
    
    for dx,dy in [(-1,0),(0,1),(0,-1),(1,0)]: #상우좌하
        nx,ny=sx+dx,sy+dy
        if 0<=nx<r and 0<=ny<c:
            if board[nx][ny]=='.' and visited[nx][ny]==0:
                visited[nx][ny]=1
                dfs(nx,ny,cnt+1)
                visited[nx][ny]=0

r,c,k=map(int,input().split())
visited=[[0]*c for _ in range(r)]
visited[r-1][0]=1
board=[[*input()][:-1] for _ in range(r)]
answer=0

dfs(r-1,0,1)
    
print(answer)