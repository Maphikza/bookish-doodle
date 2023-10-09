import random
from sequence_score import standard_deviation
import os
from pathlib import Path


def generate_numbers() -> tuple:
    num_trials = 10000
    try:
        lower_dev = float(input("What is your preferred lower deviation amount.\n").strip())
        upper_dev = float(input("What is your preferred upper bound deviation amount.\n").strip())
    except ValueError:
        lower_dev = 12
        upper_dev = 16
        print("It seems you have entered invalid numbers, so we are using default values.")
    for _ in range(num_trials):
        numbers = [num for num in range(1, 52 + 1)]
        picked_numbers = []
        for _ in range(6):
            random.shuffle(numbers)
            selected_number = random.choice(numbers)
            picked_numbers.append(selected_number)
            numbers.remove(selected_number)
        with open("results.txt", "a") as file:
            if lower_dev <= standard_deviation(picked_numbers) < upper_dev:
                file.write(f"{picked_numbers}\n")

    with open("results.txt", "r") as results_file:
        results = results_file.readlines()
    new_dev = 0, None
    for pos, result in enumerate(results):
        result_list = (result.replace('[', '')
                       .replace(']', '')
                       .replace(' ', '')
                       .replace('\n', '')
                       .split(','))
        sequence = [int(num) for num in result_list]
        dev = standard_deviation(sequence)
        if dev > new_dev[0]:
            new_dev = dev, sequence
    return new_dev


if __name__ == "__main__":
    generated_numbers = generate_numbers()
    print(generated_numbers)
    if Path("results.txt").exists():
        os.remove("results.txt")
