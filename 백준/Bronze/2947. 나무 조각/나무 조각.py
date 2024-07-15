l=[*map(int,input().split())]
while l!=[1,2,3,4,5]:
 for i in range(4):
  if l[i]>l[i+1]:l[i],l[i+1]=l[i+1],l[i];print(*l)