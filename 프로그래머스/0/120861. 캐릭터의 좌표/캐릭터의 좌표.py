def solution(keyinput, board):
    answer = [0, 0]
    x_half_board=board[0]//2
    y_half_board=board[1]//2
    dic = {'up': [0, 1], 'down': [0, -1], 'left': [-1, 0], 'right': [1, 0]}

    for i in keyinput:
        answer[0]+=dic[i][0]
        answer[1]+=dic[i][1]
        if answer[0]<0 and answer[0] < -x_half_board:
            answer[0] = -x_half_board
        elif answer[0]>0 and answer[0]>x_half_board:
            answer[0] = x_half_board
        if answer[1]<0 and answer[1] < -y_half_board:
            answer[1] = -y_half_board
        elif answer[1]>0 and answer[1]>y_half_board:
            answer[1] = y_half_board
    return answer