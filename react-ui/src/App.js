import React, { useState, useEffect } from 'react';
import axios from 'axios';
import "./app.css";
import TimeSeriesChart from './TimeSeriesChart';
import Table from './Table';

const App = (props) => {
  const [randomNums, setRandomNums] = useState(props.randomNums);
  const [probabilities, setProbabilities] = useState(props.probabilities);
  const [modelRunOutcome, setModelRunOutcome] = useState("Please run the model . . .");
  const [avgPerformanceOutcome, setAvgPerformanceOutcome] = useState("Loading . . .");
  const url = 'https://mathematicuslucian.eu.pythonanywhere.com';
  const result_avg_path = '/performance_results_avg';
  const run_model_path = '/run_model';

  const fetchData = async (API_URL, PARAMS=null) => {
    const request = (!PARAMS) 
      ? await axios.get(`${API_URL}`, {
        'Host': 'mathematicuslucian.eu.pythonanywhere.com',
        'Content-Type': 'application/json'
      })
      : await axios.post(`${API_URL}`, PARAMS, {
        'Host': 'mathematicuslucian.eu.pythonanywhere.com',
        'Content-Type': 'application/json',
        'Content-Length': '79'
      });
    const result = await request.data;
    return result;
  };

  useEffect(async () => {
    // To fetch average performance runs data on load. GET request 
    const API_URL = url+result_avg_path;
    await fetchData(API_URL).then((modelOutcomeData) => {
      setAvgPerformanceOutcome(JSON.stringify(modelOutcomeData));
    }).catch((error) => console.error('Error while making the HTTP request to fetch average performance results:', error));
  }, []);

  const handleRandomNumsChange = (e) => {
    setRandomNums(e.target.value);
  };

  const handleProbabilitiesChange = (e) => {
    setProbabilities(e.target.value);
  };

  const handleClick = async () => {
    event.preventDefault();
    // To run most optimal model and fetch performance run times. POST request 
    const API_URL = url+run_model_path;
    const PARAMS = { "randomNums": randomNums, "probabilities": probabilities.map(Number) };
    await fetchData(API_URL, PARAMS).then((modelOutcomeData) => {
      setModelRunOutcome(JSON.stringify(modelOutcomeData));
    }).catch(error => {
      console.error('Error occurred while making the HTTP request to run most optimal model:', error);
    });
  };

  return (
    <div>
      <h1>🌟Number Generation Models🌟 🚀 </h1>
      <div id="form">
        <div class="formElement">
          <label htmlFor="randomNums">Random Numbers:</label>
          <input type="text" id="randomNums" value={randomNums} onChange={handleRandomNumsChange} />
        </div>
        <div class="formElement">
          <label htmlFor="probabilities">Probabilities:</label>
          <input type="text" id="probabilities" value={probabilities} onChange={handleProbabilitiesChange} />
        </div>
      </div>
      <div class="formElement">
        <button id="btn_run_model" onClick={handleClick}>Results of the Most Optimal Model:</button>
      </div>
      <div id="modelRunOutcome">
        <h2>Random Results (most efficient model)</h2>
        { <div>{modelRunOutcome}</div> }
      </div>
      <hr />
      <div id="averageRuns">
          <h2>Average performance runs, all models</h2>
          <div style={{height:600}}>
          <> 
            <TimeSeriesChart data={avgPerformanceOutcome} />
          </>
          </div>
          <> 
            <Table data={avgPerformanceOutcome} />
          </>
      </div>
    </div>
  );
};

export default App;