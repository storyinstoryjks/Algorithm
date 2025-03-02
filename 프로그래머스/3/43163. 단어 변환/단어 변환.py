from collections import deque

def solution(begin, target, words):
    if target not in words:
        return 0
    
    q=deque([(begin,0)])
    visited=set()
    visited.add(begin)
    
    str_size=len(begin)
    alphas=[]
    for i in range(str_size):
        tmp=set()
        for word in words:
            tmp.add(word[i])
        alphas.append([*tmp])

    while q:
        word,depth=q.popleft()
        for i in range(str_size):
            flag=False
            for c in alphas[i]:
                next_word=[*word]
                next_word[i]=c
                next_word=''.join(next_word)
                if (next_word in words) and (next_word not in visited):
                    if next_word==target:
                        return depth+1
                    visited.add(next_word)
                    q.append((next_word,depth+1))

    
    return 0
            