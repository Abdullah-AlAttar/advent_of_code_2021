import enum
from pickle import FALSE
from re import A
import sys
from typing import List

boards = []
mask = []
who_won = []

def parse_board(f):
    board = []
    for i in range(5):
        line = f.readline()
        line = list(map(int, line.strip().split()))
        board.append(line)
    return board

def mark(n: int):
    for i, board in enumerate(boards):
        for j, row in enumerate(board):
            for k, col in enumerate(row):
                if col == n:
                    mask[i][j][k] = 1



def bingo_check():
    for i, board in enumerate(boards):
        if who_won[i]:
            continue
        for j in range(5):
            if all([row[j] for row in mask[i]]):
                return True, i
        for j, row in enumerate(board):
            # for k, col in enumerate(row):
                if all(mask[i][j]):
                    return True, i
                
    return False, -1

def mask_check(a : List[List[List[int]]]):
    for i, board in enumerate(a):
        for j, row in enumerate(board):
            for k, col in enumerate(row):
                if col == 0 :
                    return False
    return True

with open(sys.argv[1], 'r') as f:
    draws = list(map(int, f.readline().split(',')))
    print(draws)
    for line in f:
        if len(line.strip()) == 0:
            boards.append(parse_board(f))
            mask.append([
                [0, 0, 0, 0, 0],
                [0, 0, 0, 0, 0],
                [0, 0, 0, 0, 0],
                [0, 0, 0, 0, 0],
                [0, 0, 0, 0, 0],
            ])
            who_won.append(False)
    # for board in boards:
    #     print(board)
    # for m in mask:
    #     print(m)
    # draws = [22, 8 ,21, 6,1,5]
    for num in draws:
        print(num)
        mark(num)
        is_bingo ,idx = bingo_check()
        if is_bingo:
           who_won[idx] = True
        print(who_won)
        if all(who_won):
            print('yes', num) 
            exit() 
        # if is_bingo:
        #     print("yay", idx, num)
        #     res = 0
        #     for i, row in enumerate(boards[idx]):
        #         for j, col in enumerate(row):
        #             if not mask[idx][i][j]:
        #                 res += col 
        #     print(res, num, res * num)
        #     break
        