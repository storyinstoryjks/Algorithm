def solution(array):
    ll={i:array.count(i)for i in set(array)}
    m=max(ll.values())
    return -1 if [*ll.values()].count(m)>1 else {array.count(i):i for i in set(array)}.get(m)