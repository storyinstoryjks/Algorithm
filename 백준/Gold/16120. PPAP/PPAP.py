# https://www.acmicpc.net/problem/16120
# PPAP
# 스택,문자열

input=__import__('sys').stdin.readline

S=input()[:-1]
stk=[]
cnt_p,cnt_a=0,0

for i in S:
    if cnt_p<3:
        stk.append(i)
        if i=='P':cnt_p+=1
        else:cnt_a+=1
    elif cnt_a>0 and stk[-1:-5:-1]==['P','A','P','P']:
        for _ in range(4):
            t=stk.pop()
            if t=='P':cnt_p-=1
            else:cnt_a-=1
        stk.append('P');cnt_p+=1
        stk.append(i)
        if i=='P':cnt_p+=1
        else:cnt_a+=1
    else:
        stk.append(i)
        if i=='P':cnt_p+=1
        else:cnt_a+=1

if stk==['P','P','A','P'] or stk==['P']:
    print('PPAP')
else:
    print('NP')