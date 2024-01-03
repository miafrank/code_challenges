from typing import List

# Find the first duplicate number for which the second occurrence has the minimal index
# In other words, if there are more than 1 duplicated numbers,
# return the number for which the second occurrence has a smaller
# index than the second occurrence of the other number does.
# If there are no such elements, return -1.

# Assumptions:
# There are either 0 or pair of duplicates
# If there are doubles, each number will appear exactly twice

# Solution:
# Create dictionary where key: number value: [index]
# Example {2: [0, 5], 3: [2, 4]}

# Iterate through dictionary
# Filter out keys where value == 1
# If no doubles dict == {} -> return -1
# Find smallest index of second occurence
# Return key


def check_valid_doubles(doubles):
    return -1 if len(doubles) == 0 else doubles


def filter_non_doubles(doubles):
    return {k: v for k, v in doubles.items() if len(v) > 1}


def find_smallest_index(fitlered_doubles):
    fitlered_doubles_keys = list(fitlered_doubles.keys())
    if len(fitlered_doubles_keys) == 1:
        return fitlered_doubles_keys[0]

    fitlered_doubles_number_one = fitlered_doubles[fitlered_doubles_keys[0]]
    fitlered_doubles_number_two = fitlered_doubles[fitlered_doubles_keys[1]]

    if fitlered_doubles_number_one[1] > fitlered_doubles_number_two[1]:
        return fitlered_doubles_keys[1]
    return fitlered_doubles_keys[0]


def first_double(numbers: List[int]):
    not_found = -1
    doubles = {}
    for index in range(len(numbers)):
        if numbers[index] in doubles:
            doubles[numbers[index]].append(index)
        else:
            doubles[numbers[index]] = [index]

    filtered_doubles = filter_non_doubles(doubles)
    valid_doubles = check_valid_doubles(filtered_doubles)

    if valid_doubles == not_found:
        return not_found

    return find_smallest_index(filtered_doubles)
