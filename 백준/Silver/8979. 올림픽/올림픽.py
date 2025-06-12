# https://www.acmicpc.net/problem/8979
# 올림픽

n,k=map(int,input().split())
l=[[*map(int,input().split())] for _ in range(n)]
s=sorted(l,key=lambda x:(-x[1],-x[2],-x[3]))

cur=1
ranks=[0]*(n+1)
ranks[s[0][0]]=cur

prev=s[0]
equals=1
for i in range(1,n):
    if prev[1]>s[i][1] or prev[2]>s[i][2] or prev[3]>s[i][3]:
        cur+=equals
        equals=1
    else:
        equals+=1
    ranks[s[i][0]]=cur
    prev=s[i]
    
print(ranks[k])