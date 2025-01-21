### Bottom-UP
input=__import__('sys').stdin.readline

for _ in range(int(input())):
    n=int(input())
    
    if n in [0,1]:
        print(*'1001'[n::2])
        continue
    
    dp=[[0,0] for _ in range(n+1)]
    dp[0],dp[1]=[1,0],[0,1]
    
    for x in range(2,n+1):
        dp[x][0]=dp[x-1][0]+dp[x-2][0]
        dp[x][1]=dp[x-1][1]+dp[x-2][1]
    
    print(*dp[n])