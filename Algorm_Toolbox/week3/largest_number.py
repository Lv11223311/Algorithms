#Uses python3

import sys

def largest_number(a):
    #write your code here
    res = ""
    max_diget = -float('inf')
    for x in a:
        if x >= max_diget:
            max_diget = x
    
    return res

if __name__ == '__main__':
    input = sys.stdin.read()
    data = input.split()
    a = data[1:]
    print(largest_number(a))
    
