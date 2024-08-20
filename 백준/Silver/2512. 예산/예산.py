# https://www.acmicpc.net/problem/2512
# 예산
# 이분탐색

from sys import stdin 
input=stdin.readline

n=int(input())
reqs=[*map(int,input().split())]
total=int(input())

if sum(reqs)>total:
    start,end=0,total
    result=0

    while start<=end:
        mid=(start+end)//2
        preTotal=sum(min(i,mid) for i in reqs)
        if preTotal<=total:
            result=mid
            start=mid+1
        else:
            end=mid-1
    print(result)
else:
    print(max(reqs))