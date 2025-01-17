# https://www.acmicpc.net/problem/25556
# 포스텍
# 스택, 그리디

input=__import__('sys').stdin.readline

n=int(input())
stacks=[[] for _ in range(4)]
A=[*map(int,input().split())]

stacks[0].append(A[0]) # 초기값 설정
for i in range(1,n):
    cur=A[i] # 현재 타겟 넘버
    flag,idx,value=False,0,200000 # 삽입후보존재여부,후보스택인덱스,해당값
    for j in range(4):
        ## 해당 스택이 공백이 아니고
        if stacks[j]: 
            # 현재 타겟이 해당 스택 마지막값보다 크고,
            # (타겟-스택마지막값)이 기존 후보의 차이값보다 작은 경우
            if cur>stacks[j][-1] and cur-stacks[j][-1]<value:
                flag=True
                idx,value=j,cur-stacks[j][-1] # 후보 갱신
        ## 이전 스택의 후보에 선정되지 못해서 이번 스택 공백에 넣어야 하는 경우
        elif not flag:
            stacks[j].append(cur)
            break
    # 후보 존재할 경우
    if flag:
        stacks[idx].append(cur)

answer=False
cur_target=n
while cur_target>=1:
    flag=False
    for i in range(4):
        if stacks[i] and stacks[i][-1]==cur_target:
            flag=True
            stacks[i].pop()
            break
    if not flag:
        answer=True
        break
    cur_target-=1

print("YNEOS"[answer::2])