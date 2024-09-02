N,m,M,T,R=map(int,input().split())
X=m 
t,c=0,0
if m+T>M:
    print(-1)
    exit(0)
while c<N:
    #print(X)
    if X+T<=M:
        X+=T
        c+=1
    elif X-R>=m:
        X-=R
    elif X-R<m:
        X=m
    else:
        t=-1
        break
    t+=1
print(t)