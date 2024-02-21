# 🌟 RandomGeneratorModels 🌟 🚀 

# Introduction
The random generator services aim to generate random numbers based on the given probabilities. The probabilities are used to determine the likelihood of each random number occurring.

Python was opted for.

# Python Model

## <img src="./assets/PyTest.svg" width="20" height="20" /> First line/unit testing/TDD: PyTest

``pytest --html=report.html test_solution.py``

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