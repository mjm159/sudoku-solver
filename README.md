# sudoku-solver

### Setup
```bash
git clone git@github.com:mjm159/sudoku-solver.git
cd sudoku-solver
virtualenv env
source env/bin/activate
pip3 install -r requirements.txt
```

### Usage


### Algorithm Choice
After researching various sudoku solving algorithms, I decided to proceed with the Backtrack algorithm. Here is my logic behind this decision:
- Implementing an algorithm to mimic how an average person would solve a sudoku by (crosshatching)[http://www.bigfishgames.com/blog/how-to-solve-sudoku-puzzles-quickly-and-reliably/] though simpler to implement, breaks down on harder puzzles
- Implementing an stochastic algorithm, though it would have a faster runtime, is significantly more difficult to implememnt.
- Backtrack is reliable, even if a little slow compared to fancier algorithms and it's a hell of a lot faster than brute force.
Source for psuedocode: (here)[https://codemyroad.wordpress.com/2014/05/01/solving-sudoku-by-backtracking/]
#### References
(Sudoku Solving Algorithms)[https://en.wikipedia.org/wiki/Sudoku_solving_algorithms]
(Sudoku Problem Solving)[http://www.academia.edu/6207354/Sudoku_Problem_Solving_using_Backtracking_Constraint_Propagation_Stochastic_Hill_Climbing_and_Artificial_Bee_Colony_Algorithms-METU_2013]
(STOCHASTIC OPTIMIZATION APPROACHES FOR SOLVING SUDOKU)[https://arxiv.org/pdf/0805.0697.pdf]
