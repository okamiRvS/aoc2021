import time
import pdb


def one():

    f =  open("d2.txt", "r")
    forward = depth = 0
    for x in f:
        line = x.replace("\n", "").split(" ")
        command = line[0]
        val = int(line[1])

        if command == "forward":
            forward+=val
        elif command == "down":
            depth+=val
        else:
            depth-=val

    print(forward*depth)


def two():

    f =  open("d2.txt", "r")
    forward = depth = aim = 0
    for x in f:
        line = x.replace("\n", "").split(" ")
        command = line[0]
        val = int(line[1])

        if command == "forward":
            forward+=val
            depth = depth + (aim * val)
        elif command == "down":
            aim+=val
        else:
            aim-=val

    print(forward*depth)


if __name__ == "__main__":

    one()
    two()