def solution(n):
    return len([*filter(lambda x:x<=n,[eval("*".join(map(str,range(1,i+2))))for i in range(10)])])