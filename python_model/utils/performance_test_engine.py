import time
import numpy as np
import pandas as pd

# Generate test data with varying sizes using Pandas DataFrame
def generate_test_data(iterations, random_nums, probabilities):
    data = []
    for size in iterations:
        data.append({'size': size, 'random_nums': random_nums, 'probabilities': probabilities})
    return pd.DataFrame(data)

# Performance test function
def perform_performance_test(df, PYTHON_RANDOM_GEN_CLASSES):
    
    execution_times = {}

    for _, row in df.iterrows():

        size = row['size']
        random_nums = row['random_nums']
        probabilities = row['probabilities']

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

    return execution_times