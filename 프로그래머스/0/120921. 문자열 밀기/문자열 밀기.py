def solution(A, B):
    answer=-1
    
    for i in range(len(A)):
        if A==B:
            answer=i
            break
        A=A[-1]+A[:-1]
        
    return answer