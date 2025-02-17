from itertools import combinations
def solution(clothes):
    answer=1
    d={}
    for cloth,type in clothes:
        try:
            d[type]+=1
        except:
            d[type]=1
    
    for key in d.keys():
        answer*=d[key]+1
        
    return answer-1