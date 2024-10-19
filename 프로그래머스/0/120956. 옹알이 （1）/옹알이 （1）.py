from itertools import permutations
def solution(babbling):
    cnt=0
    for i in range(1,5):
        for l in permutations(["aya","ye","woo","ma"],i):
            cnt+=babbling.count("".join(map(str,l)))
    return cnt