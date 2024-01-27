# 1697 
import sys,collections
input=sys.stdin.readline
deque=collections.deque

def bfs(root,target):
    q=deque([root])
    while q:
        x=q.popleft()
        if x==target:
            return path[x]
        for node in [x-1,x+1,2*x]:
            if 0<=node<100001 and not path[node]:
                q.append(node)
                path[node]=path[x]+1
        
n,k=map(int,input().split())
path=[0 for _ in range(100001)]
print(bfs(n,k))