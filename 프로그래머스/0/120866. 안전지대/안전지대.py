def solution(board):
    n,s=len(board),set()
    dx,dy=[-1,1,0,0,-1,1,-1,1],[0,0,-1,1,-1,-1,1,1]
    
    for i in range(n):
        for j in range(n):
            if board[i][j]==1:
                s.add((i,j))
                for k in range(8):
                    nx,ny=i+dx[k],j+dy[k]
                    if 0<=nx<n and 0<=ny<n:
                        s.add((nx,ny))
    
    return n**2-len(s)