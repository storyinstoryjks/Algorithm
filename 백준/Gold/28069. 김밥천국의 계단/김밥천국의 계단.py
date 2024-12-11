# https://www.acmicpc.net/problem/28069
# 김밥천국의 계단
# 그래프 탐색

n,k=map(int,__import__('sys').stdin.readline().split())
dp=[1e9]*(n+1)
dp[0]=0

for i in range(n):
    if i+1<=n:
        dp[i+1]=min(dp[i+1],dp[i]+1)
    if m:=i+i/2<=n:
        dp[i+i//2]=min(dp[i+i//2],dp[i]+1)

print(['water','minigimbob'][dp[n]<=k])