# 20055 : Robot on the Convayer belt

from sys import stdin
from collections import deque
scan=lambda:map(int,stdin.readline().split())

def rotate_belt():
    global start,end
    start=2*n-1 if start==0 else start-1
    end=2*n-1 if end==0 else end-1
    if robots and robots[-1]==end:
        robots.pop()

def move_robot():
    for idx in range(len(robots)-1,-1,-1):
        nextPos=(robots[idx]+1)%(n*2)
        if nextPos not in robots:
            if A[nextPos]>=1:
                A[nextPos]-=1
                robots[idx]=nextPos
        if idx==0 and robots[-1]==end:
            robots.pop()

def add_robot():
    if A[start]>0:
        A[start]-=1
        robots.appendleft(start)

n,k=scan()
A=[*scan()]
robots=deque([])
start,end=0,n-1
step=1

while True:
    rotate_belt()
    move_robot()
    add_robot()
    durability=0
    for i in range(2*n):
        if A[i]==0:
            durability+=1
        if durability==k:
            print(step)
            exit(0)
    step+=1