import sudoku_solver as ss

TEST_TXT = 'test_puzzles.txt'

puzzle_1 = '''
Puzzle 1
040000050 
001943600 
009000300 
600050002 
103000506 
800020007 
005000200 
002436700 
030000040 
'''

puzzle_1_solution = '''
348267951
571943627
269185374
697351482
123874596
854729137
415798263
982436715
736512849
'''

puzzle_2 = '''
Puzzle 2
004000000 
000030002
390700080
400009001
209801307
600200008
010008053
900040000
000000800
'''

puzzle_3 = '''
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

class TestSudokuPuzzle:

    def test_set_puzzle_1(self):
        puzzle = ss.SudokuPuzzle()
        puzzle.set_puzzle(puzzle_1)
        temp = puzzle_1.strip().split('\n')
        expected_answer = []
        for i in temp[1:]:
            expected_answer.append(list(i.strip()))
        assert expected_answer == puzzle.puzzle

    def test_set_puzzle_2(self):
        puzzle = ss.SudokuPuzzle()
        puzzle.set_puzzle(puzzle_2)
        temp = puzzle_2.strip().split('\n')
        expected_answer = []
        for i in temp[1:]:
            expected_answer.append(list(i.strip()))
        assert expected_answer == puzzle.puzzle
