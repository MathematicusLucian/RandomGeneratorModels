import numpy as np

class RandomGenBinarySearchNumpy:
    def __init__(self, random_nums, probabilities):
        self._random_nums = np.array(random_nums)
        self._probabilities = np.array(probabilities)
        self._cumulative_prob = np.cumsum(self._probabilities, dtype=float)
        self._results = {}
        self.validate_probabilities()

    def validate_probabilities(self):
        prob_sum = self._cumulative_prob[len(self._cumulative_prob)-1]
        if not np.isclose(prob_sum, 1.0):
            raise ValueError("Sum of probabilities required to be 1")

    def next_num(self):
        rand_num = np.random.random()
        index = np.searchsorted(self._cumulative_prob, rand_num, side='right')
        num = self._random_nums[index]
        if num in self._results:
            self._results[num] += 1
        else:
            self._results[num] = 1
        return self._results