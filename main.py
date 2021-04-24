"""
Assignment 2 - Sudoku as a Constraint Satisfaction Problem 
CS480/580 Introduction to Artificial Intelligence

Authors: Kimberly Gonzales
         Patricia Ile-Mendoza
         Mckayla Hagerty
"""
import os
import platform
import sys
import timeit

import naive_backtracking
import smart_backtracking

#make simulated sudoku puzzle from sile input
def make_board(file_contents):
	
    board = []

    for line in file_contents:
        for num in line:
            board_line = []
            for j in range(0, 9):
                board_line.append(int(num[j]))                    
            
            board.append(board_line)

    return board

#print board to the screen
def print_board(board):
    for line in board:
        print(line)


def Main():    
   
    with open(sys.argv[1], 'r') as f:
        file_contents = [[num for num in line.split(' ')] for line in f]

    board = make_board(file_contents)

    print_board(board)


    #select algorithm
    while True:
    
        print("How would you like to solve the sudoku puzzle?")
        print("    1. Naive Backtracking")
        print("    2. Smart Backtracking")
        print("    3. Exit")
        try:
            option = int(input("Enter a number: "))
            if option < 1 or option > 4:
                raise Exception
        except:
            continue

        break

    
    if option == 3:
        sys.exit(0)

    result = None
    #return solved puzzle if solvable
    if option == 1:
        start = timeit.default_timer()
        result = naive_backtracking.search(board)
        print(" Execution time: ", timeit.default_timer() - start)
    elif option == 2:
        start = timeit.default_timer()
        result = smart_backtracking.search(board)
        print(" Execution time: ", timeit.default_timer() - start)

    if result is None:
        print("No solution")
    else:
        print_board(result)


if __name__=='__main__':
    Main()