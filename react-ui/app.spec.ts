import React from 'react';
import { describe, test, expect } from '@types/jest';
import { render, fireEvent, waitFor } from '@testing-library/react';
import App from './src/App';

describe('App component', () => {
  test('renders correctly', () => {
    const { getByText, getByLabelText } = render(<App>);
    expect(getByText('Number Generation Models')).toBeInTheDocument();
    expect(getByLabelText('Random Numbers:')).toBeInTheDocument();
    expect(getByLabelText('Probabilities:')).toBeInTheDocument();
    expect(getByText('Run the most optimal model')).toBeInTheDocument();
    expect(getByText('Random Results (most efficient model)')).toBeInTheDocument();
    expect(getByText('Average performance runs, all models')).toBeInTheDocument();
  });

  test('input fields are editable', () => {
    const defaultRandomNums = [-1, 0, 1, 2, 3];
    const defaultProbabilities = [0.01, 0.3, 0.58, 0.1, 0.01];
    const { getByLabelText } = render(<App randomNums={defaultRandomNums} probabilities={defaultProbabilities} />);
    const randomNumsInput = getByLabelText('Random Numbers:');
    const probabilitiesInput = getByLabelText('Probabilities:');
    fireEvent.change(randomNumsInput, { target: { value: '1 2 3' } });
    fireEvent.change(probabilitiesInput, { target: { value: '0.1 0.2 0.3' } });
    expect(randomNumsInput).toBe('1 2 3');
    expect(probabilitiesInput).toBe('0.1 0.2 0.3');
  });

  test('handles click event correctly', async () => {
    // Mocking the fetch function to return a response with the expected schema
    global.fetch = jest.fn().mockResolvedValue({
      json: () =>
        Promise.resolve({
          "Arg Max": 0.081,
          "Basic": 0.018,
          "Binary Search": 0.020,
          "Numpy B Search wv EH": 0.070,
          "Numpy Binary Search": 0.081,
          "Random Choices": 0.041,
          "Zip": 0.017
        })
    });

    const defaultRandomNums = [-1, 0, 1, 2, 3];
    const defaultProbabilities = [0.01, 0.3, 0.58, 0.1, 0.01];
    const { getByText, getByLabelText, getByTestId } = render(<App randomNums={defaultRandomNums} probabilities={defaultProbabilities} />);
    const button = getByTestId('btn_run_model');
    fireEvent.click(button);

    // Wait for the component to update with the response
    await waitFor(() => {
      expect(getByText('Arg Max:')).toBeInTheDocument();
      expect(getByText('Basic:')).toBeInTheDocument();
      expect(getByText('Binary Search:')).toBeInTheDocument();
      expect(getByText('Numpy B Search wv EH:')).toBeInTheDocument();
      expect(getByText('Numpy Binary Search:')).toBeInTheDocument();
      expect(getByText('Random Choices:')).toBeInTheDocument();
      expect(getByText('Zip:')).toBeInTheDocument();
    });
  });
});
