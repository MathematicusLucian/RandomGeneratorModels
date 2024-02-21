# 🌟 RandomGeneratorModels 🌟 🚀 
---

## Table of Contents
1. [Introduction](#introduction)
2. [Python Models 🐍🐍🐍 - including with Numpy](#python)

    a. [First line/unit testing/TDD: PyTest](#pytest)

    b. [VirtualEnv](#virtualenv)

    c. [Requirements File](#generate-requirements-file)

3. [Java](#java)
---

# Introduction
The random generator services aim to generate random numbers based on the given probabilities. The probabilities are used to determine the likelihood of each random number occurring. This README file provides an explaination of the approach, and some instructions for setting up, running, testing, and deploying the random generator models.

*(Nb. these are within the same repo for simplicity when it comes to sharing this with whomever will review this; but if this was a real project, I would be inclined to have microservices in seperate repos, rather than a monorep.)*

Python was opted for.

# Python Models 🐍🐍🐍
This repo provides and compares the performance of seven Python models of a random number generator service. 

The solutions are as folows:
1. **Basic:** Simple implementation. Quickly thrown together, without third-party libraries. Iterates through probabilities to find the appropriate random number.
### OOP with a constructor
2. **Zip:** There is encouragement in the exercise critieria to look at making the solution more "pythonic". I added a constructor. I also used 'zip' to align the RandomNums and Probabilites arrays - intent being to speed up the model through "precompute" of the time-consuming alignment of the two arrays (RandomM and probabilities.)
3. **Random Choices:** I then added Random Choices. 
4. **Arg Max & Numpy:** Tried the third-party library Numpy to see if its array functions would speed up the model.
5. **Binary Search (with Numpy):** Implemented NumPy arrays to store random numbers and probabilities. At this momement, I also took binary search tree approach. The thought behind this was that combining NumPy efficient array operations with functional programming principles would leverage the best of both worlds: the computational efficiency and versatility of NumPy with the clarity and maintainability of functional programming. This was faster than Arg Max, but not as quick as the other vanilla approaches. This may need deeper investigation. NumPy allows operations to be performed on entire arrays at once, known as vectorization, and thus, avoids the need to explicitly loop over elements.
6. **Binary Search (with Numpy, and ErrorHandling):** I tweaked the approach from #5, and added some error handling. The next_num method utilizes NumPy functions like np.random.random() for generating random numbers and np.cumsum() for calculating cumulative probabilities. The np.argmax() function is employed again - to find the index of the first occurrence where the generated random number is less than the cumulative probabilities.
7. **Binary Search (without Numpty):** At this moment, I wanted to see like-for-like whether the binary search was faster with or without Numpy. 

``__init__`` utilised so that these are modules that can be referenced by the unit tests, and even hypothetically, Flask or FastAPI, or a performance tests.

### Navigate to the python directory
``cd python_models``: there is a directory for each of the seven solutions respectively.

### Install dependencies
``pip install -r requirements.txt``

### Run Python - without additional libraries
``python random_gen.py``

## First line/unit testing/TDD: PyTest
There is a file ``test_solution_all.py`` in the main 'python_models' folder that will call all 7 Python apps, and run tests on them. (Also, individual test files, if you prefer, in each folder, beside the respective Python app.)

``pytest --html=report.html test_solution.py``

![test results](./assets/randomgen_test_output.png)

![test results_details](./assets/randomgen_test_output2.png)

The unit tests are conducted for all the Python approaches, with or without a constructor, and whether or not they have third-party libraries. In all cases, the same test data is utilised.

As the output of the generator is random, this limits the test options, i.e. I cannot test that a certain integer value is returned. Thinking of financial scenarios, with considerations such as variability, and velocity, where deviance, such as beyond the efficient frontier, or high/low fluctuations in stock prices, may be critical, I tested that the count of each 'random number' is within a tolerance of its respective expected probability.

***Crude Factory:*** *I didn't want to write the same test code over and over, so I hacked together a crude factory method approach to feed the classes into a function, that generates each in turn, running the tests. If any fail, it gives the name of the respective class. This could be prettier, but I will stop there, because I have already exceeded the remit.*

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

# Java
**This has not received as much attention as the Python approach.** I have not pursued this far, because that would be beyond remit.

Provides a Java implementation of the random number generator service. Computes the cumulative probability and selects a random number based on the probabilities.

### Compile the Java code
I have not pursued this far, because that would be beyond remit, and do not promise that it functions well:
``javac RandomGen.java``

### Run the Java application
I have not pursued this far, because that would be beyond remit, and do not promise that it functions well: ``java RandomGen``

### <img src="./assets/JUnit.svg" width="20" height="20" /> Unit Tests
The file ``tests-junit.java``
