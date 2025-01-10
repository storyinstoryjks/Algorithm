# https://www.acmicpc.net/problem/2210
# 숫자판 점프
# 그래프탐색,브루트포스,dfs

input=__import__('sys').stdin.readline

def dfs(sx,sy,string_num,cnt):
    if cnt>=5:
        if string_num not in check_nums:
            check_nums.append(string_num)
        return
    
    for dx,dy in [(-1,0),(1,0),(0,-1),(0,1)]:
        nx=sx+dx
        ny=sy+dy
        if 0<=nx<5 and 0<=ny<5:
            if not visited[nx][ny]:
                #visited[nx][ny]=1
                dfs(nx,ny,string_num+str(board[nx][ny]),cnt+1)
                #visited[nx][ny]=0
                
board=[[*map(int,input().split())] for _ in range(5)]
check_nums=[]

for i in range(5):
    for j in range(5):
        visited=[[0]*5 for _ in range(5)]
        dfs(i,j,f'{board[i][j]}',0)

#print(check_nums)
print(len(check_nums))