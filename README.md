# sudoku-solver

### Setup
```bash
git clone git@github.com:mjm159/sudoku-solver.git
cd sudoku-solver
virtualenv env
source env/bin/activate
pip3 install -r requirements.txt
chmod +x sudoku_solver.py
```

### Testing
```bash
py.test -v test_sudoku_solver.py
```

### Usage
##### Command Line
Get help:  
```bash
./sudoku_solver.py -h
```  
Print nice version of puzzle (pre-solution)
```bash
./sudoku_solver.py -p puzzle_1.txt
```  
Solve and print solution along with original puzzle
```bash
./sudoku_solver.py -f puzzle_1.txt
```  
##### Flask
Setup:  
```bash
python sudoku_flask.py
```  
Interaction:
```python
import requests
file_name = 'puzzle_1.txt'

with open(file_name, 'r') as f:
    data = {'text': f.read()}
resp = requests.post(url, data=data)
print(resp.status_code)
print(resp.text)
```

### Design
This project will be built out using the Test Driven Development paradigm (i.e. unit tests first, followed by the functional code).  

For the design architecture of the code itself, the following steps will be taken:  
- [x] Create a SudokuPuzzle class skeleton  
- [x] Flesh out parsing puzzle from string into 2D list representation  
- [x] implement check for end of grid    
- [x] implement next_position  
- [x] implement check if cell_is_valid
- [x] implement check if grid_is_valid  
- [x] cobble together pieces to create Backtrack  
- [x] Wrap Backtrack in 'solve' function  
- [x] Implement simple 'print pretty'  
- [x] Implement command line interface  

Above and beyond tasks (if there's time):
- [x] Implement Flask wrapper for sudoku solver
- [x] Include performance evaluation
- [x] Better formating with 'print pretty'

### Algorithm Choice
After researching various sudoku solving algorithms, I decided to proceed with the Backtrack algorithm. Here is my logic behind this decision:
- Brute force is a classic technique, but severely lacks in performance.
- Stochastic algorithms can be faster, but are significantly more difficult to implememnt.
- Backtrack is reliable, and is considered slower when compared to fancier algorithms, but it's a hell of a lot faster than brute force.
Source for psuedocode: [here](https://codemyroad.wordpress.com/2014/05/01/solving-sudoku-by-backtracking/)  

### Notes  
~Originally I had the intention of implementing a RESTful API as a fun "Extra Credit" wrapper around the solution, which factored in my decision to put the solution into a class. Ultimately I ran out of time for implementing a Flask wrapper, but felt the Object Oriented design was solid and decided to keep it. Later, I might come back and implement that wrapper just for fun.~  

Thanks for taking the time to review my code.  
 - Michael

### References  
[Sudoku Solutions](http://www.sudoku-solutions.com/)
[Sudoku Solving Algorithms](https://en.wikipedia.org/wiki/Sudoku_solving_algorithms)  
[Sudoku Problem Solving](http://www.academia.edu/6207354/Sudoku_Problem_Solving_using_Backtracking_Constraint_Propagation_Stochastic_Hill_Climbing_and_Artificial_Bee_Colony_Algorithms-METU_2013)  
[STOCHASTIC OPTIMIZATION APPROACHES FOR SOLVING SUDOKU](https://arxiv.org/pdf/0805.0697.pdf)  
