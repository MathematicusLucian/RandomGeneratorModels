import random

class RandomGen(object):
    # Values that may be returned by next_num()
    _random_nums = []
    # Probability of the occurence of random_nums
    _probabilities = [] 

    def next_num(self):
        """
        Returns one of the randomNums. When this method is called multiple
        times over a long period, it should return the numbers roughly with
        the initialized probabilities.
        """
        return {}