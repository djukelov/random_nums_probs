import random

#You might implement this more "pythonically" when instead of initializing class variables outside of the class, use a constructor to initialize them inside the class.
#the logic of a function(in the current example - pass) has to be on the next row, otherways it will return invalid syntax.

class RandomGen:
    def __init__(self, random_nums, probabilities):
        self.random_nums = random_nums
        self.probabilities = probabilities

    def next_num(self):
        """
        Returns one of the random_nums. When this method is called multiple
        times over a long period, it should return the numbers roughly with
        the initialized probabilities.
        """
        pass

#When i read the task i notice something.
# As a quick check, given Random Numbers are [-1, 0, 1, 2, 3] and Probabilities are [0.01, 0.3, 0.58, 0.1, 0.01] if we call nextNum() 100 times
# The given probabilities are wrong the correct ones are [0.01,0.22,0.57,0.20,0] based on the output:
#-1:  1 times   ->  1/100 = 0.01
# 0:  22 times  ->  22/100 = 0.22
# 1:  57 times  ->  57/100 = 0.57
# 2:  20 times  ->  20/100 =0.20
# 3:  0 times   ->  0 