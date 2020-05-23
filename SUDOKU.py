import numpy as np

a = input()
ar = list(map(int, a))
arr = np.array(ar).reshape(9, 9)


def print_sudoku():
    for i in range(9):
        print(arr[i])


def number_unassigned(row, col):
    global arr
    num_unassign = 0
    for i in range(9):
        for j in range(9):
            if arr[i][j] == 0:
                row = i
                col = j
                num_unassign = 1
                a = [row, col, num_unassign]
                return a
    a = [-1, -1, num_unassign]
    return a


def is_safe(n, r, c):
    for i in range(9):
        if arr[r][i] == n:
            return False
    for i in range(9):
        if arr[i][c] == n:
            return False
    row_start = (r // 3) * 3
    col_start = (c // 3) * 3
    for i in range(row_start, row_start + 3):
        for j in range(col_start, col_start + 3):
            if arr[i][j] == n:
                return False
    return True


def solve_sudoku():
    row = 0
    col = 0

    a = number_unassigned(row, col)
    if a[2] == 0:
        return True
    row = a[0]
    col = a[1]
    for i in range(1, 10):
        if is_safe(i, row, col):
            arr[row][col] = i

            if solve_sudoku():
                return True

            arr[row][col] = 0
    return False


if solve_sudoku():
    print_sudoku()
else:
    print("NO SOLUTION")
