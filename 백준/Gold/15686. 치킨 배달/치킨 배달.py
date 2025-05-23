import itertools;n,m=map(int,input().split());l=[[*map(int,input().split())]for _ in range(n)];c,h=[],[];r=999999
for i in range(n):
 for j in range(n):
  if l[i][j]==2:c+=[(i+1,j+1)]
  elif l[i][j]==1:h+=[(i+1,j+1)]
for C in itertools.combinations(c,m):
 d=0
 for i,j in h:d+=min(abs(x-i)+abs(y-j)for x,y in C)
 r=min(r,d)
print(r)