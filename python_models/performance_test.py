from one.randomgen import RandomGen
from two.zippy import RandomGenZip
from three.randomchoices import RandomGenRandomChoices
from four.argmaxnumpy import RandomGenNumpyArgMax
from five.binarynumpy import RandomGenBinarySearchNumpy
from sIx.binarynumpyerrorh import BinaryNumpyWithErrorHandling
from seven.binarysearch import RandomGenBinarySearch
from utils.performance_test_engine import generate_test_data, evaluate_models
import matplotlib.pyplot as plt
from utils.plotter import add_data_to_plotter, generate_chart

def test_all_models(models_to_test, random_nums, probabilities, iteration_levels, tolerance):
    # Pandas dataframe
    prepared_test_dataframe = generate_test_data(iteration_levels, random_nums, probabilities)

    # Use the Performance Test Engine to run each model
    return evaluate_models(prepared_test_dataframe, models_to_test, tolerance)

def save_plot_chart(iteration_levels, execution_times_panda):
    # # Plot execution time vs. input size
    for generator_name, generator_times in execution_times_panda.items():
        add_data_to_plotter(plt, iteration_levels, generator_times, generator_name)
    generate_chart(plt)

if __name__ == '__main__':
    # Test data
    random_nums = [-1, 0, 1, 2, 3]
    probabilities = [0.01, 0.3, 0.58, 0.1, 0.01]
    iteration_levels = [10, 100, 1000, 10000]  # Add more levels as required
    tolerance = 1.0
    PYTHON_RANDOM_GEN_CLASSES = [
        { "class": RandomGen, "name": "Basic", "hasConstructor": False },
        { "class": RandomGenZip, "name": "Zip", "hasConstructor": True },
        { "class": RandomGenRandomChoices, "name": "Random Choices", "hasConstructor": True },
        { "class": RandomGenNumpyArgMax, "name": "Arg Max", "hasConstructor": True },
        { "class": BinaryNumpyWithErrorHandling, "name": "Numpy B Search wv EH", "hasConstructor": True },
        { "class": RandomGenBinarySearchNumpy, "name": "Numpy Binary Search", "hasConstructor": True },
        { "class": RandomGenBinarySearch, "name": "Binary Search", "hasConstructor": True }
    ]

    # Run the performance tests
    execution_times_panda = test_all_models(PYTHON_RANDOM_GEN_CLASSES, random_nums, probabilities, iteration_levels, tolerance)

    for generator_name, generator_times in execution_times_panda.items():
        print(f"\n{generator_name, iteration_levels, generator_times}")
    
    # This line runs the function to save the chart to file (when running on local machine; disabled on the server)
    # Could dump this image data in a different format into a database
    # save_plot_chart(iteration_levels, execution_times_panda)