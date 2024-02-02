from sys import stdin
inp = stdin.readline

class NGE:
    def __init__(self):
        self.n, self.ans = 0, []
        self.lst, self.stk = [], []
        self.getInfo()

    def getInfo(self):
        self.n = int(inp())
        self.ans = [-1 for _ in range(self.n)]
        self.lst = list(map(int, inp().split()))
        self.mainLogic()

    def mainLogic(self):
        for i in range(self.n):
            try:
                while self.lst[self.stk[-1]] < self.lst[i]:
                    self.ans[self.stk.pop()] = self.lst[i]
            except:
                pass

            self.stk.append(i)
        print(' '.join(map(str, self.ans)))

if __name__ == '__main__':
    NGE()