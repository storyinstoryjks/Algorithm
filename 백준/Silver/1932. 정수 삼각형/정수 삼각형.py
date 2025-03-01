# https://www.acmicpc.net/problem/1932
# 정수 삼각형
# dp

input=__import__('sys').stdin.readline

n=int(input())
dp=[[*map(int,input().split())] for _ in range(n)]

for i in range(1,n):
    for j in range(i+1):
        if j==0:
            dp[i][j]+=dp[i-1][j]
        elif j==i:
            dp[i][j]+=dp[i-1][j-1]
        else:
            dp[i][j]=max(dp[i-1][j-1]+dp[i][j], dp[i-1][j]+dp[i][j])

print(max(dp[n-1]))