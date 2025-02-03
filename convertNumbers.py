import sys
import time

def read_numbers_from_file(filename):
    numbers = []
    try:
        with open(filename, 'r') as file:
            for line in file:
                try:
                    numbers.append(int(line.strip()))
                except ValueError:
                    print(f"Invalid data ignored: {line.strip()}")
    except FileNotFoundError:
        print(f"Error: File '{filename}' not found.")
        sys.exit(1)
    return numbers

def int_to_binary(num):
    if num == 0:
        return "0"
    binary = ""
    while num > 0:
        binary = str(num % 2) + binary
        num //= 2
    return binary

def int_to_hexadecimal(num):
    hex_chars = "0123456789ABCDEF"
    if num == 0:
        return "0"
    hexa = ""
    while num > 0:
        hexa = hex_chars[num % 16] + hexa
        num //= 16
    return hexa

def convert_to_binary_and_hex(numbers):
    conversions = [
        (num, int_to_binary(num), int_to_hexadecimal(num))
        for num in numbers
    ]
    return conversions

def save_conversion_results(filename, conversions, elapsed_time):
    with open(filename, 'w') as file:
        for num, binary, hexa in conversions:
            file.write(f"{num} -> Binary: {binary}, Hex: {hexa}\n")
        file.write(f"Elapsed Time: {elapsed_time:.4f} seconds\n")

def main():
    if len(sys.argv) != 2:
        print("Usage: python convertNumbers.py fileWithData.txt")
        sys.exit(1)

    input_file = sys.argv[1]
    numbers = read_numbers_from_file(input_file)

    start_time = time.time()
    conversions = convert_to_binary_and_hex(numbers)
    elapsed_time = time.time() - start_time

    if conversions:
        save_conversion_results("ConvertionResults.txt", conversions, elapsed_time)
        print("Results saved in ConvertionResults.txt")
    else:
        print("No valid numbers found in file.")

if __name__ == "__main__":
    main()
