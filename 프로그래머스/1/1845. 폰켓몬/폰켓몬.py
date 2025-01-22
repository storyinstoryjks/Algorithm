def solution(nums):
    answer = 0
    n,d=len(nums),{}
    
    for i in nums:
        if i not in d.keys():
            d[i]=1
            continue
        d[i]+=1
    
    check=[]
    for i in d.keys():
        if answer==n//2:
            break
        if i not in check:
            check.append(i)
            answer+=1
    
    return answer