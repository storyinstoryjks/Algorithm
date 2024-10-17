def solution(n):
    return n//7+[0,1][n%7>0]