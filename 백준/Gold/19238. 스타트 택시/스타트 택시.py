from sys import stdin 
from collections import deque
import heapq
input=stdin.readline

def find_client_goal(cX,cY,gX,gY):
    q=deque([(cX,cY)])
    visited=[[0]*n for _ in range(n)]
    visited[cX][cY]=1
    
    while q:
        x,y=q.popleft()
        if x==gX and y==gY:
            return True, visited[x][y]-1
        for i in range(4):
            nx=x+dx[i]; ny=y+dy[i]
            if 0<=nx<n and 0<=ny<n and graph[nx][ny]!=1:
                if visited[nx][ny]==0:
                    visited[nx][ny]=visited[x][y]+1
                    q.append((nx,ny))
                else:
                    visited[nx][ny]=min(visited[nx][ny],visited[x][y]+1)

    return False, -1

def find_client_taxi(sx,sy):
    q=deque([(sx,sy)])
    heap,visited=[],[[0]*n for _ in range(n)]
    visited[sx][sy]=1
    heap_size=0
    
    while q:
        x,y=q.popleft()
        if (x,y) in clientDis and clientDis[(x,y)][3]==False: # 
            heap_size+=1
            heapq.heappush(heap,(visited[x][y]-1,x,y))
        for i in range(4):
            nx=x+dx[i]; ny=y+dy[i]
            if 0<=nx<n and 0<=ny<n and graph[nx][ny]!=1:
                if visited[nx][ny]==0:
                    visited[nx][ny]=visited[x][y]+1
                    q.append((nx,ny))
                else:
                    visited[nx][ny]=min(visited[nx][ny],visited[x][y]+1)
                
    return heap_size,heap
    
dx=[-1,1,0,0]
dy=[0,0,-1,1]
n,m,fuel=map(int,input().split())
graph=[[*map(int,input().split())] for _ in range(n)]
curX,curY=map(int,input().split())

curX-=1; curY-=1
clientDis={}
moveFlag=True

for _ in range(m):
    clientX,clientY,goalX,goalY=map(int,input().split())
    flag,distance=find_client_goal(clientX-1,clientY-1,goalX-1,goalY-1)
    if flag==False:
        moveFlag=False
    clientDis[(clientX-1,clientY-1)]=(goalX-1,goalY-1,distance,False)

if moveFlag:
    for i in range(m):
        heap_size,heap=find_client_taxi(curX,curY)
        if i==0 and heap_size!=m: 
            moveFlag=False
            break
        
        taxi_client_distance,clientX,clientY=heapq.heappop(heap)
        goalX,goalY,client_goal_distance,_=clientDis[(clientX,clientY)]
        
        total_move_distance=taxi_client_distance+client_goal_distance
        if total_move_distance>fuel:
            moveFlag=False
            break
            
        curX,curY=goalX,goalY
        fuel=(fuel-total_move_distance)+(2*client_goal_distance)
        clientDis[(clientX,clientY)]=(0,0,0,True)
    
print(fuel if moveFlag else -1)