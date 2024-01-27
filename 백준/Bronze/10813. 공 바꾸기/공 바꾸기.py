# 10813 : Change Ball index

import sys
input=sys.stdin.readline 

n,m=map(int,input().split())
l=[i for i in range(n+1)]
for _ in range(m):
    a,b=map(int,input().split())
    t=l[a]
    l[a]=l[b]
    l[b]=t

print(*l[1:])