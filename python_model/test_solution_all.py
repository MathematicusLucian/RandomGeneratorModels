import pytest
import numpy as np
from one.randomgen import RandomGen
from two.zippy import RandomGenZip
from three.randomchoices import RandomGenRandomChoices
from four.argmaxnumpy import RandomGenNumpyArgMax
from five.binarynumpy import RandomGenBinarySearchNumpy
from sIx.binarynumpyerrorh import BinaryNumpyWithErrorHandling
from seven.binarysearch import RandomGenBinarySearch

# Test data
__random_nums = [-1, 0, 1, 2, 3]
__probs = [0.01, 0.3, 0.58, 0.1, 0.01]
__tolerance = 1
PYTHON_RANDOM_GEN_CLASSES = [
    { "class": RandomGen, "name": 'Basic' },
    { "class": RandomGenZip, "name": 'Zip' },
    { "class": RandomGenRandomChoices, "name": 'Random Choices' },
    { "class": RandomGenNumpyArgMax, "name": 'Arg Max' },
    { "class": RandomGenBinarySearchNumpy, "name": 'Numpy Binary Search' },
    { "class": BinaryNumpyWithErrorHandling, "name": 'Numpy B Search wv EH' },
    { "class": RandomGenBinarySearch, "name": 'Binary Search' }
]

def create_random_gen(generator_obj):
    if(str(generator_obj["name"]).__eq__("Basic")):
        random_gen = generator_obj["class"]()
        random_gen._random_nums = __random_nums
        random_gen._probabilities = __probs
        random_gen._results = {}
    else:
        random_gen = generator_obj["class"](__random_nums,__probs)
    return random_gen

# # Test the constructor
# Define the test function that takes a class as a parameter
@pytest.mark.parametrize("generator_obj", [item for item in PYTHON_RANDOM_GEN_CLASSES])
def test_constructor(generator_obj):
    if(str(generator_obj["name"]) != "Basic"):    
        random_gen = generator_obj["class"](__random_nums,__probs)
        # Check if _random_nums and _probabilities are set correctly
        assert np.array_equal(random_gen._random_nums, __random_nums), f"{generator_obj['name']} object: Random numbers not set by constructor."
        assert np.array_equal(random_gen._probabilities, __probs), f"{generator_obj['name']} object: Probabilities not set by constructor."

# # Positive tests
# # Call once: valid_random_num
# Define the test function that takes a class as a parameter
@pytest.mark.parametrize("generator_obj", [item for item in PYTHON_RANDOM_GEN_CLASSES])
def test_positive_next_num_once__valid_random_num(generator_obj):
    random_gen = create_random_gen(generator_obj)
    results = random_gen.next_num()
    for num, count in results.items():
        assert num in __random_nums, f"{generator_obj['name']} object: Number {num} not found in random numbers: {__random_nums}."

# Call 100 times: valid_random_num
# Define the test function that takes a class as a parameter
@pytest.mark.parametrize("generator_obj, iterations", [(item, 100) for item in PYTHON_RANDOM_GEN_CLASSES])
def test_positive_next_num_100__valid_random_num(generator_obj, iterations):
    random_gen = create_random_gen(generator_obj)
    for _ in range(iterations):
        results = random_gen.next_num()
    for num, count in results.items():
        assert num in __random_nums, f"{generator_obj['name']} object: Number {num} not found in random numbers: {__random_nums}."

# Call 100 times: valid_number_of_calls
# Define the test function that takes a class as a parameter
@pytest.mark.parametrize("generator_obj, iterations", [(item, 100) for item in PYTHON_RANDOM_GEN_CLASSES])
def test_positive_next_num_100__valid_number_of_calls(generator_obj, iterations):
    random_gen = create_random_gen(generator_obj)
    for _ in range(iterations):
        results = random_gen.next_num()
    cum_sum = 0
    for num, count in results.items():
        cum_sum += count   
    assert cum_sum == iterations, f"{generator_obj['name']} object: sum {cum_sum} not equal to iterations {iterations}."

# # # Call once: one item
# Define the test function that takes a class as a parameter
@pytest.mark.parametrize("generator_obj, iterations, expected_total", [(item, 1, 1) for item in PYTHON_RANDOM_GEN_CLASSES])
def test_positive_next_num_once__one_item(generator_obj, iterations, expected_total):
    random_gen = create_random_gen(generator_obj)
    for _ in range(iterations):
        results = random_gen.next_num()
    for num, count in results.items():
        for numx, prob in zip(__random_nums, __probs):
            if numx == num:
                distribution = count/iterations
    assert distribution == expected_total, f"{generator_obj['name']} object: Distribution is {num} not 1."

# # Call 100 times: probabilities_in_tolerance
# Define the test function that takes a class as a parameter
@pytest.mark.parametrize("generator_obj, tolerance, iterations", [(item, __tolerance, 100) for item in PYTHON_RANDOM_GEN_CLASSES])
def test_positive_next_num_100__probabilities_in_tolerance(generator_obj, tolerance, iterations):
    random_gen = create_random_gen(generator_obj)
    for _ in range(iterations):
        results = random_gen.next_num()
    for num, count in results.items():
        for numx, prob in zip(__random_nums, __probs):
            if numx == num:
                distribution = count/iterations
                is_in_tolerance = prob - tolerance <= distribution <= prob + tolerance
        assert is_in_tolerance, f"{generator_obj['name']} object: Tolerance not met {is_in_tolerance}."

# # Negative tests
# # Call 100 times: number_of_calls_not_zero
# Define the test function that takes a class as a parameter
@pytest.mark.parametrize("generator_obj, iterations, not_expected_calls", [(item, 100, 0) for item in PYTHON_RANDOM_GEN_CLASSES])
def test_positive_next_num_100__number_of_calls_not_zero(generator_obj, iterations, not_expected_calls):
    random_gen = create_random_gen(generator_obj)
    for _ in range(iterations):
        results = random_gen.next_num()
    cum_sum = 0
    for num, count in results.items():
        cum_sum += count   
    assert cum_sum != not_expected_calls, f"{generator_obj['name']} object: Total of probabilities {cum_sum} equal to {not_expected_calls}l should be 1."

# # # Call once: total_probability_not_two
# Define the test function that takes a class as a parameter
@pytest.mark.parametrize("generator_obj, iterations, not_expected_calls", [(item, 1, 2) for item in PYTHON_RANDOM_GEN_CLASSES])
def test_positive_next_num_once__total_probability_not_two(generator_obj, iterations, not_expected_calls):
    random_gen = create_random_gen(generator_obj)
    for _ in range(iterations):
        results = random_gen.next_num()
    for num, count in results.items():
        for numx, prob in zip(__random_nums, __probs):
            if numx == num:
                distribution = count/iterations
    assert distribution != not_expected_calls, f"{generator_obj['name']} object: Distribution {distribution} equal to {not_expected_calls}; should be 1."