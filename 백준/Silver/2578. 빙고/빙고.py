def k(t):
 for i in range(5):
  if b[i]==[0]*5:t+=1
 for i in range(5):
  if all(b[j][i]==0 for j in range(5)):t+=1
 if all(b[i][i]==0 for i in range(5)):t+=1
 if all(b[i][4-i] == 0 for i in range(5)):t+=1
 return t
b=[[*map(int,input().split())]for _ in range(5)]
s=[]
for _ in range(5):s+=[*map(int, input().split())]
c,t=0,0
for i in range(25):
 for x in range(5):
  for y in range(5):
   if s[i]==b[x][y]:b[x][y]=0;c+=1
 if c>=12:
  r=k(t)
  if r>=3:print(i+1);break