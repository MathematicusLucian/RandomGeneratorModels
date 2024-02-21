from one.randomgen import RandomGen

if __name__ == '__main__':
    # Example usage and test cases
    random_gen = RandomGen()
    random_gen._random_nums = [-1, 0, 1, 2, 3]
    random_gen._probabilities = [0.01, 0.3, 0.58, 0.1, 0.01]
    random_gen._results = {}
    num_iterations = 100
    results = {}
    for _ in range(num_iterations):
        results = random_gen.next_num()
        print(1)
    # Print results
    for num, count in results.items():
        print(f"{num}: {count} times")