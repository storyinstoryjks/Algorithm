def solution(my_string):
    return "".join([i.upper(),i.lower()][65<=ord(i)<=90]for i in my_string)