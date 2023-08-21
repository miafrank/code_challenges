from validate_sudoku import validate_sudoku

grid1 = [
    [2, 3, 1],
    [1, 2, 3],
    [3, 1, 2]
]

grid2 = [
    [1, 2, 3],
    [3, 2, 1],
    [3, 1, 2],
]

grid3 = [
    [2, 2, 3],
    [3, 1, 2],
    [2, 3, 1]
]

grid4 = [
    [1],
]

grid5 = [
    [-1, -2, -3],
    [-2, -3, -1],
    [-3, -1, -2],
]

grid6 = [
    [1, 3, 3],
    [3, 1, 2],
    [2, 3, 1],
]

grid7 = [
    [1, 2, 3, 4],
    [4, 3, 2, 1],
    [1, 3, 2, 4],
    [4, 2, 3, 1],
]

grid8 = [
    [0, 3],
    [3, 0],
]

grid9 = [
    [0, 1],
    [1, 0],
]

grid10 = [
    [0, 2],
    [2, 0],
]

grid11 = [
    [1, 2, 3, 4],
    [2, 3, 1, 4],
    [3, 1, 2, 4],
    [4, 2, 3, 1],
]

grid12 = [
    [-1, -2, 12, 1],
    [12, -1, 1, -2],
    [-2, 1, -1, 12],
    [1, 12, -2, -1],
]

grid13 = [
    [2, 3, 3],
    [1, 2, 1],
    [3, 1, 2],
]


def test_validate_sudoku():
    assert validate_sudoku(grid1) is True
    assert validate_sudoku(grid2) is False
    assert validate_sudoku(grid3) is False
    assert validate_sudoku(grid4) is True
    assert validate_sudoku(grid5) is False
    assert validate_sudoku(grid6) is False
    assert validate_sudoku(grid7) is False
    assert validate_sudoku(grid8) is False
    assert validate_sudoku(grid9) is False
    assert validate_sudoku(grid10) is False
    assert validate_sudoku(grid11) is False
    assert validate_sudoku(grid12) is False
    assert validate_sudoku(grid13) is False
