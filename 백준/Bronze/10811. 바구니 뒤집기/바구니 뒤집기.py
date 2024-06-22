n,m=map(int,input().split())
l=[*range(1,n+1)]
for _ in [0]*m:
 i,j=map(int,input().split())
 l=l[:i-1]+l[i-1:j][::-1]+l[j:]
print(*l)