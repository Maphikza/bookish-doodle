def standard_deviation(sequence: list) -> float:
    # Calculate the mean of the sequence
    mean = sum(sequence) / len(sequence)

    # Calculate the variance (mean of squared differences from the mean)
    variance = sum((num - mean) ** 2 for num in sequence) / len(sequence)

    # Calculate the standard deviation (square root of variance)
    standard_deviation_score = variance ** 0.5

    return standard_deviation_score


def common_numbers(list1, list2):
    # Convert lists to sets
    set1 = set(list1)
    set2 = set(list2)

    # Find common numbers using set intersection
    common = set1.intersection(set2)

    return len(common), common
