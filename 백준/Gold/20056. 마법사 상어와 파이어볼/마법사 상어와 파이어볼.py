# 20056: Shark and Fireball
# https://www.acmicpc.net/problem/20056

from sys import stdin
from collections import deque
scan=lambda:map(int,stdin.readline().split())

def move():
    for i in range(n):
        for j in range(n):
            tmp=[]
            while board[i][j]:
                m,s,d,flag=board[i][j].popleft()
                if flag==True:
                    tmp.append((m,s,d,True))
                    continue
                ni=(i+dx[d]*s)%n
                nj=(j+dy[d]*s)%n
                board[ni][nj].append((m,s,d,True))
            if tmp:
                for e in tmp:
                    board[i][j].append(e)

def set_fireball():
    for i in range(n):
        for j in range(n):
            if board[i][j]:
                check_len=len(board[i][j])
                if check_len<2:
                    for _ in range(check_len):
                        m,s,d,_=board[i][j].popleft()
                        board[i][j].append((m,s,d,False))
                else:
                    total_m,total_cnt,total_s=0,0,0
                    check_d=-1
                    while board[i][j]:
                        m,s,d,_=board[i][j].popleft()
                        total_m+=m; total_cnt+=1; total_s+=s
                        if check_d!=-2 and check_d==-1:
                            check_d=0 if d%2==0 else 1
                        else:
                            f=0 if d%2==0 else 1
                            check_d=-2 if f!=check_d else check_d
                    new_dir=[1,3,5,7] if check_d==-2 else [0,2,4,6]
                    new_m=total_m//5
                    new_s=total_s//total_cnt
                    if new_m>0:
                        for new_d in new_dir:
                            board[i][j].append((new_m,new_s,new_d,False))
            
    
dx=[-1,-1,0,1,1,1,0,-1]
dy=[0,1,1,1,0,-1,-1,-1]
n,m,k=scan()
board=[[deque([]) for _ in range(n)] for _ in range(n)]

for _ in range(m):
    r,c,m,s,d=scan()
    board[r-1][c-1].append((m,s,d,False))

for h in range(k):
    move()
    set_fireball()
    
ans=0
for i in range(n):
    for j in range(n):
        if board[i][j]:
            while board[i][j]:
                m,s,d,_=board[i][j].popleft()
                ans+=m
print(ans)