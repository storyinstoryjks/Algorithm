# https://www.acmicpc.net/problem/5073
# 삼각형과 세변

while 1:
    a,b,c=map(int,input().split())
    if (a,b,c)==(0,0,0):
        break
    if a+b<=c or b+c<=a or a+c<=b:
        print("Invalid")
    elif a==b==c:
        print("Equilateral")
    elif a!=b and b!=c and a!=c:
        print("Scalene ")
    else:
        print("Isosceles ")