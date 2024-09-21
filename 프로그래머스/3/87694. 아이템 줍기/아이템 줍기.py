from collections import deque

def bfs(sx,sy,gx,gy,graph):
    q=deque([(sx,sy)])
    distance={(sx,sy):1}
    dx,dy=[-1,1,0,0],[0,0,-1,1]
    
    while q:
        x,y=q.popleft()
        if (x,y)==(gx,gy):
            return distance[(x,y)]//2
        for i in range(4):
            nx,ny=x+dx[i],y+dy[i]
            if 1<=nx<102 and 1<=ny<102:
                if graph[nx][ny]==1 and (nx,ny) not in distance:
                    distance[(nx,ny)]=distance[(x,y)]+1
                    q.append((nx,ny))
                    
    # 무조건 가는 경우만 주어지기에 못가는 경우는 없음.
    
def solution(rectangle, characterX, characterY, itemX, itemY):
    board=[[2]*102 for _ in range(102)] # 51*2
    
    for l in rectangle:
        lx,ly,rx,ry=map(lambda x:x*2,l)
        for i in range(lx,rx+1):
            for j in range(ly,ry+1):
                if lx<i<rx and ly<j<ry:
                    board[i][j]=0
                elif board[i][j]!=0:
                    board[i][j]=1
    
    return bfs(characterX*2, characterY*2, itemX*2, itemY*2, board)
    
    