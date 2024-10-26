def solution(array, height):
    return len([*filter(lambda x:x>height,array)])