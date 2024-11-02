import math

def check(n):
    l=set()
    
    t=2
    while n>1:
        if t==n:
            l.add(n)
            break
        if n%t==0:
            n//=t
            l.add(t)
        else:
            t+=1
            
    l=sorted([*l])
    return l==[2] or l==[5] or l==[2,5] or l==[]
    
def solution(a, b):
    m=math.gcd(a,b)
    a,b=a//m,b//m
    return 3-(-~check(b))