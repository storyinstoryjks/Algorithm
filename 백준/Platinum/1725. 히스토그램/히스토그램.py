import sys;p=sys.stdin.readline
l=[0]+[int(p())for _ in[0]*int(p())]+[0];s,a=[0],0
for i in range(1,len(l)):
 while s and l[s[-1]]>l[i]:e=s.pop();a=max(a,(i-1-s[-1])*l[e])
 s+=[i]
print(a)