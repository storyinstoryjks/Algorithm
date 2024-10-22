def solution(n):
    k = 2
    answer = []
    while n>1:
        if n%k==0:
            answer.append(k)
            while n%k==0:
                n//=k
        k+=1

    return answer