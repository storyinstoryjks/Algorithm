# https://www.acmicpc.net/problem/9184
# 신나는 함수 실행
# 재귀,DP

input=__import__('sys').stdin.readline
import sys
sys.setrecursionlimit(10**8)

def w(a,b,c):
    if a<=0 or b<=0 or c<=0:
        return 1
    if a>20 or b>20 or c>20:
        if (a,b,c) in dp.keys():
            return dp[(a,b,c)]
        dp[(a,b,c)]=w(20,20,20)
        return dp[(a,b,c)]
    if a<b and b<c:
        if (a,b,c) in dp.keys():
            return dp[(a,b,c)]
        dp[(a,b,c)]=w(a,b,c-1)+w(a,b-1,c-1)-w(a,b-1,c)
        return dp[(a,b,c)]
    
    if (a,b,c) in dp.keys():
        return dp[(a,b,c)]
    dp[(a,b,c)]=w(a-1,b,c)+w(a-1,b-1,c)+w(a-1,b,c-1)-w(a-1,b-1,c-1)
    return dp[(a,b,c)]
    

while True:
    a,b,c=map(int,input().split())
    if (a,b,c)==(-1,-1,-1):
        break
    dp={}
    dp[(a,b,c)]=w(a,b,c)
    print(f"w({a}, {b}, {c}) = {dp[(a,b,c)]}")