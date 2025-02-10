# https://www.acmicpc.net/problem/2217
# 로프
# 수학, 그리디

input=__import__('sys').stdin.readline

n=int(input())
ropes=sorted([int(input()) for _ in range(n)])

answer=0
for i in range(n):
    answer=max(answer,(n-i)*ropes[i])

print(answer)