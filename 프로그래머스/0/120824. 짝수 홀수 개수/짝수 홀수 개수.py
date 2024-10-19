def solution(num_list):
    return [len([*filter(lambda x:x&1==0,num_list)]),len([*filter(lambda x:x&1,num_list)])]