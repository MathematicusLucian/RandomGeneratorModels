from one.randomgen import RandomGen
from two.zippy import RandomGenZip
from three.randomchoices import RandomGenRandomChoices
from four.argmaxnumpy import RandomGenNumpyArgMax
from five.binarynumpy import RandomGenBinarySearchNumpy
from sIx.binarynumpyerrorh import BinaryNumpyWithErrorHandling
from seven.binarysearch import RandomGenBinarySearch
from utils.performance_test_engine import perform_performance_test

if __name__ == '__main__':

    # Test data
    random_nums = [-1, 0, 1, 2, 3]
    probabilities = [0.01, 0.3, 0.58, 0.1, 0.01]
    iterations = [10, 100, 1000, 10000]  # Add more sizes as needed
    PYTHON_RANDOM_GEN_CLASSES = [
        { "class": RandomGen, "name": 'Basic' },
        { "class": RandomGenZip, "name": 'Zip' },
        { "class": RandomGenRandomChoices, "name": 'Random Choices' },
        { "class": RandomGenNumpyArgMax, "name": 'Arg Max' },
        { "class": BinaryNumpyWithErrorHandling, "name": 'Numpy B Search wv EH' },
        { "class": RandomGenBinarySearchNumpy, "name": 'Numpy Binary Search' },
        { "class": RandomGenBinarySearch, "name": 'Binary Search' }
    ]

    performance_run = perform_performance_test(random_nums, probabilities, iterations, PYTHON_RANDOM_GEN_CLASSES)
    print(performance_run)