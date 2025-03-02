# https://www.acmicpc.net/problem/6236
# 용돈 관리
# 이분 탐색

input==__import__('sys').stdin.readline

n,m=map(int,input().split())
days=[int(input()) for _ in range(n)]

left,right=max(days),sum(days)
answer=0

while left<=right:
    mid=(left+right)//2
    cnt,balance=1,mid
    balance=mid
    
    for day_cash in days:
        if balance<day_cash:
            balance=mid
            cnt+=1
        balance-=day_cash
    
    if cnt>m:
        left=mid+1
    else:
        right=mid-1
        answer=mid

print(answer)