s=lambda:map(int,input().split())
n,w,l=s()
q,a=[*s()],0
t=[0]*w
while t:
 t.pop(0);a+=1
 if q:t.append(q.pop(0))if sum(t)+q[0]<=l else t.append(0)
print(a)