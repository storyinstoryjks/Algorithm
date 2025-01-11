# https://www.acmicpc.net/problem/1463
# 1로 만들기
# 재귀,트리,DP

# Bottom-Up

input=__import__('sys').stdin.readline
x=int(input())
dp=[0]*(x+1)

for i in range(2,x+1):
    dp[i]=dp[i-1]+1
    if i%3==0:
        dp[i]=min(dp[i],dp[i//3]+1)
    if i%2==0:
        dp[i]=min(dp[i],dp[i//2]+1)

print(dp[x])