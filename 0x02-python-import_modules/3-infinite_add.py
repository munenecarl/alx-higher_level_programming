#!/usr/bin/python3

if __name__ == "__main__":
    import sys
    from calculator_1 import add
    args = sys.argv
    length = len(args)
    if length == 1:
        print("0")
    elif length == 2:
        print(args[1])
    else:
        sum = 0
        for i in range(1, length):
            sum = add(sum, int(args[i]))
        print(sum)
