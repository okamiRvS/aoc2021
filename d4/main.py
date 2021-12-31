import time
import pdb
import numpy as np


def computeBingo(steps, data, x):

    for step in steps:

        for matrix in data:

            for i in range(x):

                matrix[matrix == step] = -1 # set to -1 if it exists that step

                s_row = np.sum(matrix, axis=0) # sum row
                s_col = np.sum(matrix, axis=1) # sum column
                if -x in s_row or -x in s_col:
                    print("bingo!")
                    sum_not_marked = np.sum(matrix[matrix!=-1])
                    return sum_not_marked * step


def one():

    f =  open("d4.txt", "r")
    first_row = f.readline()
    steps = np.array([int(el) for el in first_row.split(",")])

    arr = []
    matrix = []
    flag = False
    for x in f:

        if x =="\n":
            if len(matrix) != 0:
                arr.append(matrix)
                matrix = []
        else:
            row = [int(el) for el in x.split()]
            matrix.append(row)

   
    data = np.array(arr)

    z, x, y = data.shape

    print(computeBingo(steps, data, x))


def computeLastBingo(steps, data, x):

    alreadySeen = []
    lastStep = -1

    for step in steps:

        for idx, matrix in enumerate(data):

            for i in range(x):
                
                if idx not in alreadySeen:

                    matrix[matrix == step] = -1 # set to -1 if it exists that step

                    s_row = np.sum(matrix, axis=0) # sum row
                    s_col = np.sum(matrix, axis=1) # sum column

                    if -x in s_row or -x in s_col:

                        #print("bingo!")
                        sum_not_marked = np.sum(matrix[matrix!=-1])
                        
                        alreadySeen.append(idx)
                        lastStep = step

    return lastStep * sum_not_marked


def two():

    f =  open("d4.txt", "r")
    first_row = f.readline()
    steps = np.array([int(el) for el in first_row.split(",")])

    arr = []
    matrix = []
    flag = False
    for x in f:

        if x =="\n":
            if len(matrix) != 0:
                arr.append(matrix)
                matrix = []
        else:
            row = [int(el) for el in x.split()]
            matrix.append(row)

   
    data = np.array(arr)

    z, x, y = data.shape

    print(computeLastBingo(steps, data, x))


if __name__ == "__main__":

    #one()
    two()