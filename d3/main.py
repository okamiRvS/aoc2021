import time
import pdb
import numpy as np


def binaryToDecimal(binary):
     
    binary1 = binary
    decimal, i, n = 0, 0, 0
    while(binary != 0):
        dec = binary % 10
        decimal = decimal + dec * pow(2, i)
        binary = binary//10
        i += 1
    return decimal


def one():

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

    g_rate = ""
    e_rate = ""
    for i in range(m):
        val = sum(data[:,i] == 1)
        if val > int(n/2):
            g_rate += "1"
            e_rate += "0"
        else:
            g_rate += "0"
            e_rate += "1"

    res = binaryToDecimal(int(g_rate)) * binaryToDecimal(int(e_rate))

    print(res)


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

    # one()
    two()