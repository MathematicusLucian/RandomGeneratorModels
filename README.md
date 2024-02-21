# 🌟 RandomGeneratorModels 🌟 🚀 

**⚡️ LIVE ⚡️ The models are hosted, and they can be triggered with this Flask API endpoint:** 

[Click here to open the ``/run_performance`` endpoint](https://mathematicuslucian.eu.pythonanywhere.com/run_performance)

- This will take a split-second to load; because it runs a thousand iterations, and across seven Python models, but it will then show you the performance/execution times. *(Alternatively, use [ReqBin](https://reqbin.com/), or [Postman](https://www.postman.com/) for the ``/get_model`` POST request that will allow you to change the parameters. See the section below.)*
---

[![skills](https://skillicons.dev/icons?i=python,flask,java,typescript,js,html,css,react,babel,redux,npm,webpack,jest,sqlite,md,git&perline=8)](https://skillicons.dev)


## Table of Contents
1. [Introduction](#introduction)
2. [Python Models (x7) 🐍🐍🐍 - including with Numpy](#python)

    a. [First line/unit testing/TDD: PyTest](#pytest)

    b. [🌟 Python Performance Tests 📈 - utilises Panda, and MatPlotLib](#python-performance-tests)

    c. [VirtualEnv](#virtualenv)

    d. [Requirements File](#generate-requirements-file)

***Work-in-Progress*** *(These fall outside of the remit. I saw may Quant roles ask for React and Python, and wanted to demonstrate that I can build a fullstack app.)*

3. [Java Model](#java)
4. [TypesScript Model](#typescript)
5. [Flask API](#flask-api)
6. [React UI](#react-ui)
7. [Deployment](#deployment)
---

# Introduction
The random generator services aim to generate random numbers based on the given probabilities. The probabilities are used to determine the likelihood of each random number occurring. Python was opted for. *(There are also implementations in Java, and TypeScript, though less time was put into these solutions. I wrote a WebAssembly model with Rust, but I have not committed this to the repo.)* This README file provides an explanation of the approach, and some instructions for setting up, running, testing, and deploying the random generator services in different languages. 

*(Nb. these are within the same repo for simplicity when it comes to sharing this with whomever will review this; but if this was a real project, I would be inclined to have microservices in seperate repos, rather than a monorep.)*

![chart of performance speeds](./assets/generator_perf_test_results.png)

# Python Models 🐍🐍🐍
![python](https://img.shields.io/badge/Python-FFD43B?style=for-the-badge&logo=python&logoColor=blue)
![numpy](https://img.shields.io/badge/Numpy-777BB4?style=for-the-badge&logo=numpy&logoColor=white)

This repo provides and compares the performance of seven Python models of a random number generator service. 

The solutions are as folows:
1. **Basic:** Simple implementation. Quickly thrown together, without third-party libraries. Iterates through probabilities to find the appropriate random number.
### OOP with a constructor
2. **Zip:** There is encouragement in the exercise critieria to look at making the solution more "pythonic". I added a constructor. I also used 'zip' to align the RandomNums and Probabilites arrays - intent being to speed up the model through "precompute" of the time-consuming alignment of the two arrays (RandomM and probabilities), but this was slower than the initial crude approach.
3. **Random Choices:** I then added Random Choices, but I found this was even slower. 
4. **Arg Max & Numpy:** Tried the third-party library Numpy to see if its array functions would speed up the model.  I found Arg Max was slower again (the less optimal peformance of the 7 solutions.)
5. **Binary Search (with Numpy):** Implemented NumPy arrays to store random numbers and probabilities. At this momement, I also took binary search tree approach. The thought behind this was that combining NumPy efficient array operations with functional programming principles would leverage the best of both worlds: the computational efficiency and versatility of NumPy with the clarity and maintainability of functional programming. This was faster than Arg Max, but not as quick as the other vanilla approaches. This may need deeper investigation. NumPy allows operations to be performed on entire arrays at once, known as vectorization, and thus, avoids the need to explicitly loop over elements.
6. **Binary Search (with Numpy, and ErrorHandling):** I tweaked the approach from #5, and added some error handling, but the performance difference was negligible. The next_num method utilizes NumPy functions like np.random.random() for generating random numbers and np.cumsum() for calculating cumulative probabilities. The np.argmax() function is employed again - to find the index of the first occurrence where the generated random number is less than the cumulative probabilities.
7. **Most Optimal  🌟 🌟 🌟 Binary Search (without Numpty):** At this moment, I wanted to see like-for-like whether the binary search was faster with or without Numpy. 

``__init__`` utilised so that these are modules that can be referenced by the unit tests, and even hypothetically, Flask or FastAPI, or a performance tests.

### The Python models directory
``cd python_models``: there is a directory for each of the seven solutions respectively.

### Install dependencies
``pip install -r requirements.txt``

### Run Python model ONE - without additional libraries
``python random_gen.py``

## 👩‍🔬 First line/unit testing/TDD: PyTest
There is a file ``test_solution_all.py`` in the main 'python_models' folder that will call all 7 Python apps, and run tests on them. (Also, individual test files, if you prefer, in each folder, beside the respective Python app.)

Navigate to the directory of one of the models: ``pytest --html=report.html test_solution.py``

![test results](./assets/randomgen_test_output.png)

![test results_details](./assets/randomgen_test_output2.png)

The unit tests are conducted for all the Python approaches, with or without a constructor, and whether or not they have third-party libraries. In all cases, the same test data is utilised.

As the output of the generator is random, this limits the test options, i.e. I cannot test that a certain integer value is returned. Thinking of financial scenarios, with considerations such as variability, and velocity, where deviance, such as beyond the efficient frontier, or high/low fluctuations in stock prices, may be critical, I tested that the count of each 'random number' is within a tolerance of its respective expected probability.

***🏭 Crude Factory:*** *I didn't want to write the same test code over and over, so I hacked together a crude factory method approach to feed the classes into a function, that generates each in turn, running the tests. If any fail, it gives the name of the respective class. This could be prettier, but I will stop there, because I have already exceeded the remit.*

## 🌟 Performance Test Engine (Python) 📈
![pandas](https://img.shields.io/badge/Pandas-2C2D72?style=for-the-badge&logo=pandas&logoColor=white) **MatPlotLib**

In ``performance_test_engine.py``.

- **Sample implementation:** In the file ``performance_test.py``. This can be triggered from a FASTAPI or Flask API service, or you can call it from the CLI: ``python3 performance_test.py``

- **Purpose:** I need to evalute these models, and find out their actual speeds, to compare their performance. The performance test is conducted for all the Python approaches, with or without a constructor, and whether or not they have third-party libraries. In all cases, the same test data is utilised (and prepared as a Pandas dataframe):

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

- **Pandas 🐼🐼🐼:** The ``generate_test_data`` function (in the utils folder) runs the performance tests. It returns it as a Pandas DataFrame, featuring the execution times for each generator to each defined level of iteration. I implemented with Pandas to handle the input data in a more structured and efficient way. (Or perhaps an excuse to demonstrate that I can utilise these third-party libraries.)

- **📈 Chart with MatPlotLib** I employed MatPlotLib to generate a chart (above in the README) of the performance results. ``save_plot_chart``: This line runs the function to save the chart to file (when running on local machine; disabled on the server.) Could dump this image data in a different format into a database.

- **Results:** Current result, shows Binary Search is the faster model:

        ('Basic', [10, 100, 1000, 10000], [0.0027840137481689453, 0.0027718544006347656, 0.0028028488159179688, 0.0027649402618408203])

        ('Zip', [10, 100, 1000, 10000], [0.0032629966735839844, 0.003304004669189453, 0.0032529830932617188, 0.0032510757446289062])

        ('Random Choices', [10, 100, 1000, 10000], [0.00604701042175293, 0.006039142608642578, 0.005906820297241211, 0.005939960479736328])

        ('Arg Max', [10, 100, 1000, 10000], [0.014555931091308594, 0.014529943466186523, 0.01449441909790039, 0.014703035354614258])

        ('Numpy B Search wv EH', [10, 100, 1000, 10000], [0.010276079177856445, 0.01022195816040039, 0.0103607177734375, 0.010721921920776367])

        ('Numpy Binary Search', [10, 100, 1000, 10000], [0.010213851928710938, 0.010170936584472656, 0.0103302001953125, 0.010263204574584961])

        ('Binary Search', [10, 100, 1000, 10000], [0.002596139907836914, 0.0026030540466308594, 0.0026056766510009766, 0.002586841583251953])

- **Opportunities:** I have gone beyond the remit already, so restrain my desire to create a broader sample. There may be less potential bias if the performance tests were run again for all input sizes, but with several different sets of random numbers and probabilities. 

- ***🏭 Crude Factory:*** *I didn't want to write the same test code over and over, so I hacked together a crude factory method approach to feed the classes into a function, that generates each in turn, running the tests. This could be prettier, but I will stop there, because I have already exceeded the remit.*

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
![junit](https://img.shields.io/badge/Junit5-25A162?style=for-the-badge&logo=junit5&logoColor=white)

**This has not received as much attention as the Python approach.** I have not pursued this far, because that would be beyond remit. Provides a Java implementation of the random number generator service. Computes the cumulative probability and selects a random number based on the probabilities.

### Compile the Java code
I have not pursued this far, because that would be beyond remit, and do not promise that it functions well:
``javac RandomGen.java``

### Run the Java application
I have not pursued this far, because that would be beyond remit, and do not promise that it functions well: ``java RandomGen``

### Unit Tests
The file ``tests-junit.java``

# Typescript
![typescript](https://img.shields.io/badge/TypeScript-007ACC?style=for-the-badge&logo=typescript&logoColor=white)
![javascript](https://img.shields.io/badge/JavaScript-323330?style=for-the-badge&logo=javascript&logoColor=F7DF1E)

**This has not received as much attention as the Python approach.** I have not pursued this far, because that would be beyond remit. Provides a TypeScript implementation of the random number generator service. Computes the cumulative probability and selects a random number based on the probabilities.

### Compile the TypeScript code
``tsc randomGen.ts``

### Run the TypeScript code using Node.js
I have not pursued this far, because that would be beyond remit, and do not promise that it functions well:``ts-node RandomGen.ts``

### Unit Tests
I have not pursued this far, because that would be beyond remit, and do not promise that it functions well:``npm test``

# Flask API
![flask](https://img.shields.io/badge/Flask-000000?style=for-the-badge&logo=flask&logoColor=white)
![json](https://img.shields.io/badge/json-5E5C5C?style=for-the-badge&logo=json&logoColor=white)
![sqlite3](https://img.shields.io/badge/Sqlite-003B57?style=for-the-badge&logo=sqlite&logoColor=white)

PythonAnywhere is free hosting (yay!) but cheap or free isn't always best. It does not support ASGI, so no FastAPI, which would have auto-generate lovely Swagger docs if I declared the structures of the data types.

- **Localhost:** ``python3 app.py``
- **Deploy with uWSGI:** ``uwsgi --http :5000 --module app:app`` (or could use gunicorn)
- **.Env File:** None of this hardcoding passwords into repos security risk nonsense. Details in a ``.env`` file that the ``.gitignore`` file notes is to be ignored.

**Endpoints**

``/run_model``: Runs the most optimal model.

- (POST request)

- Requires to which expects two parameters `random_nums`, and `probabilities`, i.e. to some degree this is dynamic. (Allows for a UI to be employed so that a user may pass through different values.)

- Example reponse:
        
        {"i":99,"num_iterations":100,"nums":{"0":35,"1":52,"2":11,"3":1,"-1":1}}

- **Opportunity:** An improvement would be not to hardcode which model to run, but present a Select element to the user (in the UI) so they determine which class to run (or even an option for the app to determine such according to upon the exec times in the database) - but this Flask API microservice is already beyond the remit.

``/run_performance``: Runs each model.

- (GET request)

- Will save the performance to the Sqlite3 database.

- This is hardcoded, i.e. the names of the models; which relate to Python classes, but this could be dynamic, with error handling where an invalid class name - but this Flask API microservice is already beyond the remit. The actual Performance Test Engine is dynamic. 

- Another improvement would be to save timestamp with each performance run; and this could allow a time-series consideration, except this may be an opportunity demonstrate/explore the logic/functionality rather than necessarily a use case to run a performance test daily.

``/performance_results_avg``: Returns from the Sqlite3 database the average execution time per model, per iteration level, across all past performance runs (these are stored in the database.) 

- (GET request)

- *The taking of an average across multiple performance evalution runs increases the sample size, and thus reduces bias.*

- Example response:

        {"Arg Max":{"10":{"avg":0.11333048343658447,"times":[0.08194303512573242,0.08903098106384277,0.05990767478942871,0.2783229351043701,0.08499717712402344,0.06452178955078125,0.1658320426940918,0.07851338386535645,0.16077756881713867,0.0694582462310791]},"100":{"avg":0.09228651523590088,"times":[0.06506800651550293,0.0677955150604248,0.09227132797241211,0.1995706558227539,0.07744741439819336,0.06029963493347168,0.08309412002563477,0.08857131004333496,0.12388134002685547,0.0648658275604248]},"1000":{"avg":0.09561753273010254,"times":[0.05861020088195801,0.0666964054107666,0.09510135650634766,0.11152291297912598,0.061911582946777344,0.06280970573425293,0.06630921363830566,0.24945497512817383,0.10023379325866699,0.08352518081665039]},"10000":{"avg":0.08213450908660888,"times":[0.06139945983886719,0.060410499572753906,0.05787920951843262,0.15497446060180664,0.06276106834411621,0.07339310646057129,0.0653078556060791,0.09101462364196777,0.10239815711975098,0.09180665016174316]}},"Basic":{"10":{"avg":0.03723549842834473,"times":[0.030828475952148438,0.028399944305419922,0.015941858291625977,0.11081457138061523,0.019611835479736328,0.015602588653564453,0.035280704498291016,0.023244857788085938,0.07680559158325195,0.015824556350708008]},"100":{"avg":0.020389437675476074,"times":[0.015342235565185547,0.03021526336669922,0.025055408477783203,0.030376434326171875,0.01868152618408203,0.014687538146972656,0.02181410789489746,0.015507936477661133,0.0175478458404541,0.014666080474853516]},"1000":{"avg":0.0298095703125,"times":[0.015374183654785156,0.014328241348266602,0.04241371154785156,0.029564619064331055,0.015279293060302734,0.014774560928344727,0.015547037124633789,0.1026158332824707,0.019852876663208008,0.028345346450805664]},"10000":{"avg":0.019308805465698242,"times":[0.014739036560058594,0.014397859573364258,0.015268087387084961,0.02663397789001465,0.014365911483764648,0.014869213104248047,0.01415395736694336,0.01726245880126953,0.038083791732788086,0.02331376075744629]}},"Binary Search":{"10":{"avg":0.021104264259338378,"times":[0.015213489532470703,0.029119491577148438,0.025835037231445312,0.04006814956665039,0.01865863800048828,0.014423370361328125,0.021145105361938477,0.015161514282226562,0.01682591438293457,0.01459193229675293]},"100":{"avg":0.024357295036315917,"times":[0.014279365539550781,0.01447916030883789,0.056333065032958984,0.028710365295410156,0.01540827751159668,0.015196800231933594,0.015625476837158203,0.04892587661743164,0.01996016502380371,0.014654397964477539]},"1000":{"avg":0.020333147048950194,"times":[0.014454126358032227,0.014209747314453125,0.01561284065246582,0.026325702667236328,0.014803171157836914,0.014820575714111328,0.015360116958618164,0.016226530075073242,0.05235862731933594,0.019160032272338867]},"10000":{"avg":0.020894575119018554,"times":[0.016194581985473633,0.014358997344970703,0.014553546905517578,0.038555145263671875,0.014809370040893555,0.017980098724365234,0.014515876770019531,0.03192257881164551,0.024572372436523438,0.021483182907104492]}},"Numpy B Search wv EH":{"10":{"avg":0.09020447731018066,"times":[0.05765795707702637,0.08458113670349121,0.05377078056335449,0.22792267799377441,0.07214975357055664,0.05295681953430176,0.10526847839355469,0.06263995170593262,0.13402295112609863,0.05107426643371582]},"100":{"avg":0.07023792266845703,"times":[0.05017518997192383,0.05054879188537598,0.07650399208068848,0.1457686424255371,0.06768465042114258,0.052614688873291016,0.051641225814819336,0.06267142295837402,0.0935206413269043,0.05124998092651367]},"1000":{"avg":0.07863841056823731,"times":[0.05058455467224121,0.052571773529052734,0.08580732345581055,0.08885359764099121,0.0521087646484375,0.05255746841430664,0.05247950553894043,0.0800771713256836,0.10810470581054688,0.1632392406463623]},"10000":{"avg":0.072220778465271,"times":[0.05191516876220703,0.053276777267456055,0.053941965103149414,0.1542036533355713,0.05155801773071289,0.055753231048583984,0.05259346961975098,0.07256364822387695,0.08952045440673828,0.08688139915466309]}},"Numpy Binary Search":{"10":{"avg":0.08176672458648682,"times":[0.07132673263549805,0.08991837501525879,0.11205816268920898,0.16617965698242188,0.07015323638916016,0.05293536186218262,0.07904553413391113,0.06261730194091797,0.06332850456237793,0.050104379653930664]},"100":{"avg":0.06819784641265869,"times":[0.05258345603942871,0.05634498596191406,0.08789587020874023,0.10889196395874023,0.061128854751586914,0.05195474624633789,0.05283808708190918,0.07553839683532715,0.08244919776916504,0.0523529052734375]},"1000":{"avg":0.06730847358703614,"times":[0.05234527587890625,0.04966855049133301,0.055498600006103516,0.07853841781616211,0.05045485496520996,0.05263519287109375,0.050075531005859375,0.06374931335449219,0.1258389949798584,0.09428000450134277]},"10000":{"avg":0.08190431594848632,"times":[0.05109214782714844,0.051891326904296875,0.0495302677154541,0.2626161575317383,0.056314706802368164,0.06447410583496094,0.05686831474304199,0.057755231857299805,0.08475494384765625,0.08374595642089844]}},"Random Choices":{"10":{"avg":0.05444214344024658,"times":[0.06903266906738281,0.0528106689453125,0.03324103355407715,0.08116483688354492,0.04183363914489746,0.036121368408203125,0.07334566116333008,0.0402679443359375,0.08430337905883789,0.03230023384094238]},"100":{"avg":0.04854292869567871,"times":[0.035799264907836914,0.03565335273742676,0.05557560920715332,0.11174345016479492,0.04278826713562012,0.03244781494140625,0.04845070838928223,0.039144277572631836,0.05063343048095703,0.033193111419677734]},"1000":{"avg":0.05663292407989502,"times":[0.032404184341430664,0.038815975189208984,0.04136228561401367,0.08588671684265137,0.03310990333557129,0.03321051597595215,0.03761005401611328,0.1552290916442871,0.05745291709899902,0.051247596740722656]},"10000":{"avg":0.04255526065826416,"times":[0.03368782997131348,0.032263994216918945,0.03501176834106445,0.06270074844360352,0.03707408905029297,0.03886151313781738,0.032598018646240234,0.04453277587890625,0.060100555419921875,0.0487213134765625]}},"Zip":{"10":{"avg":0.024190711975097656,"times":[0.027120351791381836,0.02601337432861328,0.015843629837036133,0.03824663162231445,0.01944732666015625,0.016076087951660156,0.025489330291748047,0.022948741912841797,0.03469419479370117,0.016027450561523438]},"100":{"avg":0.02208881378173828,"times":[0.01597762107849121,0.024075746536254883,0.024359941482543945,0.04967379570007324,0.018898487091064453,0.014900684356689453,0.022167444229125977,0.01568007469177246,0.020648956298828125,0.014505386352539062]},"1000":{"avg":0.02592325210571289,"times":[0.016355514526367188,0.01971125602722168,0.03070974349975586,0.027549266815185547,0.014943599700927734,0.015175580978393555,0.015987157821655273,0.07527399063110352,0.02014899253845215,0.023377418518066406]},"10000":{"avg":0.018039941787719727,"times":[0.014801740646362305,0.01517629623413086,0.014863967895507812,0.025807619094848633,0.014735221862792969,0.01516270637512207,0.014274835586547852,0.01677870750427246,0.02752232551574707,0.021275997161865234]}}}

``/performance_results_all``: This is similar to ``/performance_results_avg`` but returns from the Sqlite3 database ALL execution times per mode, per iteration level.

- (GET request)

# React UI
![react](https://img.shields.io/badge/React-20232A?style=for-the-badge&logo=react&logoColor=61DAFB)
![babel](https://img.shields.io/badge/Babel-F9DC3E?style=for-the-badge&logo=babel&logoColor=white)
![eslint](https://img.shields.io/badge/eslint-3A33D1?style=for-the-badge&logo=eslint&logoColor=white)
![redux](https://img.shields.io/badge/Redux-593D88?style=for-the-badge&logo=redux&logoColor=white)
![jest](https://img.shields.io/badge/Jest-8A4182?style=for-the-badge&logo=Jest&logoColor=white)
![webpack](https://img.shields.io/badge/Webpack-8DD6F9?style=for-the-badge&logo=Webpack&logoColor=white)
![npm](https://img.shields.io/badge/npm-CB3837?style=for-the-badge&logo=npm&logoColor=white)

Very crude app. I have not pursued this far, because that would be beyond remit. If this were for production, I would add more tests, liniting, and even setup Storybook, etc.. This is outside the remit, and just hacked together to show the chart.

![ui](./assets/ui.png)

**Local Setup**
To run the React UI and the random generator services locally, follow these steps:
1. **Install dependencies:** ``npm install`` (or ``npm i``)
2. **Run the development server** ``npm run build && serve -s build``, and then open http://localhost:3000 in your browser.

**Webpack:** For a production app, this would have environments established, e.g. dev, staging, and prod.

**Opportunities:** Implement [axios](https://axios-http.com/docs/intro) for asynchronous HTTTP requests; and GraphQL. *(Kafka would be unnecessary, but could be nice to demonstrate it; especially if were to deploy this Flask app as multiple functions/lambdas.)* Use styling, .e.g. some Tailwind CSS based components. This could be server-side rendered (Next.js, etc.)

## Deployment 📦📦📦

Tempted to setup Docker, and also to deploy this as an AWS Lambda, but as the Flask API service is outside the remit, I have simply just put it on a free PythonAnywhere account.

**UI URL**

``TBD``

**Flask endpoints**

``https://mathematicuslucian.eu.pythonanywhere.com/run_model``

``https://mathematicuslucian.eu.pythonanywhere.com/run_performance``

``https://mathematicuslucian.eu.pythonanywhere.com/performance_results_avg``

``https://mathematicuslucian.eu.pythonanywhere.com/performance_results_all``