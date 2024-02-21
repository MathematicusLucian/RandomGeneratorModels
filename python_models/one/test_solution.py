import pytest
from one.randomgen import RandomGen

__random_nums = [-1, 0, 1, 2, 3]
__probs = [0.01, 0.3, 0.58, 0.1, 0.01]

# Positive tests
# Call once: valid_random_num
@pytest.mark.parametrize("test_input, expected_output", [(__probs, __random_nums)])
def test_positive_next_num_once__valid_random_num(test_input, expected_output):
    random_gen = RandomGen()
    random_gen._random_nums = expected_output
    random_gen._probabilities = test_input
    random_gen._results = {}
    results = random_gen.next_num()
    for num, count in results.items():
        assert num in expected_output

# Call 100 times: valid_random_num
@pytest.mark.parametrize("test_input, expected_output", [(__probs, __random_nums)])
def test_positive_next_num_100__valid_random_num(test_input, expected_output):
    iterations = 100
    random_gen = RandomGen()
    random_gen._random_nums = expected_output
    random_gen._probabilities = test_input
    random_gen._results = {}
    for _ in range(iterations):
        results = random_gen.next_num()
        # print(results)
    for num, count in results.items():
        assert num in expected_output

# Call 100 times: valid_number_of_calls
iterations = 100
@pytest.mark.parametrize("test_input, probs, random_nums", [(iterations, __probs, __random_nums)])
def test_positive_next_num_100__valid_number_of_calls(test_input, probs, random_nums):
    random_gen = RandomGen()
    random_gen._random_nums = random_nums
    random_gen._probabilities = probs
    random_gen._results = {}
    for _ in range(test_input):
        print('1')
        results = random_gen.next_num()
        print(results)
    print(results)
    cum_sum = 0
    for num, count in results.items():
        cum_sum += count   
    assert cum_sum == test_input

# # # Call once: one item
@pytest.mark.parametrize("probs, random_nums, expected_output", [(__probs, __random_nums, 1)])
def test_positive_next_num_once__one_item(probs, random_nums, expected_output):
    iterations = 1
    random_gen = RandomGen()
    random_gen._random_nums = random_nums
    random_gen._probabilities = probs
    random_gen._results = {}
    for _ in range(iterations):
        results = random_gen.next_num()
    for num, count in results.items():
        for numx, y in zip(random_nums, probs):
            if numx == num:
                distribution = count/iterations
    assert distribution == expected_output

# # Call 100 times: probabilities_in_tolerance
@pytest.mark.parametrize("tolerance, probs, random_nums", [(0.1, __probs, __random_nums)])
def test_positive_next_num_100__probabilities_in_tolerance(tolerance, probs, random_nums):
    iterations = 100
    random_gen = RandomGen()
    random_gen._random_nums = random_nums
    random_gen._probabilities = probs
    random_gen._results = {}
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
@pytest.mark.parametrize("probs, random_nums, expected_output", [(__probs, __random_nums, 0)])
def test_positive_next_num_100__number_of_calls_not_zero(probs, random_nums, expected_output):
    iterations = 100
    random_gen = RandomGen()
    random_gen._random_nums = random_nums
    random_gen._probabilities = probs
    random_gen._results = {}
    for _ in range(iterations):
        results = random_gen.next_num()
    cum_sum = 0
    for num, count in results.items():
        cum_sum += count   
    assert cum_sum != expected_output

# # # Call once: total_probability_not_two
@pytest.mark.parametrize("probs, random_nums, expected_output", [(__probs, __random_nums, 2)])
def test_positive_next_num_once__total_probability_not_two(probs, random_nums, expected_output):
    iterations = 1
    random_gen = RandomGen()
    random_gen._random_nums = random_nums
    random_gen._probabilities = probs
    random_gen._results = {}
    for _ in range(iterations):
        results = random_gen.next_num()
    for num, count in results.items():
        for numx, prob in zip(random_nums, probs):
            if numx == num:
                distribution = count/iterations
    assert distribution != expected_output