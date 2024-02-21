import React from 'react';
import { render } from 'react-dom';
import App from './App'

const defaultRandomNums = [-1, 0, 1, 2, 3];
const defaultProbabilities = [0.01, 0.3, 0.58, 0.1, 0.01]

render(<App randomNums={defaultRandomNums} probabilities={defaultProbabilities} />, document.getElementById('root'));