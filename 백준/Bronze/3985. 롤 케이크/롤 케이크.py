I=input
L=int(I())
c=[0]*4
f=[]
for i in range(int(I())):
 P,K=map(int,I().split())
 if K-P+1>c[1]:c[0]=i+1;c[1]=K-P+1
 t=0
 for j in range(P,K+1):
  if j not in f:f.append(j);t+=1
 if t>c[3]:c[3]=t;c[2]=i+1
print(c[0],c[2])