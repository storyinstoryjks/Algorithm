def solution(emergency):
    return [{j:i+1 for i,j in enumerate(sorted(emergency)[::-1])}[i] for i in emergency]