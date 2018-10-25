#Uses python3

import sys

def lcs2(a, b):
    #write your code here
    count = 0
    for i in range(len(a)):
        for j in range(len(b)):
            if a[i] == b[j]:
                count += 1
    return min(len(a), len(b))



if __name__ == '__main__':
    input = sys.stdin.read()
    data = list(map(int, input.split()))

    n = data[0]
    data = data[1:]
    a = data[:n]

    data = data[n:]
    m = data[0]
    data = data[1:]
    b = data[:m]

    print(lcs2(a, b))
