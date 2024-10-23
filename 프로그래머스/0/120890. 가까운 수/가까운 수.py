def solution(array, n):
    answer = 0
    check=1000
    for i in sorted(array):
        t=abs(i-n)
        if t<check:
            check=t;answer=i
    return answer