from sys import stdin 
scan=lambda:map(int,stdin.readline().split())

def spread():
    while dusts:
        x,y,e=dusts.pop(0)
        cnt=0
        for i in range(4):
            nx,ny=x+dx[i],y+dy[i]
            if 0<=nx<r and 0<=ny<c:
                if room[nx][ny]!=-1:
                    room[nx][ny]+=e//5
                    cnt+=1
        room[x][y]-=(e//5)*cnt

def rotate(C,f):
    curX,curY=C,1
    prev,idx=0,0
    while 1:
        nx,ny=curX+dx[idx],curY+dy[idx]
        if nx==r or ny==c or nx<0 or ny<0:
            idx=idx+1 if f else idx-1
            continue
        if curX==C and curY==0:
            break
        room[curX][curY],prev=prev,room[curX][curY]
        curX,curY=nx,ny

r,c,t=scan()
room=[[*scan()] for _ in [0]*r]
visited=[[-1]*c for _ in [0]*r]
dusts,cleaner=[],[]
dx,dy=[0,-1,0,1],[1,0,-1,0]

for i in range(r):
    for j in range(c):
        if room[i][j]>0:dusts.append((i,j,room[i][j]))
        if room[i][j]<0:cleaner.append(i)

for _ in [0]*t:
    spread();rotate(cleaner[0],1);rotate(cleaner[1],0)
    dusts=[(i,j,room[i][j])for j in range(c)for i in range(r)if room[i][j]>0]
print(sum(i[2]for i in dusts))