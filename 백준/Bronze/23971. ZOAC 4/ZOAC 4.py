h,w,n,m=map(int,input().split())
l=lambda x,y:(x+y)//(y+1)
print(l(h,n)*l(w,m))