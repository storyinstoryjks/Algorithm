def solution(sides):
    answer = 0
    longest1 = max(sides)
    min_sides = min(sides)
    longest2 = sides[0]+sides[1]
    for i in range(longest1-min_sides, longest1+1):
        if i+min_sides>longest1:
            answer+=1
    for i in range(longest1+1, longest1+min_sides):
        if i<longest2:
            answer+=1
    return answer