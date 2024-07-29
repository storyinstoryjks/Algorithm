d={}
n=int(input())
for i in map(int,input().split()):
    try:d[i]+=1
    except:d[i]=1
m=int(input())
l=[]
for i in map(int,input().split()):
    try:l.append(d[i])
    except:l.append(0)
print(*l)