import sys


class SudokuPuzzle:
    '''Representation of a Sudoku puzzle
    '''
    def __init__(self):
        self.name = None
        self.puzzle = None
        self.solution = None

    def print(self):
        '''Print puzzle in a formated grid
        '''
        pass

    def puzzle_to_string(self, puzzle):
        '''Convert a 2D puzzle list to a string
        '''
        resp = ''
        for row in puzzle:
            for cell in row:
                resp = ''.join([resp, cell])
            resp = ''.join([resp, '\n'])
        return resp

    def set_puzzle(self, puzzle_string):
        '''Parse puzzle string and set instances puzzle

            expects string in format:
                """
                Puzzle 3
                000000000 
                009805100 
                051907420 
                290401065 
                000000000 
                140508093 
                026709580 
                005103600 
                000000000  
                """
        '''
        lines = puzzle_string.strip().split('\n')
        if 'Puzzle' in lines[0]:
            self.name = lines[0]
            index = 1
        else:
            index = 0
        self.puzzle = [list(line.strip()) for line in lines[index:]]
        self.solution = self.puzzle

    def end_of_grid(self, row, col):
        '''Returns True if at end of grid
        '''
        return True if row > 8 else False

    def next_position(self, row, col):
        '''Returns position of next open cell
        '''
        while self.solution[row][col] != '0':
            col += 1
            if col > 8:
                row += 1
                col = 0
            if row > 8:
                break
        return row, col

    def grid_is_valid(self, row, col):
        '''Return boolean if puzzle grid is valid
        '''
        valid = True
        temp = self.solution[row][col]
        self.solution[row][col] = 'x'
        # offsets for generating cube
        r_off = row - row % 3
        c_off = col - col % 3
        cube = []
        for i in range(r_off, r_off + 3):
            for j in range(c_off, c_off + 3):
                cube.append(self.solution[i][j])
        # Row check
        if temp in self.solution[row]:
            valid = False
        elif temp in [self.solution[x][col] for x in range(9)]:
            valid = False
        elif temp in cube:
            valid = False
        self.solution[row][col] = temp
        return valid

    def backtrack(self):
        '''Solve puzzle and return solution
        '''
        return puzzle_1_solution

if __name__ == '__main__':
    pass
