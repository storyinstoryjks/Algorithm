n=int(input())
P=sorted([*map(int,input().split())])
print(sum(P[i]*(n-i) for i in range(n)))