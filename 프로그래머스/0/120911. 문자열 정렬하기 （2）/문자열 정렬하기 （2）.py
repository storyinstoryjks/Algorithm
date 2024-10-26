def solution(my_string):
    return ''.join(sorted(map(lambda x:x.lower(),my_string)))