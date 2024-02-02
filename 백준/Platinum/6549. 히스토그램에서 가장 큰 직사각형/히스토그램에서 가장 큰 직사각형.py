while 1:
 n,*l=[*map(int,input().split())]
 if n==0:break
 l=[0]+l+[0];c=[0];a=0
 for i in range(1,n+2):
  while(c and(l[c[-1]]>l[i])):d=c.pop();a=max(a,(i-1-c[-1])*l[d])
  c+=[i]
 print(a)