# https://www.acmicpc.net/problem/1662
# 압축
# 스택,재귀

input=__import__('sys').stdin.readline

stk=[]
before_str_cnt,k=0,''

for c in input()[:-1]:
    if c=='(':
        stk.append((before_str_cnt-1, k))
        before_str_cnt=0
    elif c==')':
        target_before_cnt,cur_k=stk.pop()
        before_str_cnt=before_str_cnt*cur_k+target_before_cnt
    else:
        before_str_cnt+=1
        k=int(c)

print(before_str_cnt)