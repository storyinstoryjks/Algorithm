def solution(my_string):
    l=[];exec('for i in my_string:l.append(i) if i not in l else []')
    return "".join(l)