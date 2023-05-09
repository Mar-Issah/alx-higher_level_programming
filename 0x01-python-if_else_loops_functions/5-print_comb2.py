#!/usr/bin/python3
for idx in range(100):
    if idx < 99:
        print("{:02d},".format(idx), end=' ')
    elif idx == 99:
        print("{:d}".format(idx))
