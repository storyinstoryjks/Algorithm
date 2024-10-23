def solution(s):
    s=s.split()
    return eval("+".join([[s[i],f"-{s[i-1]}"][s[i]=='Z'] for i in range(len(s))]))