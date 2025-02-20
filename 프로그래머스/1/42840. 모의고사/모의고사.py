def solution(answers):
    scores = [0]*3
    students={
        0:'12345',
        1:'21232425',
        2:'3311224455'
    } # 5 8 10
    
    for problem_num in range(len(answers)):
        scores[0]+=(str(answers[problem_num])==students[0][problem_num%5])
        scores[1]+=(str(answers[problem_num])==students[1][problem_num%8])
        scores[2]+=(str(answers[problem_num])==students[2][problem_num%10])
    
    answer,target_score=[],0
    for student_id,score in sorted(enumerate(scores),key=lambda x:(x[1],-x[0]))[::-1]:
        if target_score==0:
            answer.append(student_id+1)
            target_score=score
        elif score==target_score:
            answer.append(student_id+1)
            
    return answer