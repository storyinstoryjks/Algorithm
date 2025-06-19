# https://www.acmicpc.net/problem/20125
# 쿠키 신체 측정

class Cookie():
    def __init__(self):
        self.n=int(input())
        self.board=[[*input()] for _ in range(self.n)]
        self.heart_idx=()
        self.leg_flag_idx=()
        self.spec=[0]*5
        
    def find_heart(self):
        for i in range(self.n):
            for j in range(self.n):
                if self.board[i][j]=='*':
                    return (i+1,j)
    
    def find_left_arm(self):
        for i in range(self.heart_idx[1]-1,-1,-1):
            if self.board[self.heart_idx[0]][i]=='*':
                self.spec[0]+=1
    
    def find_right_arm(self):
        for i in range(self.heart_idx[1]+1,self.n):
            if self.board[self.heart_idx[0]][i]=='*':
                self.spec[1]+=1
    
    def find_body(self):
        for i in range(self.heart_idx[0]+1,self.n):
            if self.board[i][self.heart_idx[1]]=='*':
                self.spec[2]+=1
            else:
                self.leg_flag_idx=(i-1,self.heart_idx[1])
                break
    
    def find_left_leg(self):
        for i in range(self.leg_flag_idx[0]+1, self.n):
            if self.board[i][self.leg_flag_idx[1]-1]=='*':
                self.spec[3]+=1
    
    def find_right_leg(self):
        for i in range(self.leg_flag_idx[0]+1, self.n):
            if self.board[i][self.leg_flag_idx[1]+1]=='*':
                self.spec[4]+=1
    
    def run(self):
        self.heart_idx=self.find_heart()
        self.find_left_arm(); self.find_right_arm()
        self.find_body()
        self.find_left_leg(); self.find_right_leg()
        print(self.heart_idx[0]+1,self.heart_idx[1]+1)
        print(*self.spec)
    

thread=Cookie()
thread.run()