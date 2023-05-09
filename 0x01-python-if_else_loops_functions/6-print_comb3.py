#!/usr/bin/python3
for i in range(10):
    for j in range(i + 1, 10):
        if i != j:
            if j != 9 or i != 8:
                print("{:d}{:d}, ".format(i, j), end="")
            else:
                print("{:d}{:d}".format(i, j))
