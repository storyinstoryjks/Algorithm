N,M,K=map(int,input().split())
C=[0]*4
for _ in [0]*K:
    i,j=map(int,input().split())
    if i%2==1:
        if(i+j)%2==0:C[0]=1
        else:C[1]=1
    elif (i+j)%2==0:C[2]=1
    else:C[3]=1
print('YNEOS'[all(C)<1::2])