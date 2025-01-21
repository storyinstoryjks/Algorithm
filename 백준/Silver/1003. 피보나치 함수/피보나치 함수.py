### TOP-DOWN
input=__import__('sys').stdin.readline

def dfs(x):
    if x==0:
        dp[0]=[1,0]
        return dp[x]
    if x==1:
        dp[1]=[0,1]
        return dp[x]
    
    if dp[x]!=[0,0]:
        return dp[x]
    
    left=dfs(x-1)
    right=dfs(x-2)
    dp[x][0]+=left[0]+right[0]
    dp[x][1]+=left[1]+right[1]
    return dp[x]
    
for _ in range(int(input())):
    n=int(input())
    dp=[[0,0] for _ in range(n+1)]
    dfs(n)
    print(*dp[n])