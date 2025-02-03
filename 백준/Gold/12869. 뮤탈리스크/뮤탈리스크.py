# https://www.acmicpc.net/problem/12869
# 뮤탈리스크
# dp,그래프탐색

input=__import__('sys').stdin.readline

def dfs_n_3(s1,s2,s3,cnt):
    if s1<=0 and s2<=0 and s3<=0:
        try:
            dp[(0,0,0)]=min(dp[(0,0,0)],cnt)
        except:
            dp[(0,0,0)]=cnt
        return dp[(0,0,0)]
    
    if (s1,s2,s3) in dp.keys():
        return dp[(s1,s2,s3)]
    
    for i,j,k in [(9,3,1),(9,1,3),(3,9,1),(3,1,9),(1,9,3),(1,3,9)]:
        dp[(s1,s2,s3)]=dfs_n_3(s1-i,s2-j,s3-k,cnt+1)
    
    return dp[(s1,s2,s3)]

def dfs_n_2(s1,s2,cnt):
    if s1<=0 and s2<=0:
        try:
            dp[(0,0)]=min(dp[(0,0)],cnt)
        except:
            dp[(0,0)]=cnt
        return dp[(0,0)]
    
    if (s1,s2) in dp.keys():
        return dp[(s1,s2)]
    
    for i,j in [(9,3),(9,1),(3,9),(3,1),(1,9),(1,3)]:
        dp[(s1,s2)]=dfs_n_2(s1-i,s2-j,cnt+1)
    
    return dp[(s1,s2)]

def dfs_n_1(s,cnt):
    if s<=0:
        try:
            dp[0]=min(dp[0],cnt)
        except:
            dp[0]=cnt
        return dp[0]
    
    if s in dp.keys():
        return dp[s]
    
    for i in [9,3,1]:
        dp[s]=dfs_n_1(s-i,cnt+1)
    
    return dp[s]

n=int(input())
scvs=[*map(int,input().split())]
dp={}

if n==3:
    print(dfs_n_3(scvs[0],scvs[1],scvs[2],0))
elif n==2:
    print(dfs_n_2(scvs[0],scvs[1],0))
else:
    print(dfs_n_1(scvs[0],0))