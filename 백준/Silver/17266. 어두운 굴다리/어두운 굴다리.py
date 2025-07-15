# https://www.acmicpc.net/problem/17266
# 어두운 굴다리
# 이분 탐색

n=int(input())
m=int(input())
L=[*map(int,input().split())]
l,r=1,100001
ans=r

while l<=r:
    m=(l+r)//2
    c=0
    for i in L:
        if i-m>c:
            break
        c=i+m
    if c>=n:
        ans=min(ans,m)
        r=m-1
    else:
        l=m+1

print(ans)