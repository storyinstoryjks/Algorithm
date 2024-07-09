s=lambda:map(int,input().split())
n,m=s();l=[*range(n+1)];exec('i,j,k=s();l[i:j+1]=l[k:j+1]+l[i:k];'*m);print(*l[1:])