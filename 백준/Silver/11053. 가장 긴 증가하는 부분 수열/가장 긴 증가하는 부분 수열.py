# DP
# n=int(input())
# a=[*map(int,input().split())]
# dp=[1]*n # 초반 모든 길이를 1로 초기화

# for i in range(1,n):
#     for j in range(i):
#         if a[i]>a[j]:
#             dp[i]=max(dp[i],dp[j]+1) # 1씩 길이 증가. (메모제이션역할이 들어간것)
# print(max(dp))

# 이진탐색
def binary_search(target):
    left,right=0,len(LIS)-1
    while left<=right:
        mid=(left+right)//2
        if LIS[mid]<target:
            left=mid+1
        else:
            right=mid-1
    return left
    
n=int(input())
a=[*map(int,input().split())]
LIS=[a[0]] # LIS 배열의 초기원소

for i in range(1,n):
    # 2-1
    if a[i]>LIS[-1]:
        LIS.append(a[i])
    # 2-2
    else:
        idx=binary_search(a[i])
        LIS[idx]=a[i]

print(len(LIS))