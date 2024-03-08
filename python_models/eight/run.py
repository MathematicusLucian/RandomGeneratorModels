from python_models.eight.bisect_right import BisectRight

if __name__ == '__main__':
    # Example usage and test cases
    random_nums = [-1, 0, 1, 2, 3]
    probabilities = [0.01, 0.3, 0.58, 0.1, 0.01]
    random_gen = BisectRight(random_nums, probabilities)
    num_iterations = 100
    results = {}

    for _ in range(num_iterations):
        results = random_gen.next_num()
    # # Print results
    for num, count in results.items():
        print(f"{num}: {count} times") 