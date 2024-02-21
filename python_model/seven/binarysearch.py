import random

class RandomGenBinarySearch(object):
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

        # Precompute cumulative probabilities and sorted random numbers
        self._sorted_cumulative_probs, self._sorted_random_nums = self._precompute_cumulative_probs()

    def _precompute_cumulative_probs(self):
        """
        Returns one of the randomNums. When this method is called multiple
        times over a long period, it should return the numbers roughly with
        the initialized probabilities.
        """
        # Validate probabilities
        # Zip probabilities and random numbers, sort by probabilities in descending order
        sorted_prob_num = sorted(zip(self._probabilities, self._random_nums), key=lambda x: x[0], reverse=True)
        # Compute cumulative probabilities and extract sorted random numbers
        cumulative_probs = []
        sorted_random_nums = []
        total_prob = 0
        for prob, num in sorted_prob_num:
            total_prob += prob
            cumulative_probs.append(total_prob)
            sorted_random_nums.append(num)
        return cumulative_probs, sorted_random_nums

    @staticmethod
    def _binary_search(arr, target):
        left, right = 0, len(arr)
        while left < right:
            mid = (left + right) // 2
            if arr[mid] < target:
                left = mid + 1
            else:
                right = mid
        return left

    def next_num(self):
        """
        Returns one of the randomNums. When this method is called multiple
        times over a long period, it should return the numbers roughly with
        the initialized probabilities.
        """
        # Generate a random number between 0 and 1
        rand_val = random.random()
        # Use binary search to find the index of the random number
        index = self._binary_search(self._sorted_cumulative_probs, rand_val)
        # Return the corresponding random number
        num = self._sorted_random_nums[index]
        if num in self._results:
            self._results[num] += 1
        else:
            self._results[num] = 1
        return self._results