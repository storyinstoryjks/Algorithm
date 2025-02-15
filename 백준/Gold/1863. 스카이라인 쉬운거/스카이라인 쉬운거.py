# https://www.acmicpc.net/problem/1863
# 스카이라인 쉬운거
# 스택

input=__import__('sys').stdin.readline

stk,answer=[],0
for _ in range(int(input())):
    x,y=map(int,input().split())
    stk.append((x,y))

while stk:
    target_x,target_y=stk.pop()
    if target_y==0:
        continue
    
    tmp=[]
    while stk:
        if stk[-1][1]>target_y:
            tmp.append(stk.pop())
        elif stk[-1][1]==target_y:
            t=stk.pop()
            tmp.append((t[0],0))
        else:
            break
        
    while tmp:
        stk.append(tmp.pop())
        
    answer+=1

print(answer)