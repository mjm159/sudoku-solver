#!/usr/bin/python3

'''
puzzle_flask.py

Flask wrapper for sudoku_solver

Author: Michael Malocha
Last Revision: June 16th, 2016
'''

from flask import Flask, request

from sudoku_solver import SudokuPuzzle

app = Flask(__name__)

@app.route('/test', methods=['GET'])
def test():
    return 'OK', '200'

@app.route('/sudoku/solve', methods=['POST'])
def solve_puzzle():
    '''Solve Sudoku puzzle.
    '''
    text = request.form['text']
    pzl = SudokuPuzzle()
    pzl.set_puzzle(text)
    result = pzl.solve()
    return result, '200'

if __name__ == '__main__':
    app.run(debug=True)
