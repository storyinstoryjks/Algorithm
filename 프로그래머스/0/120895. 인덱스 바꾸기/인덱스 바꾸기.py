def solution(st, n1, n2):
    return st[:n1]+st[n2]+st[n1+1:n2]+st[n1]+st[n2+1:]