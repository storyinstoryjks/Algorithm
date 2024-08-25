n=1000-int(input())
c=0
for i in[500,100,50,10,5,1]:c+=n//i;n%=i
print(c)