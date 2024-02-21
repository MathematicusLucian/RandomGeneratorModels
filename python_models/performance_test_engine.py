import time
from one.randomgen import RandomGen
from two.zippy import RandomGenZip
from three.randomchoices import RandomGenRandomChoices
from four.argmaxnumpy import RandomGenNumpyArgMax
from five.binarynumpy import RandomGenBinarySearchNumpy
from sIx.binarynumpyerrorh import BinaryNumpyWithErrorHandling
from seven.binarysearch import RandomGenBinarySearch

# The 'run_model' function calls the object's nexNum class, and returns execution time
def run_model(model):
    # print(model)
    start_time = time.time()
    for _ in range(10000):
        model.next_num()
    end_time = time.time()
    exec_time = (end_time - start_time)
    return exec_time

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
    
    execution_times = {}
    random_gen_objs = {}

    random_gen = PYTHON_RANDOM_GEN_CLASSES[0]["class"]()
    first_class = PYTHON_RANDOM_GEN_CLASSES[0]["name"]
    random_gen._random_nums = random_nums
    random_gen._probabilities = probabilities
    random_gen._results = {}
    random_gen_objs[first_class] = random_gen

    for random_gen_class in PYTHON_RANDOM_GEN_CLASSES[1:]:
        random_gen_class_name = random_gen_class["name"]
        random_gen_obj = random_gen_class["class"](random_nums, probabilities)
        random_gen_objs[random_gen_class_name] = random_gen_obj

    for generator_name, random_generator in random_gen_objs.items():
        # print(random_generator)
        start_time = time.time()
        for _ in range(10000):
            random_generator.next_num()
        end_time = time.time()
        if generator_name not in execution_times:
            execution_times[generator_name] = []   
        execution_times[generator_name].append(end_time - start_time)
    
    print(execution_times)