# 난이도 : 보통
# 시간 : 40분
"""
핵심: "경계선 내부 공간을 어떻게 찾는가?"

1. 순차탐색 진행
2. 첫 경계선을 만나면, flag=True로 하여, '다음부터는 내부공간!'이란 의미 전달. (순차탐색: 왼쪽부터 하니까!)
3. flag=True and 선거구 미배정이면, 5번 선거구로 갱신!
"""
import sys
N = int(sys.stdin.readline())

pan = [[]]
for _ in range(N):
    pan.append([0] + list(map(int, sys.stdin.readline().split())))

def mancount(x,y,d1,d2):
    count = [0,0,0,0,0]
    fifth = [[0 for _ in range(N+1)] for i in range(N+1)]
    for i in range(d1+1):
        fifth[x+i][y-i] = 1 
        fifth[x+d2+i][y+d2-i] = 1 
    for j in range(d2+1):
        fifth[x+j][y+j] = 1 
        fifth[x+d1+j][y-d1+j] =1 
    for i in range(x+1,x+d1+d2):
        flag = False
        for j in range(N+1):
            if fifth[i][j]==1:
                if flag==True:
                    flag=False
                else:
                    flag=True
            else: 
                if flag==True:
                    fifth[i][j] = 1
    for i in range(1,N+1):
        for j in range(1,N+1):
            if i < x+d1 and j <= y and fifth[i][j] != 1:
                count[0] += pan[i][j]
            elif i <= x+d2 and y < j and fifth[i][j] != 1:
                count[1] += pan[i][j]
            elif x+d1 <= i and j < y-d1+d2 and fifth[i][j] != 1:
                count[2] += pan[i][j]
            elif x+d2 < i and y-d1+d2 <= j and fifth[i][j] != 1:
                count[3] += pan[i][j]
            elif fifth[i][j]==1:
                count[4] += pan[i][j]
    return max(count) - min(count)

min_count = float('inf')
for x in range(1, N+1):
    for y in range(1, N+1):
        for d1 in range(1, N+1):
            for d2 in range(1, N+1):
                if 1 <= x < x+d1+d2 <= N  and 1 <= y-d1 < y < y+d2 <= N:
                    min_count = min(min_count,mancount(x,y,d1,d2))

print(min_count)