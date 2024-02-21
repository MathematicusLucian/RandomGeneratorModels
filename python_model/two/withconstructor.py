import random

class RandomGen(object):
    # Values that may be returned by next_num()
    _random_nums = []
    # Probability of the occurence of random_nums
    _probabilities = [] 
    _results = {}

    def next_num(self):
        """
        Returns one of the randomNums. When this method is called multiple
        times over a long period, it should return the numbers roughly with
        the initialized probabilities.
        """
        rand_val = random.random()
        cumulative_prob = 0
        for i, prob in enumerate(self._probabilities):
            cumulative_prob += prob
            if rand_val <= cumulative_prob:
                num = self._random_nums[i]
                if num in self._results:
                    self._results[num] += 1
                else:
                    self._results[num] = 1
                return self._results