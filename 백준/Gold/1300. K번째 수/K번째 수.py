n=int(input())
k=int(input())
s,e=1,n*n
while s<=e:
 m=(s+e)//2
 c=sum(min(m//i,n)for i in range(1,n+1))
 if c>=k:e=m-1
 else:s=m+1
print(s)