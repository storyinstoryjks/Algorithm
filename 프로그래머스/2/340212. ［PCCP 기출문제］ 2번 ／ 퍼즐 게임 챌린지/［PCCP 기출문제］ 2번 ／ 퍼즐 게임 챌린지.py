def solution(diffs, times, limit):
    # left,right,mid : level의 최소,최대,중간
    # 정답변수 : level_right
    left,right=1,max(diffs)
    answer=right
    diffs_size=len(diffs)
    
    while left<=right:
        mid=(left+right)//2
        
        cur_limit=times[0]
        for i in range(1,diffs_size):
            if diffs[i]<=mid:
                cur_limit+=times[i]
                continue
            cur_limit+=(times[i]+times[i-1])*(diffs[i]-mid)
            cur_limit+=times[i]

        if cur_limit<=limit:
            answer=min(answer,mid)
            right=mid-1
        else:
            left=mid+1
    
    return answer