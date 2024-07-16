I=input
n=int(I())
m=int(I())
h,i=[],0
for s in [*map(int,I().split())]:
 f=0
 for j in range(len(h)):
  if h[j][0]==s:h[j][1]+=1;f=1;break
 if f:continue
 i+=1
 if len(h)<n:h+=[[s,1,i]]
 else:h.sort(key=lambda x:(x[1],x[2]));h[0]=[s,1,i]
print(*[i[0]for i in sorted(h,key=lambda x:x[0])])