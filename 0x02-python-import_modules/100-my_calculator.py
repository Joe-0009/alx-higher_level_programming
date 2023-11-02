#!/usr/bin/python3

if __name__ == "__main__":
    import sys
    from calculator_1.py import add, sub, mul, div

    if len(sys.argv) != 3:
        print("Usage: ./100-my_calculator.py <a> <operator> <b>")
        exit(1)
    
    a = int(sys.argv[1])
    b = int(sys.argv[3])

    if sys.argv[2] == '+':
        print("{} {} {} = {}".format(a, sys.argv[2], b, a + b))
    elif sys.argv[2] == '-':
        print("{} {} {} = {}".format(a, sys.argv[2], b, a - b))
    elif sys.argv[2] == '*':
        print("{} {} {} = {}".format(a, sys.argv[2], b, a * b))
    elif sys.argv[2] == '/':
        print("{} {} {} = {}".format(a, sys.argv[2], b, a / b))
    else:
        print("Unknown operator. Available operators: +, -, * and /")
        exit(1)
