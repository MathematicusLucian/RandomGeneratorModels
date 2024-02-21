import pytest
import numpy as np
from python_model.six.binarynumpyerrorh import BinaryNumpyWithErrorHandling

__random_nums = [-1, 0, 1, 2, 3]
__probs = [0.01, 0.3, 0.58, 0.1, 0.01]

# Test the constructor
def test_constructor():
    # Define the expected random_nums and probabilities
    random_nums = np.array([-1, 0, 1, 2, 3])
    probabilities = [0.01, 0.3, 0.58, 0.1, 0.01]
    
    # Create an instance of RandomGen
    random_gen = BinaryNumpyWithErrorHandling(__random_nums, __probs)
    
    # Check if _random_nums and _probabilities are set correctly
    assert np.array_equal(random_gen._random_nums, random_nums)
    assert np.array_equal(random_gen._probabilities, probabilities)

# Positive tests
# Call once: valid_random_num
@pytest.mark.parametrize("probs, random_nums", [(__probs, __random_nums)])
def test_positive_next_num_once__valid_random_num(probs, random_nums):
    random_gen = BinaryNumpyWithErrorHandling(random_nums,probs)
    results = random_gen.next_num()
    print(results)
    # for num, count in results.items():
    #     assert num in random_nums

# Call 100 times: valid_random_num
@pytest.mark.parametrize("iterations, probs, random_nums", [(100, __probs, __random_nums)])
def test_positive_next_num_100__valid_random_num(iterations, probs, random_nums):
    random_gen = BinaryNumpyWithErrorHandling(random_nums,probs)
    for _ in range(iterations):
        results = random_gen.next_num()
    for num, count in results.items():
        assert num in random_nums

# Call 100 times: valid_number_of_calls
@pytest.mark.parametrize("iterations, probs, random_nums", [(100, __probs, __random_nums)])
def test_positive_next_num_100__valid_number_of_calls(iterations, probs, random_nums):
    random_gen = BinaryNumpyWithErrorHandling(random_nums,probs)
    for _ in range(iterations):
        results = random_gen.next_num()
    cum_sum = 0
    for num, count in results.items():
        cum_sum += count   
    assert cum_sum == iterations

# # # Call once: one item
@pytest.mark.parametrize("iterations, probs, random_nums, expected_total", [(1, __probs, __random_nums, 1)])
def test_positive_next_num_once__one_item(iterations, probs, random_nums, expected_total):
    random_gen = BinaryNumpyWithErrorHandling(random_nums,probs)
    for _ in range(iterations):
        results = random_gen.next_num()
    for num, count in results.items():
        for numx, prob in zip(random_nums, probs):
            if numx == num:
                distribution = count/iterations
    assert distribution == expected_total

# # Call 100 times: probabilities_in_tolerance
@pytest.mark.parametrize("tolerance, iterations, probs, random_nums", [(0.1, 100, __probs, __random_nums)])
def test_positive_next_num_100__probabilities_in_tolerance(tolerance, iterations, probs, random_nums):
    random_gen = BinaryNumpyWithErrorHandling(random_nums,probs)
    for _ in range(iterations):
        results = random_gen.next_num()
    for num, count in results.items():
        for numx, prob in zip(random_nums, probs):
            if numx == num:
                distribution = count/iterations
                is_in_tolerance = prob - tolerance <= distribution <= prob + tolerance
        assert is_in_tolerance

# # Negative tests
# # Call 100 times: number_of_calls_not_zero
@pytest.mark.parametrize("iterations, probs, random_nums, not_expected_calls", [(100, __probs, __random_nums, 0)])
def test_positive_next_num_100__number_of_calls_not_zero(iterations, probs, random_nums, not_expected_calls):
    random_gen = BinaryNumpyWithErrorHandling(random_nums,probs)
    for _ in range(iterations):
        results = random_gen.next_num()
    cum_sum = 0
    for num, count in results.items():
        cum_sum += count   
    assert cum_sum != not_expected_calls

# # # Call once: total_probability_not_two
@pytest.mark.parametrize("iterations, probs, random_nums, not_expected_calls", [(1, __probs, __random_nums, 2)])
def test_positive_next_num_once__total_probability_not_two(iterations, probs, random_nums, not_expected_calls):
    random_gen = BinaryNumpyWithErrorHandling(random_nums,probs)
    for _ in range(iterations):
        results = random_gen.next_num()
    for num, count in results.items():
        for numx, prob in zip(random_nums, probs):
            if numx == num:
                distribution = count/iterations
    assert distribution != not_expected_calls