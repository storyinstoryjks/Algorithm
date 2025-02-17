def solution(participant, completion):
    d={}
    for name in participant:
        try:
            d[name]+=1
        except:
            d[name]=1
    
    for name in completion:
        d[name]-=1
    
    answer=''
    for name in d.keys():
        if d[name]>=1:
            answer=name
            break
            
    return answer