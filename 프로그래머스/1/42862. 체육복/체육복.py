def solution(n, lost, reserve):
    tmp_lost=list(set(lost)-set(reserve))
    tmp_reserve=list(set(reserve)-set(lost))
    
    if tmp_reserve==[]:
        return n-len(tmp_lost)
    if tmp_lost==[]:
        return n
    
    cnt_find=0
    for i in tmp_lost:
        if i-1 in tmp_reserve:
            cnt_find+=1
            tmp_reserve.remove(i-1)
        elif i+1 in tmp_reserve:
            cnt_find+=1
            tmp_reserve.remove(i+1)
            
    return n-(len(tmp_lost)-cnt_find)