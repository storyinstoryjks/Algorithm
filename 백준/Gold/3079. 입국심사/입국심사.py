# https://www.acmicpc.net/problem/3079
# 입국심사
# 이분탐색

input=__import__('sys').stdin.readline

n,m=map(int,input().split())
T=[int(input()) for _ in range(n)]

left,right=min(T),max(T)*m
answer=right

while left<=right:
    mid=(left+right)//2
    total_cur_possible=sum(mid//T[i] for i in range(n))
    
    if total_cur_possible>=m:
        answer=min(answer,mid)
        right=mid-1
    else:
        left=mid+1

print(answer)