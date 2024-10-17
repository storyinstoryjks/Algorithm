import math
def solution(slice, n):
    return math.floor(n/slice)+1 if n%slice>0 else n//slice