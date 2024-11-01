def solution(n):
    answer = []
    
    num=1
    for i in range(1,101):
        while num%3==0 or '3' in str(num):
            num+=1
        answer.append(num)
        num+=1
    
    return answer[n-1]
