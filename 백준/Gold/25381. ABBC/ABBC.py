# https://www.acmicpc.net/problem/25381
# ABBC
# 그리디,큐

input=__import__('sys').stdin.readline
deque=__import__('collections').deque

def check(c1,c2):
    cnt,left,right=0,0,1
    
    while True:
        while left<n and S[left]!=c1:
            left+=1
        while right<n and (S[right]!=c2 or left>right):
            right+=1
        if right==n:
            break
        S[left]='e'
        S[right]='e'
        cnt+=1
    
    return cnt

S=[*input()[:-1]]
n=len(S)
answer=0

answer+=check('B','C')
answer+=check('A','B')

print(answer)