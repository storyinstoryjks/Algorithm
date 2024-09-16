from sys import stdin
input=stdin.readline

def dfs(idx,curW,time):
    global ans
    if time>m:
        return
    if time<=m:
        ans=max(ans,curW)
    if idx<=n-2:
        dfs(idx+2,(curW//2)+a[idx+2],time+1)
    if idx<=n-1:
        dfs(idx+1,curW+a[idx+1],time+1)
    
n,m=map(int,input().split())
a=[1]+[*map(int,input().split())]
ans=-1
dfs(0,1,0)
print(ans)