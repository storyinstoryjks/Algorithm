for _ in[0]*int(input()):
    n=int(input())
    c=[0]*(n+1)
    for k in range(1,n+1):
        for i in range(1,n//k+1):
            c[k*i]=not c[k*i]
    print(sum(c))