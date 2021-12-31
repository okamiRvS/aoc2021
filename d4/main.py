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



def two():

    f =  open("d3.txt", "r")
    arr = []
    for x in f:
        row = []
        x = x.split("\n")[0]
        for val in x:
            row.append(int(val))

        arr+=[row]
    
    data = np.array(arr)

    n, m = data.shape

    g_rate = data
    e_rate = data

    for i in range(m):
        val0 = sum(g_rate[:,i] == 0)
        val1 = sum(g_rate[:,i] == 1)

        if val0 > val1:
            g_rate = g_rate[g_rate[:,i] == 0]
        else:
            g_rate = g_rate[g_rate[:,i] == 1]

        if g_rate.shape[0] == 1:
            break

    for i in range(m):
        val0 = sum(e_rate[:,i] == 0)
        val1 = sum(e_rate[:,i] == 1)

        if val0 > val1:
            e_rate = e_rate[e_rate[:,i] == 1]
        else:
            e_rate = e_rate[e_rate[:,i] == 0]

        if e_rate.shape[0] == 1:
            break

    e_rate = "" .join(str(x) for x in e_rate[0])
    g_rate = "" .join(str(x) for x in g_rate[0])

    res = binaryToDecimal(int(g_rate)) * binaryToDecimal(int(e_rate))

    print(res)



if __name__ == "__main__":

    one()
    #two()