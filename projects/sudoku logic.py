# sudoku_generator.py
import random

class Sudoku3D:
    def __init__(self, block_size=3):
        self.block_size = block_size
        self.grid_size = block_size * block_size
        self.board = self._create_board()
        self.backtrack_count = 0
        self.box_row_ranges = [range(i, i + block_size) for i in range(0, self.grid_size, block_size)]

    def _create_board(self):
        return [[[0 for _ in range(self.block_size)] for _ in range(self.block_size)] for _ in range(self.grid_size)]

    def print_board(self):
        for row in range(self.grid_size):
            row_output = []
            for group in range(self.block_size):
                row_output.append(" ".join(str(num) if num != 0 else ' ' for num in self.board[row][group]))
            print(" ".join(row_output))
        print()

    def is_in_row(self, row, num):
        return any(num in group for group in self.board[row])

    def is_in_col(self, group, index, num):
        return any(self.board[row][group][index] == num for row in range(self.grid_size))

    def is_in_box(self, row, group, num):
        for row_range in self.box_row_ranges:
            if row in row_range:
                for r in row_range:
                    for val in self.board[r][group]:
                        if val == num:
                            return True
                break
        return False

    def is_valid(self, row, group, index, num):
        return not (
            self.is_in_row(row, num) or
            self.is_in_col(group, index, num) or
            self.is_in_box(row, group, num)
        )

    def set_value(self, row, group, index, num):
        self.board[row][group][index] = num

    def fill_board(self):
        for row in range(self.grid_size):
            for group in range(self.block_size):
                for index in range(self.block_size):
                    if self.board[row][group][index] == 0:
                        nums = list(range(1, self.grid_size + 1))
                        random.shuffle(nums)
                        for num in nums:
                            if self.is_valid(row, group, index, num):
                                self.set_value(row, group, index, num)
                                if self.fill_board():
                                    return True
                                self.board[row][group][index] = 0
                                self.backtrack_count += 1
                        return False
        return True

    def is_solved_correctly(self):
        expected = list(range(1, self.grid_size + 1))

        # Check each row
        for row in range(self.grid_size):
            row_values = [num for group in self.board[row] for num in group]
            if sorted(row_values) != expected:
                return False

        # Check each column
        for group in range(self.block_size):
            for index in range(self.block_size):
                col_values = [self.board[row][group][index] for row in range(self.grid_size)]
                if sorted(col_values) != expected:
                    return False

        # Check each box (box = all values in a column group and a row range)
        for group in range(self.block_size):
            for row_range in self.box_row_ranges:
                box_values = [self.board[r][group][i] for r in row_range for i in range(self.block_size)]
                if sorted(box_values) != expected:
                    return False

        return True

    def generate_puzzle(self, clues=30):
        assert 17 <= clues <= self.grid_size * self.grid_size, "Clues must be between 17 and total number of cells"
        self.fill_board()
        total_cells = self.grid_size * self.grid_size
        cells_to_remove = total_cells - clues

        # Convert 3D board to flat index map and remove random values
        indices = [(r, g, i) for r in range(self.grid_size) for g in range(self.block_size) for i in range(self.block_size)]
        random.shuffle(indices)

        for _ in range(cells_to_remove):
            row, group, index = indices.pop()
            self.board[row][group][index] = 0

if __name__ == "__main__":
    try:
        user_block_size = int(input("Enter block size (e.g., 3 for 9x9, 4 for 16x16): "))
        if user_block_size < 2 or user_block_size > 5:
            raise ValueError("Block size should be between 2 and 5 for practical generation.")

        grid_size = user_block_size ** 2
        total_cells = grid_size * grid_size

        print("Choose difficulty: [1] Easy  [2] Medium  [3] Hard")
        difficulty = input("Enter difficulty level (1-3): ")

        if difficulty == '1':
            clues = int(total_cells * 0.45)  # Easy: ~45% clues
        elif difficulty == '2':
            clues = int(total_cells * 0.35)  # Medium: ~35% clues
        elif difficulty == '3':
            clues = int(total_cells * 0.25)  # Hard: ~25% clues
        else:
            raise ValueError("Invalid difficulty level. Enter 1, 2, or 3.")

        game = Sudoku3D(block_size=user_block_size)
        game.generate_puzzle(clues=clues)
        game.print_board()
        print(f"Board Size: {grid_size}x{grid_size} - Difficulty: {['Easy','Medium','Hard'][int(difficulty)-1]}")
    except Exception as e:
        print(f"Error: {e}")
