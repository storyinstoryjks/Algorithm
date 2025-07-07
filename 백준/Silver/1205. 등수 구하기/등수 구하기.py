# https://www.acmicpc.net/problem/1205
# 등수 구하기

n,s,p=map(int,input().split())
if n==0:
    print(1)
    exit(0)

l=[*map(int,input().split())]
rank=1
for score in l:
    if score>s:
        rank+=1
        continue
    if score==s:
        if n<p or rank+l.count(s)-1<n:
            print(rank); exit(0)
        else:
            print(-1); exit(0)
    else:
        print(rank); exit(0)

print(rank if rank<=p else -1)