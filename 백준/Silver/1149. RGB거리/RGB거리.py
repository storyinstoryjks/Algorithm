# https://www.acmicpc.net/problem/1149
# RGB거리
# dp

input=__import__('sys').stdin.readline

n=int(input())
dp=[0]*(n+1)

for i in range(n):
    dp[i+1]=[*map(int,input().split())]

for i in range(2,n+1):
    dp[i][0]=min(dp[i-1][1],dp[i-1][2])+dp[i][0]
    dp[i][1]=min(dp[i-1][0],dp[i-1][2])+dp[i][1]
    dp[i][2]=min(dp[i-1][0],dp[i-1][1])+dp[i][2]
    
print(min(dp[n]))