# https://www.acmicpc.net/problem/16294
# Bee Problem
# 그래프탐색,BFS,DFS

input=__import__('sys').stdin.readline
deque=__import__('collections').deque

def bfs(sx,sy):
    q=deque([(sx,sy)])
    visited.add((sx,sy))
    cnt=1
    
    while q:
        x,y=q.popleft()
        for k in range(6):
            nx,ny=x+dx[k],y+dy[k]
            if 0<=nx<n and 0<=ny<2*m-1+(nx%2):
                if board[nx][ny]=='.' and (nx,ny) not in visited:
                    visited.add((nx,ny))
                    cnt+=1
                    q.append((nx,ny))
    
    return cnt

h,n,m=map(int,input().split())
board=[[*input()[:-1]] for _ in range(n)]
visited=set()
dx=[0,0,1,1,-1,-1]
dy=[2,-2,1,-1,1,-1]

if h==0:
    print(0)
    exit(0)

group=[]
answer=0
for i in range(n):
    for j in range(i%2,2*m-1+(i%2),2):
        if (i,j) not in visited and board[i][j]=='.':
            cnt=bfs(i,j)
            group.append(cnt)

for i in sorted(group)[::-1]:
    answer+=1
    if h<=0 or i>=h:
        break
    h-=i
print(answer)