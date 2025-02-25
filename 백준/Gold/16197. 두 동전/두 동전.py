# https://www.acmicpc.net/problem/16197
# 두 동전
# 그래프 탐색, bfs

deque=__import__('collections').deque
input=__import__('sys').stdin.readline

def bfs():
    while coins:
        x1,y1,x2,y2,depth=coins.popleft()
        if depth>=10:
            return -1
        
        for dx,dy in [(-1,0),(1,0),(0,-1),(0,1)]:
            nx1,ny1=x1+dx,y1+dy
            nx2,ny2=x2+dx,y2+dy
            if (0<=nx1<n and 0<=ny1<m) and (0<=nx2<n and 0<=ny2<m):
                if board[nx1][ny1]=='#':
                    nx1,ny1=x1,y1
                if board[nx2][ny2]=='#':
                    nx2,ny2=x2,y2
                coins.append((nx1,ny1,nx2,ny2,depth+1))
            elif (0<=nx1<n and 0<=ny1<m) or (0<=nx2<n and 0<=ny2<m):
                return depth+1
            else:
                continue
            
    return -1

n,m=map(int,input().split())
coins=deque([])
board=[]

temp=[]
for i in range(n):
    l=[*input()[:-1]]
    for j in range(m):
        if l[j]=='o':
            temp.append((i,j))
    board.append(l)
    
coins.append((temp[0][0],temp[0][1],temp[1][0],temp[1][1],0))

print(bfs())