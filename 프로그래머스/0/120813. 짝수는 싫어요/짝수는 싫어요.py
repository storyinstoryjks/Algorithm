def solution(n):
    return [*filter(lambda x:x&1,range(1,n+1))]