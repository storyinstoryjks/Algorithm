# https://www.acmicpc.net/problem/2470
# 두 용액
# 정렬, 이분탐색, 투 포인터

n=int(input())
a=sorted([*map(int,input().split())])

start,end=0,n-1
value=abs(a[start]+a[end])
ans=(a[start],a[end])

while start<end:
    sum=a[start]+a[end]
    if abs(sum)<value:
        value=abs(sum)
        ans=(a[start],a[end])
        if sum==0:break
    if sum<0:start+=1
    else:end-=1

print(*ans)