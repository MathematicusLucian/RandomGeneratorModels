import React, { useState, useEffect } from 'react';

const App = (props) => {
  const [randomNums, setRandomNums] = useState(props.randomNums);
  const [probabilities, setProbabilities] = useState(props.probabilities);
  const [response, setResponse] = useState("Please run the model . . .");
  const [results, setResults] = useState("Loading . . .");
  const url = 'https://mathematicuslucian.eu.pythonanywhere.com';
  const result_avg_path = '/performance_results_avg';
  const run_model_path = '/run_model';

  useEffect(() => {
    // To fetch average performance runs data on load. GET request 
    fetch(url+result_avg_path)
      .then((response) => response.json())
      .then((data) => {
        console.log('data', data);
        setResults(JSON.stringify(data));
      })
      .catch((error) => console.error('Error while making the HTTP request to fetch average performance results:', error));
  }, []);

  const handleRandomNumsChange = (e) => {
    setRandomNums(e.target.value);
  };

  const handleProbabilitiesChange = (e) => {
    setProbabilities(e.target.value);
  };

  const handleClick = async () => {
    // To run most optimal model and fetch performance run times. POST request 
    try {
      console.log(randomNums);
      console.log(probabilities);
      console.log(probabilities.map(Number));
      const data = { randomNums: randomNums, probabilities: probabilities.map(Number) };
      const response = await fetch(url+run_model_path, {
        method: 'POST',
        headers: {
          'Content-Type': 'application/json',
        },
        body: JSON.stringify(data),
      });
      const result = await response.text();
      setResponse(result);
    } catch (error) {
      console.error('Error occurred while making the HTTP request to run most optimal model:', error);
    }
  };

  return (
    <div>
      <h1>Number Generation Models</h1>
      <label htmlFor="randomNums">Random Numbers:</label>
      <input type="text" id="randomNums" value={randomNums} onChange={handleRandomNumsChange} />
      <br />
      <label htmlFor="probabilities">Probabilities:</label>
      <input type="text" id="probabilities" value={probabilities} onChange={handleProbabilitiesChange} />
      <br />
      <button id="btn_run_model" onClick={handleClick}>Run the most optimal model</button>
      <br />
      <h2>Random Results (most efficient model)</h2>
      <div>{response}</div>
      <hr />
      {/* graph */}
      <h2>Average performance runs, all models</h2>
      <div>{results}</div>
    </div>
  );
};

export default App;