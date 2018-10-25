# python 3
import sys

def GCD(a, b):
    if b == 0:
        return a
    else:
        a, b = b, (a % b)
        return GCD(a, b)


if __name__ == "__main__":
    input = sys.stdin.read()
    tokens = input.split()
    a = int(tokens[0])
    b = int(tokens[1])
    print(GCD(a, b))