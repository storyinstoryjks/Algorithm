# Problems
# https://www.acmicpc.net/problem/1766

"""
import sys
input=sys.stdin.readline

n,m=map(int,input().split())
graph=[[0]*(n+1) for _ in range(n+1)]

for _ in range(m):
    a,b=map(int,input().split())
    graph[a][b]=1

ans=[]

while len(ans)<n:
    degreeCnt,node=200000,0
    for i in range(1,n+1):
        tmp=0
        if i not in ans:
            for j in range(1,n+1):
                tmp+=graph[j][i]
            if tmp<degreeCnt:
                degreeCnt=tmp
                node=i
            elif tmp==degreeCnt and i<node:
                node=i
    ans.append(node)
    for i in range(1,n+1):
        graph[i][node]=0
        graph[node][i]=0

print(*ans)
"""

import sys,heapq
input=sys.stdin.readline

n,m=map(int,input().split())
graph=[[] for _ in range(n+1)]
degree=[0 for _ in range(n+1)]

for _ in range(m):
    a,b=map(int,input().split())
    graph[a].append(b)
    degree[b]+=1

heap,ans=[],[]

for i in range(1,n+1):
    if degree[i]==0:
        heapq.heappush(heap,i);

while heap:
    sel=heapq.heappop(heap)
    ans.append(sel)
    for i in graph[sel]:
        degree[i]-=1
        if degree[i]==0:
            heapq.heappush(heap,i);
            
print(*ans)