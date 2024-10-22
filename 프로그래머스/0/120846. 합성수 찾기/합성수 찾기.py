def solution(n):
    cnt=0
    for i in range(1,n+1):
        tmp=0
        for j in range(1,int(i**0.5)+1):
            if i%j==0:
                tmp=tmp+2 if i!=j else tmp+1
        if tmp>=3:
            cnt+=1
    return cnt