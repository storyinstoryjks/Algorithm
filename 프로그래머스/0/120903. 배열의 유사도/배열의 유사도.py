def solution(s1, s2):
    return len([1 for i in set(s1+s2) if i in s1 and i in s2])