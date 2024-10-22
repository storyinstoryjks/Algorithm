def solution(numbers):
    return eval("*".join(map(str,sorted(numbers)[-2:])))