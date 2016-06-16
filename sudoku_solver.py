#!/usr/bin/python3
'''
sudoku_solver.py

Solves sudoku puzzles.

Author: Michael Malocha
Last Revised: June 15th, 2016
'''

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
        self.solution = list(self.puzzle)

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

    def grid_is_valid(self):
        '''Return boolean if puzzle is valid
        '''
        for i, row in enumerate(self.solution):
            for j, cell in enumerate(row):
                if cell != '0':
                    if not self.cell_is_valid(i, j):
                        return False
        return True

    def cell_is_valid(self, row, col):
        '''Return boolean if puzzle grid is valid
        '''
        valid = True
        temp = self.solution[row][col]
        self.solution[row][col] = 'x'
        # Offsets for generating cube
        r_off = row - row % 3
        c_off = col - col % 3
        cube = []
        # Representing Sudoku sub-box as a list
        for i in range(r_off, r_off + 3):
            for j in range(c_off, c_off + 3):
                cube.append(self.solution[i][j])
        # Row check
        if temp in self.solution[row]:
            valid = False
        # Column check
        elif temp in [self.solution[x][col] for x in range(9)]:
            valid = False
        # Box check
        elif temp in cube:
            valid = False
        self.solution[row][col] = temp
        return valid

    def backtrack(self, row, col):
        '''Run backtrack against self.solution
        '''
        if self.end_of_grid(row, col):
            return True
        for num in range(1, 10):
            self.solution[row][col] = str(num)
            #if self.grid_is_valid(row, col):
            if self.grid_is_valid():
                new_row, new_col = self.next_position(row, col)
                if self.backtrack(new_row, new_col):
                    return True
        self.solution[row][col] = '0'
        return False

    def solve(self):
        '''Initiate and backtrack method
        '''
        result = self.backtrack(0, 0)
        if not result:
            self.solution = self.puzzle
            for i, row in enumerate(self.solution):
                for j, cell in enumerate(row):
                    if cell == '0':
                        self.solution[i][j] = 'x'
        return self.puzzle_to_string(self.solution)


def parse_for_puzzles(filename):
    '''Parse a text file for puzzles and return array of strings
    '''
    puzzles = []
    with open(filename) as f:
        puzz_buff = ''
        count = 0
        for line in f.readlines():
            count += 1
            puzz_buff = ''.join([puzz_buff, line])
            if count == 10:
                puzzles.append(puzz_buff)
                puzz_buff = ''
                count = 0
    return puzzles


if __name__ == '__main__':
    if '-h' in sys.argv or '--help' in sys.argv:
        with open('help.txt', 'r') as f:
            print('\n')
            for line in f.readlines():
                print(line.rstrip())
            print('\n')
    elif '-f' in sys.argv:
        try:
            filename = sys.argv[sys.argv.index('-f')+1]
            for puzzle in parse_for_puzzles(filename):
                pzl = SudokuPuzzle()
                pzl.set_puzzle(puzzle)
                pzl.solve()
                pzl.print_solution()
        except IndexError:
            print('Error: Missing command line argument after \'-f\'')
    else:
        print('For help use the \'-h\' command line argument')
