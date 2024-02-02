l=input();r=0;t=1;f=1;s=[]
for i in range(len(l)):
 if l[i]=="(":t*=2;s+=[l[i]]
 elif l[i]=="[":t*=3;s+=[l[i]]
 elif (l[i]==")"and(s==[]or s[-1]!="("))or(l[i]=="]"and(s==[]or s[-1]!="[")):f=0;break
 elif l[i]==")":
  if l[i-1]=="(":r+=t;
  s.pop();t//=2
 else:
  if l[i-1]=="[":r+=t;
  s.pop();t//=3
print([r,0][f==0 or s!=[]])