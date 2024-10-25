def solution(quiz):
    return ['XO'[eval(i.split('=')[0])==int(i.split('=')[1])] for i in quiz]