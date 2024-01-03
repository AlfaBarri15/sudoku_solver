from random import sample


class SudokuBuilder:
    base = 3
    side = base * base
    full_board = None
    board = None

    def __init__(self):
        r_base = range(self.base)
        rows = [g * self.base + r for g in self.shuffle(r_base) for r in self.shuffle(r_base)]
        cols = [g * self.base + c for g in self.shuffle(r_base) for c in self.shuffle(r_base)]
        nums = self.shuffle(range(1, self.base * self.base + 1))

        # produce board using randomized baseline pattern
        self.board = [[nums[self.pattern(r, c)] for c in cols] for r in rows]
        for line in self.board:
            print(line)
        print()

        squares = self.side * self.side
        empties = squares * 3 // 4
        for p in sample(range(squares), empties):
            self.board[p // self.side][p % self.side] = 0

    def pattern(self, r, c):
        return (self.base * (r % self.base) + r//self.base + c) % self.side

    def shuffle(self, s):
        return sample(s, len(s))