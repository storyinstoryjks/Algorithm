# https://www.acmicpc.net/problem/9095
# 1,2,3 더하기
# 그래프, dp

input=__import__('sys').stdin.readline

dp=[0]*(11) # n은 최대 10까지 입력됨
dp[1],dp[2],dp[3]=1,2,4

for i in range(4,11):
    dp[i]=dp[i-1]+dp[i-2]+dp[i-3]

for _ in range(int(input())):
    print(dp[int(input())])