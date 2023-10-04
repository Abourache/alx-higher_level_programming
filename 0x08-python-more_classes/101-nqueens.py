#!/usr/bin/python3
"""Solves the N-queens puzzle.

Determines all possible solutions to placing N
N non-attacking queens on an NxN chessboard.

Example:
    $ ./101-nqueens.py N

N must be an integer greater than or equal to 4.

Attributes:
    board (list): A list of lists representing the chessboard.
    solutions (list): A list of lists containing solutions.

Solutions are represented in the format [[r, c], [r, c], [r, c], [r, c]]
where `r` and `c` represent the row and column, respectively, where a
queen must be placed on the chessboard.
"""
from sys import argv

if len(argv) is not 2:
    print('Usage: nqueens N')
    exit(1)

if not argv[1].isdigit():
    print('N must be a number')
    exit(1)

N = int(argv[1])

if N < 4:
    print('N must be at least 4')
    exit(1)


def board_column_gen(board=[]):
    """Adds a column of zeroes to the right of any board about to be tested for
    queen arrangements in that column.

    Args:
        board (list) of (list) of (int): 2D list of ints, only as wide as
        needed to test the rightmost column for queen conflicts.

    Returns:
        modified 2D list

    """
    if len(board):
        for row in board:
            row.append(0)
    else:
        for row in range(N):
            board.append([0])
    return board


def add_queen(board, row, column):
    """Sets "queen," or 1, to coordinates given in board.

    Args:
        board (list) of (list) of (int): 2D list of ints, only as wide as
            needed to test the rightmost column for queen conflicts.
        row (int): first dimension index
        col (int): second dimension index

    """
    board[row][column] = 1


def new_queen_safe(board, row, column):
    """For the board given, checks that for a new queen placed in the rightmost
    column, there are no other "queen"s, or 1 values, in the martix to the
    left, and diagonally up-left and down-left.

    Args:
        board (list) of (list) of (int): 2D list of ints, only as wide as
            needed to test the rightmost column for queen conflicts.
        row (int): first dimension index
        col (int): second dimension index

    Returns:
        True if no left side conflicts found for new queen, or False if a
    conflict is found.

    """
    x = row
    y = column
    for i in range(1, N):
        if (y - i) >= 0:
            # check up-left diagonal
            if (x - i) >= 0:
                if board[x - i][y - i]:
                    return False
            # check left
            if board[x][y - i]:
                return False
            # check down-left diagonal
            if (x + i) < N:
                if board[x + i][y - i]:
                    return False
    return True


def coordinate_format(my_candidates):
    """Converts a board (matrix of 1 and 0) into a series of row/column
    indicies of each queen/1.

    Args:
    my_candidates (list) of (list) of (list) of (int): list of all successful
        solutions for amount of columns last checked

    Attributes:
        my_list (list) of (list) of (int): each member list contains the row
    column number for each queen found

    Returns:
        my_list, the list of coordinates

    """
    my_list = []
    for x, attempt in enumerate(my_candidates):
        my_list.append([])
        for i, row in enumerate(attempt):
            my_list[x].append([])
            for j, column in enumerate(row):
                if column:
                    my_list[x][i].append(i)
                    my_list[x][i].append(j)
    return my_list

# init my_candidates list with first column of 0s
my_candidates = []
my_candidates.append(board_column_gen())

# proceed column by column, testing the rightmost
for column in range(N):
    # start a new generation of the candidate list for every round of testing
    my_new_candidates = []
    # test each candidate from previous round, at current column
    for matrix in my_candidates:
        # for every row in that candidate's rightmost column
        for row in range(N):
            # are there any conflicts in placing a queen at those coordinates?
            if new_queen_safe(matrix, row, column):
                # no? then create a "child" (copy) of that candidate
                temp = [line[:] for line in matrix]
                # place a queen in that position
                add_queen(temp, row, column)
                # and unless you're in the last round of testing,
                if column < N - 1:
                    # add a new column of 0s on the right for the next round
                    board_column_gen(temp)
                # add that new candidate to this round's list of successes
                my_new_candidates.append(temp)
    # when finished with the round, discard the "parent" my_candidates
    my_candidates = my_new_candidates

# format results to match assignment output
for item in coordinate_format(my_candidates):
    print(item)
