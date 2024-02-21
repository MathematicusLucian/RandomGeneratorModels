// A binary search algorithm (binarySearch) to find the index corresponding to the random number generated. Relative to a linear approach, this approach reduces the time complexity of finding the next random number to O(log n).

export default class RandomGen {
    private _random_nums: number[];
    private _probabilities: number[];
    private _cumulative_prob: number[];
    private _results: Record<number, number>;

    constructor(random_nums: number[], probabilities: number[]) {
        this._random_nums = random_nums;
        this._probabilities = probabilities;
        this._cumulative_prob = this.calculateCumulativeProbabilities(this._probabilities);
        this._results = {};
        this.validateProbabilities();
    }

    private isClose(a: number, b: number, epsilon: number = 1e-6): boolean {
        return Math.abs(a - b) < epsilon;
    }

    private validateProbabilities(): void {
        const probSum: number = this._cumulative_prob[this._cumulative_prob.length - 1];
        const epsilon: number = 1e-6;

        if (!this.isClose(probSum, 1.0)) {
            throw new Error("Sum of the probabilities must be 1");
        }

        if (this._random_nums.length !== this._probabilities.length) {
            throw new Error("Random_nums and probabilities must be of equal length");
        }

        if (this._probabilities.some(prob => prob < 0)) {
            throw new Error("Cannot process negative probability figures");
        }

        if (!this.isClose(this._probabilities.reduce((a, b) => a + b, 0), 1, epsilon)) {
            throw new Error("Sum of the probabilities must be 1");
        }
    }

    private calculateCumulativeProbabilities(probabilities: number[]): number[] {
        let cumulativeProb: number = 0;
        return probabilities.map(prob => cumulativeProb += prob);
    }

    private binarySearch(target: number): number {
        let left: number = 0;
        let right: number = this._cumulative_prob.length - 1;

        while (left < right) {
            const mid: number = Math.floor((left + right) / 2);
            if (this._cumulative_prob[mid] < target) {
                left = mid + 1;
            } else {
                right = mid;
            }
        }

        return left;
    }

    public nextNum(): Record<number, number> {
        const randNum: number = Math.random();
        const index: number = this.binarySearch(randNum);
        const num: number = this._random_nums[index];
        
        if (num in this._results) {
            this._results[num]++;
        } else {
            this._results[num] = 1;
        }
        
        return this._results;
    }
}

// Example usage
const random_nums: number[] = [-1, 0, 1, 2, 3];
const probabilities: number[] = [0.01, 0.3, 0.58, 0.1, 0.01];
const random_gen: RandomGen = new RandomGen(random_nums, probabilities);
const num_iterations: number = 100;
let results: Record<number, number> = {};
for (let i = 0; i < num_iterations; i++) {
    results = random_gen.nextNum();
}
// Print results
for (const num in results) {
    console.log(`${num}: ${results[num]} times`);
}