# https://www.acmicpc.net/problem/7662
# 이중 우선순위 큐
# 우선순위큐, 해쉬

import sys
import heapq
input=sys.stdin.readline

for _ in range(int(input())):
    dashboard={}
    max_heap,min_heap=[],[]
    
    for _ in range(int(input())):
        C,N=input().split()
        N=int(N)
        if C=='I':
            heapq.heappush(max_heap,-N)
            heapq.heappush(min_heap,N)
            try:
                dashboard[N]+=1
            except:
                dashboard[N]=1
        elif N==1:
            while max_heap:
                root=heapq.heappop(max_heap)
                if dashboard[-root]>0:
                    dashboard[-root]-=1
                    break
        elif N==-1:
            while min_heap:
                root=heapq.heappop(min_heap)
                if dashboard[root]>0:
                    dashboard[root]-=1
                    break
    
    ans_max,ans_min=0,0
    max_flag,min_flag=False,False
    while max_heap:
        t=heapq.heappop(max_heap)
        if dashboard[-t]>0:
            ans_max=-t; max_flag=True
            break
    
    while min_heap:
        t=heapq.heappop(min_heap)
        if dashboard[t]>0:
            ans_min=t; min_flag=True
            break
    
    if (max_flag,min_flag)==(False,False):
        print("EMPTY")
    elif (max_flag,min_flag)==(True,True):
        print(ans_max,ans_min)
    else:
        t=ans_max if max_flag==True else ans_min
        print(t,t)