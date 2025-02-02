n=int(input())
l=lambda x:sorted([*map(int,input().split())])[::x]
print(sum(i*j for i,j in zip(l(1),l(-1))))