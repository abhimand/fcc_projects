# to whoever reads this code, note this: the random methods generate different 
# cases for some god awful reason i do not understand why. for this reason, choice
# is the one i have been (forcefully) selected to pass the cases. other methods
# such as randint do not. from what i read, the seed generator influence the cases
# to either pass or fail. so im sticking with choice

import copy
import random
# Consider using the modules imported above.
import collections

class Hat:
    contents = []

    def __init__(self,**kwargs):
        self.contents = list(collections.Counter(kwargs).elements())
    
    def draw(self, num) -> list: 
        balls = []
        if num >= len(self.contents): 
            return self.contents
        for i in range(num):
            ball = random.choice(self.contents)
            balls.append(ball)
            self.contents.pop(self.contents.index(ball))

        return sorted(balls)


def experiment(hat, expected_balls, num_balls_drawn, num_experiments) -> float:
    M = 0
    expected_list = list(collections.Counter(expected_balls).elements())
    for iteration in range(num_experiments):
        h = copy.deepcopy(hat)
        actual_list = h.draw(num_balls_drawn)
        l = []
        for exp_ball in expected_list: 
            flag = 0
            for act_ball in actual_list: 
                if exp_ball == act_ball: 
                    flag = 1
                    actual_list.remove(act_ball)
            if flag == 1: 
                l.append(True)
            else: 
                l.append(False)
        if False not in l: 
            M += 1
    return (M/num_experiments)