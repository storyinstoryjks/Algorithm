# https://www.acmicpc.net/problem/1072
# 게임
# 이분탐색

input=__import__('sys').stdin.readline

x,y=map(int,input().split())
z=(100*y)//x
left,right=0,x # sys.maxsize
answer=x

if z>=99:
    print(-1)
    exit(0)

while left<=right:
    mid=(left+right)//2
    new_z=(100*(y+mid))//(x+mid)
    
    if new_z<=z:
        left=mid+1
    else:
        answer=min(answer,mid)
        right=mid-1
        
print(answer)