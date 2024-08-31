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
LIS=[a[0]]

for i in range(1,n):
    if a[i]>LIS[-1]:
        LIS.append(a[i])
    else:
        idx=binary_search(a[i])
        LIS[idx]=a[i]

print(len(LIS))