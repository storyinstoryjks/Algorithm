# 10810 : insert ball

import sys
input=sys.stdin.readline

n,m=map(int,input().split())
cart=[0]*(n+1)

for _ in range(m):
    i,j,k=map(int,input().split())
    for e in range(i,j+1):
        cart[e]=k
print(*cart[1:])