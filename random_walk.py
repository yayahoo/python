from random import choice

class RandomWalk():
    def __init__(self,walk = 5000):
        #行走步数，默认5000
        self.walk = walk
        #起始位置
        self.x = [0]
        self.y = [0]
    def data(self):
        while len(self.x) < self.walk:
            x_dir = choice([1,-1])
            x_dis = choice(list(range(5)))
            x_step = x_dir * x_dis
            y_dir = choice([1, -1])
            y_dis = choice(list(range(5)))
            y_step = y_dir * y_dis
            if x_dis == 0 and y_dis == 0:
                continue
            next_x = self.x[-1]+x_step
            next_y = self.y[-1]+y_step
            self.x.append(next_x)
            self.y.append(next_y)
