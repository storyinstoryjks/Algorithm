def solution(score):
    answer=[0]*len(score)
    
    l=sorted([*zip([(i+j)/2 for i,j in score],range(len(score)))],key=lambda x:-x[0])
    
    #print(l)
    rank,max_score,cnt=1,101,0
    for sc,idx in l:
        if sc!=max_score:
            max_score=min(sc,max_score)
            rank+=cnt
            answer[idx]=rank
            cnt=0
        else:
            rank-=1
            answer[idx]=rank
            cnt+=1
        rank+=1
            
    return answer