# 해시 버전
d={}
n=int(input())
for i in set(map(int,input().split())):
    try:d[i]+=1
    except:d[i]=1
m=int(input())
for i in map(int,input().split()):
    try:print(d[i],end=" ")
    except:print(0,end=" ")