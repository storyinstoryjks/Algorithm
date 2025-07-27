# https://www.acmicpc.net/problem/19637
# IF문 좀 대신 써줘

from sys import stdin
input=stdin.readline

n,m=map(int,input().split())
books=[]

for _ in range(n):
    a,b=input().split()
    if books==[]:
        books.append((a,int(b)))
    elif books[-1][1]!=int(b):
        books.append((a,int(b)))
    
l=len(books)
for _ in range(m):
    target=int(input())
    left,right=0,l
    ans=right
    
    while left<=right:
        mid=(left+right)//2
        if target==books[mid][1]:
            ans=mid
            break
        if target<books[mid][1]:
            ans=mid
            right=mid-1
        else:
            left=mid+1
    
    print(books[ans][0])