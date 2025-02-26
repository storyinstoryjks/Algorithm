from collections import deque

def solution(numbers, target):
    answer = 0
    n=len(numbers)
    
    q=deque([(numbers[0],0,1),(-numbers[0],0,1)])
    while q:
        num,idx,depth=q.popleft()
        if depth==n:
            if num==target:
                answer+=1
            continue
        next_idx=idx+1
        if next_idx<n:
            q.append((num+numbers[next_idx],idx+1,depth+1))
            q.append((num-numbers[next_idx],idx+1,depth+1))
    
    return answer