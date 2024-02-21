# 🌟 RandomGeneratorModels 🌟 🚀 
---

## Table of Contents
1. [Introduction](#introduction)
2. [Python Models 🐍🐍🐍](#python)

    a. [First line/unit testing/TDD: PyTest](#pytest)

    b. [VirtualEnv](#virtualenv)

    c. [Requirements File](#generate-requirements-file)


---

# Introduction
The random generator services aim to generate random numbers based on the given probabilities. The probabilities are used to determine the likelihood of each random number occurring. This README file provides an explaination of the approach, and some instructions for setting up, running, testing, and deploying the random generator models.

*(Nb. these are within the same repo for simplicity when it comes to sharing this with whomever will review this; but if this was a real project, I would be inclined to have microservices in seperate repos, rather than a monorep.)*

Python was opted for.

# Python Models 🐍🐍🐍
This repo provides and compares the performance of two Python models of a random number generator service. 

The solutions are as folows:
1. **Basic:** Second-fastest. Simple implementation. Quickly thrown together, without third-party libraries. Iterates through probabilities to find the appropriate random number.
### OOP with a constructor
2. **Zip:** There is encouragement in the exercise critieria to look at making the solution more "pythonic". I added a constructor. I also used 'zip' to align the RandomNums and Probabilites arrays, but this was slower than the initial crude approach.

``__init__`` utilised so that these are modules that can be referenced by the unit tests, and even hypothetically, Flask or FastAPI, or a performance tests.

### Navigate to the python directory
``cd python_models``: there is a directory for each of the models respectively.

### Install dependencies
``pip install -r requirements.txt``

### Run Python - without additional libraries
``python random_gen.py``

## First line/unit testing/TDD: PyTest

``pytest --html=report.html test_solution.py``

![test results](./assets/randomgen_test_output.png)

![test results_details](./assets/randomgen_test_output2.png)

## VirtualEnv
A virtual environment (to ensure that the dependencies for the project are isolated from the system-wide Python installation, so as to facilitate distribution of the project.)

### Create a virtual environment named 'venv'
``pip3 install virtualenv``

``python3 -m venv randomgen_env``

Check running correctly: ``pip list`` (shows dependencies installed on the virtual environment.)

### Activate
On Windows: ``venv\Scripts\activate``

On macOS/Linux: ``source randomgen_env/bin/activate``

### Deactivate
``deactivate``

## Generate Requirements File
A requirements.txt file containing the dependencies installed to the virtual environment.

``pip install numpy`` etc.

Then: ``pip freeze > requirements.txt``

Install from a requirements file: ``pip install -r requirements.txt``