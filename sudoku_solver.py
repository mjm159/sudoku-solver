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
        '''
        self.puzzle = [['0', '4', '0', '0', '0', '0', '0', '5', '0'], ['0', '0', '1', '9', '4', '3', '6', '0', '0'], ['0', '0', '9', '0', '0', '0', '3', '0', '0'], ['6', '0', '0', '0', '5', '0', '0', '0', '2'], ['1', '0', '3', '0', '0', '0', '5', '0', '6'], ['8', '0', '0', '0', '2', '0', '0', '0', '7'], ['0', '0', '5', '0', '0', '0', '2', '0', '0'], ['0', '0', '2', '4', '3', '6', '7', '0', '0'], ['0', '3', '0', '0', '0', '0', '0', '4', '0']]

    def backtrack(self):
        '''Solve puzzle and print solution
        '''
        pass

if __name__ == '__main__':
    pass
