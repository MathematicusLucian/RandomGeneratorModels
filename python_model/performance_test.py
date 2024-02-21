from one.randomgen import RandomGen
from two.zippy import RandomGenZip
from three.randomchoices import RandomGenRandomChoices
from four.argmaxnumpy import RandomGenNumpyArgMax
from five.binarynumpy import RandomGenBinarySearchNumpy
from sIx.binarynumpyerrorh import BinaryNumpyWithErrorHandling
from seven.binarysearch import RandomGenBinarySearch
from utils.performance_test_engine import generate_test_data, perform_performance_test
import matplotlib.pyplot as plt
from utils.plotter import add_data_to_plotter, generate_chart

def test_all_models(random_nums,probabilities,iterations):
    PYTHON_RANDOM_GEN_CLASSES = [
        { "class": RandomGen, "name": 'Basic' },
        { "class": RandomGenZip, "name": 'Zip' },
        { "class": RandomGenRandomChoices, "name": 'Random Choices' },
        { "class": RandomGenNumpyArgMax, "name": 'Arg Max' },
        { "class": BinaryNumpyWithErrorHandling, "name": 'Numpy B Search wv EH' },
        { "class": RandomGenBinarySearchNumpy, "name": 'Numpy Binary Search' },
        { "class": RandomGenBinarySearch, "name": 'Binary Search' }
    ]
    test_data = generate_test_data(iterations, random_nums, probabilities)

    # Perform performance test
    return perform_performance_test(test_data, PYTHON_RANDOM_GEN_CLASSES)

if __name__ == '__main__':
    # Test data
    random_nums = [-1, 0, 1, 2, 3]
    probabilities = [0.01, 0.3, 0.58, 0.1, 0.01]
    iterations = [10, 100, 1000, 10000]  # Add more sizes as needed
    execution_times_panda = test_all_models(random_nums,probabilities,iterations)
    # # Plot execution time vs. input size
    for generator_name, generator_times in execution_times_panda.items():
        print(f"\n{generator_name, iterations, generator_times}")
        add_data_to_plotter(plt, iterations, generator_times, generator_name)
    generate_chart(plt)