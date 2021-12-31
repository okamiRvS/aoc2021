import time
import pdb


def one():

    f =  open("d1.txt", "r")
    start = f.readline()
    start = int(start.split("\n")[0])
    count = 0
    for x in f:
        x = int(x)
        if x > start:
            count+=1
        
        start=x

    print(count)


def two():

    with open("d1.txt", "r") as myfile:
        head = [int(x) for x in myfile]

    count = 0
    prev = head[0] + head[1] + head[2]
    for i in range(1, len(head)):

        if i+2 <= len(head)-1:
            cur = head[i] + head[i+1] + head[i+2]

        if cur > prev:
            count += 1

        prev = cur

    print(count)


if __name__ == "__main__":

    one()
    two()