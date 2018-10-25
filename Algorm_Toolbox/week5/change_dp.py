# Uses python3
import sys

def get_change(m):
    #write your code here
    coins = [1, 3, 4]
    MinNumCoins = [0] * (m+1)
    for i in range(1, m+1):
        MinNumCoins[i] = float('inf')
        for j in range(len(coins)):
            if i >= coins[j]:
                pos = i - coins[j]
                NumCoins = MinNumCoins[pos] + 1
                if NumCoins < MinNumCoins[i]:
                    MinNumCoins[i] = NumCoins
    return MinNumCoins[m]
            

if __name__ == '__main__':
    m = int(sys.stdin.read())
    print(get_change(m))
