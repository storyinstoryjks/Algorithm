import heapq
from sys import stdin
input=stdin.readline
h=[]
n=int(input())
for _ in range(n):
    heapq.heappush(h,int(input()))
for _ in range(n):
    print(heapq.heappop(h))