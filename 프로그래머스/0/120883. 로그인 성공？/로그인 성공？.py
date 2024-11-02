def solution(id_pw, db):
    target=[*filter(lambda x:x[0]==id_pw[0],db)]
    return "fail" if target==[] else "wrong pw" if target[0][1]!=id_pw[1] else "login"