# 1012 : Organic Cabbage

def dfs(x,y):
    stk=[[x,y]]
    
    while stk!=[]:
        e=stk.pop(0)
        x,y=e
        visited[x][y]=1
        # left
        if y-1>=0 and not visited[x][y-1] and [x,y-1] not in stk and cabbageGround[x][y-1]:
            stk=[[x,y-1]]+stk
        # right
        if y+1<m and not visited[x][y+1] and [x,y+1] not in stk and cabbageGround[x][y+1]:
            stk=[[x,y+1]]+stk
        # top
        if x-1>=0 and not visited[x-1][y] and [x-1,y] not in stk and cabbageGround[x-1][y]:
            stk=[[x-1,y]]+stk
        # bottom
        if x+1<n and not visited[x+1][y] and [x+1,y] not in stk and cabbageGround[x+1][y]:
            stk=[[x+1,y]]+stk


for _ in range(int(input())):
    m,n,k=map(int,input().split())
    cabbageGround=[[0]*m for _ in range(n)]
    visited=[[0]*m for _ in range(n)]
    
    for _ in range(k):
        col,row=map(int,input().split())
        cabbageGround[row][col]=1
    
    earthWormCnt=0
    
    for i in range(n):
        for j in range(m):
            if not visited[i][j] and cabbageGround[i][j]:
                dfs(i,j) # why? => Set to visited
                earthWormCnt+=1
                
    print(earthWormCnt)