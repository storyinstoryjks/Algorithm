# https://www.acmicpc.net/problem/16173
# 점프왕 쩰리
# 그래프 탐색, bfs, dfs

input=__import__('sys').stdin.readline

def dfs(sx,sy):
    flag=False
    
    if (sx,sy)==(n-1,n-1):
        return True
    
    jump=board[sx][sy]
    for dx,dy in [(1,0),(0,1)]:
        nx=sx+dx*jump
        ny=sy+dy*jump
        if 0<=nx<n and 0<=ny<n:
            if not visited[nx][ny]:
                visited[nx][ny]=1
                flag=dfs(nx,ny)
                if flag:
                    return True
                visited[nx][ny]=0
    
    return flag

n=int(input())
board=[[*map(int,input().split())] for _ in range(n)]
visited=[[0]*n for _ in range(n)]

visited[0][0]=1
print(['Hing','HaruHaru'][dfs(0,0)])