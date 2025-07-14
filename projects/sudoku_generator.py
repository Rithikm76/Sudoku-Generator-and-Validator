# Sudoku Prototype
import random
import math

# Get board size from user
def get_board_size():
    while True:
        try:
            n = int(input("Enter the box size (e.g., 3 for 9x9, 4 for 16x16): "))
            if n >= 2:
                return n
            else:
                print("Please enter a number >= 2")
        except ValueError:
            print("Please enter a valid number")

# Get the board size
n = get_board_size()
board_size = n * n

# Create an empty n²×n×n Sudoku board (maintaining 3D structure)
sudoku = [[[0 for _ in range(n)] for _ in range(n)] for _ in range(board_size)]

# Print the board in a readable format
def print_board(sudoku):
    for row in range(board_size):
        for group in range(n):
            print(" ".join(str(num) if num != 0 else '.' for num in sudoku[row][group]), end=' ')
        print()
    print()

# Check if num is in the given row
def is_in_row(sudoku, row, num):
    for group in sudoku[row]:
        if num in group:
            return True
    return False

# Check if num is in the given column (using group and index)
def is_in_col(sudoku, group, index, num):
    for row in range(board_size):
        if sudoku[row][group][index] == num:
            return True
    return False

# Check if num is in the same n×n box (based on row and group)
def is_in_box(sudoku, row, group, num):
    # Calculate which n×n box this cell belongs to
    box_row = row // n
    box_group = group
    
    # Calculate the range of rows for this box
    start_row = box_row * n
    end_row = start_row + n
    
    for r in range(start_row, end_row):
        for val in sudoku[r][box_group]:
            if val == num:
                return True
    return False

# Check if placing num at sudoku[row][group][index] is valid
def is_valid(sudoku, row, group, index, num):
    if is_in_row(sudoku, row, num):
        return False
    if is_in_col(sudoku, group, index, num):
        return False
    if is_in_box(sudoku, row, group, num):
        return False
    return True

# Place a value at sudoku[row][group][index]
def set_value(sudoku, row, group, index, num):
    sudoku[row][group][index] = num

# Backtracking algorithm to fill the board
def fill_board(sudoku):
    for row in range(board_size):
        for group in range(n):
            for index in range(n):
                if sudoku[row][group][index] == 0:
                    nums = list(range(1, board_size + 1))
                    random.shuffle(nums)
                    for num in nums:
                        if is_valid(sudoku, row, group, index, num):
                            set_value(sudoku, row, group, index, num)
                            if fill_board(sudoku):
                                return True
                            sudoku[row][group][index] = 0
                    return False  # Backtrack
    return True  # Board is completely filled

# Run the Sudoku generator
if __name__ == "__main__":
    fill_board(sudoku)
    print("Solved Sudoku Board:")
    print_board(sudoku) 