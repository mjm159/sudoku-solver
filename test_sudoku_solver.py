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

puzzle_1_solution = '''348267951
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

puzzle_2_solution = '''124986735
867435912
395712684
478359261
259861347
631274598
712698453
983547126
546123879
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

    def test_set_puzzle_no_name(self):
        puzzle = ss.SudokuPuzzle()
        puzzle.set_puzzle(puzzle_1_solution)
        temp = puzzle_1_solution.strip().split('\n')
        expected_answer = []
        for i in temp:
            expected_answer.append(list(i.strip()))
        assert expected_answer == puzzle.puzzle

    def test_puzzle_to_string_1(self):
        puzzle = ss.SudokuPuzzle()
        puzzle.set_puzzle(puzzle_1_solution)
        assert puzzle_1_solution == puzzle.puzzle_to_string(puzzle.puzzle)

    def test_puzzle_to_string_2(self):
        puzzle = ss.SudokuPuzzle()
        puzzle.set_puzzle(puzzle_2_solution)
        assert puzzle_2_solution == puzzle.puzzle_to_string(puzzle.puzzle)

    def test_end_of_grid_1_False(self):
        puzzle = ss.SudokuPuzzle()
        assert puzzle.end_of_grid(1, 5) == False

    def test_end_of_grid_2_True(self):
        puzzle = ss.SudokuPuzzle()
        assert puzzle.end_of_grid(9, 0) == True

    def test_next_position_1(self):
        puzzle = ss.SudokuPuzzle()
        puzzle.set_puzzle(puzzle_1)
        assert puzzle.next_position(0, 0) == (0, 0)

    def test_next_position_2(self):
        puzzle = ss.SudokuPuzzle()
        puzzle.set_puzzle(puzzle_3)
        assert puzzle.next_position(2, 1) == (2, 4)

    def test_next_position_3(self):
        puzzle = ss.SudokuPuzzle()
        puzzle.set_puzzle(puzzle_3)
        puzzle.puzzle[8][8] = '1'
        assert puzzle.next_position(8, 8) == (9, 0)

    def test_grid_is_valid_1_True(self):
        puzzle = ss.SudokuPuzzle()
        puzzle.set_puzzle(puzzle_1)
        puzzle.solution[0][3] = '2'
        assert puzzle.grid_is_valid(0, 3) == True

    def test_grid_is_valid_2_bad_row(self):
        puzzle = ss.SudokuPuzzle()
        puzzle.set_puzzle(puzzle_1)
        puzzle.solution[0][8] = '4'
        assert puzzle.grid_is_valid(0, 8) == False

    def test_grid_is_valid_3_bad_column(self):
        puzzle = ss.SudokuPuzzle()
        puzzle.set_puzzle(puzzle_1)
        puzzle.solution[2][1] = '4'
        assert puzzle.grid_is_valid(2, 1) == False

    def test_grid_is_valid_4_bad_box(self):
        puzzle = ss.SudokuPuzzle()
        puzzle.set_puzzle(puzzle_1)
        puzzle.solution[6][0] = '3'
        assert puzzle.grid_is_valid(6, 0) == False
        
    def test_backtrack_1(self):
        puzzle = ss.SudokuPuzzle()
        puzzle.set_puzzle(puzzle_1_solution)
        initial_pos = puzzle.next_position(0, 0)
        puzzle.backtrack(initial_pos[0], initial_pos[1])
        assert puzzle_1_solution == puzzle.puzzle_to_string(puzzle.solution)

    def test_backtrack_2(self):
        puzzle = ss.SudokuPuzzle()
        puzzle.set_puzzle(puzzle_2_solution)
        initial_pos = puzzle.next_position(0, 0)
        puzzle.backtrack(initial_pos[0], initial_pos[1])
        assert puzzle_2_solution == puzzle.puzzle_to_string(puzzle.solution)

