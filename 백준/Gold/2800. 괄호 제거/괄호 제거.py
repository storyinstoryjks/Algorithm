# https://www.acmicpc.net/problem/2800
# 괄호제거
# 문자열, 스택, 브루트포스

input=__import__('sys').stdin.readline
from itertools import combinations

S=input()[:-1]

## 올바른 괄호쌍 인덱스 검색 및 저장
bracket_idxs,stk=[],[]
for i in range(len(S)):
    if S[i]=='(':
        stk.append(i)
    elif S[i]==')':
        bracket_idxs.append((stk.pop(),i))

## 괄호 제거 경우들 찾기
answer=set()
for num in range(1,len(bracket_idxs)+1):
    for i in combinations(bracket_idxs,num):
        tmp=[*S]
        for left,right in i:
            tmp[left]=''
            tmp[right]=''
        answer.add(''.join(tmp))

for i in sorted(answer):
    print(i)