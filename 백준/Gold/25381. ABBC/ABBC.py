# https://www.acmicpc.net/problem/25381
# ABBC
# 그리디,큐

input=__import__('sys').stdin.readline
deque=__import__('collections').deque

AQ,BQ,CQ=[],[],[]
for i,e in enumerate([*input()[:-1]]):
    if e=='A':AQ.append(i)
    elif e=='B':BQ.append(i)
    else:CQ.append(i)

answer=0

while BQ!=[] and CQ!=[]:
    if CQ[0]<BQ[0]:
        CQ.pop(0)
        continue
    BQ.pop(0)
    CQ.pop(0)
    answer+=1

while AQ!=[] and BQ!=[]:
    if BQ[0]<AQ[0]:
        BQ.pop(0)
        continue
    AQ.pop(0)
    BQ.pop(0)
    answer+=1

print(answer)