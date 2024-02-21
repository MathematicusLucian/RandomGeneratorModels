import random

class RandomGenNumpyArgMax:
    _random_nums = []
    _probabilities = [] 
    _results = {}

    # Added a constructor
    def __init__(self, random_nums, probabilities):
        """
        Initializes the RandomGen object with random numbers and their corresponding probabilities.
        """
        self._random_nums = random_nums
        self._probabilities = probabilities
        self._results = {}

    def next_num(self):
        """
        Returns one of the randomNums. When this method is called multiple
        times over a long period, it should return the numbers roughly with
        the initialized probabilities.
        """
        num = random.choices(self._random_nums, weights=self._probabilities)[0]
        if num in self._results:
            self._results[num] += 1
        else:
            self._results[num] = 1
        return self._results