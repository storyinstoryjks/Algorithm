A,B=map(int,input().split())
F=lambda n:eval('^'.join(map(str,[*range(n//4*4,n+1)])))
print(F(A-1)^F(B))