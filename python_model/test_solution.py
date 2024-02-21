import pytest
from randomgen import RandomGen # TDD - writing tes"ts first

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
    for num, count in results.items():
        assert num in expected_output

# Negative tests
# Call 100 times: number_of_calls_not_zero
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