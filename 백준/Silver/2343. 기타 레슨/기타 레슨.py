# https://www.acmicpc.net/problem/2343
# 기타 레슨
# 이분 탐색

input=__import__('sys').stdin.readline

n,m=map(int,input().split())
lectures=[]

left,right=-1,0
for lecture in [*map(int,input().split())]:
    lectures.append(lecture)
    right+=lecture
    if lecture>left:
        left=lecture

answer=right
while left<=right:
    mid=(left+right)//2
    cur_sizes=[]
    
    cur_size,cnt=0,0
    for i in lectures:
        if cnt<m-1:
            if cur_size+i<=mid:
                cur_size+=i
            else:
                cur_sizes.append(cur_size)
                cnt+=1
                cur_size=i
        elif cnt==m-1:
            cur_size+=i
    
    if cur_size>mid:
        left=mid+1
    else:
        cur_sizes.append(cur_size)
        answer=min(answer,max(cur_sizes))
        right=mid-1

print(answer)