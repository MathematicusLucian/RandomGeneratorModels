from flask import Flask, g, request, jsonify
import json
from flask_cors import CORS
from performance_test import test_all_models
from pathlib import Path
from seven.binarysearch import RandomGenBinarySearch

app = Flask(__name__)
CORS(app)
@app.route('/')
def index():
    return "I am the Random Generators API. Either call: '/run_model/<random_nums><probabilities>'; or, '/performance_data/'."

@app.route('/run_model/', methods=['POST'])
def run_model():
    data = request.json
    random_nums = data.get('random_nums', [])
    probabilities = data.get('probabilities', [])
    random_gen = RandomGenBinarySearch(random_nums, probabilities)
    num_iterations = 100
    results = []
    for _ in range(num_iterations):
        results.append(random_gen.next_num())
    return jsonify(results)

@app.route('/run_performance/', methods=['GET'])
def run_performance():
    # Test data
    random_nums = [-1, 0, 1, 2, 3]
    probabilities = [0.01, 0.3, 0.58, 0.1, 0.01]
    iterations = [10, 100, 1000, 10000]  # Add more sizes as needed
    execution_times_panda = test_all_models(random_nums,probabilities,iterations)

    performance_results_data = {}
    for generator_name, generator_times in execution_times_panda.items():
        mapped_exec_times = []
        for iteration, generator_time in zip(iterations, generator_times):
            if not [x for x in (iteration, generator_time) if x is None]:
                mapped_exec_times.append({iteration: generator_time})
            performance_results_data[generator_name] = mapped_exec_times
    # performance_results_data["message"] = "Data saved successfully."
    return jsonify(performance_results_data)