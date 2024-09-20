from collections import deque

def checking(word1,word2,size):
    cnt=0
    for i in range(size):
        if word1[i]==word2[i]:
            cnt+=1
    return True if size-1==cnt else False
    
def bfs(start_w, goal_w, words):
    q=deque([[start_w,0,[start_w]]])
    word_size=len(start_w)
    
    while q:
        word,count,visited=q.popleft()
        if word==goal_w:
            return count
        for w in words:
            if checking(word,w,word_size) and w not in visited:
                q.append([w,count+1,visited+[w]])
    
    return 0
            
        
def solution(begin, target, words):
    return bfs(begin, target, words)