q=lambda:map(int,input().split())
h,w=q()
s,a=[*q()],0
for i in range(1,w-1):
 m=min(max(s[:i]),max(s[i+1:]))
 if m>s[i]:a+=m-s[i]
print(a)