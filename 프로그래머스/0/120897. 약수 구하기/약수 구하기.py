def solution(n):
    answer = []
    for i in range(1,int(n**.5)+1):
        if i*(n//i)==n:
            answer.append(i)
            if i!=(n//i):
                answer.append(n//i)
    return sorted(answer)