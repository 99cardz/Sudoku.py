import math
from copy import deepcopy
import time

def display_board(board, messange):
    print(messange)
    for i in range(len(board)):
        print(*board[i])

def checkavailable(input_value, h, v):
    #check for horizontal line
    if input_value in sudoku_copy[h]:
        #print ("in h")
        return 1
    #check for vertical line
    for i in range(0,8):
        #print (i)
        if input_value == sudoku_copy[i][v]:
            #print ("in v")
            return 1
    #check for block
    threebythree = []
    for r in range(3):
            for c in range(3):
                block = []
                for i in range(3):
                    for j in range(3):
                        block.append(sudoku_copy[3*r + i][3*c + j])
                threebythree.append(block)
    block_number = 0
    c = math.ceil((h+1)/3)
    r = math.ceil((v+1)/3)
    #print(c,r)
    block_number = (c-1)*3+r
    #print(block_number)
    if input_value in threebythree[block_number-1]:
        #print("in block "+str(block_number))
        return 1

def goback(horizontal,vertical, number):
    while 1>0:
        if sudoku[horizontal][vertical] == 0:
            sudoku_copy[horizontal][vertical] = 0
        if vertical == 0:
            horizontal-= 1
            vertical = 8
        else:
            vertical -= 1
        #print(horizontal, vertical)
        #print(sudoku_copy[horizontal][vertical])
        if sudoku[horizontal][vertical] == 0 and sudoku_copy[horizontal][vertical] != 9:
            number = sudoku_copy[horizontal][vertical] +1
            #print(number)
            return horizontal, vertical, number
def read_txt(sudoku):
    f = open("sudoku.txt")
    all_lines = f.readlines()
    all_lines = [line[:-1]for line in all_lines]
    #print(all_lines)
    for h in all_lines:
        line = []
        for v in h:
            line.append(int(v))
        sudoku.append(line)
    #print(sudoku)

def input_sudoku():
    for h in range(9):
        line = []
        rawline = input("Line "+str(h+1)+":")
        for v in rawline:
            line.append(int(v))
        sudoku.append(line)
    #print(sudoku)

def update_possibles():
    pass
#Start

print("Sudoku Solver with bruteforce method")
sudoku = []

read_txt(sudoku)
#input_sudoku()
sudoku_copy = deepcopy(sudoku)
print(sudoku)

display_board(sudoku,"This is your Sudokuboard:")

horizontal = 0
vertical = 0
number = 1
t = 2
start_time = time.time()
while 1>0 :
    if sudoku[horizontal][vertical] != 0:
        if vertical == 8:
            vertical = 0
            horizontal += 1
        else:
            vertical += 1
        #print("next position because not available")
    elif number == 10:
        horizontal, vertical, number = goback(horizontal, vertical, number)
        #print("going back to last possble position")
    elif not checkavailable(number, horizontal, vertical):
        #print(horizontal, vertical, number)
        sudoku_copy[horizontal][vertical] = number
        if vertical == 8:
            vertical = 0
            horizontal += 1
        else:
            vertical += 1
        number = 1

    else:
        number+=1
    if horizontal == 9:
        display_board(sudoku_copy, "This is the solution to your board:")
        display_board(sudoku, "This is the Original Board:")
        print("it took "+ str(time.time()-start_time)+"seconds")
        break
    #print(horizontal, vertical)
    #display_board(sudoku_copy,"")
    if time.time() - start_time>= t:
        display_board(sudoku_copy,"Current Process:")
        t += t
