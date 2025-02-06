# https://www.acmicpc.net/problem/2776
# 암기왕
# 정렬,이분탐색,해시

input=__import__('sys').stdin.readline

for _ in range(int(input())):
    n=int(input())
    d={i:1 for i in [*map(int,input().split())]}
    m=int(input())
    for i in [*map(int,input().split())]:
        try:
            print(d[i])
        except:
            print(0)