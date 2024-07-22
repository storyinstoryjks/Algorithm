h,w=map(int,input().split())
for _ in[0]*h:
 c=0;f=1;l=[]
 for i in[*input()]:
  if i=='.':
   if f:l+=[-1]
   else:c+=1;l+=[c]
   continue
  c=0;f=0;l+=[c]
 print(*l)