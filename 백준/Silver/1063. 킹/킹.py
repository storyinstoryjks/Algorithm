f=lambda x,y:ord(x)-64+int(y)*10
g=lambda x:(9>x//10>0<x%10<9)^1
C=lambda x:chr(x%10+64)+str(x//10)
a,b,n=input().split()
k,s=f(*a),f(*b)
t="0"*8+"L0R"+"8"*8+"T"
for _ in[0]*int(n):
 r=0
 for c in input():r+=t.find(c)-9
 q=k;k+=r;s+=r*(k==s)
 if g(s):s,k=k,q
 if g(k):k=q
print(C(k),C(s))