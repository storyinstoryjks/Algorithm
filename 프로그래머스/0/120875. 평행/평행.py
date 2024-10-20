from itertools import combinations
def solution(dots):
    for dot1,dot2 in combinations(dots,2):
        dot3,dot4=[i for i in dots if i not in [dot1,dot2]]
        if ((dot2[0]-dot1[0])/(dot2[1]-dot1[1]))==((dot4[0]-dot3[0])/(dot4[1]-dot3[1])):
            return 1
    return 0