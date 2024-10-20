def solution(n):
    a=[]
    for i in range(1,int(n**0.5)+1):
        for j in range(n//i,0,-1):
            if i*j==n:
                a.append((i,j))
                break
    return [len(a)*2,len(a)*2-1][a[-1][0]==a[-1][1]]