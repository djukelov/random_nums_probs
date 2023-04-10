import random
import unittest

class TestRandomGen(unittest.TestCase):

    def setUp(self):
        self.rg = RandomGen()
        self.next_num_list = []


    #test case test_next_num checks that next_num method is returning a list of numbers and a list of probabilities that have the same length and the probabilities sum up to 1.0.
    def test_next_num(self):
        for self.i in range(6):
            self.rg.random_nums.append(random.random())
        for self.i in range(100):
            nums, probs = self.rg.next_num()
            self.assertEqual(len(nums), len(probs))
            self.assertAlmostEqual(sum(probs), 1.0)
        

class RandomGen: 
    def __init__(self):
        self.random_nums=[]
        self.probabilities=[]

    def next_num(self):
        try:    

            # Count the frequency of each value in the list
            counts = {}
            #getting one random number from the class
            next_num_list.append(random.choice(rg.random_nums))

        # probabilities.append
            for value in next_num_list:
                if value in counts:
                    counts[value] += 1
                else:
                    counts[value] = 1

            # Calculate the probability of each value
            total = len(next_num_list)

            # Print the probabilities
            rg.probabilities.clear()
            for value, count in counts.items():
                rg.probabilities.append(count/total)
            return rg.random_nums,rg.probabilities

            #catching execption if occured
        except Exception as e:
         print(e)

if __name__ == '__main__':

    # Create list where we saved all value retuned from next_num
    next_num_list =[]

    #We initialise the class RandomGen
    rg=RandomGen()

    # Initialize the class with 5 random values 
    for x in range(5):
        rg.random_nums.append(random.random())

    #Calling the method 100 times  
    for x in range(100):
        resp=rg.next_num()

    print(resp)


    #uncomment for running test
    #unittest.main()


