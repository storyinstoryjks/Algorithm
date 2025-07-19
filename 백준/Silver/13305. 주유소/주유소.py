# https://www.acmicpc.net/problem/13305
# 주유소

n=int(input())
kms=[*map(int,input().split())]
costs=[*map(int,input().split())]

minCost=costs[0]
ans=0
for i in range(n-1):
    if costs[i]<minCost:
        minCost=costs[i]
    ans+=minCost*kms[i]

print(ans)