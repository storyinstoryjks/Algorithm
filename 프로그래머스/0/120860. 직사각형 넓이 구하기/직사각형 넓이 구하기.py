def solution(dots):
    a,b,c,d = sorted(dots, key=lambda x:(x[0],x[1]))
    return (b[1] - a[1]) * (c[0] - b[0])