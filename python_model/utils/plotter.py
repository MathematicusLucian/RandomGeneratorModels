def add_data_to_plotter(plt, input_sizes, generator_times, generator_name):
    plt.plot(input_sizes, generator_times, marker='o', label=generator_name)

def generate_chart(plt):
    plt.xlabel('Input Size (Number of Random Numbers)')
    plt.ylabel('Execution Time (Seconds)')
    plt.title('Performance Test: Time Complexity Comparison')
    plt.grid(True)
    plt.legend()
    plt.savefig('./generator_perf_test_results.png')