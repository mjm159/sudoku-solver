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

    def set_puzzle(self, puzzle_string):
        '''Parse puzzle string and set instances puzzle

        expects string in format:
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
        '''
        lines = puzzle_string.strip().split('\n')
        self.name = lines[0]
        self.puzzle = [list(line.strip()) for line in lines[1:]]


    def backtrack(self):
        '''Solve puzzle and print solution
        '''
        pass

if __name__ == '__main__':
    pass
