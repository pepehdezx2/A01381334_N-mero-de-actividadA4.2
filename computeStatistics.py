import sys
import time
from collections import defaultdict

def read_numbers_from_file(filename):
    numbers = []
    try:
        with open(filename, 'r') as file:
            for line in file:
                try:
                    numbers.append(float(line.strip()))
                except ValueError:
                    print(f"Invalid data ignored: {line.strip()}")
    except FileNotFoundError:
        print(f"Error: File '{filename}' not found.")
        sys.exit(1)
    return numbers

def compute_statistics(numbers):
    n = len(numbers)
    if n == 0:
        return None

    mean = sum(numbers) / n
    sorted_nums = sorted(numbers)
    median = (
        sorted_nums[n // 2]
        if n % 2 == 1
        else (sorted_nums[n // 2 - 1] + sorted_nums[n // 2]) / 2
    )
    mode_counts = defaultdict(int)
    for num in numbers:
        mode_counts[num] += 1
    mode = max(mode_counts, key=mode_counts.get)
    variance = sum((x - mean) ** 2 for x in numbers) / n
    std_dev = variance ** 0.5

    return mean, median, mode, variance, std_dev

def save_results(filename, results, elapsed_time):
    with open(filename, 'w') as file:
        file.write(f"Mean: {results[0]:.2f}\n")
        file.write(f"Median: {results[1]:.2f}\n")
        file.write(f"Mode: {results[2]:.2f}\n")
        file.write(f"Variance: {results[3]:.2f}\n")
        file.write(f"Standard Deviation: {results[4]:.2f}\n")
        file.write(f"Elapsed Time: {elapsed_time:.4f} seconds\n")

def main():
    if len(sys.argv) != 2:
        print("Usage: python computeStatistics.py <fileWithData.txt>")
        sys.exit(1)

    filename = sys.argv[1]
    start_time = time.time()
    numbers = read_numbers_from_file(filename)
    results = compute_statistics(numbers)
    elapsed_time = time.time() - start_time

    if results:
        print(f"Mean: {results[0]:.2f}")
        print(f"Median: {results[1]:.2f}")
        print(f"Mode: {results[2]:.2f}")
        print(f"Variance: {results[3]:.2f}")
        print(f"Standard Deviation: {results[4]:.2f}")
        print(f"Elapsed Time: {elapsed_time:.4f} seconds")
        save_results('StatisticsResults.txt', results, elapsed_time)
    else:
        print("No valid numbers found in the file.")

if __name__ == "__main__":
    main()
