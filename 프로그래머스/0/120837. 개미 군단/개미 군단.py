def solution(hp):
    ans=0
    for i in [5,3,1]:
        ans+=hp//i
        hp%=i
    return ans