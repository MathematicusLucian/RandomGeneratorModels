from flask import Flask, g, request, jsonify
import sqlite3
import json
from flask_cors import CORS
from performance_test import test_all_models
from dotenv import load_dotenv  
from pathlib import Path
import os 
from seven.binarysearch import RandomGenBinarySearch

env_path = Path('.') / '.env'
load_dotenv(dotenv_path=env_path)

app = Flask(__name__)
CORS(app)

DATABASE = os.environ.get('DATABASE')

def get_db():
    db = getattr(g, '_database', None)
    if db is None:
        db = g._database = sqlite3.connect(DATABASE)
        db.row_factory = sqlite3.Row
    return db

def save_to_db(data):
    try:
        db = get_db()
        print("No database")
        cursor = db.cursor()
        cursor.execute('''CREATE TABLE IF NOT EXISTS generator_runs (
                            id INTEGER PRIMARY KEY,
                            data TEXT
                        )''')
        json_data = json.dumps(data)
        cursor.execute("INSERT INTO generator_runs (data) VALUES (?)", (json_data,))
        db.commit()
    except:
        print("No database")

@app.teardown_appcontext
def close_connection(exception):
    db = getattr(g, '_database', None)
    if db is not None:
        db.close()

@app.route('/')
def index():
    return {"I am the Random Generators API.":"Either call: POST '/run_model/' with params in Body: <random_nums><probabilities>'; or, 'GET /performance_data/'."}

@app.route('/run_model', methods=['POST'])
def run_model():
    if request.method == 'POST':
        req_data_json = request.get_json(force=True)
        random_nums = req_data_json.get('randomNums', '')
        probabilities = req_data_json.get('probabilities', '')
        if random_nums!=None and probabilities!=None:
            random_gen = RandomGenBinarySearch(random_nums, probabilities)
            num_iterations = 100
            results = []
            for ix in range(num_iterations):
                x = random_gen.next_num()
                if((int(ix)+1) == num_iterations):
                    results = {"i": ix, "num_iterations": num_iterations, "nums": x}
            return jsonify(results)
        else:
            return jsonify({"Please define the parameters": "Either 'random_nums' or 'probabilities' is empty"})
    else:
        return jsonify({
                "I only accept POST requests.": "Call me from https://reqbin.com/ >> put these parameters in the POST body"
            },
            {
                "randomNums": [-1, 0, 1, 2, 3],
                "probabilities": [0.01, 0.3, 0.58, 0.1, 0.01]
            },
            {
                "Or, use CURL": "curl -X POST -H \"Content-Type: application/json\" -d '{\"random_nums\":[-1,0,1,2,3],\"probabilities\":[0.01,0.3,0.58,0.1,0.01]}' https://mathematicuslucian.eu.pythonanywhere.com/run_model"
            })

@app.route('/run_performance', methods=['GET'])
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
    save_to_db(performance_results_data)
    # performance_results_data["message"] = "Data saved successfully."
    return jsonify(performance_results_data)

@app.route('/performance_results_all', methods=['GET'])
def performance_results_all():
    try:
        db = get_db()
        cur = db.cursor()
        cur.execute('SELECT * FROM generator_runs')
        rows = cur.fetchall()
        formatted = {}
        # Calculate averages
        for row in rows:
            data = json.loads(row['data'])
            for model, iterations in data.items():
                for iteration_pair in iterations:
                    for iteration, exec_speed in iteration_pair.items():
                        if model not in formatted:
                            formatted[model] = {}
                        if iteration not in formatted[model]:
                            formatted[model][iteration] = []
                        formatted[model][iteration].append(exec_speed)
        return jsonify(formatted)
    except:
        return jsonify({"Error":"Cannot fetch from database; or cannot format data"})

@app.route('/performance_results_avg', methods=['GET'])
def performance_results_avg():
    try:
        db = get_db()
        cur = db.cursor()
        cur.execute('SELECT * FROM generator_runs')
        rows = cur.fetchall()
        formatted = {}
        averages = {}
        # Calculate averages
        for row in rows:
            data = json.loads(row['data'])
            for model, iterations in data.items():
                for iteration_pair in iterations:
                    for iteration, exec_speed in iteration_pair.items():
                        if model not in formatted:
                            formatted[model] = {}
                        if iteration not in formatted[model]:
                            formatted[model][iteration] = []
                        formatted[model][iteration].append(exec_speed)
        for modelx, several_times_per_iteration_level in formatted.items():
            averages[modelx] = {}
            for iteration_level, times in several_times_per_iteration_level.items():
                averages[modelx][iteration_level] = {}
                averages[modelx][iteration_level]["times"] = times
                avg_time = sum(times) / len(times)
                averages[modelx][iteration_level]["avg"] = avg_time
        return jsonify(averages)
    except:
        return jsonify({"Error":"Cannot fetch from database; or cannot format data"})

if __name__ == '__main__':
    app.run(debug=True)