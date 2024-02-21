import time
import numpy as np
import pandas as pd

# Generate test data with varying sizes using Pandas DataFrame
def generate_test_data(iteration_levels, random_nums, probabilities):
    data = []
    for size in iteration_levels:
        data.append({'size': size, 'random_nums': random_nums, 'probabilities': probabilities})
    return pd.DataFrame(data)

# Create model object from model class (and pass in the random_nums and probabilities values)
def prepare_model_to_run(generator_model_class, random_nums, probabilities):
    if generator_model_class["hasConstructor"]:
        generator_model_obj = generator_model_class["class"](random_nums, probabilities)
    else:
        # First model class does not have a constructor :. pass no parameters on object creation
        generator_model_obj = generator_model_class["class"]()
        # This is to keep to the structure given in the exericse
        # But I do not wish to pass values into a class in this way
        generator_model_obj._random_nums = random_nums
        generator_model_obj._probabilities = probabilities
        generator_model_obj._results = {}
    return generator_model_obj

# The 'run_model' function calls the object's nexNum class, and returns execution time
def run_model(model):
    # print(model)
    start_time = time.time()
    for _ in range(10000):
        model.next_num()
    end_time = time.time()
    exec_time = (end_time - start_time)
    return exec_time

# Returns the performance (execution time) of several models
def evaluate_models(prepared_test_dataframe, model_classes, tolerance):
    # The parameter 'tolerance' is not utilised - beyond remit of exercise
    # but would be interesting to see not just the speed, but the accuracy of models
    # It is however considered in the unit tests (where it was within range for all models)

    for _, row in prepared_test_dataframe.iterrows():
        size = row['size']
        random_nums = row['random_nums']
        probabilities = row['probabilities']

        # Put the objects here (that will be create per model class received)
        # These objects are declared here, and not global, i,e, 'reset' if run function more than once
        generator_model_objs = {}
        execution_times = {}

        # I could create the first object, cognisant that it does not have a constructor
        # and then reference the others with: for generator_model_class in model_classes[1:]:
        # But that is not dynamic; what if we want to add more models that do not have a constructor?
        for generator_model_class in model_classes:
            # Create model object from model class (and pass in the random_nums and probabilities values)
            generator_model_obj = prepare_model_to_run(generator_model_objs, generator_model_class, random_nums, probabilities)
            generator_model_class_name = generator_model_class["name"]
            generator_model_objs[generator_model_class_name] = generator_model_obj
            
        for model_name, model in generator_model_objs.items():
            # The 'run_model' function calls the object's nexNum class, and returns execution time
            exec_time = run_model(model)
            if model_name not in execution_times:
                execution_times[model_name] = []  
            execution_times[model_name].append(exec_time)

    return execution_times