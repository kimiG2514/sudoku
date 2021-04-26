# sudoku
Authors: 

Kimberly Gonzales 

Patricia Ile-Mendoza

McKayla Hagerty

This is a programing assignment for Backtracking Algorithms: Naive Backtracking and Smart Backtracking.

The assigned problem is a sudoku puzzle. The goal is to finish a partitially filled a 9×9 grid with digits from 1 to 9 so that each row, column, and 3×3 section contain exactly one of all 9 digits.


### Contents ###

-Alorithms: main.py, backtrack.py, naive_backtracking.py, smart_backtracking.py

-Puzzles: puzzle.txt (provided in assignment), puzzle_easy.txt, puzzle_medium.txt, puzzle_hard.txt, puzzle_evil.txt (provided by http://www.websodoku.com)


### Instructions ###
-Ensure contents of package are saved in a single file location 

-Enter, 'python3 main.py puzzle.txt' into command line 

-User will be prompted to choose Naive Backtracking or Smart Backtracking: for Naive Backtracking, enter '1', for Smart Backtracking, enter '2'


### Program Excecution ###

The naïve backtracking algorithm iterates through the board, trying all possible combinations of the digits one by one until the correct configuration is found.  
The smart backtracking algorithm method reduces the number of nodes explored by determining a reduced search domain comprised of options with the least number of constraints.


### Output Analysis ###


#### Given puzzle ####

puzzle.txt

[0, 0, 3, 0, 2, 0, 6, 0, 0]

[9, 0, 0, 3, 0, 5, 0, 0, 1]

[0, 0, 1, 8, 0, 6, 4, 0, 0]

[0, 0, 8, 1, 0, 2, 9, 0, 0]

[7, 0, 0, 0, 0, 0, 0, 0, 8]

[0, 0, 6, 7, 0, 8, 2, 0, 0]

[0, 0, 2, 6, 0, 9, 5, 0, 0]

[8, 0, 0, 2, 0, 3, 0, 0, 9]

[0, 0, 5, 0, 1, 0, 3, 0, 0]

***Naive Backtracking solution: ***

[4, 8, 3, 9, 2, 1, 6, 5, 7]

[9, 6, 7, 3, 4, 5, 8, 2, 1]

[2, 5, 1, 8, 7, 6, 4, 9, 3]

[5, 4, 8, 1, 3, 2, 9, 7, 6]

[7, 2, 9, 5, 6, 4, 1, 3, 8]

[1, 3, 6, 7, 9, 8, 2, 4, 5]

[3, 7, 2, 6, 8, 9, 5, 1, 4]

[8, 1, 4, 2, 5, 3, 7, 6, 9]

[6, 9, 5, 4, 1, 7, 3, 8, 2]

Execution time:  0.003964999999999996

***Smart Backtracking solution:***

[4, 8, 3, 9, 2, 1, 6, 5, 7]

[9, 6, 7, 3, 4, 5, 8, 2, 1]

[2, 5, 1, 8, 7, 6, 4, 9, 3]

[5, 4, 8, 1, 3, 2, 9, 7, 6]

[7, 2, 9, 5, 6, 4, 1, 3, 8]

[1, 3, 6, 7, 9, 8, 2, 4, 5]

[3, 7, 2, 6, 8, 9, 5, 1, 4]

[8, 1, 4, 2, 5, 3, 7, 6, 9]

[6, 9, 5, 4, 1, 7, 3, 8, 2]

Execution time:  0.03209620000000002

-----------------------------------------------

#### Easy Puzzle ####

puzzle_easy.txt 

[7, 0, 6, 8, 0, 0, 0, 0, 0]

[2, 4, 8, 1, 0, 7, 6, 0, 5]

[0, 5, 9, 0, 0, 0, 7, 0, 0]

[0, 0, 4, 5, 0, 0, 0, 8, 0]

[0, 3, 0, 6, 0, 2, 0, 9, 0]

[0, 6, 0, 0, 0, 4, 1, 0, 0]

[0, 0, 3, 0, 0, 0, 4, 7, 0]

[4, 0, 2, 9, 0, 1, 8, 5, 3]

[0, 0, 0, 0, 0, 3, 2, 0, 9]

***Naive Backtracking:***

[7, 1, 6, 8, 3, 5, 9, 4, 2]

[2, 4, 8, 1, 9, 7, 6, 3, 5]

[3, 5, 9, 4, 2, 6, 7, 1, 8]

[1, 2, 4, 5, 7, 9, 3, 8, 6]

[8, 3, 7, 6, 1, 2, 5, 9, 4]

[9, 6, 5, 3, 8, 4, 1, 2, 7]

[6, 9, 3, 2, 5, 8, 4, 7, 1]

[4, 7, 2, 9, 6, 1, 8, 5, 3]

[5, 8, 1, 7, 4, 3, 2, 6, 9]

Execution time:  0.003793399999999947

***Smart Backtracking:***

[7, 1, 6, 8, 3, 5, 9, 4, 2]

[2, 4, 8, 1, 9, 7, 6, 3, 5]

[3, 5, 9, 4, 2, 6, 7, 1, 8]

[1, 2, 4, 5, 7, 9, 3, 8, 6]

[8, 3, 7, 6, 1, 2, 5, 9, 4]

[9, 6, 5, 3, 8, 4, 1, 2, 7]

[6, 9, 3, 2, 5, 8, 4, 7, 1]

[4, 7, 2, 9, 6, 1, 8, 5, 3]

[5, 8, 1, 7, 4, 3, 2, 6, 9]

Execution time:  0.027835499999999902

-----------------------------------------------

#### Medium Puzzle ####

puzzle_medium.txt 

[4, 2, 0, 0, 9, 0, 7, 0, 8]

[6, 0, 8, 0, 1, 4, 5, 0, 0]

[0, 7, 3, 0, 0, 0, 0, 0, 9]

[0, 0, 0, 0, 2, 8, 0, 0, 0]

[0, 1, 0, 0, 0, 0, 0, 5, 0]

[0, 0, 0, 6, 4, 0, 0, 0, 0]

[5, 0, 0, 0, 0, 0, 4, 7, 0]

[0, 0, 1, 4, 6, 0, 9, 0, 5]

[7, 0, 9, 0, 3, 0, 0, 6, 1]

***Naive Backtracking:***

[4, 2, 5, 3, 9, 6, 7, 1, 8]

[6, 9, 8, 7, 1, 4, 5, 2, 3]

[1, 7, 3, 8, 5, 2, 6, 4, 9]

[3, 6, 7, 5, 2, 8, 1, 9, 4]

[8, 1, 4, 9, 7, 3, 2, 5, 6]

[9, 5, 2, 6, 4, 1, 3, 8, 7]

[5, 3, 6, 1, 8, 9, 4, 7, 2]

[2, 8, 1, 4, 6, 7, 9, 3, 5]

[7, 4, 9, 2, 3, 5, 8, 6, 1]

Execution time:  0.012351800000000024

***Smart Backtracking:***

[4, 2, 5, 3, 9, 6, 7, 1, 8]

[6, 9, 8, 7, 1, 4, 5, 2, 3]

[1, 7, 3, 8, 5, 2, 6, 4, 9]

[3, 6, 7, 5, 2, 8, 1, 9, 4]

[8, 1, 4, 9, 7, 3, 2, 5, 6]

[9, 5, 2, 6, 4, 1, 3, 8, 7]

[5, 3, 6, 1, 8, 9, 4, 7, 2]

[2, 8, 1, 4, 6, 7, 9, 3, 5]

[7, 4, 9, 2, 3, 5, 8, 6, 1]

Execution time:  0.03247800000000001

-----------------------------------------------

#### Hard Puzzle ####

puzzle_hard.txt 

[0, 0, 0, 8, 0, 0, 0, 6, 0]

[0, 1, 0, 0, 0, 0, 7, 0, 4]

[7, 0, 6, 0, 0, 4, 0, 3, 0]

[0, 0, 2, 0, 1, 0, 0, 0, 0]

[5, 0, 1, 0, 6, 0, 8, 0, 9]

[0, 0, 0, 0, 7, 0, 2, 0, 0]

[0, 5, 0, 9, 0, 0, 6, 0, 2]

[3, 0, 7, 0, 0, 0, 0, 8, 0]

[0, 6, 0, 0, 0, 1, 0, 0, 0]

***Naive Backtracking:***

[4, 3, 5, 8, 2, 7, 9, 6, 1]

[8, 1, 9, 6, 3, 5, 7, 2, 4]

[7, 2, 6, 1, 9, 4, 5, 3, 8]

[6, 8, 2, 4, 1, 9, 3, 5, 7]

[5, 7, 1, 3, 6, 2, 8, 4, 9]

[9, 4, 3, 5, 7, 8, 2, 1, 6]

[1, 5, 4, 9, 8, 3, 6, 7, 2]

[3, 9, 7, 2, 4, 6, 1, 8, 5]

[2, 6, 8, 7, 5, 1, 4, 9, 3]

Execution time:  0.12069890000000005

***Smart Backtracking:***

Unable to solve using smart backtracking

-----------------------------------------------

#### Evil Puzzle ####

puzzle_evil.txt 

[0, 0, 0, 0, 0, 0, 4, 0, 0]

[0, 0, 4, 0, 0, 0, 0, 6, 5]

[0, 7, 5, 0, 4, 2, 1, 0, 0]

[2, 1, 0, 7, 0, 8, 0, 0, 0]

[0, 0, 0, 0, 0, 0, 0, 0, 0]

[0, 0, 0, 9, 0, 6, 0, 1, 8]

[0, 0, 7, 4, 8, 0, 2, 9, 0]

[5, 9, 0, 0, 0, 0, 6, 0, 0]

[0, 0, 1, 0, 0, 0, 0, 0, 0]

***Naive Backtracking:***

[9, 3, 8, 6, 5, 1, 4, 7, 2]

[1, 2, 4, 3, 9, 7, 8, 6, 5]

[6, 7, 5, 8, 4, 2, 1, 3, 9]

[2, 1, 9, 7, 3, 8, 5, 4, 6]

[7, 8, 6, 5, 1, 4, 9, 2, 3]

[4, 5, 3, 9, 2, 6, 7, 1, 8]

[3, 6, 7, 4, 8, 5, 2, 9, 1]

[5, 9, 2, 1, 7, 3, 6, 8, 4]

[8, 4, 1, 2, 6, 9, 3, 5, 7]

Execution time:  7.284059600000001

***Smart Backtracking:***

Unable to solve using smart backtracking

-----------------------------------------------

***Conclusion:***

The execution times increased as the difficulty of the puzzles increased. The naïve algorithm was consistently faster than the smart method for the puzzles we tried. The smart backtracking algorithm was not able to solve the more complex puzzles.
