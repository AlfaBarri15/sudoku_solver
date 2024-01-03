class SudokuSolver:
    grid = None
    side = None
    locked_positions = []

    def __init__(self, side, grid):
        self.side = side
        self.grid = grid

        # saving the positions of filled boxes
        for i in range(self.side):
            for j in range(self.side):
                if self.grid[i][j] != 0:
                    self.locked_positions.append([i, j])

        # printing the grid to solve
        num_size = len(str(side))
        for line in self.grid:
            print(*(f"{n or '.':{num_size}} " for n in line))
        print()

    def print_grid(self):
        num_size = len(str(self.side))
        for line in self.grid:
            print(*(f"{n or '.':{num_size}} " for n in line))
        print()

    def solve_brute_force(self):
        i = 0
        while i < self.side:
            j = 0
            while j < self.side:
                if not ([i, j] in self.locked_positions):

                    # Verify if the number to be entered is valid
                    if (self.verify_line(self.grid[i][j] + 1, i)
                            and self.verify_column(self.grid[i][j] + 1, j)
                            and self.verify_subgrid(self.grid[i][j] + 1, i, j)):

                        self.grid[i][j] = self.grid[i][j] + 1

                        # Verify that the value of a box is less than 10
                        if self.grid[i][j] > 9:
                            self.grid[i][j] = 0
                            if j > 0:
                                j = j - 2

                            elif j == 0:
                                i = i - 1
                                j = 7

                            while [i,j + 1] in self.locked_positions:
                                j = j - 1
                                if j == 0:
                                    i = i-1
                                    j = 8

                    else:
                        if j > 0:
                            self.grid[i][j] = self.grid[i][j] + 1
                            j = j - 1
                        elif j == 0:
                            self.grid[i][j] = self.grid[i][j] + 1
                            i = i - 1
                            j = 8

                j = j + 1
            i = i + 1

    def verify_line(self, number_to_input, line_index):
        line = self.grid[line_index]
        if number_to_input in line:
            return False
        else:
            return True

    def verify_column(self, number_to_input, column_index):
        column = [row[column_index] for row in self.grid]
        if number_to_input in column:
            return False
        else:
            return True

    def verify_subgrid(self, number_to_input, row_index, column_index):
        if row_index < 3 and column_index < 3:
            return self.loop_subgrid(number_to_input, self.give_range_to_loop_on(1))
        elif row_index < 3 and column_index < 6:
            return self.loop_subgrid(number_to_input, self.give_range_to_loop_on(2))
        elif row_index < 3 and column_index < 9:
            return self.loop_subgrid(number_to_input, self.give_range_to_loop_on(3))
        elif row_index < 6 and column_index < 3:
            return self.loop_subgrid(number_to_input, self.give_range_to_loop_on(4))
        elif row_index < 6 and column_index < 6:
            return self.loop_subgrid(number_to_input, self.give_range_to_loop_on(5))
        elif row_index < 6 and column_index < 9:
            return self.loop_subgrid(number_to_input, self.give_range_to_loop_on(6))
        elif row_index < 9 and column_index < 3:
            return self.loop_subgrid(number_to_input, self.give_range_to_loop_on(7))
        elif row_index < 9 and column_index < 6:
            return self.loop_subgrid(number_to_input, self.give_range_to_loop_on(8))
        elif row_index < 9 and column_index < 9:
            return self.loop_subgrid(number_to_input, self.give_range_to_loop_on(9))
        else:
            raise Exception(f"The given index ({row_index}, {column_index}) is does not fit in any of the subgrids.")


    def loop_subgrid(self, number_to_input, range):
        for i in range[0]:
            for j in range[1]:
                if number_to_input == self.grid[i][j]:
                    return False
        return True

    def give_range_to_loop_on(self, subgrid):
        # it goes from left to right and then top to bottom (1 to 9)
        if subgrid == 1:
            return [range(0, 3), range(0, 3)]
        elif subgrid == 2:
            return [range(0, 3), range(3, 6)]
        elif subgrid == 3:
            return [range(0, 3), range(6, 9)]
        elif subgrid == 4:
            return [range(3, 6), range(0, 3)]
        elif subgrid == 5:
            return [range(3, 6), range(3, 6)]
        elif subgrid == 6:
            return [range(3, 6), range(6, 9)]
        elif subgrid == 7:
            return [range(6, 9), range(0, 3)]
        elif subgrid == 8:
            return [range(6, 9), range(3, 6)]
        elif subgrid == 9:
            return [range(6, 9), range(6, 9)]
        else:
            raise Exception("Not a valid subgrid.")
