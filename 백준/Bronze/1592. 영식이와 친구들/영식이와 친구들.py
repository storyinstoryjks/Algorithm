n,m,l=map(int,input().split())
c=[0]*n;c[0]=1;i=0
while c[i]<m:
 if c[i]%2>0:
     i=(i+l)%n
     c[i]+=1
 else:
  i-=l
  if i<0:i=n+i
  c[i]+=1
print(sum(c)-1) 