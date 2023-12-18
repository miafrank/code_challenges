"""
You are working on a logic game made up of a series of puzzles.
The first type of puzzle you settle on is "sub-Sudoku",
a game where the player has to position the numbers 1..N on an NxN matrix.

Your job is to write a function that, given an NxN matrix,
returns true if  every row and column contains the numbers 1..N

The UI for the game does not do any validation on the numbers the player enters,
so the matrix can contain any signed integer.

Example Input:          Example Output:
grid1 = [
    [2, 3, 1],
    [1, 2, 3],
    [3, 1, 2]
    ]                       -> True

grid2 = [
    [1, 2, 3],
    [3, 2, 1],
    [3, 1, 2]
    ]                       -> False

Solution:
1. Import numpy as np
2. Cast to np.array(nums)
    array([[3, 5, 2, 4],
        [7, 6, 8, 8],
        [1, 6, 7, 7]])
    x2[0, 0] -> 3
    x2[2, -1] -> 7

3. Iterate over grid
    array([0]) -> [2, 3, 1]
    - Get current_index list
    - get_cols -> return np.array([index])
    - get_rows -> iterate over range(len(nums))
        - Check if there are repeating numbers in both col and row
        - Check if cols == rows
    - return sorted(rows) == sorted(columns)
"""
from typing import List
import numpy as np


def contains_no_duplicates(np_col_grid):
    return len(np_col_grid) == len(set(np_col_grid))


def contains_all_positive_numbers(np_grid):
    return all(num >= 1 for num in np_grid)


def contains_all_same_number(np_grid):
    return all(num == num[0] for num in np_grid)


def fetch_cols(current_col_index, grid):
    return list(np.array(grid[current_col_index]))


def fetch_rows(current_col_index, grid):
    np_grid = np.array(grid)
    return [np_grid[np_index, current_col_index] for np_index in range(len(np_grid))]


def validate_sudoku(grid: List[List[int]]):
    if len(grid) <= 1:
        return contains_all_same_number(np.array(grid))

    grid_match = []
    for grid_index in range(len(grid)):
        cols = fetch_cols(grid_index, grid)
        rows = fetch_rows(grid_index, grid)

        contains_dupes_cols = contains_no_duplicates(cols)
        contains_dupes_rows = contains_no_duplicates(rows)
        if contains_dupes_cols is False or contains_dupes_rows is False:
            return False

        contains_all_pos_cols = contains_all_positive_numbers(cols)
        contains_all_pos_rows = contains_all_positive_numbers(rows)
        if not contains_all_pos_cols or not contains_all_pos_rows:
            return False

        grid_match.append(sorted(cols) == sorted(rows))
    return all(grid_match)
