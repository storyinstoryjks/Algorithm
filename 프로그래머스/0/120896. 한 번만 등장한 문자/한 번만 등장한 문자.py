def solution(s):
    return ''.join([i for i in sorted(set(s)) if s.count(i)==1])