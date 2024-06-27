q=input;n=int(q())
s=[0]+[*map(int,q().split())]
for _ in[0]*int(q()):
 p,N=map(int,q().split())
 if p<2:
  for i in range(N,n+1,N):s[i]=~s[i]+2
 else:
  for i in range(n//2):
   if N+i>n or N-i<1 or s[N+i]!=s[N-i]:break
   s[N+i],s[N-i]=~s[N+i]+2,~s[N-i]+2
for i in range(1,n+1):print(s[i],end=" \n"[i%20==0::2])