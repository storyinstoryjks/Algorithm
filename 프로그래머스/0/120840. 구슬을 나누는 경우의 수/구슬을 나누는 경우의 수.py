def solution(balls, share):
    l=lambda x:eval("*".join(map(str,[i+1 for i in range(x)]))) if x>0 else 1
    return l(balls)//(l(balls-share)*l(share))