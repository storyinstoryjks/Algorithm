from itertools import permutations

def is_prime(n):
    if n<2:
        return False
    
    for i in range(2,int(n**.5)+1):
        if n%i==0:
            return False
    return True
    
def solution(numbers):
    answer = 0
    visited=set()
    
    for size in range(1,len(numbers)+1):
        for i in permutations(numbers,size):
            target=int(''.join(i))
            if target not in visited:
                if is_prime(target):
                    answer+=1
                visited.add(target)

    return answer