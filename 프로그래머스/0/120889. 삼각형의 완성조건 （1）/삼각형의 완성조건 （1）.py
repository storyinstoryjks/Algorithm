def solution(sides):
    return [2,1][max(sides)<sum(sorted(sides)[:-1])]