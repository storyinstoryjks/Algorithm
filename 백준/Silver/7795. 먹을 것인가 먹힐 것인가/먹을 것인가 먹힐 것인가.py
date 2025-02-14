# https://www.acmicpc.net/problem/7795
# 먹을것인가 먹힐것인가
# 정렬,이분탐색,투포인터

input=__import__('sys').stdin.readline

for _ in range(int(input())):
    n,m=map(int,input().split())
    A=sorted([*map(int,input().split())])[::-1]
    B=sorted([*map(int,input().split())])[::-1]
    
    answer=0
    left=0
    for a in A:
        if a>B[left]:
            answer+=(m-left)
            continue
        while left<m:
            if a>B[left]:
                break
            left+=1
        if left>=m:
            break
        answer+=(m-left)
        
    print(answer)