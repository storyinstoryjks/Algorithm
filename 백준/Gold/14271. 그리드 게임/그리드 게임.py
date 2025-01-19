# https://www.acmicpc.net/problem/14271
# 그리드 게임
# 그래프탐색, bfs

input=__import__('sys').stdin.readline
deque=__import__('collections').deque

def bfs():
    global answer
    
    while q:
        x,y,time=q.popleft()
        answer+=1
        if time>=k:
            continue
        for dx,dy in [(0,-1),(0,1),(1,0),(-1,0)]:
            nx,ny=x+dx,y+dy
            if 0<=nx<3100 and 0<=ny<3100:
                if live_idxs_visited[nx][ny]==0:
                    q.append((nx,ny,time+1))
                    live_idxs_visited[nx][ny]=1

n,m=map(int,input().split())
live_idxs_visited=[[0]*3100 for _ in range(3100)]
q=deque([]) # x,y,time
answer=0

for i in range(n):
    l=[*input()[:-1]]
    for j in range(m):
        if l[j]=='o':
            x,y=i+1500,j+1500
            live_idxs_visited[x][y]=1
            q.append((x,y,0))

k=int(input())
bfs()
print(answer)