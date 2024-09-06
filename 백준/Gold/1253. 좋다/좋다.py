# https://www.acmicpc.net/problem/1253
# 좋다
# 정렬,투포인터

from sys import stdin
input=stdin.readline

n=int(input())
arr=sorted([*map(int,input().split())])
cnt=0

for i in range(n):
    target=arr[i]
    tmp=arr[:i]+arr[i+1:] # 좋은 수는 연산에 포함 x
    left,right=0,n-2
    while left<right:
        cur=tmp[left]+tmp[right]
        if cur==target:
            cnt+=1
            break
        if cur<target:
            left+=1
        else:
            right-=1

print(cnt)