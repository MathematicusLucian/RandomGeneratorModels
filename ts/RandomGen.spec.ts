import { describe, beforeEach, it, test, expect } from '@jest/globals';
import RandomGen from './RandomGen';

describe('RandomGen', () => {
  let randomGen: RandomGen;

  const totalCalls = obj => Object.values(obj).reduce((a: any, b: any) => a + b, 0);

  beforeEach(() => {
    randomGen = new RandomGen([-1, 0, 1, 2, 3], [0.01, 0.3, 0.58, 0.1, 0.01]);
  });

  it('should initialize random numbers and probabilities correctly', () => {
    expect(randomGen['_random_nums']).toEqual([-1, 0, 1, 2, 3]);
    expect(randomGen['_probabilities']).toEqual([0.01, 0.3, 0.58, 0.1, 0.01]);
  });

  it('should generate valid random numbers once', () => {
    const results = randomGen.nextNum();
    const keys = Object.keys(results).map(Number);
    expect(keys.every(num => [-1, 0, 1, 2, 3].includes(num))).toBeTruthy();
  });

  it('should generate valid random numbers 100 times', () => {
    for (let i = 0; i < 100; i++) {
      const results = randomGen.nextNum();
      const keys = Object.keys(results).map(Number);
      expect(keys.every(num => [-1, 0, 1, 2, 3].includes(num))).toBeTruthy();
    }
  });

  it('should have the correct number of calls after 100 iterations', () => {
    let results;
    for (let i = 0; i < 100; i++) {
      results = randomGen.nextNum();
    }
    const tC = totalCalls(results); 
    expect(tC).toBe(100);
  });

  it('should have probabilities within tolerance after 100 iterations', () => {
    const tolerance = 0.1;
    let results;
    for (let i = 0; i < 100; i++) {
      results = randomGen.nextNum();
    }
    for (const [num, count] of Object.entries(results)) {
      const numIndex = randomGen['_random_nums'].indexOf(Number(num));
      const countValue: number = count as number;
      const distribution = (countValue > 0) ? (countValue / 100) : 0;
      const isWithinTolerance =
        Math.abs(randomGen['_probabilities'][numIndex] - tolerance) <= distribution
        || distribution <= Math.abs(randomGen['_probabilities'][numIndex] + tolerance);
      expect(isWithinTolerance).toBeTruthy();
    }
  });

  it('should have non-zero number of calls after 100 iterations', () => {
    let results;
    for (let i = 0; i < 100; i++) {
      results = randomGen.nextNum();
    }
    const tC = totalCalls(results); 
    expect(tC).not.toBe(0);
  });

  it('should have a total probability not equal to two after one iteration', () => {
    const results = randomGen.nextNum();
    let totalProbability = 0;
    for (const [num, count] of Object.entries(results)) {
      const numIndex = randomGen['_random_nums'].indexOf(Number(num));
      const distribution = count / 1;
      totalProbability += randomGen['_probabilities'][numIndex];
    }
    expect(totalProbability).not.toBeCloseTo(2);
  });
});