s=lambda:map(int,input().split())
p=[0]+[*s()]
l=[0]*101
exec('b,e=s();l[b+1:e+1]=[x+1for x in l[b+1:e+1]];'*3)
print(sum(x*p[x]for x in l))