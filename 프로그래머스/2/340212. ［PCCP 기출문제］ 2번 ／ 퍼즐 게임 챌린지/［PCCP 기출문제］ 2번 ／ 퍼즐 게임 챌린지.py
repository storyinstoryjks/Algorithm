# left,right,mid : level의 최소,최대,중간
# 정답변수 : level_right

def solution(diffs, times, limit):
    # 1. 초기 설정
    left,right=1,max(diffs) # under-bound, upper-bound
    answer=right # 정답 변수
    diffs_size=len(diffs)
    
    # 2. 이분 탐색 시작
    while left<=right: # 2-4. left>right 될때까지 반복
        # 2-1. 중간값 구하기
        mid=(left+right)//2
        
        # 2-2. 모든 퍼즐을 푸는데 걸리는 시간 구하기
        cur_limit=times[0]
        for i in range(1,diffs_size):
            # 바로 성공 가능한 경우
            if diffs[i]<=mid:
                cur_limit+=times[i]
                continue
            # 바로 성공 불가능한 경우
            cur_limit+=(times[i]+times[i-1])*(diffs[i]-mid) # 이전 퍼즐 재풀이 시간
            cur_limit+=times[i] # 현재 퍼즐 시간
        
        # 2-3. 제한 시간 비교를 통해 Bound 갱신
        if cur_limit<=limit:
            answer=min(answer,mid)
            right=mid-1
        else:
            left=mid+1
    
    # 3. 정답 출력
    return answer