# 4963 : Count to Land
import sys
input=sys.stdin.readline
sys.setrecursionlimit(10000)

def dfs(x,y):
    visited[x][y]=1
    for i in range(8):
        nx=x+dx[i]
        ny=y+dy[i]
        if 0<=nx<h and 0<=ny<w:
            if not visited[nx][ny] and graph[nx][ny]:
                #print(f"###DFS({nx},{ny})")
                dfs(nx,ny) 
                
dx=[-1,1,0,0,-1,-1,1,1]
dy=[0,0,-1,1,-1,1,-1,1]

while True:
    w,h=map(int,input().split())
    if w==0 and h==0: break
    elif w==1 and h==1:
        print(int(input()))
        continue
    
    graph=[[]*w for _ in range(h)]
    visited=[[0]*w for _ in range(h)]
    cnt=0

    for i in range(h):
        graph[i]=[*map(int,input().split())]
    
    for i in range(h):
        for j in range(w):
            if not visited[i][j] and graph[i][j]:
                #print(f"#DFS({i},{j})")
                dfs(i,j)
                cnt+=1
    print(cnt)