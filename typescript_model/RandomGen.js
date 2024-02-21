"use strict";
// A binary search algorithm (binarySearch) to find the index corresponding to the random number generated. Relative to a linear approach, this approach reduces the time complexity of finding the next random number to O(log n).
Object.defineProperty(exports, "__esModule", { value: true });
var RandomGen = /** @class */ (function () {
    function RandomGen(random_nums, probabilities) {
        this._random_nums = random_nums;
        this._probabilities = probabilities;
        this._cumulative_prob = this.calculateCumulativeProbabilities(this._probabilities);
        this._results = {};
        this.validateProbabilities();
    }
    RandomGen.prototype.isClose = function (a, b, epsilon) {
        if (epsilon === void 0) { epsilon = 1e-6; }
        return Math.abs(a - b) < epsilon;
    };
    RandomGen.prototype.validateProbabilities = function () {
        var probSum = this._cumulative_prob[this._cumulative_prob.length - 1];
        var epsilon = 1e-6;
        if (!this.isClose(probSum, 1.0)) {
            throw new Error("Sum of the probabilities must be 1");
        }
        if (this._random_nums.length !== this._probabilities.length) {
            throw new Error("Random_nums and probabilities must be of equal length");
        }
        if (this._probabilities.some(function (prob) { return prob < 0; })) {
            throw new Error("Cannot process negative probability figures");
        }
        if (!this.isClose(this._probabilities.reduce(function (a, b) { return a + b; }, 0), 1, epsilon)) {
            throw new Error("Sum of the probabilities must be 1");
        }
    };
    RandomGen.prototype.calculateCumulativeProbabilities = function (probabilities) {
        var cumulativeProb = 0;
        return probabilities.map(function (prob) { return cumulativeProb += prob; });
    };
    RandomGen.prototype.binarySearch = function (target) {
        var left = 0;
        var right = this._cumulative_prob.length - 1;
        while (left < right) {
            var mid = Math.floor((left + right) / 2);
            if (this._cumulative_prob[mid] < target) {
                left = mid + 1;
            }
            else {
                right = mid;
            }
        }
        return left;
    };
    RandomGen.prototype.nextNum = function () {
        var randNum = Math.random();
        var index = this.binarySearch(randNum);
        var num = this._random_nums[index];
        if (num in this._results) {
            this._results[num]++;
        }
        else {
            this._results[num] = 1;
        }
        return this._results;
    };
    return RandomGen;
}());
exports.default = RandomGen;
// Example usage
var random_nums = [-1, 0, 1, 2, 3];
var probabilities = [0.01, 0.3, 0.58, 0.1, 0.01];
var random_gen = new RandomGen(random_nums, probabilities);
var num_iterations = 100;
var results = {};
for (var i = 0; i < num_iterations; i++) {
    results = random_gen.nextNum();
}
// Print results
for (var num in results) {
    console.log("".concat(num, ": ").concat(results[num], " times"));
}
