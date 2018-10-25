# Uses python3

import numpy as np
import re
def evalt(a, b, op):
    if op == '+':
        return a + b
    elif op == '-':
        return a - b
    elif op == '*':
        return a * b
    else:
        assert False

def get_maximum_value(dataset):
    # extract digit
    args = filter(lambda ch:ch in '0123456789', dataset)
    num_list = list(args)
    num_list = [int(i) for i in num_list]
    n = len(num_list)
    # extract opration
    opt = list(filter(lambda ch:ch in '+-*/', dataset))

    # completion
    D = np.zeros((n, n))
    for i in range(2, n):
        D[i,i] = num_list[i]
    for 
            


    return 0


if __name__ == "__main__":
    print(get_maximum_value(input()))
