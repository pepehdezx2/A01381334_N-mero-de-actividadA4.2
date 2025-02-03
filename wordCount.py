import sys
import time
from collections import defaultdict

def count_word_frequencies(filename):
    word_count = defaultdict(int)
    try:
        with open(filename, 'r') as file:
            for line in file:
                words = line.strip().split()
                for word in words:
                    word_count[word.lower()] += 1
    except FileNotFoundError:
        print(f"Error: File '{filename}' not found.")
        sys.exit(1)
    return word_count

def save_word_count_results(filename, word_count, elapsed_time):
    with open(filename, 'w') as file:
        for word, count in sorted(word_count.items()):
            file.write(f"{word}: {count}\n")
        file.write(f"Elapsed Time: {elapsed_time:.4f} seconds\n")

def main():
    if len(sys.argv) != 2:
        print("Usage: python wordCount.py fileWithData.txt")
        sys.exit(1)

    input_file = sys.argv[1]

    start_time = time.time()
    word_count = count_word_frequencies(input_file)
    elapsed_time = time.time() - start_time

    if word_count:
        for word, count in sorted(word_count.items()):
            print(f"{word}: {count}")
        print(f"Elapsed Time: {elapsed_time:.4f} seconds")
        save_word_count_results("WordCountResults.txt", word_count, elapsed_time)
    else:
        print("No valid words found in the file.")

if __name__ == "__main__":
    main()
