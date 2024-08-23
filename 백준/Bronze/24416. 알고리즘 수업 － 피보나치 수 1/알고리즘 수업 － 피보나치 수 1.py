# dp basic

def fib(n):
    f=[0]*(n+1)
    f[1]=f[2]=1
    for i in range(3,n+1):
        f[i]=f[i-1]+f[i-2]
    return f[n]

def fib_dp(n):
    return n-2

n=int(input())
print(fib(n),fib_dp(n))