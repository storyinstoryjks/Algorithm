# Min Heap
# https://www.acmicpc.net/problem/1927

import heapq,sys
input=sys.stdin.readline

min_heap=[]
for _ in range(int(input())):
    s=int(input())
    if s==0:
        print(heapq.heappop(min_heap) if min_heap else 0)
    else:
        heapq.heappush(min_heap,s)